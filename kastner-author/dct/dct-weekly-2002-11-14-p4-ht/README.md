# PC Deals Special: Pentium 4 with HyperThreading

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-11-14 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

HT technology works by providing hardware support for a second executing compute task. There is still only a single central processor unit (CPU). But HT provides a second ready task with the hardware-assist needed to quickly swap from one task to another.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 6 |
| observations.csv | 15 |
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

Peter S. Kastner (2002). PC Deals Special: Pentium 4 with HyperThreading.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
