# OLTP Market Analysis for Encore Computer Series 90

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1990-01-01 |
| Type | market-study |
| Domain | OLTP-applications, commercial-computing-market |
| License | CC-BY-4.0 |

## Abstract

This reference catalog, prepared for Encore Computer's Series 90 engagement, surveys OLTP application requirements across major vertical markets including manufacturing, distribution, banking, insurance, retail, and government, documenting typical transaction volumes, leading application software vendors, and competitive hardware suppliers for each segment. The catalog serves as a structured market intelligence resource mapping vertical OLTP demand to hardware capability requirements, supporting Encore's commercial go-to-market planning. Coverage spans applications from shop floor control and MRP to online banking and airline reservation systems.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 8 |
| observations.csv | 18 |
| codes.csv | 23 |

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

Peter S. Kastner (1990). OLTP Market Analysis for Encore Computer Series 90.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-research, vertical-market-analysis, application-cataloging
