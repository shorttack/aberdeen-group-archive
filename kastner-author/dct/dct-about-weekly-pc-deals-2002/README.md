# About Aberdeen Weekly PC Deals

| Field | Value |
|-------|-------|
| Author | Caroline S. Kastner |
| Date | 2002-09-25 |
| Type | dct |
| Domain | dct/consumer-pc-retail |
| License | CC-BY-4.0 |

## Abstract

Program documentation for Aberdeen Group's Weekly PC Deals Section, describing methodology for tracking online retailers' lowest prices on name-brand PCs from Compaq, Dell, eMachines, Gateway, HP, and Sony. Defines nine price-point targets from $550 to $1,550+ reflecting the mass-market U.S. consumer PC segment, with weekly winner selection based on processor speed, memory, hard drive, optical drives, and bundled components.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 3 |
| observations.csv | 13 |
| codes.csv | 24 |

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

Caroline S. Kastner (2002). About Aberdeen Weekly PC Deals.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, industry-analysis
