# Vista: How Soon Until Deployment?

| Field | Value |
|-------|-------|
| Author | David Garrett |
| Date | 2006-11-03 |
| Type | news-article |
| Domain | Windows-Vista-enterprise-deployment-cadence |
| License | CC-BY-4.0 |

## Abstract

NewsFactor reports analyst views on enterprise Vista adoption pace. Peter Kastner, Aberdeen vice-president and research director for enterprise technology, frames a three-year hardware-lifecycle 'cadence' that places full Vista deployment in 2010 as new Vista-laden machines replace XP. Kastner predicts Microsoft will stop shipping XP in small business retail systems in 2007, forcing Vista uptake. He disagrees with Gartner's recommendation that businesses wait until 2008.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 5 |
| observations.csv | 8 |
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

David Garrett (2006). Vista: How Soon Until Deployment?.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, expert-quote-aggregation, hardware-lifecycle-analysis
