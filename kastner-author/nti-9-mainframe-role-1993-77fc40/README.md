# The Role of the Mainframe

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner, John Logan, Thomas Willmott |
| Date | 1993-05-01 |
| Type | market-study |
| Domain | mainframe-computing |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group objectively evaluates the declining role of the IBM ES/9000 mainframe in enterprise computing, contrasting it with Unisys A-Series growth. The study analyzes the paradox of increasing mainframe MIPS adoption alongside financial losses, software economics failures, and the blending of mainframe and midrange hardware capabilities. Aberdeen concludes that IBM mainframes will gradually be phased out and recommends either evolutionary (surround, rehost, rewrite) or green-field replacement strategies for IS executives.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 19 |
| technologies.csv | 14 |
| observations.csv | 29 |
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

Peter S. Kastner, John Logan, Thomas Willmott (1993). The Role of the Mainframe.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, technology-assessment, vendor-profiling
