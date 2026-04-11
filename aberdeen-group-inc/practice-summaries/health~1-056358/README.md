# Healthcare: 1998 Industry Practice Summary

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-05-01 |
| Type | other-research |
| Domain | healthcare-IT |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group's 1998 survey of the Healthcare Information Systems (HIS) market, covering integrated HIS vendors, independent software vendors, professional services firms, and systems suppliers. The report maps the three application tiers—business, clinical, and management information—and assesses the impact of managed care consolidation, client-server adoption, Internet/intranet deployment, and Year 2000 compliance on healthcare IT buyers. Brief vendor profiles are provided for fifteen named companies.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 24 |
| technologies.csv | 14 |
| observations.csv | 25 |
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

Aberdeen Group (1998). Healthcare: 1998 Industry Practice Summary.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, market-overview
