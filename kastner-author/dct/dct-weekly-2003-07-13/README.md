# PC Deals Weekly Update: July 13, 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-07-13 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

Nothing very exciting happening in desktop deals this week. Dell has replaced its Dimension 2350 with the newer 2400, but we have yet to notice any difference in these models other than a price drop. EMachines' and HP's newest desktops dominate the weekly deals flyers from Best Buy and Circuit City this week.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 16 |
| technologies.csv | 6 |
| observations.csv | 23 |
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

Peter S. Kastner (2003). PC Deals Weekly Update: July 13, 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
