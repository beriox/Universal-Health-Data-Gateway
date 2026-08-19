from __future__ import annotations

from typing import Any, Dict

from CAPPY.models import HealthData, Observation, Patient


class WearableAdapter:
    """Normalize a platform-neutral wearable payload into HealthData."""

    provider_name = "wearable"

    def read(self, payload: Dict[str, Any]) -> HealthData:
        patient = payload.get("patient") or {}
        patient_obj = patient if isinstance(patient, Patient) else Patient(
            id=patient.get("id", "unknown-patient"),
            name=patient.get("name", "Unknown Patient"),
            country=patient.get("country"),
            language=patient.get("language"),
        )
        health_data = HealthData(
            patient=patient_obj,
            source=self.provider_name,
            source_system=self.provider_name,
            metadata={"wearable": self.provider_name, "simulated": True},
        )
        for measurement in payload.get("measurements", []):
            health_data.observations.append(
                Observation(
                    code=measurement.get("code", measurement.get("type", "wearable")),
                    display=measurement.get("display", measurement.get("type", "Wearable measurement")),
                    value=measurement.get("value"),
                    unit=measurement.get("unit"),
                    effective_date=measurement.get("effective_date"),
                )
            )
        return health_data
