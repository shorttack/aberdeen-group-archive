# Personal Information Technology — Aberdeen Practice Launch

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2001-09-01 |
| Type | dct |
| Domain | dct/practice-framework |
| License | CC-BY-4.0 |

## Abstract

Program-launch description of Aberdeen Group's Personal Information Technology practice, established by Peter Kastner in 2001. Articulates the nine market paradoxes driving the practice (PC commoditization, digital-device convergence, home-network emergence, 3G wireless, digital TV transition, in-home services needs), catalogs service offerings, technology segments, strategic market questions, key market trends, and the supplier coverage list (Microsoft, Intel, AMD, Compaq, Dell, HP, IBM, Sony, Toshiba, Apple, Gateway, Micron, AOL, Epson, Lexmark, Canon, Nvidia, Cirrus Logic).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 24 |
| technologies.csv | 16 |
| observations.csv | 23 |
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

Peter S. Kastner (2001). Personal Information Technology — Aberdeen Practice Launch.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis
