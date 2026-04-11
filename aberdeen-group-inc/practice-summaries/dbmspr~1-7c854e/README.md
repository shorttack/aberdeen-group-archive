# Data Management: 1998 Practice Summary

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-05-01 |
| Type | other-research |
| Domain | data-management |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group's 1998 practice summary on the Database Management Systems (DBMS) market, covering relational, object-relational, object, embedded, and mobile DBMS categories. The report surveys major vendors including Oracle, IBM, Informix, Sybase, Microsoft, and Computer Associates, assesses turbulent 1997 market dynamics including revenue stagnation among major vendors, and forecasts the impact of Windows NT, packaged applications, commoditization, and Internet technologies on DBMS market segmentation. Aberdeen predicts continued Oracle dominance on Unix, Microsoft SQL Server growth on NT, and emerging opportunities in business intelligence, mobile user, and Web content management segments.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 23 |
| technologies.csv | 22 |
| observations.csv | 30 |
| codes.csv | 25 |

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

Aberdeen Group (1998). Data Management: 1998 Practice Summary.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, market-overview
