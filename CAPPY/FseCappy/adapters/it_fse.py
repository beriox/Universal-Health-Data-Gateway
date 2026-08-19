from __future__ import annotations

from typing import Any, Dict

from CAPPY.adapters import FSEAdapter
from CAPPY.models import HealthData


class ItalianFseAdapter(FSEAdapter):
    """Illustrative Italian FSE destination profile."""

    provider_name = "it-fse"

    def write(self, health_data: HealthData) -> Dict[str, Any]:
        payload = super().write(health_data)
        payload["profile"] = "it-fse-placeholder"
        return payload
