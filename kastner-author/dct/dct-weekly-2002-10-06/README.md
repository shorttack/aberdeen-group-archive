# PC Deals Weekly Analysis: October 6, 2002

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-10-06 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

After two slow weeks after the end of the school buying season, this week sees a major rotation in the retail channel. As a result, caveat emptor! Buyers will want to make sure they get the latest technology at a good price, and not last summer's leftover inventory clearance.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 12 |
| observations.csv | 25 |
| codes.csv | 24 |

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

Peter S. Kastner (2002). PC Deals Weekly Analysis: October 6, 2002.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
