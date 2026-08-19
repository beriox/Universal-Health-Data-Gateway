# 🗺️ CAPPY - Modular Roadmap

This document outlines future pathways for `CAPPY`, the project's decoupled routing foundation.
CAPPY provides reusable processing, normalization, compliance, and adapter building blocks. The
UHDG `index.html` is currently the illustrative `AirCappy` scenario: a diplomatic and emergency
routing prototype showing how the engine could navigate geographic, institutional, and regulatory
friction.

This approach keeps the foundation clean and allows independent development by different
organizations, regions, or project teams.

See the [AirCappy prototype](../index.html) for the current interactive demonstration.

---

### 📦 Core Modules

*   **`AirCappy`**: Aviation, Emergency & Geo-Routing
    *   **Scope**: Manages routing for in-flight medical emergencies, integration with OpenStreetMap/Overpass for facility discovery, and geo-fenced compliance.

*   **`FseCappy`**: National & Regional Gateway Integration
    *   **Scope**: Handles interoperability with official national and regional health record systems (e.g., Italian FSE, US Core/USCDI, MyHealth@EU). Contains mappings for local standards like ATC and RxNorm.

*   **`CappyHospital`**: Low-Resource & Humanitarian EMRs
    *   **Scope**: Provides adapters for Electronic Medical Record systems used in low-resource or humanitarian contexts, with a primary focus on `OpenHospital`.

*   **`WearyCappy`**: Wearables & IoT Telemetry
    *   **Scope**: Focuses on ingesting and normalizing data from consumer wearables and IoT devices (e.g., Apple HealthKit, Huawei Health Kit) for preventative care and personal health records.

---

## Future pathways

### Smartwatch pathway

CAPPY can illustrate a future path in which a citizen authorizes a session and monitoring data
from an Apple Watch/HealthKit or Huawei Watch/Health Kit source is read from a platform and
prepared for an FSE exchange. This is an architectural example only; the current project does not
connect to either platform yet.

The two examples are deliberately useful without claiming API market share. Counterpoint Research
reported Q1 2026 global smartwatch shipment shares of 23% for Apple and 17% for Huawei. Shipment
share is not the same as API adoption or installed base, but it supports showing both ecosystems
in a conceptual demo. See the [Counterpoint market snapshot](https://www.counterpointresearch.com/insights/global-smartwatch-shipments-market-share/),
[Apple HealthKit documentation](https://developer.apple.com/health-fitness/), and
[Huawei Health Kit developer portal](https://developer.huawei.com/consumer/en/).

### Temporary cloud sharing and flight assistance

A traveler could authorize a limited session so relevant data is available to authorized
assistance staff or to a healthcare structure in another country. Consent scope, expiry,
minimization, and audit would need to be implemented before any real deployment.

This pathway belongs to the wider UHDG/AirCappy use case; CAPPY supplies the reusable routing,
payload-processing, and adapter foundation.

### OpenHospital pathway

An authorized source, such as FHIR, FSE, a cloud platform, or a smartwatch-derived session, could
prepare a clinical summary for an OpenHospital-compatible destination. Open Hospital is a free and
open-source health information system focused in particular on hospitals and health centers in
developing countries.

This is not a claim that CAPPY already connects to Open Hospital. The official project lists an OH
API REST component as work in progress, so the endpoint and payload shown in the simulator are
placeholders for a future adapter to be agreed with the Open Hospital maintainers. See the
[Open Hospital repository](https://github.com/informatici/openhospital), [OH API repository](https://github.com/informatici/openhospital-api),
and [official website](https://www.open-hospital.org/).

## Implementation notes

The CAPPY sample follows a narrow adapter pattern:

- `HealthData` is the internal canonical record;
- each adapter translates between a provider payload and that model;
- `HealthDataGateway` selects the appropriate adapter;
- `ComplianceEvaluator` provides a minimal routing decision for the simulation.

The current adapters and API exchanges are illustrative and run in memory. They do not send HTTPS
requests or connect to live FSE, cloud, HealthKit, Huawei Health Kit, or OpenHospital endpoints.
The `INTEGRATIONS.md` examples are target integration profiles, not live connectors.

## Future implementation directions

Additional adapters may be added only after a concrete endpoint, authentication model, data
mapping, consent contract, and compliance responsibility are defined. Candidate directions include:

- regional FSE and FHIR profiles;
- Azure, AWS, and Google healthcare services;
- wearable and consumer-health platforms;
- humanitarian and low-resource EMRs;
- facility discovery through the `AirCappy` registry layer.