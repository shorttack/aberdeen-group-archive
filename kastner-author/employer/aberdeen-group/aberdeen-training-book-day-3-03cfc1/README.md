# How To Write A Profile and How To Conduct A RAMP

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 2000-06 |
| Type | employer-record |
| Domain | IT market research methodology; analyst deliverable production; RAMP engagement |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group's Day 3 training manual for new analyst hires. Covers how to write Aberdeen Profiles (objective third-party supplier assessments), how to conduct a RAMP (Rapid Accurate Market Positioning) engagement, and how to communicate research results to clients and media. Documents the anatomy of Aberdeen's core deliverables: Profile, RAMP, Impact, Viewpoint, Executive Briefing Paper, and White Paper. Provides interview techniques, writing standards, and client management guidelines. Represents Aberdeen's core methodology documentation circa 2000.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 5 |
| observations.csv | 33 |
| codes.csv | 51 |

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

Peter S. Kastner / Aberdeen Group (2000). How To Write A Profile and How To Conduct A RAMP.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

internal-training
