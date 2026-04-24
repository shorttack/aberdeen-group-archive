# VERITAS a Believer in Itanium

| Field | Value |
|-------|-------|
| Author | Clint Boulton |
| Date | 2004-06-08 |
| Type | news-article |
| Domain | Itanium-Linux-storage-software |
| License | CC-BY-4.0 |

## Abstract

VERITAS extends Foundation Suite 2.2 and Cluster Server 2.2 to Intel Itanium 2 on Red Hat Linux 3.0. IDC forecasts the Itanium-Linux server market reaching $2B by 2008. Aberdeen Group analyst Peter Kastner notes 400 applications have been certified on Itanium architecture — addressing the historical Itanium application-ecosystem complaint.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 13 |
| technologies.csv | 8 |
| observations.csv | 7 |
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

Clint Boulton (2004). VERITAS a Believer in Itanium.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, expert-quote-aggregation, vendor-spokesperson
