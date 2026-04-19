# PC Deals Weekly Update: December 30, 2002

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-12-30 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

You may have already read that this year's holiday season's sales yielded the lowest rate of growth in decades. Frankly, PC Deals is not surprised. As we've been reporting, the holiday PC deals have been disappointing, especially from usual deal winners like Dell.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 3 |
| observations.csv | 15 |
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

Peter S. Kastner (2002). PC Deals Weekly Update: December 30, 2002.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
