# Midline Messaging Workshop Prep Guide

| Field | Value |
|-------|-------|
| Author | Peter Kastner, David Hill, John Boyne |
| Date | 2004-02-06 |
| Type | employer-record |
| Domain | enterprise-storage |
| License | CC-BY-4.0 |

## Abstract

Pre-workshop preparation guide distributed to Maxtor executives and core team before the February 13 2004 midline category creation workshop in Shrewsbury MA. Provides session goals and pre-read questions for three workshop sessions covering category definition, go-to-market strategy, and messaging finalization. Includes appendices defining Pools of Storage concepts and messaging foundations.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 6 |
| observations.csv | 20 |
| codes.csv | 34 |

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

Peter Kastner, David Hill, John Boyne (2004). Midline Messaging Workshop Prep Guide.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

workshop-facilitation, category-creation, stakeholder-engagement
