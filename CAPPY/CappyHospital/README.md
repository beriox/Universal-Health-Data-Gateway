# CappyHospital

Module for hospital, humanitarian, and low-resource health information systems.

This module currently owns the OpenStreetMap hospital seed dataset and its respectful downloader:

- `hospitals_global.csv` is the partial browser/demo seed;
- `fetch_hospitals_osm.py` fetches small, delayed per-country samples;
- `AirCappy/index.html` consumes the CSV as a discovery layer.

Potential scope:

- OpenHospital and comparable EMR adapters;
- offline-friendly exchange patterns;
- facility capability profiles;
- mappings agreed with participating maintainers and care organizations.

No live clinical connector is implemented here yet. The OSM dataset is a facility-discovery asset,
not a patient-data source.
