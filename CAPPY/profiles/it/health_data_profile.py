"""Italian profile overlay on the shared EU baseline."""

from ..eu.health_data_profile import PROFILE as EU_PROFILE

PROFILE = {
    **EU_PROFILE,
    "profile_id": "it-fse-overlay",
    "jurisdiction": "IT",
    "national_override": "FSE",
}
