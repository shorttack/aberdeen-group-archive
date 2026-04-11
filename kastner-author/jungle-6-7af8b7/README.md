# Welcome to the RDBMS Jungle — Chapter 6

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 1995 |
| Type | consulting-report |
| Domain | RDBMS vendor competitive analysis; technology ratings; IBM DB2 positioning |
| License | CC-BY-4.0 |

## Abstract

Chapter 6 continuation of the RDBMS Jungle training deck. Reprises market size and supplier data from Chapters 1-5, then provides expanded competitive detail: vendor-by-vendor weakness analyses, RDBMS technology rating breakdowns (scalability, distributed data, open technology, development tools, other technologies, supplier solutions), ISV platform support data (IBM gaining Unix share at HP's expense in 1994), IBM RS/6000 + DB2 best-fit scenarios, and wrap-up on RDBMS market dynamics. 58-slide deck.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 25 |
| observations.csv | 42 |
| codes.csv | 32 |

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

Peter S. Kastner / Aberdeen Group (1995). Welcome to the RDBMS Jungle — Chapter 6.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

expert-analysis; competitive-intelligence; market-research
