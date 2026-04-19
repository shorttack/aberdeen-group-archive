# PC Deals Weekly Update: June 8, 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-06-08 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

The retail world calls this time of year the "Dads and Grads" season. It's the last holiday on which retailers count to get them through the slow summer months until "Back to School" shopping frenzy beings in August. Surprisingly (to us, anyways), retailers do not seem to be giving desktops much attention.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 16 |
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

Peter S. Kastner (2003). PC Deals Weekly Update: June 8, 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
