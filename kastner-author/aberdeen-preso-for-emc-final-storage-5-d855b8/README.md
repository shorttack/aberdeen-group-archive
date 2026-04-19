# Accelerating the Process At Every Step — EMC-Aberdeen Workshop

| Field | Value |
|-------|-------|
| Author | Aberdeen Group (Peter S. Kastner) |
| Date | 2004-06-01 |
| Type | market-study |
| Domain | enterprise-storage |
| License | CC-BY-4.0 |

## Abstract

Aberdeen sales-acceleration deck prepared for EMC outlining a research-driven program to pull through storage solutions. Positions Pools of Storage and Information Lifecycle Management (ILM) as the CIO strategic agenda, argues the 'opening gun just went off' on ILM and predicts ILM will be the big storage-related market battle of the decade. Maps Q1 Storage Research findings on cost, consolidation, retention policies, regulation, and ILM.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 5 |
| observations.csv | 36 |
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

Aberdeen Group (Peter S. Kastner) (2004). Accelerating the Process At Every Step — EMC-Aberdeen Workshop.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, competitive-profiling, expert-opinion, framework-development
