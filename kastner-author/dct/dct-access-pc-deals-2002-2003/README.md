# DCT Access PC Deals Database, 2002-2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-08-24 |
| Type | dct |
| Domain | dct |
| License | CC-BY-4.0 |

## Abstract

Aggregate Microsoft Access-derived database of weekly U.S. consumer desktop PC pricing from July 2002 through August 2003, covering 2,159 SKU-week listings across 10 canonical PC makers (Dell, HP, Compaq, Sony, eMachines, Gateway, Alienware, VPR Matrix, Medion, Best Buy house brand) and 23 canonical retail channels (Dell.com, BestBuy.com/stores, HP Shopping, Circuit City, CompUSA, Sony Style, Staples, MicroCenter, and others). Kastner built this as the canonical reference dataset for his Digital Consumer Technology weekly pricing commentary, capturing list price, CPU class/speed, memory, HDD, optical, monitor, printer, and merchant for each tracked configuration across 51 distinct pricing dates.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 32 |
| technologies.csv | 10 |
| observations.csv | 122 |
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

Peter S. Kastner (2003). DCT Access PC Deals Database, 2002-2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking
