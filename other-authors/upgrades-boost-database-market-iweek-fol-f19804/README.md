# Upgrades Boost Database Market (data mining and SGI-IBM rivalry)

| Field | Value |
|-------|-------|
| Author | John Foley |
| Date | 1996-04-15 |
| Type | news-article |
| Domain | database-market-data-mining-1996 |
| License | CC-BY-4.0 |

## Abstract

InformationWeek (Issue 575) reporting Silicon Graphics' data-mining entry against IBM at DB Expo, San Francisco. Context: Sybase and Informix warned on Q1 1996 revenue, triggering double-digit share-price declines (Informix -28% in one day). Kastner (Aberdeen Group analyst) calls the sell-off 'a wrong conclusion' from individual situations — argues database leaders remain solid double-digit growers. Oracle then reassured analysts, sparking database-stock rebound.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 7 |
| observations.csv | 8 |
| codes.csv | 28 |

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

John Foley (1996). Upgrades Boost Database Market (data mining and SGI-IBM rivalry).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, analyst-quote-aggregation, market-analysis
