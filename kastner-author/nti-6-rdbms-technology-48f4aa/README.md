# RDBMS Report Card

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner, John Logan, Thomas Willmott |
| Date | 1993-04-01 |
| Type | market-study |
| Domain | relational-database-management |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group evaluates the role of relational database management systems (RDBMS) in enterprise computing, covering their use in OLTP and decision support. The study profiles six leading independent RDBMS vendors—Oracle, Ingres, Sybase, Informix, Software AG, and Progress—against seven functional criteria and produces a best-in-class report card. Aberdeen concludes that RDBMS has become the central application platform for enterprises and that Oracle leads the market while IBM's DB2 trails all competitors.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 16 |
| technologies.csv | 18 |
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

Peter S. Kastner, John Logan, Thomas Willmott (1993). RDBMS Report Card.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, technology-assessment, vendor-profiling
