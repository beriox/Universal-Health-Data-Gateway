# AirCappy

AirCappy is the aviation, emergency, geographic, and compliance-aware scenario built on the
CAPPY foundation.

This directory currently contains a discovery-layer demo for rendering 50,000+ global
OpenStreetMap health nodes using Web Workers (PapaParse) and Leaflet MarkerCluster.

The map consumes its seed dataset from [`CappyHospital`](../CappyHospital/):
`../CappyHospital/hospitals_global.csv`.

## What this demonstrates

The map is a global registry and network-discovery experiment. It helps identify possible
healthcare nodes that could participate in a future health-data exchange:

- hospitals and health centres
- pharmacies
- laboratories
- medical, dental, and physiotherapy practices
- NGO and humanitarian care points

The current dataset focuses on OSM objects tagged as hospitals. The other categories are future
extensions and should be added with their own filters and metadata rather than being silently
labelled as hospitals.

This directory does not contain patient data and does not send clinical records to the mapped
facilities. It complements [`CAPPY`](..), which demonstrates the
separate canonical-model and adapter layer for authorized data exchanges.

The public UHDG GitHub Pages demo remains the primary AirCappy prototype for now:

https://beriox.github.io/Universal-Health-Data-Gateway/

## Possible adoption path

A future participating facility could publish or expose a small capability profile alongside its
location, for example:

- facility type and services
- country and jurisdiction
- FHIR or other interoperability support
- connectivity and operating mode
- consent and emergency-routing capabilities
- a maintainer or institutional contact

The registry would help discover a destination; it would not itself authorize access or replace
the facility's clinical, identity, consent, and compliance systems. Real integrations should be
agreed with each participating organization.

OpenHospital is a useful humanitarian example for this future path, while organizations such as
Auxologico and Centro Medico Santagostino could be potential Italian innovation or pilot contacts.
They should be presented as prospective partners, not as current integrations.

The repository includes a partial CSV seed so visitors can try the map without querying
OpenStreetMap. To generate or update a small sample locally, change into `CappyHospital` and run:

```bash
cd ../CappyHospital
python3 fetch_hospitals_osm.py
```

The downloader requests at most five records per country by default, with a deliberate delay
between requests. This is intentional: do not turn a public demo into a full-world scrape or run
multiple downloads in parallel. A larger sample can be requested explicitly, for example
`python3 fetch_hospitals_osm.py --limit-per-country 10`, but the default is the recommended setting.

To build a separate worldwide sample while keeping the bundled seed untouched, use a separate
output path and a conservative delay:

```bash
cd ../CappyHospital
python3 fetch_hospitals_osm.py \
	--output hospitals_global.generated.csv \
	--limit-per-country 5 \
	--request-delay 90
```

This makes roughly one small, serial request per country. Depending on server load and failures,
the run can still take hours; that is expected and preferable to stressing a public service.

For a small test, restrict the run to selected countries:

```bash
cd ../CappyHospital
python3 fetch_hospitals_osm.py --countries AF,AL,DZ,AD,AO,AG,AR,AM
```

This is the recommended way to test the downloader. It avoids accidentally starting a worldwide
run just because the CSV was moved temporarily.

The script resumes from an existing CSV in `CappyHospital` and skips countries already represented
there. This means
the bundled seed normally eliminates the need to query the public server at all. The map can be
hosted locally from the `CAPPY` directory, so the AirCappy page can reach the sibling CappyHospital
dataset:

```bash
cd ..
python3 -m http.server
```

Then open `http://localhost:8000/AirCappy/index.html`.
