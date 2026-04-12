# Aberdeen Group Disk Storage Usage Questionnaire (v1)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner; David Hill (Aberdeen Group) |
| Date | 2003-02-01 |
| Type | market-study |
| Domain | enterprise-storage / disk-tiering / ILM |
| License | CC-BY-4.0 |

## Abstract

First version of the Aberdeen Group telephone survey questionnaire developed for the Maxtor RAMP project measuring enterprise disk storage usage patterns and receptivity to a midline ATA storage tier. The 28-question instrument covers total disk capacity, utilization, architecture breakdown (internal DAS / external DAS / SAN / NAS), OS platform distribution, redundancy schemes (RAID / mirroring / snapshot / remote copy / tape), cold data identification, technology willingness assessment, backup window issues, and terminology awareness. A demographic section captures company scope, job titles, revenues, IT budget, CIO reporting structure, and industry vertical. This v1 instrument was subsequently refined into Maxtor Survey v2.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 12 |
| observations.csv | 27 |
| codes.csv | 26 |

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

Peter S. Kastner; David Hill (Aberdeen Group) (2003). Aberdeen Group Disk Storage Usage Questionnaire (v1).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

ramp-survey-design, telephone-survey, quantitative-research
