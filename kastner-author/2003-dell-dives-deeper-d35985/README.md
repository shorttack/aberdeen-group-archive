# Aberdeen: Dell dives deeper, wider into enterprise

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-04-16 |
| Type | authored-column |
| Domain | enterprise-computing |
| License | CC-BY-4.0 |

## Abstract

Kastner-authored analyst column 'special to SearchCIO.com' (published on searchdatamanagement.techtarget.com). Reviews Dell's enterprise push via its partnerships with Oracle, EMC, Intel, and Microsoft following Dell's FY2003 $35.4B in sales. Details Dell's Oracle 9i reseller program extension to Europe and Asia, Dell/EMC CX200/CX400/CX600 storage program with petabytes sold to 2,500 new customers, and Dell's 46-70% TCO advantage running Intel+Windows vs Unix servers. Concludes Dell will gain share in OLTP, messaging, data warehouse, and file/print markets as the IT megatrend favors standards-based computing.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 7 |
| observations.csv | 13 |
| codes.csv | 27 |

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

Peter S. Kastner (2003). Aberdeen: Dell dives deeper, wider into enterprise.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, competitive-profiling
