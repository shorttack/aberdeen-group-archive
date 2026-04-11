# Making the Corporate Platform Decision (ITT Hartford)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 1995 |
| Type | consulting-report |
| Domain | platform selection methodology; corporate IT strategy; desktop OS; workgroup server |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group consulting presentation for ITT Hartford on corporate platform decision-making. Background is 1994 Commercial Lines Coop review. Covers desktop OS selection (Windows 95 vs OS/2 Warp vs NT Workstation), workgroup OS strategy (Windows NT/AS and Novell NetWare), platform management, network management, groupware, electronic mail, and distributed software management. 9-slide deck.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 4 |
| observations.csv | 12 |
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

Peter S. Kastner / Aberdeen Group (1995). Making the Corporate Platform Decision (ITT Hartford).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

expert-consulting; risk-assessment
