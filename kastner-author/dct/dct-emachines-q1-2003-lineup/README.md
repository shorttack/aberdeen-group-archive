# eMachines Q1 2003 Product Lineup

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-01-15 |
| Type | dct |
| Domain | dct |
| License | CC-BY-4.0 |

## Abstract

Compact snapshot of the eMachines Q1 2003 desktop product lineup: T1842 ($399 Celeron 1.8 GHz), T2042 ($499 Celeron 2.0 GHz), T2260 ($599 Athlon XP 2200+), and T2460 ($649 Athlon XP 2400+). All ship with 128-256 MB memory, 40-60 GB HDD, CD-ROM or CD-RW/DVD optical, sold direct via www.emachines.com. Documents eMachines' successful sub-$500 value positioning at the bottom of the U.S. consumer PC market, which ultimately led to Gateway's 2004 acquisition of the company.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 1 |
| technologies.csv | 2 |
| observations.csv | 6 |
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

Peter S. Kastner (2003). eMachines Q1 2003 Product Lineup.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

competitive-profiling
