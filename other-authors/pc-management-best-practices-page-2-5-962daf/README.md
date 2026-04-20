# PC Management Best Practices: A Study of the Total Cost of Ownership, Risk, Security, and Audit (IIA Research Foundation feature)

| Field | Value |
|-------|-------|
| Author | The IIA Research Foundation (RF Report, Issue No. 6) |
| Date | 2004-02-01 |
| Type | newsletter |
| Domain | PC-management-audit |
| License | CC-BY-4.0 |

## Abstract

The Institute of Internal Auditors Research Foundation biannual RF Report (February 2004, Issue No. 6) featuring the Foundation's new research report 'PC Management Best Practices: A Study of the Total Cost of Ownership, Risk, Security, and Audit' by Mark Salamasick and Charles Le Grand (2003). Peter Kastner (EVP and chief research officer, Aberdeen Group) is quoted from a technology forum: vulnerable machines may be called negligence; older PCs actually cost more to operate; and the optimal desktop lifecycle is three years, matching the duration of a standard warranty.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 5 |
| observations.csv | 7 |
| codes.csv | 28 |

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

The IIA Research Foundation (RF Report, Issue No. 6) (2004). PC Management Best Practices: A Study of the Total Cost of Ownership, Risk, Security, and Audit (IIA Research Foundation feature).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

editorial-coverage, expert-opinion, industry-analysis
