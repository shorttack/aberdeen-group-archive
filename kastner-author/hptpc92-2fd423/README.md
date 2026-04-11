# HP Section: TPC Benchmark Viewpoint (Aberdeen Group, 1992)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 1992 |
| Type | market-study |
| Domain | OLTP-benchmarking, RISC-computing, commercial-price-performance |
| License | CC-BY-4.0 |

## Abstract

This section of Aberdeen's 1992 TPC Benchmark Viewpoint analyzes Hewlett-Packard's progress in the TPC benchmark arena, documenting HP's transformation from a company that did not consider itself a commercial performance leader to a frequent top-ranked contender in TPC price-performance. The analysis covers HP's simultaneous improvements on both MPE/iX and HP-UX operating systems sharing the same Precision RISC architecture, the rise of HP's ALLBASE RDBMS to serious-contender status, and the equalization of price-performance between HP's two OS platforms to remove the penalty of OS choice for buyers.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 6 |
| observations.csv | 7 |
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

Peter S. Kastner / Aberdeen Group (1992). HP Section: TPC Benchmark Viewpoint (Aberdeen Group, 1992).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

benchmark-analysis, competitive-analysis, price-performance-modeling
