# PC Deals Weekly Update: January 19, 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-01-19 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

It's getting on to February. Intel has not changed microprocessor prices since November. As a result, we have not seen much of a downward trend in high-end configurations, such as the 2.8 GHz machines.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 17 |
| technologies.csv | 13 |
| observations.csv | 25 |
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

Peter S. Kastner (2003). PC Deals Weekly Update: January 19, 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
