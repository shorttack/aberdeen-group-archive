# Information Security: 1998 Practice Summary

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-05-01 |
| Type | other-research |
| Domain | information-security |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group's 1998 overview of the enterprise information security market, sizing it at $4.285 billion in 1997 with a projected 24% CAGR to $10 billion by 2000. The report maps the security landscape into access-control and risk-management categories, identifies fragmentation and non-interoperability as the dominant pain points, and forecasts consolidation, the rise of VPNs, and the commoditization of standalone firewalls. Supplier profiles cover 14 vendors including Check Point, Axent, Network Associates, IBM, and VeriSign.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 15 |
| technologies.csv | 10 |
| observations.csv | 24 |
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

Aberdeen Group (1998). Information Security: 1998 Practice Summary.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis
