# Data Warehouse Query Tools: Evolving to Relational OLAP

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1995-07-01 |
| Type | market-study |
| Domain | data-warehousing-OLAP |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group market viewpoint analyzing the evolution of data warehouse query tools toward relational OLAP (ROLAP), examining multidimensional analysis, vendor strategies, and convergence of OLAP and relational database technologies.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 20 |
| technologies.csv | 28 |
| observations.csv | 54 |
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

Aberdeen Group (1995). Data Warehouse Query Tools: Evolving to Relational OLAP.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis,competitive-profiling,benchmarking
