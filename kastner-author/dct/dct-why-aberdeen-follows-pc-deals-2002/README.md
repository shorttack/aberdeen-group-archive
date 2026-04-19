# Why Aberdeen Is Following Consumer PC Deals — DCT Practice Methodology

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-07-01 |
| Type | dct |
| Domain | DCT,PC-retail,pricing-methodology |
| License | CC-BY-4.0 |

## Abstract

Methodology paper explaining Aberdeen's Digital Consumer Technology practice approach to weekly consumer PC price tracking. Defines the research questions, six tracked brands (Compaq, Dell, eMachines, Gateway, HP, Sony), an 8-factor price-value hierarchy (CPU, memory, modem/NIC, HDD, monitor, OS, printer, software), and weekly commentary format. Acknowledges 90 days of prior tracking; explicitly excludes Apple (no head-to-head competition).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 14 |
| observations.csv | 19 |
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

Peter S. Kastner (2002). Why Aberdeen Is Following Consumer PC Deals — DCT Practice Methodology.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis,market-tracking,competitive-profiling
