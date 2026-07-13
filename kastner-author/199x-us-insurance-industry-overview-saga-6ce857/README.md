# U.S. Insurance Industry Overview

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (Chief Research Officer, Aberdeen Group) |
| Date | 1998 |
| Type | market-study |
| Domain | insurance-IT |
| License | CC-BY-4.0 |

## Abstract

This presentation profiles the late-1990s U.S. insurance industry for Software AG's North American middleware business, combining market sizing, business drivers, industry trends, and an insurance claims architecture example. It argues that insurance offers a large but demanding opportunity for SAGA SOM because insurers face disintermediation, e-commerce, Y2K, and data-management pressures while remaining skeptical of immature middleware and new suppliers. Prepared circa 1998, the deck also proposes partner categories spanning insurance ISVs and integrators.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 26 |
| technologies.csv | 11 |
| observations.csv | 40 |
| codes.csv | 27 |

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

Peter S. Kastner (Chief Research Officer, Aberdeen Group) (1998). U.S. Insurance Industry Overview.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, market-segmentation, expert-opinion
