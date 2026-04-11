# Mid-Line Disk Storage: Emerging as Significant Cost-Saving Opportunity

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 2003-06-13 |
| Type | white-paper |
| Domain | Enterprise Storage / Information Lifecycle Management |
| License | CC-BY-4.0 |

## Abstract

Seminal Aberdeen Group white paper defining "mid-line storage" as a new enterprise storage tier between high-performance Fibre Channel/SCSI disks and tape. Based on primary research with 75 storage managers at $1B+ enterprises. Defines four-level storage pyramid with mid-line ATA disks as a distinct tier. Key findings: ATA disks offer 2-8x capacity of FC/SCSI at ~half the cost per GB; 75% of storage buyers moderately or highly likely to purchase mid-line storage; over 60% report data restorations more than once a year; over 80% face backup window problems. Introduces Information Lifecycle Management (ILM) framework. Authored by Peter Kastner and David Hill of Aberdeen Group; sponsored by Maxtor Corporation.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 15 |
| observations.csv | 40 |
| codes.csv | 36 |

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

Peter S. Kastner / Aberdeen Group (2003). Mid-Line Disk Storage: Emerging as Significant Cost-Saving Opportunity.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Primary market research; 75 face-to-face and telephone interviews with storage managers at companies $1B+ revenue; survey research; analyst field research
