# Aberdeen Group Overview — Mercury One-2-One

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (Aberdeen Group) |
| Date | 1996 |
| Type | employer-record |
| Domain | employer/aberdeen-group |
| License | CC-BY-4.0 |

## Abstract

This nine-slide deck is a corporate and capabilities overview for Aberdeen Group that was customized for Mercury One-2-One. It summarizes Aberdeen's charter, research practices, technology-practice taxonomy, solution focus areas, and custom consulting offerings rather than presenting a deep analytic study. As an employer-record for Aberdeen Group, it functions as a capabilities-overview and records Peter S. Kastner in the Vice President role context supplied for this ingest.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 9 |
| observations.csv | 12 |
| codes.csv | 23 |

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

Peter S. Kastner (Aberdeen Group) (1996). Aberdeen Group Overview — Mercury One-2-One.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review
