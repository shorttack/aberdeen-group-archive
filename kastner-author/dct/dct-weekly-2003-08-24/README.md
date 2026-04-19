# PC Deals Weekly Update: August 24, 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-08-24 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

Gateway lowered its prices on its 500S, 500X, and 500XL desktops by $100, making these models much more competitive. We suspect this much needed drop in Gateway's desktop prices comes as Dell announces price cuts ranging from 6% in consumer desktops to 22% for business servers. We were not sure how Dell's price cuts would be reflected in the Dimension models we configure for Pc Deals as Dell's prices have fluctuated in the past weeks.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 16 |
| technologies.csv | 6 |
| observations.csv | 23 |
| codes.csv | 25 |

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

Peter S. Kastner (2003). PC Deals Weekly Update: August 24, 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
