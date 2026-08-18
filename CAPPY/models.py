from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class Patient:
    id: str
    name: str
    birth_date: Optional[str] = None
    sex: Optional[str] = None
    country: Optional[str] = None
    language: Optional[str] = None


@dataclass
class Observation:
    code: str
    display: str
    value: Any
    unit: Optional[str] = None
    effective_date: Optional[str] = None
    status: str = "final"


@dataclass
class Medication:
    name: str
    dose: Optional[str] = None
    frequency: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None


@dataclass
class Allergy:
    substance: str
    reaction: Optional[str] = None
    severity: Optional[str] = None


@dataclass
class Encounter:
    id: str
    type: str
    status: str = "finished"
    start: Optional[str] = None
    end: Optional[str] = None
    facility: Optional[str] = None


@dataclass
class Consent:
    subject: str
    scope: str
    granted: bool = True
    valid_from: Optional[str] = None
    valid_to: Optional[str] = None
    jurisdiction: Optional[str] = None


@dataclass
class HealthData:
    patient: Patient
    observations: List[Observation] = field(default_factory=list)
    medications: List[Medication] = field(default_factory=list)
    allergies: List[Allergy] = field(default_factory=list)
    encounters: List[Encounter] = field(default_factory=list)
    consents: List[Consent] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    source: Optional[str] = None
    source_system: Optional[str] = None
    captured_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "patient": self.patient.__dict__,
            "observations": [obs.__dict__ for obs in self.observations],
            "medications": [med.__dict__ for med in self.medications],
            "allergies": [allergy.__dict__ for allergy in self.allergies],
            "encounters": [encounter.__dict__ for encounter in self.encounters],
            "consents": [consent.__dict__ for consent in self.consents],
            "metadata": self.metadata,
            "source": self.source,
            "source_system": self.source_system,
            "captured_at": self.captured_at,
        }
