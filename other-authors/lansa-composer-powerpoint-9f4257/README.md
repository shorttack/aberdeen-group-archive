# LANSA Composer: Practical Business Process Integration on System i (BPI/SOA)

| Field | Value |
|-------|-------|
| Author | LANSA (vendor authorship); Peter Kastner of Aberdeen Group and Mike Gilpin of Forrester Research (quoted) |
| Date | 2007-01-01 |
| Type | vendor-presentation |
| Domain | soa-bpi-system-i |
| License | CC-BY-4.0 |

## Abstract

LANSA marketing presentation promoting LANSA Composer as a practical Business Process Integration (BPI) and SOA solution for the IBM System i (iSeries/AS/400) midmarket. Deck opens with two quoted analyst endorsements: Mike Gilpin (Forrester) on web services and Peter Kastner (Aberdeen) on API/screen/message replacement as an on-ramp to SOA. Slides cover transport protocols, data transformation, process orchestration, and ESB/J2EE integration layers.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 7 |
| observations.csv | 7 |
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

LANSA (vendor authorship); Peter Kastner of Aberdeen Group and Mike Gilpin of Forrester Research (quoted) (2007). LANSA Composer: Practical Business Process Integration on System i (BPI/SOA).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

vendor-marketing, expert-opinion, technology-demonstration
