# Aberdeen Group Mutual Confidentiality Agreement Template

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 2000-01-01 |
| Type | employer-record |
| Domain | legal-documents-NDA |
| License | CC-BY-4.0 |

## Abstract

This is Aberdeen Group's standard Mutual Confidentiality Agreement template, governed by Massachusetts law. It establishes mutual obligations for confidentiality of proprietary information shared during potential business transactions, including a 24-month non-solicitation of employees clause, provisions for return/destruction of confidential information, and standard exceptions for publicly available information. The document is blank with placeholder fields for parties and dates.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 0 |
| observations.csv | 7 |
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

Aberdeen Group (2000). Aberdeen Group Mutual Confidentiality Agreement Template.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review
