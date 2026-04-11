# Power Academy RDBMS Sales Training

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1996-01-23 |
| Type | benchmark |
| Domain | RDBMS-competitive-analysis |
| License | CC-BY-4.0 |

## Abstract

A comprehensive RDBMS competitive intelligence training deck prepared by Aberdeen Group for IBM's Power Academy in January 1996. The document provides detailed competitive analysis of six major RDBMS vendors (Computer Associates/Ingres, IBM DB2, Informix, Oracle, Sybase, Microsoft, Progress, Red Brick, and Software AG) across dimensions including scalability, distributed technology, open technology, development tools, other technologies, and supplier value-add. Financial data, market share, strengths, weaknesses, and IBM-specific selling tips are included.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 19 |
| technologies.csv | 33 |
| observations.csv | 45 |
| codes.csv | 29 |

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

Peter S. Kastner (1996). Power Academy RDBMS Sales Training.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

competitive-profiling, benchmarking, industry-analysis, expert-opinion
