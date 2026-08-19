#!/usr/bin/env python3
"""
fetch_hospitals_osm.py
-----------------------
Downloads a small sample of OpenStreetMap facilities tagged
amenity=hospital or healthcare=hospital, one country at a time, via
the public Overpass API, and writes a lightweight CSV with exactly
these columns:

    id, name, latitude, longitude, country_code

Approach
--------
A single "give me every hospital on Earth" Overpass query is heavy
enough that the public server will usually time out or refuse it, and
hammering it with one giant request is against Overpass's fair-use
policy. Instead this script queries ONE COUNTRY AT A TIME, using each
country's OSM administrative boundary (the "ISO3166-1" tag on
admin_level=2 relations) as the search area. That has two benefits:
  1. Each request is small enough to complete reliably.
  2. The country code comes for free from the loop, so we don't need
     a separate reverse-geocoding step (Overpass tag data for
     addr:country is inconsistent/missing on most hospital objects).

Nodes are used as-is; ways/relations (hospital *buildings* /
*campuses*, common for bigger hospitals) are queried with
`out center;` so we still get a single representative lat/lon.

IMPORTANT — please read before running
---------------------------------------
* By default this requests at most five results per country. It still
    fires ~195 requests, but each response is intentionally small and
    avoids asking the public server for every hospital worldwide.
* Do not change the limit casually or parallelize requests against
    the public server. A complete worldwide export is not the purpose
    of this demo and should use an appropriate data-extraction process.
* If overpass-api.de is overloaded, switch OVERPASS_URL to a mirror,
  e.g. "https://overpass.kumi.systems/api/interpreter" or
  "https://overpass.openstreetmap.ru/api/interpreter".
* Be a good citizen of a free public service: keep REQUEST_DELAY as
  is (or increase it), and don't run this on a schedule/cron.
* Requires only the Python standard library (no pip installs).

Resuming / interrupting
------------------------
This script is safe to Ctrl-C and re-run. On startup it reads any
existing OUTPUT_FILE, collects the set of country_code values already
present, and treats each of those countries as fully downloaded —
skipping them entirely on the next run. New results are appended, not
overwritten.

This means: if a country's request failed partway (e.g. a 504 Gateway
Timeout) or you stopped the script mid-country, delete that country's
rows from the CSV before re-running (grep/filter them out by
country_code) so the script knows to retry it — otherwise a partial
country would be silently treated as complete. A country that failed
outright (no rows ever written for it) doesn't need any manual
cleanup: since nothing was written for it, it's naturally retried.
"""

import argparse
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

OVERPASS_URL = "https://overpass-api.de/api/interpreter"
OUTPUT_FILE = "hospitals_global.csv"
DEFAULT_NAME = "Emergency Health Centre"
DEFAULT_LIMIT_PER_COUNTRY = 5
REQUEST_DELAY = 60          # seconds between requests — be nice to the free server
TIMEOUT_QUERY = 180        # seconds, matches the Overpass [timeout:] setting below
TIMEOUT_HTTP = 210         # a bit more than TIMEOUT_QUERY, for the HTTP call itself
MAX_RETRIES = 3

# ISO 3166-1 alpha-2 codes for every country/territory Overpass/OSM
# tags with ISO3166-1 on its admin_level=2 boundary. A handful of
# micro-territories with no such boundary in OSM will simply return
# zero results and are skipped automatically.
COUNTRY_CODES = [
    "AF","AL","DZ","AD","AO","AG","AR","AM","AU","AT","AZ","BS","BH","BD","BB",
    "BY","BE","BZ","BJ","BT","BO","BA","BW","BR","BN","BG","BF","BI","CV","KH",
    "CM","CA","CF","TD","CL","CN","CO","KM","CG","CD","CR","CI","HR","CU","CY",
    "CZ","DK","DJ","DM","DO","EC","EG","SV","GQ","ER","EE","SZ","ET","FJ","FI",
    "FR","GA","GM","GE","DE","GH","GR","GD","GT","GN","GW","GY","HT","HN","HU",
    "IS","IN","ID","IR","IQ","IE","IL","IT","JM","JP","JO","KZ","KE","KI","KP",
    "KR","KW","KG","LA","LV","LB","LS","LR","LY","LI","LT","LU","MG","MW","MY",
    "MV","ML","MT","MH","MR","MU","MX","FM","MD","MC","MN","ME","MA","MZ","MM",
    "NA","NR","NP","NL","NZ","NI","NE","NG","MK","NO","OM","PK","PW","PA","PG",
    "PY","PE","PH","PL","PT","QA","RO","RU","RW","KN","LC","VC","WS","SM","ST",
    "SA","SN","RS","SC","SL","SG","SK","SI","SB","SO","ZA","SS","ES","LK","SD",
    "SR","SE","CH","SY","TW","TJ","TZ","TH","TL","TG","TO","TT","TN","TR","TM",
    "TV","UG","UA","AE","GB","US","UY","UZ","VU","VA","VE","VN","YE","ZM","ZW",
]


def build_query(country_code, limit_per_country):
    return f"""
    [out:json][timeout:{TIMEOUT_QUERY}];
    area["ISO3166-1"="{country_code}"][admin_level=2]->.country;
    (
      node["amenity"="hospital"](area.country);
      way["amenity"="hospital"](area.country);
      relation["amenity"="hospital"](area.country);
      node["healthcare"="hospital"](area.country);
      way["healthcare"="hospital"](area.country);
      relation["healthcare"="hospital"](area.country);
    );
    out center tags {limit_per_country};
    """


def fetch_country(country_code, limit_per_country, request_delay):
    query = build_query(country_code, limit_per_country)
    payload = urllib.parse.urlencode({"data": query}).encode("utf-8")
    req = urllib.request.Request(
        OVERPASS_URL,
        data=payload,
        headers={
            # Overpass asks that clients identify themselves.
            "User-Agent": "UHDG-hospital-fetch/1.0 (single-use research script)"
        },
    )
    last_err = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT_HTTP) as resp:
                return json.load(resp)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            last_err = e
            wait = request_delay * attempt * 2
            print(f"    retry {attempt}/{MAX_RETRIES} after error ({e}) — waiting {wait}s",
                  file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"giving up on {country_code}: {last_err}")


def extract_rows(osm_json, country_code, seen_ids):
    rows = []
    for el in osm_json.get("elements", []):
        # Prefix by element type so node/way/relation IDs (which share
        # the same numeric namespace in OSM) never collide.
        osm_id = f"{el['type'][0]}{el['id']}"
        if osm_id in seen_ids:
            continue

        if el["type"] == "node":
            lat, lon = el.get("lat"), el.get("lon")
        else:
            center = el.get("center") or {}
            lat, lon = center.get("lat"), center.get("lon")
        if lat is None or lon is None:
            continue

        seen_ids.add(osm_id)
        name = (el.get("tags") or {}).get("name") or DEFAULT_NAME
        rows.append([osm_id, name, round(lat, 6), round(lon, 6), country_code])
    return rows


def read_existing_progress(path):
    """Return (completed_countries, seen_ids, file_exists).

    A country counts as "completed" if ANY row with that country_code
    is already in the file — see the resume note in the module
    docstring about removing partial-country rows before re-running.
    """
    completed = set()
    seen_ids = set()
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return completed, seen_ids, False
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cc = row.get("country_code")
            rid = row.get("id")
            if cc:
                completed.add(cc)
            if rid:
                seen_ids.add(rid)
    return completed, seen_ids, True


def parse_args():
    parser = argparse.ArgumentParser(
        description="Fetch a small, respectful OpenStreetMap hospital sample."
    )
    parser.add_argument(
        "--limit-per-country",
        type=int,
        default=DEFAULT_LIMIT_PER_COUNTRY,
        help=f"Maximum records requested per country (default: {DEFAULT_LIMIT_PER_COUNTRY}).",
    )
    parser.add_argument(
        "--countries",
        help="Comma-separated ISO country codes to fetch, for example AF,AL,DZ,AD,AO,AG,AR,AM.",
    )
    parser.add_argument(
        "--output",
        default=OUTPUT_FILE,
        help=f"CSV output path (default: {OUTPUT_FILE}).",
    )
    parser.add_argument(
        "--request-delay",
        type=int,
        default=REQUEST_DELAY,
        help=f"Seconds between requests (default: {REQUEST_DELAY}).",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    if args.limit_per_country < 1:
        raise SystemExit("--limit-per-country must be at least 1")
    if args.request_delay < 0:
        raise SystemExit("--request-delay cannot be negative")

    output_file = args.output
    completed_countries, seen_ids, file_exists = read_existing_progress(output_file)
    requested_countries = COUNTRY_CODES
    if args.countries:
        requested_countries = [cc.strip().upper() for cc in args.countries.split(",") if cc.strip()]
        unknown = sorted(set(requested_countries) - set(COUNTRY_CODES))
        if unknown:
            raise SystemExit(f"Unknown country code(s): {', '.join(unknown)}")

    remaining = [cc for cc in requested_countries if cc not in completed_countries]
    skipped = len(requested_countries) - len(remaining)

    if file_exists:
        print(f"Found existing {output_file}: {skipped} countries already "
              f"downloaded ({len(seen_ids)} rows) — resuming with the "
              f"remaining {len(remaining)}.", file=sys.stderr)
    else:
        print(f"No existing {output_file} found — starting fresh "
              f"({len(remaining)} countries).", file=sys.stderr)

    mode = "a" if file_exists else "w"
    total = 0
    failed = []

    with open(output_file, mode, newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["id", "name", "latitude", "longitude", "country_code"])
            f.flush()

        for i, cc in enumerate(remaining, 1):
            print(f"[{i}/{len(remaining)}] {cc} ...", file=sys.stderr, end=" ")
            try:
                data = fetch_country(cc, args.limit_per_country, args.request_delay)
            except Exception as e:
                # Give up on this country for now, but keep everything
                # written so far safely on disk, note it, and move on —
                # no need to stop the whole run over one bad country.
                print(f"FAILED after {MAX_RETRIES} attempts ({e}) — "
                      f"progress so far is saved, skipping to next country.",
                      file=sys.stderr)
                f.flush()
                failed.append(cc)
                time.sleep(args.request_delay)
                continue

            rows = extract_rows(data, cc, seen_ids)
            writer.writerows(rows)
            f.flush()
            total += len(rows)
            print(f"{len(rows)} hospitals (running total this run: {total})", file=sys.stderr)
            time.sleep(args.request_delay)

        print(f"\nDone with this run. {total} new hospitals appended to {output_file}.",
                    file=sys.stderr)
    if failed:
        print(f"{len(failed)} countries failed and were skipped: {', '.join(failed)}",
              file=sys.stderr)
        print("Just re-run the script — failed countries have no rows in the "
              "CSV yet, so they'll be retried automatically.", file=sys.stderr)


if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------
# Slimming the file down for a browser demo
# ---------------------------------------------------------------------------
# hospitals_global.csv from a full run is a real-world dataset, not a demo
# fixture — likely tens of MB. Before shipping it next to index.html,
# consider:
#
#   1. Dropping unnamed entries (keep only ones with a real OSM name):
#        awk -F',' 'NR==1 || $2!="Emergency Health Centre"' hospitals_global.csv \
#          > hospitals_named.csv
#
#   2. Rounding coordinates more aggressively (4 decimals ≈ 11m precision
#      is already overkill for a world map) — already done above at 6.
#
#   3. Converting to a smaller binary/columnar format, or gzipping it and
#      having the browser fetch + DecompressionStream it, if you need to
#      keep every record.
#
# The accompanying index.html update assumes you'll serve whatever CSV
# you end up with (full or slimmed) as ./hospitals_global.csv.
