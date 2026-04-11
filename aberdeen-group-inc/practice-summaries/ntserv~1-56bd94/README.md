# Windows NT Server: 1998 Practice Summary

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-05-01 |
| Type | other-research |
| Domain | windows-nt-server |
| License |  clustering (Microsoft Cluster Server/Wolfpack) |

## Abstract

Aberdeen Group's 1998 practice summary on the Windows NT Server market covering Intel-based server hardware and the NT operating environment. The report sizes the NT server hardware market at $6 billion in 1997 and projects 50% annual growth; it also covers SMP architectures

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 17 |
| technologies.csv | 14 |
| observations.csv | 23 |
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

Aberdeen Group (1998). Windows NT Server: 1998 Practice Summary.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis
