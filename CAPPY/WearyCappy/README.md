# WearyCappy

Module for wearable, mobile-health, and IoT telemetry ingestion.

The current adapters are lightweight, simulated source adapters that normalize platform-shaped
measurements into CAPPY's shared `HealthData` model. They do not call vendor SDKs or live APIs.

Potential scope:

- Apple HealthKit and Huawei Health Kit pathways;
- Android Health Connect and Fitbit pathways for the Google wearable ecosystem;
- consented citizen monitoring sessions;
- normalization into the shared `HealthData` model;
- privacy, minimization, and provenance requirements.

No live connector is implemented here yet. A future `cappy_simulator.py` scenario can import these
adapters and pass their normalized output to an FSE, cloud, or hospital destination adapter.
