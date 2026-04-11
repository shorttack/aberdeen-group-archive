# Informix Software Overview

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 1995 |
| Type | consulting-report |
| Domain | RDBMS product portfolio; competitive positioning; Informix software architecture |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group overview of Informix Software for sales training. Covers company profile (Top-10 ISV, fastest-growing RDBMS company), full product portfolio (SE, OnLine, Dynamic Server, XPS, specialized variants), parallel DSA technology architecture, database middleware (replication, connectivity), tools revenue ($150M of $470M in 1994, 500K+ licenses), application development tools (NewEra, 4GL, SQL Suite, CLI/ESQL), end-user access, and services. 38-slide deck used in Informix sales training.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 17 |
| observations.csv | 30 |
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

Peter S. Kastner / Aberdeen Group (1995). Informix Software Overview.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

expert-analysis; product briefing
