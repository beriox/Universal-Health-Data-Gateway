from __future__ import annotations

from typing import Any, Dict

from CAPPY.adapters import FhirAdapter
from CAPPY.models import HealthData


class EuFhirAdapter(FhirAdapter):
    """Illustrative EU FHIR destination profile using the shared FHIR mapping."""

    provider_name = "eu-fhir"

    def write(self, health_data: HealthData) -> Dict[str, Any]:
        payload = super().write(health_data)
        payload["profile"] = "eu-fhir-baseline"
        return payload
