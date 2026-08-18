<p align="center">
   <img src="CAPPY.png" alt="CAPPY, the capybara healthcare routing mascot" width="180" />
</p>

# 🦫 CAPPY: Capybara Adaptive Payload Processing Engine

> *"The calmest, most interoperable data routing agent in the healthcare ecosystem."*

## Who is CAPPY?

In nature, the capybara is famous for its calm demeanor and its ability to get along with many
species.

In this repository, **CAPPY** is the lightweight execution engine and simulation CLI that
demonstrates the **Universal Health Data Gateway (UHDG)** architecture in action.

## What does CAPPY do?

CAPPY sits between health-data sources and target platforms, keeping the demonstration focused on
portable, consent-aware interoperability:

- accepts illustrative clinical, wearable, and citizen-authorized inputs;
- normalizes them into the shared `HealthData` model;
- prepares FHIR, FSE, cloud, smartwatch, and OpenHospital-compatible payloads;
- demonstrates routing decisions without sending real network requests.

The current implementation is a local simulation. It does not yet connect to live FSE, cloud,
HealthKit, Huawei Health Kit, or OpenHospital endpoints.

This folder contains a small, browsable prototype for an adapter-driven health data architecture.

## Goal

Keep the design simple and aligned with the repository's conceptual direction:

- define one internal canonical model: `HealthData`
- adapt external ecosystems to that model
- keep routing and compliance decisions separate from data conversion logic
- start with the most relevant systems instead of building a world-scale ontology too early

## How to run the demo

This sample currently runs in simulated mode without cloud credentials or live service contracts.
The adapters translate payloads in memory; they do not yet call real FSE, Azure, AWS, or Google
Cloud endpoints.

### Default mode

```bash
python3 "CAPPY/cappy_simulator.py"
```

The script runs in simulated mode by default; cloud connection variables are not required or used.

### Explicit simulated mode

```bash
python3 "CAPPY/cappy_simulator.py" --simulated
```

The complete example output is available in [`demo-output.txt`](demo-output.txt), so the
interop flow can be reviewed directly on GitHub without running Python.

There is no live mode yet. Supplying credentials or `UHDG_MODE=live` does not create a real
connection; the script rejects live mode explicitly until transport, authentication, endpoint
configuration, and provider-specific clients are implemented.

## What the journey demonstrates

The demo is intentionally understandable as a health-data journey, even for readers who do not
work with APIs every day:

1. Read a record from an EU healthcare structure through FHIR.
2. Check jurisdiction, consent, and routing rules before transmission.
3. Normalize the record into the shared `HealthData` model.
4. Prepare a FHIR record for an EU healthcare structure.
5. Prepare an FSE exchange for an authorized application or institution.
6. Prepare a temporary cloud transfer authorized by the citizen.
7. Illustrate smartwatch monitoring data read from a cloud platform and prepared for FSE.
8. Illustrate temporary cloud sharing for in-flight assistance or care in another country.
9. Illustrate routing an authorized clinical summary to an OpenHospital-compatible endpoint.

The last steps print illustrative API messages, but do not send HTTPS requests. They show the
shape of a future integration while keeping this proof of concept safe to run locally.

### Smartwatch pathway

The sample also illustrates an attractive future path: a citizen authorizes a session in which
monitoring data from an Apple Watch/HealthKit or Huawei Watch/Health Kit source is read from a
platform and prepared for an FSE exchange. This is an architectural example only; the sample
does not connect to either platform yet.

The two examples are deliberately useful without claiming API market share. Counterpoint Research
reported Q1 2026 global smartwatch shipment shares of 23% for Apple and 17% for Huawei. Shipment
share is not the same as API adoption or installed base, but it supports showing both ecosystems
in the conceptual demo. See the [Counterpoint market snapshot](https://www.counterpointresearch.com/insights/global-smartwatch-shipments-market-share/),
[Apple HealthKit documentation](https://developer.apple.com/health-fitness/), and
[Huawei Health Kit developer portal](https://developer.huawei.com/consumer/en/).

The temporary cloud-sharing scenario connects to the wider flight-assistance use case: a traveler
could authorize a limited session so relevant data is available to authorized assistance staff or
to a healthcare structure in another country. Consent scope, expiry, minimization, and audit would
need to be implemented before any real deployment.

### OpenHospital pathway

The final example shows how an authorized source, such as FHIR, FSE, a cloud platform, or a
smartwatch-derived session, could prepare a clinical summary for an OpenHospital-compatible
destination. Open Hospital is a free and open-source health information system focused in
particular on hospitals and health centers in developing countries.

This is not a claim that the sample already connects to Open Hospital. The official project lists
an OH API REST component as work in progress, so the endpoint and payload shown here are placeholders
for a future adapter to be agreed with the Open Hospital maintainers. See the [Open Hospital
repository](https://github.com/informatici/openhospital), [OH API repository](https://github.com/informatici/openhospital-api),
and [official website](https://www.open-hospital.org/).

## Core idea

The project follows a narrow, explicit adapter pattern:

- `HealthData` represents the internal canonical record
- each adapter translates between a provider-specific payload and the internal model
- `HealthDataGateway` routes work to the appropriate adapter
- `ComplianceEvaluator` makes routing decisions based on jurisdiction and consent

## Current implementation focus

The sample currently demonstrates the first three architectural layers in sequence:

1. `FhirAdapter`
   - this is the active first priority
   - it converts a realistic FHIR bundle into the internal canonical model and back
   - it acts as the interoperability boundary for health data normalization

2. `FSEAdapter`
   - it represents EU / FSE-oriented exchanges and portability patterns
   - it is a second-step provider-style adapter, not a replacement for FHIR

3. `CloudAdapter`
   - it provides the shared cloud record envelope
   - concrete Azure, AWS, and Google Cloud adapters demonstrate provider-specific routing targets
   - the demo presents these as API-style exchanges without requiring live cloud contracts

## Why this is a good starting point

This keeps the project focused on the realistic first wave of health data interoperability without overbuilding a global ontology.

The direction is intentionally incremental:

- internal data model first
- FHIR as the normalization layer
- narrow provider adapters only after the boundary is proven
- compliance logic separated from data translation

## Future expansions

Additional adapters may be added later, but only after the core adapter boundary is validated.

The current matrix document is a planning reference, not an active implementation list.

Possible future categories include:

- Azure / AWS / Google healthcare ecosystems
- EU or national health data platforms
- wearable or consumer-health integrations
- hospital or EHR-specific connectors

These should be added only when the repository is ready for a concrete implementation and a defined mapping contract.
