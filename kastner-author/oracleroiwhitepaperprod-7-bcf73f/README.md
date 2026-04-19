# Point Solutions Versus Integrated Oracle Applications: The Road to IT Investment ROI

| Field | Value |
|-------|-------|
| Author | Aberdeen Group (Katherine Jones, Tom Dwyer, Peter S. Kastner) |
| Date | 2001-06-01 |
| Type | white-paper |
| Domain | enterprise-software/integration-roi (Oracle-sponsored) |
| License | CC-BY-4.0 |

## Abstract

Oracle-sponsored Aberdeen Executive White Paper (June 2001) — SAME core research as study 6 ('Leaving Well Enough Alone', July 2001) but Oracle-branded. Conclusion substitutes 'Oracle provides such an application suite' for the vendor-neutral closing. Chronologically predates study 6 — this is likely the commissioned original; study 6 is the vendor-neutral generalization Aberdeen then released on its own behalf. Cites Beneficial Life and Indian Motorcycle (Oracle customers) only — drops Credit Suisse First Boston/Carreckers (PeopleSoft) and State of Michigan (Lawson) references that appear in study 6.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 24 |
| technologies.csv | 9 |
| observations.csv | 17 |
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

Aberdeen Group (Katherine Jones, Tom Dwyer, Peter S. Kastner) (2001). Point Solutions Versus Integrated Oracle Applications: The Road to IT Investment ROI.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, customer-interview, document-review
