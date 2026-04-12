# Mid-Line Disk Storage Emerging as Significant Cost-Saving Opportunity

| Field | Value |
|-------|-------|
| Author | Peter Kastner; David Hill / Aberdeen Group |
| Date | 2003-06-13 |
| Type | white-paper |
| Domain | enterprise-storage |
| License | CC-BY-4.0 |

## Abstract

The seminal Aberdeen Group white paper that defined and named the 'midline' storage tier — ATA-based online storage positioned between high-performance FC/SCSI disk arrays and magnetic tape. Based on 75 face-to-face and telephone interviews with storage managers at billion-dollar enterprises, it presented a four-level storage pyramid, documented that 75% of enterprise buyers were moderately or highly likely to purchase midline storage, and predicted that over 50% of enterprise data would eventually migrate to the midline tier. The paper established ILM principles (Ageing, Freezing, Accumulation, Redundancy) as the rationale for a new storage tier.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 10 |
| observations.csv | 40 |
| codes.csv | 33 |

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

Peter Kastner; David Hill / Aberdeen Group (2003). Mid-Line Disk Storage Emerging as Significant Cost-Saving Opportunity.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

primary-research, face-to-face-interviews, industry-analysis, expert-opinion, survey-research
