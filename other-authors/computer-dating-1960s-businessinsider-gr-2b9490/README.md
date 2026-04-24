# This Is What 'Computer Dating' Looked Like In The 1960s

| Field | Value |
|-------|-------|
| Author | Aimee Groth |
| Date | 2011-07-10 |
| Type | topic-analysis |
| Domain | computing-history-1960s-IBM-1400-Operation-Match-TACT |
| License | CC-BY-4.0 |

## Abstract

Business Insider historical piece recounting the mid-1960s origins of computer dating: the Harvard-originated Operation Match (1965) and its New York follow-on Project TACT (Technical Automated Compatibility Testing) by Lewis Altfest and Robert Ross, running on an IBM 1400 Series computer for $5 per client. TACT spread across NYC before becoming the subject of a 1966 Brooklyn DA grand jury over student questionnaires. Cited as the direct ancestor of today's Match.com.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 3 |
| observations.csv | 6 |
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

Aimee Groth (2011). This Is What 'Computer Dating' Looked Like In The 1960s.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

historical-reporting, archival-research
