"""German profile overlay on the shared EU baseline."""

from ..eu.health_data_profile import PROFILE as EU_PROFILE

PROFILE = {
    **EU_PROFILE,
    "profile_id": "de-health-overlay",
    "jurisdiction": "DE",
    "national_override": "DE-specific gateway and terminology rules",
}
