# High Tech Monday Update: SARS and the Tech Stock Rally

| Field | Value |
|-------|-------|
| Author | Thomson Financial Corporate Group (via PR Newswire) |
| Date | 2003-04-07 |
| Type | news-article |
| Domain | IT-investment-outlook-supply-chain |
| License | CC-BY-4.0 |

## Abstract

Thomson Financial 'High Tech Monday Update' distributed via PR Newswire (Apr 7 2003) summarizing the prior week in technology stocks. The piece blends four themes: SARS impact on electronics manufacturers (Motorola closed a Singapore factory temporarily; Intel and HP shut Hong Kong offices briefly); Semiconductor Industry Association's 3.3% YoY worldwide sales decline (February); UBS Warburg caution on IT spending; and war-news-driven midweek rally. Peter Kastner, analyst at Aberdeen Group, is cited via Dow Jones Newswires on the SARS risk to tech supply chains: 'At a minimum, the SARS epidemic will cause schedule slippages and disrupt the aggressive growth plans that global electronics companies have for the affected geographies. Worst case, it could result in major supply-chain disruptions and another downdraft for an already challenged industry.' Barry Ritholtz (Maxim Group) and Peter Gottlieb (First Albany Asset Management) also quoted on rally dynamics.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 2 |
| observations.csv | 7 |
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

Thomson Financial Corporate Group (via PR Newswire) (2003). High Tech Monday Update: SARS and the Tech Stock Rally.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, analyst-commentary
