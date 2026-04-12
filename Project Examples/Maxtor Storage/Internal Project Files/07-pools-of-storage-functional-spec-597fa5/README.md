# Pools of Storage Decision Tool — Functional Specification (Aberdeen Internal)

| Field | Value |
|-------|-------|
| Author | Peter Kastner (executive sponsor); Jay Erikson (primary author) |
| Date | 2003-11-26 |
| Type | employer-record |
| Domain | midline-storage / ILM / software-development / Aberdeen-internal |
| License | CC-BY-4.0 |

## Abstract

Internal Aberdeen Group functional specification for the Pools of Storage Decision Tool — explicitly marked 'Do Not Share With Maxtor.' Version 1.0 dated November 25 2003 describing a guided decision support web application built in Microsoft ASP/SQL Server 2000 targeting Internet Explorer 5.5+ on Windows. The tool has four stages: Solution Workflow (recommend business process); Competitive Workflow (maturity grid positioning); Financial Framework (KPI analysis); and Case for Action (ROI/TCO calculation with PDF output). Planned development cost $23101.55 over 6 weeks with Aberdeen hosting 3 months.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 6 |
| observations.csv | 20 |
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

Peter Kastner (executive sponsor); Jay Erikson (primary author) (2003). Pools of Storage Decision Tool — Functional Specification (Aberdeen Internal).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review
