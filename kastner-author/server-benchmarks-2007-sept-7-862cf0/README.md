# Intel and AMD Server Benchmarks (September 2007)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2007-09-01 |
| Type | benchmark |
| Domain | server-cpu-benchmarks/intel-vs-amd |
| License | CC-BY-4.0 |

## Abstract

Kastner-authored Excel spreadsheet comparing Intel Xeon 7140M dual-core, Xeon 7350 quad-core, and AMD Opteron 8220se dual-core and Barcelona 8222 across SQL Server database, ERP SAP-SD, Java SPECjbb, Integer SPECint_rate_2006, and SPEC webserver 2005 benchmarks. Includes DP chipset RAS feature comparison for Intel 5000X, 5000P, and 5000V. Primary document of Intel's quad-core lead over AMD's first-generation Barcelona in 2007.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 11 |
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

Peter S. Kastner (2007). Intel and AMD Server Benchmarks (September 2007).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

benchmarking, competitive-profiling
