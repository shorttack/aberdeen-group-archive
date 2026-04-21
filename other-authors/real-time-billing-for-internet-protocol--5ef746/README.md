# Real-Time Billing for Internet Protocol (IP) Services

| Field | Value |
|-------|-------|
| Author | International Engineering Consortium (IEC) tutorial |
| Date | 1998-12-01 |
| Type | white-paper |
| Domain | isp-billing-cmb-systems |
| License | CC-BY-4.0 |

## Abstract

International Engineering Consortium online tutorial (authored ~1998 based on IDC/Forrester projections cited for 2002-2003) on the shift from back-office batch Customer Management and Billing (CM&B) systems to real-time front-office systems for Internet service providers. Peter Kastner, chief research officer of Aberdeen Group, is quoted arguing that traditional 30-45 day billing cycles don't work in the Internet's 'dog-eat-dog competitive world' — ISPs need infrastructure allowing customers to 'turn on a dime, try new services right away.' Supporting data: IDC's 1997 estimate of 68 million web users worldwide; Forrester projection of a $58B US business Internet services market by 2003.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 4 |
| observations.csv | 7 |
| codes.csv | 24 |

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

International Engineering Consortium (IEC) tutorial (1998). Real-Time Billing for Internet Protocol (IP) Services.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, technology-tutorial
