# The Strategic R/3 Solution for the Enterprise

| Field | Value |
|-------|-------|
| Author | Sequent Computer Systems |
| Date | 1996 |
| Type | benchmark |
| Domain | SAP-benchmarking, enterprise-servers |
| License | CC-BY-4.0 |

## Abstract

This vendor presentation by Sequent Computer Systems presents the SAP R/3 SD benchmark results achieved on the Sequent Symmetry SE70 SMP server running R/3 version 2.2d on both Windows NT and UNIX. The document positions the Sequent platform favorably versus HP, Sun/Cray, and IBM on user count, independent certification, and RDBMS CPU utilization.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
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

Sequent Computer Systems (1996). The Strategic R/3 Solution for the Enterprise.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

benchmarking, competitive-profiling
