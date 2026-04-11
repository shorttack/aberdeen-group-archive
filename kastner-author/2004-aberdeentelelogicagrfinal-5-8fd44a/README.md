# Aberdeen Group Consulting Agreement — Telelogic (February 2004)

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 2004-02-26 |
| Type | consulting-report |
| Domain | IT Research Services / Consulting Contract |
| License | CC-BY-4.0 |

## Abstract

Standard Aberdeen Group Client Service Agreement with Telelogic (Irvine, CA) for a 12-month Development Solutions program at the Gold service level. Contract dated February 26, 2004 for $25,000. Includes ad hoc phone inquiry (2 hrs/month), quarterly briefings, market visibility services (2 webinars with replay rights), access to publications library, survey research, and IT Access community. Also includes Schedule B: Executive White Paper on UML (Unified Modeling Language), 5-6 pages, based on interviews with 5 Telelogic users. Analyst assigned: Wayne Kernochan (VP Development Solutions). Sales Executive: Jim Schaffer.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 2 |
| observations.csv | 15 |
| codes.csv | 28 |

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

Aberdeen Group (2004). Aberdeen Group Consulting Agreement — Telelogic (February 2004).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Standard client service agreement; Development Solutions program; includes white paper research via 5 user interviews
