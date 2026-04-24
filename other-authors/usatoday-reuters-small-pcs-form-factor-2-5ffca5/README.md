# Small Is Huge in PCs These Days

| Field | Value |
|-------|-------|
| Author | Kenneth Li (Reuters) |
| Date | 2004-04-07 |
| Type | news-article |
| Domain | PC-form-factor-living-room-design |
| License | CC-BY-4.0 |

## Abstract

Reuters reports the rise of small-form-factor PCs designed for the living room. Gartner forecasts shipment volume rising from 1.2M units (2003) to 32.1M (2008). Peter Kastner of Aberdeen Group describes 'the next form factor battles being fought in the living room' as size and decor begin to matter. Gateway's 901 Family Room Media Center exemplified the trend at $1,000-2,000.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
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

Kenneth Li (Reuters) (2004). Small Is Huge in PCs These Days.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, expert-quote-aggregation, market-forecast
