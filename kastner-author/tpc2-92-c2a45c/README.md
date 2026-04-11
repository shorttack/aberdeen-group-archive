# Here Come the Hot Boxes: Unix/RDBMS TPC-A Performance Analysis (1992)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 1992 |
| Type | market-study |
| Domain | Unix/RDBMS TPC Benchmarking / Price-Performance Competition |
| License | CC-BY-4.0 |

## Abstract

A brief 1992 Aberdeen Group section analyzing the emergence of Unix/RDBMS servers as leaders in TPC-A transaction processing price-performance benchmarks. Bull's DPX/2 and Sun's Sparcserver took TPC-A leadership positions pushing best price-performance below $10K/TPS-A, and Aberdeen explains why Unix/RDBMS vendors are increasingly favoring TPC-A over TPC-B for competitive benchmarking.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 6 |
| observations.csv | 10 |
| codes.csv | 27 |

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

Peter S. Kastner / Aberdeen Group (1992). Here Come the Hot Boxes: Unix/RDBMS TPC-A Performance Analysis (1992).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

benchmark-analysis, expert-opinion
