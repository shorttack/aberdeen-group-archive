# Analysis of Intel Processor Prices in PC Deals (January 2003)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-01-15 |
| Type | dct |
| Domain | dct |
| License | CC-BY-4.0 |

## Abstract

Analysis of Intel Celeron and Pentium 4 processor price tiers observed in Aberdeen's PC Deals tracking from August 2002 through January 2003. Documents the bifurcation of P4 into 400 MHz and 533 MHz front-side-bus families, the introduction of hyperthreading 3.06 GHz P4, and the mechanics of older CPUs being pushed down price bands by new releases. Predicts near-term obsolescence of the P4 2.0 GHz.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 18 |
| observations.csv | 19 |
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

Peter S. Kastner (2003). Analysis of Intel Processor Prices in PC Deals (January 2003).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, price-series-analysis
