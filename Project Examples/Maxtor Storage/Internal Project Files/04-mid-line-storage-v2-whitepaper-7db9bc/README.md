# Mid-Line Disk Storage Emerging As Significant Cost-Saving Opportunity

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 2003-08-01 |
| Type | white-paper |
| Domain | midline-storage / enterprise-storage / ILM |
| License | Aberdeen Group's Executive White Paper presenting the case for a new 'mid-line' disk storage tier using ATA technology positioned between high-performance FC/SCSI disk arrays and tape. Based on 75 face-to-face and telephone interviews with Fortune-class storage managers. The paper defines four tiers of the storage pyramid (high-performance disk / mid-line / near-line / tape) and argues that mid-line ATA disk can serve at least 20% of enterprise data — and potentially over half — at 50% lower cost per gigabyte. It also introduces information lifecycle management (ILM) as the strategic framework for multi-tier storage. |

## Abstract

04-Mid-Line-Storage-V2-WhitePaper.txt

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 10 |
| observations.csv | 34 |
| codes.csv | 29 |

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

Aberdeen Group (2003). Mid-Line Disk Storage Emerging As Significant Cost-Saving Opportunity.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

primary-research
