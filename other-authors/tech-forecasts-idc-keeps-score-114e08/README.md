# Tech Forecasts: IDC Keeps Score

| Field | Value |
|-------|-------|
| Author | Elisa Batista, Wired |
| Date | 2002-12-23 |
| Type | news-article |
| Domain | IT-spending-forecast |
| License | CC-BY-4.0 |

## Abstract

Wired article (Dec 23 2002) by Elisa Batista scoring IDC's 2002 tech-predictions report card and previewing IDC's 2003 forecast. IDC admitted it was off by a year in predicting a 2002 IT-spending recovery; now forecasts companies will replace outdated hardware in 2003 and projects 6% IT-spending growth. Competing analysts project closer to 3%. Craig Lawton (Boston Consulting Group) and Peter Kastner (Aberdeen Group) weigh in — Kastner credits IDC with correctly calling the Windows XP launch as a non-event: 'They did get that one right. Because it is a stable operating system, the Windows XP launch came and went without much brouhaha.' Article also covers Jupiter Research's warning that web-services hype had reached 'hysteria levels' with 82% of executives claiming their companies use web services in some capacity.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 3 |
| observations.csv | 6 |
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

Elisa Batista, Wired (2002). Tech Forecasts: IDC Keeps Score.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, analyst-commentary
