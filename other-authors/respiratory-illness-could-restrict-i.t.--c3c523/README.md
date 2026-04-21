# Respiratory Illness Could Restrict I.T. Supply Lines

| Field | Value |
|-------|-------|
| Author | Gregg Keizer, Techweb News, with Eric Chabrow and Marianne Kolbasuk McGee (InformationWeek) |
| Date | 2003-04-07 |
| Type | news-article |
| Domain | IT-supply-chain-pandemic-risk |
| License | CC-BY-4.0 |

## Abstract

InformationWeek news story (2003-04-07 issue) on the potential impact of SARS (severe acute respiratory syndrome) on IT hardware supply chains. Peter Kastner, an Aberdeen Group analyst, warns in a recent report that 'worst case, it could result in major supply-chain disruptions and another downdraft for an already challenged industry' — because much of the world's electronics manufacturing (including most AC-to-DC power supplies) is concentrated in Guangdong province, China, which is also where SARS broke out. IT consultant Joe Wetz (K-Lag Technology) reports that his team is already building hardware-delay buffers into project timelines, with longer delays requiring alternate sourcing.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 2 |
| observations.csv | 6 |
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

Gregg Keizer, Techweb News, with Eric Chabrow and Marianne Kolbasuk McGee (InformationWeek) (2003). Respiratory Illness Could Restrict I.T. Supply Lines.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, analyst-commentary
