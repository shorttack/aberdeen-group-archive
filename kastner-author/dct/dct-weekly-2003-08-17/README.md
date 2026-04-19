# PC Deals Weekly Update: August 17, 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-08-17 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

Last week was a great time to customize a new desktop at www.dell.com. This week, Dimension desktop prices jolted upwards in some cases over $200. But this doesn't mean that other online retailers that allow customization have increased their prices.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 17 |
| technologies.csv | 9 |
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

Peter S. Kastner (2003). PC Deals Weekly Update: August 17, 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
