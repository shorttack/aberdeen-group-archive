# PC Deals Weekly Update: December 15, 2002

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-12-15 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

Our secret shoppers say eMachine's and Sony PC are the hot ticket at retail this week. EMachines, a consistent performer in the under-$1000 PC Deals prices bands, wins on - ta, dah - low price, according to store managers. No need for a lot of analysis on that observation, but we'll point out again that PC demand is price elastic, just like the economists tells us.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 8 |
| observations.csv | 15 |
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

Peter S. Kastner (2002). PC Deals Weekly Update: December 15, 2002.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
