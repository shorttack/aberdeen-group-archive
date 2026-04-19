# PC Deals Weekly Update: June 22, 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-06-22 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

June 18th, HP announced it's newest addition to its desktop line-up, the m200 series. This Media Center PC series has both retail and online customized versions, starting at under $999. Customizing a m200 series desktop will allow consumers to choose from the full range of Intel's Hyper-Threading (HT) processors, including the brand new 3.2 GHz processor.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 15 |
| technologies.csv | 4 |
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

Peter S. Kastner (2003). PC Deals Weekly Update: June 22, 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
