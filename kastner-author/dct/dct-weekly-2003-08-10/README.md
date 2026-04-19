# PC Deals Weekly Update: August 10, 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-08-10 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

This week launched the back-to-school season deals we've been expecting. Ads from Best Buy, Circuit City, Staples, CompUSA, and HP appeared in the Boston Globe. Not surprisingly, Best Buy and Circuit City led the pack with the most numerous and best priced offers.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 17 |
| technologies.csv | 10 |
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

Peter S. Kastner (2003). PC Deals Weekly Update: August 10, 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
