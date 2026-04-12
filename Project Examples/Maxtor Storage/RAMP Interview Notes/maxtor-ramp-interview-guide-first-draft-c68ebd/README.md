# Maxtor RAMP Interview Guide: First Draft

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner; David Hill (Aberdeen Group) |
| Date | 2003-03-01 |
| Type | market-study |
| Domain | enterprise-storage / disk-tiering / ILM |
| License | CC-BY-4.0 |

## Abstract

Structured face-to-face interview guide developed by Aberdeen Group for the Maxtor RAMP (Rapid Accurate Market Prediction) project validating a proposed midline ATA disk storage tier. The guide covers 16 general storage questions and 18 per-application questions across three application tiers (primary database, primary file-based, and third application), plus miscellaneous questions on terminology awareness and CIO reporting lines. The instrument was designed to probe enterprise storage architectures (DAS/SAN/NAS), data activity patterns, backup/recovery regimes, retention policies, and willingness to trade availability for cost savings on cold data.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 18 |
| observations.csv | 30 |
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

Peter S. Kastner; David Hill (Aberdeen Group) (2003). Maxtor RAMP Interview Guide: First Draft.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

interview-design, ramp-survey-design, qualitative-research
