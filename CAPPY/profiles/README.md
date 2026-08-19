# CAPPY Profiles

Profiles provide jurisdiction-aware configuration for CAPPY adapters.

Resolution order:

1. a country-specific overlay, such as `it` or `de`;
2. the shared `eu` baseline for EU countries without a custom overlay;
3. a future global or jurisdiction-specific profile for non-EU jurisdictions.

The files are architectural examples, not legal advice or complete implementations of national
health-data law. Concrete profiles should be reviewed with the relevant healthcare and compliance
stakeholders before use.

Example:

```python
from CAPPY.profiles import get_profile

profile = get_profile("FR")  # falls back to the EU baseline
```
