# Traveling With Centrino

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-05-28 |
| Type | dct |
| Domain | dct |
| License | CC-BY-4.0 |

## Abstract

Hands-on review after two months of travel with a Gateway 450 Intel Centrino notebook. Covers the Pentium M + chipset + WiFi Centrino platform architecture, 15in 1400x1050 screen trade-offs, 6.2lb weight versus preferred thin-and-light 4lb class, 1.5 GHz performance versus Pentium III/P4 desktops, battery life including DVD playback plus work day, WiFi range improvements including a Cometa McDonald's hotspot picked up from a 15th-floor hotel room across the street, and corporate 3-notebooks-per-7-desktops adoption forecast.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 14 |
| observations.csv | 19 |
| codes.csv | 26 |

## Load with Python

```python
import pandas as pd
studies = pd.read_csv('data/studies.csv')
observations = pd.read_csv('data/observations.csv')
```

## Validate

```bash
frictionless validate datapackage.json
```

## Citation

Peter S. Kastner (2003). Traveling With Centrino.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

product-review, field-test
