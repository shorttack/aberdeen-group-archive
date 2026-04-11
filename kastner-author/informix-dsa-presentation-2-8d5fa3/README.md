# Choosing The Right Markets and the Right Partners for Informix

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 1995-1996 |
| Type | consulting-report |
| Domain | market segmentation; channel strategy; client-server solutions; RDBMS vertical markets |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group analysis of the optimal markets and channel partners for Informix. Covers industry trends (open systems, RAD, distributed computing, client-server), customer decision-making dynamics, CSS market characteristics with pricing tiers ($500-$150k/module by company size), and detailed channel partner assessments (VARs, ISVs, OEMs, SIs, Big 6). Includes vertical market ratings for telecomm, retail, banking, manufacturing, and state/local government. 67-slide deck used in Informix sales training.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 13 |
| technologies.csv | 10 |
| observations.csv | 30 |
| codes.csv | 33 |

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

Peter S. Kastner / Aberdeen Group (1995). Choosing The Right Markets and the Right Partners for Informix.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

expert-analysis; market segmentation; channel strategy
