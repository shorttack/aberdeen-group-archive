# Q1 2003 Worldwide and U.S. PC Shipments — IDC and Gartner Data

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-04-30 |
| Type | dct |
| Domain | dct |
| License | CC-BY-4.0 |

## Abstract

Compact worksheet summarizing Q1 2003 PC shipment statistics from IDC and Gartner: IDC reported 1.5% U.S. / 2.1% WW growth (third consecutive quarter of growth); Gartner reported 7.7% U.S. / 5.5% WW growth; Dell led at 30.7% U.S. share / 17.3% WW share with 5,989,000 units shipped (29% of which were consumer); HP had 19.5% U.S. / 15.8% WW share with 34% consumer mix but -6% growth; IBM at 5.4% WW; total industry shipments ~34.6M units worldwide. Gartner also forecast 6.6% WW IT spending growth for 2003.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 0 |
| observations.csv | 18 |
| codes.csv | 23 |

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

Peter S. Kastner (2003). Q1 2003 Worldwide and U.S. PC Shipments — IDC and Gartner Data.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis
