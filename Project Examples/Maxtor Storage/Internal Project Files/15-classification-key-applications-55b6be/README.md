# Classification of Key Applications by Storage Category

| Field | Value |
|-------|-------|
| Author | Aberdeen Group (David Hill) |
| Date | 2003-01-01 |
| Type | case-analysis |
| Domain | enterprise-storage |
| License | CC-BY-4.0 |

## Abstract

A concise classification matrix mapping eight major enterprise application types to their data access characteristics (read/write patterns and data structures). The framework distinguishes Traditional OLTP, Contemporary OLTP, Business Intelligence, Web Applications, Personal Productivity, Interactive Design, Unique Large Files, and Large File Distribution. This taxonomy serves as the foundational analytical framework supporting Maxtor's midline storage category creation project.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 10 |
| observations.csv | 15 |
| codes.csv | 26 |

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

Aberdeen Group (David Hill) (2003). Classification of Key Applications by Storage Category.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis
