# Business PC Deals: December 2002

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-12-02 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

For six months, Aberdeen has been publishing our research on consumer desktop PC price-values - the bang for the buck - at www.Aberdeen.com/PCDeals. Now, we are focusing our years of PC research on corporate PCs. Here are our current recommendations for small-medium business desktop PC buyers.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 10 |
| observations.csv | 18 |
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

Peter S. Kastner (2002). Business PC Deals: December 2002.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
