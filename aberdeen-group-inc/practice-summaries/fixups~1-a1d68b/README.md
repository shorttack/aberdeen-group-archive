# Practice Summary Production Editing Notes

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-01-01 |
| Type | other-research |
| Domain | internal-production |
| License | CC-BY-4.0 |

## Abstract

A one-page internal Aberdeen Group checklist of formatting and structural corrections needed across multiple 1998 Practice Summary documents. Items cover Word style mapping (heading levels vs. Table of Contents behavior), page number format inconsistencies (Roman vs. Arabic), header/footer problems, and import artifacts (double spaces after periods). Named practice summaries requiring fixes include DBMS, Electronic Commerce, Systems Management, EC Professional Services, Managed Services, Middleware, and Networking.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 1 |
| observations.csv | 5 |
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

Aberdeen Group (1998). Practice Summary Production Editing Notes.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review
