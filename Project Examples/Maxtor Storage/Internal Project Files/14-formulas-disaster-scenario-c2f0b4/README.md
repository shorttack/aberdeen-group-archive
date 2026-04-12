# Formulas for Disaster Recovery Scenario

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 2003-01-01 |
| Type | case-analysis |
| Domain | enterprise-storage |
| License | CC-BY-4.0 |

## Abstract

Companion document to the downtime strategy formulas, applying similar financial modeling to disaster recovery scenarios. Defines a multi-stage recovery time model comparing old tape-based architecture to a new midline disk hybrid. Uses an online book/CD seller scenario (modeled on Amazon.com) with 50,000 customers/hour at $20-30/order to quantify revenue impact of improved recovery time. Models parallel disk/disk and disk/tape recovery paths to show New Way always recovers faster than Old Way, with minimum recovery time at 1/3 of Old Way.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 5 |
| observations.csv | 20 |
| codes.csv | 32 |

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

Aberdeen Group (2003). Formulas for Disaster Recovery Scenario.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

financial-modeling, disaster-recovery, tco-analysis
