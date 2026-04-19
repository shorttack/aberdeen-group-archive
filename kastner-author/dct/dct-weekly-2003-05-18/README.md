# PC Deals Weekly Update: May 18, 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-05-18 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

As we stated last week in this column, prices on PCs with Intel Pentium 4 Hyper-Threading technology have been falling into quite affordable price points. In response to these price decreases PC Deals has decided to eliminate the separate Hyper-Threading (HT) category at the bottom of our weekly spreadsheet. From now on we will place HT machines along side "regular" P4 machines and compare all PCs side-by-side by price.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 16 |
| technologies.csv | 7 |
| observations.csv | 22 |
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

Peter S. Kastner (2003). PC Deals Weekly Update: May 18, 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
