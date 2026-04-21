# Tech Investor: Deflation, the dropping dollar, and tech

| Field | Value |
|-------|-------|
| Author | Eric Hellweg, CNN/Money |
| Date | 2003-05-21 |
| Type | column-opinion |
| Domain | macroeconomics-tech-sector |
| License | CC-BY-4.0 |

## Abstract

CNN/Money Tech Investor column (May 21 2003) by Eric Hellweg analyzing the 'toxic twins' of a weakening dollar (Treasury Secretary John Snow signaling departure from the strong-dollar policy) and deflation fears (April CPI down 0.3%, biggest drop in 19 months). Peter Kastner, chief research officer at Aberdeen Group, provides the central analyst voice on why deflation is the '800-pound gorilla in the room': 'Hardware manufacturers have to produce and sell a lot more units at a lower price to keep up on the revenue treadmill. Units are up almost 30 percent at Dell, but revenues were only up 18 percent.' Kastner argues the tech industry is 'inherently deflationary' and therefore more resilient than other sectors — but warns the unit-revenue gap will squeeze PC-maker margins.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 3 |
| observations.csv | 5 |
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

Eric Hellweg, CNN/Money (2003). Tech Investor: Deflation, the dropping dollar, and tech.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

macro-commentary, analyst-commentary
