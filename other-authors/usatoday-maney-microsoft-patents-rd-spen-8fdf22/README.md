# Microsoft Spends a Bunch on Patents — But Is It Worth It?

| Field | Value |
|-------|-------|
| Author | Kevin Maney |
| Date | 2004-04-21 |
| Type | news-column |
| Domain | Microsoft-RD-patent-strategy |
| License | CC-BY-4.0 |

## Abstract

USA Today's Kevin Maney calculates Microsoft spent ~$9.5M per patent in 2003 — far more than IBM ($2.5M), HP, or Sun. Maney questions whether $5B+ annual R&D yields breakthrough products. Peter Kastner of Aberdeen Group defends Microsoft Research as underappreciated. The piece foregrounds the disconnect between research output and commercial mega-hits beyond Windows and Office.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 5 |
| observations.csv | 7 |
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

Kevin Maney (2004). Microsoft Spends a Bunch on Patents — But Is It Worth It?.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

tech-column, R-and-D-cost-analysis, expert-quote-aggregation
