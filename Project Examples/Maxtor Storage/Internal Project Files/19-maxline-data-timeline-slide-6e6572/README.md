# MaXLine in the Data Center Spectrum: Data Value vs. Duration Positioning Slide

| Field | Value |
|-------|-------|
| Author | Maxtor Corporation |
| Date | 2003-01-01 |
| Type | employer-record |
| Domain | storage-strategy / product-positioning |
| License | CC-BY-4.0 |

## Abstract

A single product positioning slide depicting MaXLine's placement in the enterprise data center storage spectrum along two axes: Data Value (high to low) and Data Duration (minutes to years). The slide defines three storage zones — Active Data (served by Atlas high-end SCSI), Recallable Data (served by MaXLine nearline/midline), and Archive Data (served by Tape) — and characterizes MaXLine's tier as medium-speed bulk storage with low cost per GB, network-attached sequential and random access, and moderate I/O performance. This is the core visual artifact of Maxtor's midline storage positioning strategy.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 8 |
| observations.csv | 15 |
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

Maxtor Corporation (2003). MaXLine in the Data Center Spectrum: Data Value vs. Duration Positioning Slide.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis
