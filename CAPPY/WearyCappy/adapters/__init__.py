"""Illustrative wearable source adapters."""

from .apple_healthkit import AppleHealthKitAdapter
from .fitbit import FitbitAdapter
from .health_connect import HealthConnectAdapter
from .huawei_health_kit import HuaweiHealthKitAdapter

__all__ = [
    "AppleHealthKitAdapter",
    "FitbitAdapter",
    "HealthConnectAdapter",
    "HuaweiHealthKitAdapter",
]
