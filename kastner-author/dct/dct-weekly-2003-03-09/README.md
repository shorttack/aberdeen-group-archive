# PC Deals Weekly Update: March 9, 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-03-09 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

Looks like Compaq is putting out the best mid-range and high-end deals. With winners in the $900, $1050, $1200, and $1400 categories this week - and a decent showing at $600 and $750 - it looks like HP's branding of Compaq Presario's for consumers as "best value" machines is paying off. By far, the best deal of the week is the Compaq 6000T at BestBuy's configuration station.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 14 |
| technologies.csv | 8 |
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

Peter S. Kastner (2003). PC Deals Weekly Update: March 9, 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
