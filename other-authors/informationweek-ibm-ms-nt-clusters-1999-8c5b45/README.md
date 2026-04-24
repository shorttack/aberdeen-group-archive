# IBM, Microsoft Team On NT Clusters

| Field | Value |
|-------|-------|
| Author | InformationWeek staff |
| Date | 1999-05-21 |
| Type | news-article |
| Domain | windows-nt-clustering-enterprise-servers |
| License | CC-BY-4.0 |

## Abstract

InformationWeek reports IBM's TechEd '99 demonstration of an eight-server Windows NT cluster code-named 'Cornhusker'. The IBM clustering technology is compatible with Microsoft Cluster Services and certified initially only on IBM Netfinity NT servers. Peter Kastner, research director and EVP at Aberdeen Group, observes that an increasing number of enterprise customers are embracing NT-based clustering and being constrained by two-node limits, predicting warm reception for Cornhusker among critical-application operators.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 5 |
| observations.csv | 6 |
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

InformationWeek staff (1999). IBM, Microsoft Team On NT Clusters.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, expert-quote
