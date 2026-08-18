from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

try:
    from .models import Allergy, Consent, Encounter, HealthData, Medication, Observation, Patient
except ImportError:  # pragma: no cover - supports direct execution from this folder
    from models import Allergy, Consent, Encounter, HealthData, Medication, Observation, Patient


class HealthDataAdapter(ABC):
    """Base interface for every provider or ecosystem adapter."""

    @property
    @abstractmethod
    def provider_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def read(self, payload: Any) -> HealthData:
        """Translate provider-specific payload into the canonical internal model."""
        raise NotImplementedError

    @abstractmethod
    def write(self, health_data: HealthData) -> Any:
        """Translate canonical model back into provider-specific representation."""
        raise NotImplementedError


class FhirAdapter(HealthDataAdapter):
    """Adapter for FHIR-based health systems."""

    provider_name = "fhir"

    @staticmethod
    def _patient_name_to_text(patient_resource: Dict[str, Any]) -> str:
        names = patient_resource.get("name", [])
        if not names:
            return "Unknown Patient"
        first_name = names[0]
        given = " ".join(first_name.get("given", []))
        family = first_name.get("family", "")
        return " ".join(part for part in [given, family] if part).strip()

    def read(self, payload: Dict[str, Any]) -> HealthData:
        patient_resource = {}
        observations = []
        medications = []

        for entry in payload.get("entry", []):
            resource = entry.get("resource", {})
            resource_type = resource.get("resourceType")

            if resource_type == "Patient":
                patient_resource = resource
            elif resource_type == "Observation":
                observations.append(resource)
            elif resource_type == "MedicationStatement":
                medications.append(resource)

        patient_name = self._patient_name_to_text(patient_resource)
        patient_obj = Patient(
            id=patient_resource.get("id", "unknown-patient"),
            name=patient_name,
            birth_date=patient_resource.get("birthDate"),
            sex=patient_resource.get("gender"),
            country=(patient_resource.get("address", [{}])[0] or {}).get("country"),
            language=(patient_resource.get("communication", [{}])[0] or {}).get("language", {}).get("text"),
        )

        health_data = HealthData(
            patient=patient_obj,
            source="fhir",
            source_system="FHIR R4",
            metadata={"raw_payload_type": "Bundle"},
        )

        for obs in observations:
            health_data.observations.append(
                Observation(
                    code=obs.get("code", {}).get("coding", [{}])[0].get("code", "unknown"),
                    display=obs.get("code", {}).get("text", "Observation"),
                    value=obs.get("valueQuantity", {}).get("value") or obs.get("valueString"),
                    unit=obs.get("valueQuantity", {}).get("unit"),
                    effective_date=obs.get("effectiveDateTime"),
                    status=obs.get("status", "final"),
                )
            )

        for med in medications:
            med_obj = Medication(
                name=med.get("medicationCodeableConcept", {}).get("text") or "Medication",
                dose=(med.get("dosage", [{}])[0] or {}).get("text"),
                frequency=(med.get("dosage", [{}])[0] or {}).get("timing", {}).get("code", {}).get("text"),
                start_date=med.get("effectivePeriod", {}).get("start"),
                end_date=med.get("effectivePeriod", {}).get("end"),
            )
            health_data.medications.append(med_obj)

        return health_data

    def write(self, health_data: HealthData) -> Dict[str, Any]:
        patient_name = [{"family": health_data.patient.name.split()[-1], "given": health_data.patient.name.split()[:-1]}]
        bundle_entries = [
            {
                "resource": {
                    "resourceType": "Patient",
                    "id": health_data.patient.id,
                    "name": patient_name,
                    "gender": health_data.patient.sex,
                    "birthDate": health_data.patient.birth_date,
                }
            }
        ]

        for observation in health_data.observations:
            bundle_entries.append(
                {
                    "resource": {
                        "resourceType": "Observation",
                        "status": getattr(observation, "status", "final"),
                        "code": {
                            "coding": [{"code": getattr(observation, "code", "unknown")}],
                            "text": getattr(observation, "display", "Observation"),
                        },
                        "valueQuantity": {
                            "value": getattr(observation, "value"),
                            "unit": getattr(observation, "unit"),
                        },
                        "effectiveDateTime": getattr(observation, "effective_date"),
                    }
                }
            )

        for medication in health_data.medications:
            bundle_entries.append(
                {
                    "resource": {
                        "resourceType": "MedicationStatement",
                        "status": "active",
                        "medicationCodeableConcept": {"text": getattr(medication, "name", "Medication")},
                        "effectivePeriod": {
                            "start": getattr(medication, "start_date"),
                            "end": getattr(medication, "end_date"),
                        },
                        "dosage": [{
                            "text": getattr(medication, "dose") or "As prescribed",
                            "timing": {"code": {"text": getattr(medication, "frequency") or "Daily"}},
                        }],
                    }
                }
            )

        return {
            "resourceType": "Bundle",
            "type": "collection",
            "entry": bundle_entries,
            "source": health_data.source,
        }


class FSEAdapter(HealthDataAdapter):
    """Adapter for European FSE-like systems / public health infrastructures."""

    provider_name = "fse"

    def read(self, payload: Dict[str, Any]) -> HealthData:
        return HealthData(
            patient=payload["patient"],
            source="fse",
            source_system="FSE",
            metadata={"jurisdiction": payload.get("jurisdiction")},
        )

    def write(self, health_data: HealthData) -> Dict[str, Any]:
        return {
            "provider": "fse",
            "patient_id": health_data.patient.id,
            "country": health_data.patient.country,
            "observations": [obs.__dict__ for obs in health_data.observations],
        }


class CloudAdapter(HealthDataAdapter):
    """Generic adapter for cloud-based ecosystems and storage providers."""

    provider_name = "cloud"

    def __init__(self, cloud_name: str):
        self.cloud_name = cloud_name

    def read(self, payload: Dict[str, Any]) -> HealthData:
        patient = payload.get("patient")
        if isinstance(patient, dict):
            pat = Patient(**patient)
        else:
            pat = patient

        return HealthData(
            patient=pat,
            source=self.cloud_name,
            source_system=f"{self.cloud_name} Cloud",
            metadata={"cloud": self.cloud_name, "raw_payload_type": "cloud_record"},
        )

    def write(self, health_data: HealthData) -> Dict[str, Any]:
        return {
            "provider": self.cloud_name,
            "patient_id": health_data.patient.id,
            "record": health_data.to_dict(),
        }


class AzureCloudAdapter(CloudAdapter):
    """Azure-oriented cloud adapter."""

    provider_name = "azure"

    def __init__(self):
        super().__init__("azure")


class AwsCloudAdapter(CloudAdapter):
    """AWS-oriented cloud adapter."""

    provider_name = "aws"

    def __init__(self):
        super().__init__("aws")


class GoogleCloudAdapter(CloudAdapter):
    """Google Cloud-oriented cloud adapter."""

    provider_name = "google-cloud"

    def __init__(self):
        super().__init__("google-cloud")


class HealthDataGateway:
    """Routes health data through the appropriate provider adapter."""

    def __init__(self, adapters: Optional[List[HealthDataAdapter]] = None):
        self.adapters = adapters or []

    def register(self, adapter: HealthDataAdapter) -> None:
        self.adapters.append(adapter)

    def read(self, provider_name: str, payload: Any) -> HealthData:
        for adapter in self.adapters:
            if adapter.provider_name == provider_name:
                return adapter.read(payload)
        raise ValueError(f"No adapter registered for provider: {provider_name}")

    def write(self, provider_name: str, health_data: HealthData) -> Any:
        for adapter in self.adapters:
            if adapter.provider_name == provider_name:
                return adapter.write(health_data)
        raise ValueError(f"No adapter registered for provider: {provider_name}")
