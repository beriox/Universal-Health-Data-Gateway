# Universal Health Data Gateway (UHDG) & Cappy - Project Context

## Vision & Architecture
This repository is a prototype and architecture blueprint for portable, secure, citizen-centric health data routing. It models core flows for interoperability, compliance, and multi-cloud integration.

## Core Hierarchy & Terminology
1. **UHDG:** High-level architectural framework.
2. **Cappy:** The core, decoupled, adapter-driven routing engine and Open Source mascot.
3. **Canonical Model:** All external systems normalize into `HealthData`.
4. **Cappy Modules (Sub-packages in `/modules/<region>`):**
   - `AirCappy`: Aviation, Emergency, OSM/Overpass routing.
   - `FseCappy`: National/EU/US gateways & EHR onboarding (`it_fse`, `us_core`, `emea`).
   - `CappyHospital`: Low-resource EMRs & OpenHospital adapters.
   - `WearyCappy`: Sports, wearables & IoT telemetry ingestion (Apple HealthKit, Huawei Health Kit).

## Code Generation & Architecture Principles
- Prefer a clean abstraction over direct one-off integrations.
- Keep interfaces narrow, explicit, and composable.
- Maintain clear separation: Data Model | Connectors | Routing/Compliance | Demo Scripts.
- Regional standards (ATC, RxNorm, LOINC, SNOMED) live inside `/modules/<region>` as dictionaries, keeping the core router agnostic.
- Keep the example simulation CLI (`CAPPY/cappy_simulator.py`) fully functional.