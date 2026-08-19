"""Select a national profile, falling back to the shared EU baseline."""

from importlib import import_module
from typing import Dict

EU_COUNTRY_CODES = {
    "at", "be", "bg", "hr", "cy", "cz", "dk", "ee", "fi", "fr", "de",
    "gr", "hu", "ie", "it", "lv", "lt", "lu", "mt", "nl", "pl", "pt",
    "ro", "sk", "si", "es", "se",
}


def get_profile(country_code: str) -> Dict[str, object]:
    """Return a national overlay or the EU baseline for an EU country."""
    normalized = country_code.strip().lower()
    if len(normalized) != 2:
        raise ValueError("country_code must be a two-letter ISO code")

    try:
        module = import_module(f"CAPPY.profiles.{normalized}.health_data_profile")
    except ModuleNotFoundError as error:
        if error.name != f"CAPPY.profiles.{normalized}":
            raise
        if normalized not in EU_COUNTRY_CODES:
            raise ValueError(f"No CAPPY profile is defined for {country_code.upper()}") from None
        module = import_module("CAPPY.profiles.eu.health_data_profile")

    return dict(module.PROFILE)
