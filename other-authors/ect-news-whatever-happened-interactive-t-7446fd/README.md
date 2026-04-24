# Whatever Happened to Interactive TV?

| Field | Value |
|-------|-------|
| Author | Lou Hirsh |
| Date | 2002-06-25 |
| Type | news-feature |
| Domain | interactive-tv-market-failure-2002 |
| License | CC-BY-4.0 |

## Abstract

E-Commerce Times reporter Lou Hirsh examines why interactive TV (ITV) failed to materialize as a mass-market category circa 2002. Aberdeen Group chief research officer Peter Kastner argues consumer time and dollars have shifted to broadband Internet and that interactive gaming from Microsoft and Sony will not require a TV set. Kastner predicts ITV capabilities must be built into future TV sets because consumers won't pay extra for set-top hardware on existing TVs.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 5 |
| observations.csv | 4 |
| codes.csv | 23 |

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

Lou Hirsh (2002). Whatever Happened to Interactive TV?.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-feature, expert-quote-aggregation
