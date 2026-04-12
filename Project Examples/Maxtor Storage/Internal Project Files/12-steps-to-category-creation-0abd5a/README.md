# Steps to Category Creation

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 2003-01-01 |
| Type | market-study |
| Domain | enterprise-storage |
| License | CC-BY-4.0 |

## Abstract

Working draft of Aberdeen Group's 10-step category creation methodology presentation, developed for the Maxtor midline storage engagement circa 2003. Enumerates and briefly describes each step: Define, Differentiate, Debunk, Define argument/position/messages, Deliver to influencers, Create awareness, Evangelize, Measure and report, Let influencers take over, and Nurture. Includes several placeholder slides indicating this was a working/incomplete version.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 2 |
| observations.csv | 15 |
| codes.csv | 34 |

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

Aberdeen Group (2003). Steps to Category Creation.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

category-creation, market-strategy, methodology-framework
