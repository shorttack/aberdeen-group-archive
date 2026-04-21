# SAP, Sybase Face Off

| Field | Value |
|-------|-------|
| Author | Doug Bartholomew, InformationWeek (Issue #564) |
| Date | 1996-01-29 |
| Type | news-article |
| Domain | enterprise-database-ERP |
| License | CC-BY-4.0 |

## Abstract

InformationWeek news story (Jan 29 1996, Issue #564) on a feud between SAP AG and Sybase Inc. over database support for SAP's R/3 ERP system. Sybase had promised in October 1995 that SAP R/3 would support its SQL Server System 11 database, but the support does not appear imminent: Mike Regan (GM applications support, Sybase Emeryville) says SAP decides the timing; Paul Wahl (EVP international marketing, SAP Walldorf) says the ball is in Sybase's court. The dispute centers on row-level locking, which Sybase System 10/11 does not support; SAP R/3 requires it for satisfactory multi-user performance. An anonymous former Sybase source describes row-level locking as 'a deal-breaker' for SAP. Peter Kastner, VP and analyst at Aberdeen Group Inc. in Boston, comments: 'There is no doubt Sybase is missing a huge amount of business with SAP. Just look at what a great business SAP has been for Informix.'

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 5 |
| observations.csv | 6 |
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

Doug Bartholomew, InformationWeek (Issue #564) (1996). SAP, Sybase Face Off.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, analyst-commentary
