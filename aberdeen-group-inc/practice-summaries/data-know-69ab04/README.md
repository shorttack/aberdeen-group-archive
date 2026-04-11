# Expanding the Data Knowledge Practice

| Field | Value |
|-------|-------|
| Author | Bob Moran |
| Date | 2000-01-01 |
| Type | other-research |
| Domain | data-management |
| License | Internal Aberdeen Group presentation by Research VP Bob Moran proposing expansion of the Data Knowledge practice covering decision support and knowledge management technologies (data warehouses, OLAP, query/reporting, data mining, CRM analytics, content management, personalization, and ETL). Includes market sizing data for 1999-2003 showing the total core tools market growing from $8.3B (1999) to $18.2B (2003) at 45% CAGR, and BI infrastructure from $1.2B to $2.6B at 29% CAGR. Also features vendor presentations from Oracle, Cognos, and Acxiom with financial data and strategic positioning. |

## Abstract

data know.ppt

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 13 |
| observations.csv | 21 |
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

Bob Moran (2000). Expanding the Data Knowledge Practice.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis
