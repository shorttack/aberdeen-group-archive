# Welcome to the RDBMS Jungle — Chapters 1-5

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 1995 |
| Type | consulting-report |
| Domain | RDBMS market dynamics; competitive analysis; vendor profiles; buyer needs |
| License | CC-BY-4.0 |

## Abstract

Core market-dynamics training deck for Informix sales reps, chapters 1-5. Covers: overall database market size ($20B WW, $5.5B RDBMS); market characteristics (9 RDBMS licenses per 10 multiuser servers); supplier profiles for Sybase, Computer Associates/Ingres, Informix, Oracle, IBM, and Microsoft; hardware partnership dynamics; RDBMS technology rating framework (scalability, distributed data, open access, development tools, other technologies, supplier solutions); and competitive weaknesses for each major RDBMS vendor. 64-slide deck — richest single document in the set.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 22 |
| observations.csv | 40 |
| codes.csv | 32 |

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

Peter S. Kastner / Aberdeen Group (1995). Welcome to the RDBMS Jungle — Chapters 1-5.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

expert-analysis; market-research; competitive-intelligence
