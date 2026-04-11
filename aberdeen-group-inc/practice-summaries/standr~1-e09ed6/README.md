# Fax Cover Sheet — Kastner to Michael Lindgren

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2026-04-11 |
| Type | other-research |
| Domain | personal-administrative |
| License | CC-BY-4.0 |

## Abstract

A Microsoft Word fax cover sheet template populated with Peter S. Kastner's contact information at St. Andrew's Episcopal in Wellesley MA. The recipient is Michael Lindgren (fax 212-592-9426) and the subject is 'Claim' (5 pages total). The document appears to be a personal/administrative artifact with template boilerplate text instructing the user to replace it. Date field shows 4/11/2026 which likely reflects a system date artifact rather than actual transmission date.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 2 |
| observations.csv | 2 |
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

Peter S. Kastner (2026). Fax Cover Sheet — Kastner to Michael Lindgren.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review
