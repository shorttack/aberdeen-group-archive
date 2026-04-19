# PC Deals Weekly Update: August 3, 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-08-03 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

A lot more deals appeared in this week's flyers from Best Buy and Circuit City, finally hailing the back-to-school buying frenzy. While HP, Sony, and eMachines all had multiple bundled offers, Compaq only had one desktop deal. We noticed an increase in Compaq's pricing on customized desktops at www.hpshopping.com, especially on Compaq monitors.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 17 |
| technologies.csv | 10 |
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

Peter S. Kastner (2003). PC Deals Weekly Update: August 3, 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
