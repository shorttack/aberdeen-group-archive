# PC Deals Weekly Update: March 23, 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-03-23 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

In PC Deals, the $1200 and $1400 price categories, previously hot spots for deals, have diminished to sparse pickings. Concurrently, a new group of systems has boomed in the over $1600 range. What does this all mean?

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 14 |
| technologies.csv | 10 |
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

Peter S. Kastner (2003). PC Deals Weekly Update: March 23, 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
