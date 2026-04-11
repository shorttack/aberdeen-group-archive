# Digital's VAX: Alive and Kicking With TPC Benchmarks

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1992-03-15 |
| Type | market-study |
| Domain | OLTP-benchmarking, minicomputer-price-performance |
| License | CC-BY-4.0 |

## Abstract

This Viewpoint section analyzes Digital Equipment Corporation's March 1992 VAX product-line price-performance realignment, using TPC-A benchmark data to show that Digital simultaneously rationalized pricing across its entire VAX range—from MicroVAX 3100 to VAX 6000—while achieving the industry's best price-performance at the entry level. Aberdeen concludes that Digital has deliberately repositioned the VAX as a commercial price-performance leader, tripling cost-efficiency since 1990 and becoming competitive not only with HP and IBM but also with emerging RISC vendors such as Sequent.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 8 |
| observations.csv | 15 |
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

Peter S. Kastner (1992). Digital's VAX: Alive and Kicking With TPC Benchmarks.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

benchmark-analysis, competitive-analysis, price-performance-modeling
