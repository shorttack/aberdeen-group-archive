# PC Deals Analysis: August 24-31, 2002

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-08-24 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

With three weeks to go in the back-to-school promotion season, the market is in the midst of adding enormous technology bang for the buyer's buck. Pentium 4 2.53 GHz high-end microprocessors, too expensive for PC Deals' mass-market focus to date, exploded onto our radar screen, while 2.26 GHz machines are now under $900. Led by Compaq, this week's deals include a 2.0A GHz Pentium 4 with monitor for under $750, and a 2.26 GHz machine with monitor for under $800.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 10 |
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

Peter S. Kastner (2002). PC Deals Analysis: August 24-31, 2002.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
