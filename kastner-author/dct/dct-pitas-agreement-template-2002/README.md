# Aberdeen PITAS (Personal Information Technology Awareness Service) 2002 Agreement Template

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-01-01 |
| Type | dct |
| Domain | DCT,agreement-template,vendor-awareness |
| License | CC-BY-4.0 |

## Abstract

Contract template (with <NAME><COMPANY> placeholders) for Aberdeen's Personal Information Technology Awareness Service (PITAS) 2002 program at $2,500/year. Deliverables: Supplier Snapshot on Aberdeen website, objective press quotes, analyst reference for press/investors, and bi-annual one-hour briefings. Principal analysts: Peter Kastner, Ethan Cohen, Isaac Ro. Includes renewal, reprint fees ($1/reprint), and legal liability provisions.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 4 |
| observations.csv | 13 |
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

Peter S. Kastner (2002). Aberdeen PITAS (Personal Information Technology Awareness Service) 2002 Agreement Template.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review
