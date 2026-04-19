# Dell Services — Discussion Materials

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (Executive VP, Research, Aberdeen Group) |
| Date | 2004-05-19 |
| Type | topic-analysis |
| Domain | IT-services-commoditization |
| License | CC-BY-4.0 |

## Abstract

Aberdeen discussion deck prepared for Dell executives analyzing the restructuring of IT professional services. Argues services are beginning a major cost restructuring mirroring US manufacturing 30 years prior, driven by offshore labor arbitrage, BPO/On Demand account control, and ERP-vendor hosted solutions. Proposes a four-stage partner-ecosystem maturity model and asks where Dell sits on that continuum.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 5 |
| observations.csv | 33 |
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

Peter S. Kastner (Executive VP, Research, Aberdeen Group) (2004). Dell Services — Discussion Materials.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, expert-opinion
