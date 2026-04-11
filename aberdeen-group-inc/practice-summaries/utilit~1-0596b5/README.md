# Utilities: 1998 Industry Practice Summary

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-05-01 |
| Type | other-research |
| Domain | utilities-IT |
| License | Aberdeen Group's 1998 practice summary covering information technology for electric and natural gas utilities facing deregulation. The document defines three practice pillars — Distribution (billing/CIS/call centers/meter networks), Asset Management (SCADA/EMS/ERP/GIS), and Transactions (energy trading/risk management/ISO systems) — and profiles 12 vendors. Key findings include that U.S. gas and electric utilities represent $300B in revenues; the last major U.S. monopoly being deregulated; and that conservative IT buying behavior will coexist with urgent spending on billing, CIS, and customer-facing systems. |

## Abstract

UTILIT~1.DOC

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 20 |
| technologies.csv | 12 |
| observations.csv | 20 |
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

Aberdeen Group (1998). Utilities: 1998 Industry Practice Summary.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis
