from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional

try:
    from .models import Consent, HealthData
except ImportError:  # pragma: no cover - supports direct execution from this folder
    from models import Consent, HealthData


@dataclass
class RoutingPolicy:
    jurisdiction: str
    allowed_regions: Optional[List[str]] = None
    requires_consent: bool = True
    max_retention_days: Optional[int] = None


class ComplianceEvaluator:
    """Minimal evaluator to decide whether a record can be routed."""

    def __init__(self, policy: RoutingPolicy):
        self.policy = policy

    def can_route(self, health_data: HealthData) -> bool:
        if not health_data.patient.country:
            return False

        if self.policy.allowed_regions and health_data.patient.country not in self.policy.allowed_regions:
            return False

        if self.policy.requires_consent:
            for consent in health_data.consents:
                if consent.subject == health_data.patient.id and consent.granted:
                    return True
            return False

        return True

    def route_decision(self, health_data: HealthData) -> Dict[str, object]:
        allowed = self.can_route(health_data)
        return {
            "allowed": allowed,
            "jurisdiction": self.policy.jurisdiction,
            "requires_consent": self.policy.requires_consent,
            "patient_id": health_data.patient.id,
        }
