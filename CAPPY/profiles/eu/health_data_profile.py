"""Shared EU baseline for jurisdiction-aware CAPPY adapters.

This is an architectural profile, not legal advice or a complete implementation
of GDPR, EHDS, or any national health-data gateway.
"""

PROFILE = {
    "profile_id": "eu-baseline",
    "jurisdiction": "EU",
    "standards": ["FHIR R4", "GDPR", "EHDS"],
    "requires_consent": True,
    "data_minimization": True,
    "audit_required": True,
    "national_override": None,
}
