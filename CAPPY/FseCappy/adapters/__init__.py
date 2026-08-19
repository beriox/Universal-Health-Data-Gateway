"""Illustrative FSE and FHIR destination adapters."""

from .eu_fhir import EuFhirAdapter
from .it_fse import ItalianFseAdapter

__all__ = ["EuFhirAdapter", "ItalianFseAdapter"]
