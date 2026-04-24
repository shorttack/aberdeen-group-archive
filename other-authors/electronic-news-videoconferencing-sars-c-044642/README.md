# Videoconferencing Booms on SARS Fears

| Field | Value |
|-------|-------|
| Author | Ry Crozier |
| Date | 2003-05-14 |
| Type | news-article |
| Domain | videoconferencing-SARS-supply-chain-2003 |
| License | CC-BY-4.0 |

## Abstract

Electronic News (Electronics News Australia) reports videoconferencing surge tied to SARS-driven travel bans. Aberdeen Group analysts Russ Craig and Peter Kastner warn that the entire electronics assembly industry has 'critical, no-second-source dependence' on China-made components — a vulnerability SARS could expose. They frame the supply-chain risk as solvable only via aggressive public-health response.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 2 |
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

Ry Crozier (2003). Videoconferencing Booms on SARS Fears.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, expert-quote-aggregation
