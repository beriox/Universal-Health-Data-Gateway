# Cloud Capability Matrix

This document is intentionally a planning artifact, not an active implementation list.

The purpose is to keep a map of future possibilities without prematurely turning the prototype into a provider catalog or a broad cloud strategy document.

## Core idea

The project keeps the cloud layer abstract at the start. A provider is only added as a concrete adapter when the integration contract and compliance requirements are clear.

The internal health-data layer remains the real source of truth. FHIR is the first canonical interoperability boundary, and the current sample includes simulated Azure, AWS, and Google Cloud deployment targets.

## Generic cloud readiness checklist

A provider may be considered for future integration if it satisfies the following capabilities:

- encrypted data at rest
- encrypted data in transit
- region-aware storage and routing control
- identity and access policy enforcement
- auditability of access and mutations
- key management and rotation support
- retention / deletion controls
- support for export and portability
- support for geographic or legal compliance constraints
- clear isolation / tenancy boundary for patient data

## Provider categories

### Healthcare-native providers

These are explicitly health-data ecosystems and are the most relevant long-term targets for domain-specific adapters.

- Azure Health Data Services
- AWS HealthLake
- Google Cloud Healthcare API
- national or regional health data platforms
- FHIR-enabled provider ecosystems

### Generic cloud foundations

These are not healthcare-specific by design, but they can host health workloads when the right compliance and adapter layer is in place.

- Azure
- AWS
- Google Cloud

### Future ecosystem candidates

These are possible later additions, but they are not part of the current active implementation scope.

- OVHCloud
- Hetzner
- Aruba
- Huawei Health / wearable ecosystem
- other local or specialized healthcare systems

## Current roadmap

### Phase 1: FHIR-first canonical bridge

The active prototype focus is:

- define `HealthData` as the internal canonical model
- map FHIR resources to and from the internal model
- validate with sample payloads and simulation workflows

### Phase 2: main cloud adapter shapes

The sample now demonstrates the provider-facing adapter shapes without making live network calls.
Real integrations should only be implemented after each endpoint, authentication, data residency,
and compliance contract is defined.

Recommended initial adapters:

- Azure
- AWS
- Google Cloud

### Phase 3: wider ecosystem expansion

Only after the adapter contract is proven should the project consider additional platforms or
ecosystem-specific integrations, such as OpenHospital or wearable-health platforms.

## Compliance reference

For compliance readiness, use the Cloud Security Alliance ecosystem as a checklist reference rather than as a hardcoded list of active implementations.

Recommended references to keep in mind:

- CSA STAR
- Cloud Controls Matrix (CCM)
- region sovereignty and data residency controls
- jurisdiction-aware routing policies

## Design note

This document is intentionally a future-oriented map. It exists to frame possibilities without implying that those providers are already implemented or required in the current sample.
