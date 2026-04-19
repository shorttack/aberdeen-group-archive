# PC Deals Weekly Update: March 2, 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-03-02 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

Here Today, Gone Tomorrow We do a lot of online shopping in order to bring our PC Deals to you. Unfortunately, we can't be at the console 24x7, which is what really is necessary to keep tabs on this industry. Think airline ticket prices.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 6 |
| observations.csv | 20 |
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

Peter S. Kastner (2003). PC Deals Weekly Update: March 2, 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
