# Data Knowledge: 1998 Practice Summary

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-07-01 |
| Type | other-research |
| Domain | data-management |
| License | Aberdeen Group's 1998 practice summary for the Data Knowledge and Complex Decision Support practice, covering data warehousing, data marts, OLAP, query/reporting/analysis tools, data mining, and Customer Relationship Management (CRM). The report frames these technologies as components of an enterprise Data Knowledge strategy and assesses their integration with CIS, ERP, and Electronic Commerce applications. Thirteen primary vendors receive detailed abstracts including NCR/Teradata, IBM, Oracle, Cognos, Business Objects, SAS, Arbor/Essbase, and MicroStrategy, plus a second tier of over a dozen additional suppliers. |

## Abstract

DSSUNE~1.DOC

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 28 |
| technologies.csv | 20 |
| observations.csv | 30 |
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

Aberdeen Group (1998). Data Knowledge: 1998 Practice Summary.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis
