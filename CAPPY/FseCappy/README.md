# FseCappy

Module for national and regional health-record gateway integrations.

The current adapters are illustrative destination profiles built on CAPPY's shared FHIR/FSE
mapping. They do not call public-authority endpoints or implement authentication yet.

Potential scope:

- FSE and regional FHIR profiles;
- jurisdiction-specific terminology and mapping rules;
- consent, authorization, and exchange contracts;
- future adapters agreed with public-health stakeholders.

Current examples:

- `EuFhirAdapter`: shared EU FHIR baseline;
- `ItalianFseAdapter`: Italian FSE-oriented overlay placeholder.

No live connector is implemented here yet.
