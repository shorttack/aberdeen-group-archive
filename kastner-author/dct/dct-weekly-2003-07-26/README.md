# PC Deals Weekly Update: July 26, 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-07-26 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

As of this week, PC Deals no longer follows pricing on old eMachines, HP, and Compaq desktops because these manufacturers have released new line-ups at prices that compete with the older models. Excellent deals can still be found on these clearance models at websites like www.hpshopping.com, www.pcconnection.com, and www.pcdeals.com. While desktop deals haven't been overly impressive for the past few weeks, we've noticed that prices on computer accessories have been excell...

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 16 |
| technologies.csv | 11 |
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

Peter S. Kastner (2003). PC Deals Weekly Update: July 26, 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
