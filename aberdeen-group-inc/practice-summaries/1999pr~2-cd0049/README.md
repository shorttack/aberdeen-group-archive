# Internal Memo: Template for Next Round of Practice Summaries

| Field | Value |
|-------|-------|
| Author | Wayne Kernochan |
| Date | 1999-04-11 |
| Type | other-research |
| Domain | IT-research-methodology |
| License | CC-BY-4.0 |

## Abstract

An internal Aberdeen Group memorandum from analyst Wayne Kernochan to Peter Kastner proposing a revised template for Aberdeen Practice Summary documents. The memo provides a detailed five-chapter master outline with worked examples drawn from NOS (Network Operating System) and NT/Intel server practice areas, and argues for recasting Practice Summaries as sales-oriented hot-topics vehicles. Two template versions are offered: a lightly revised version with prior-year examples and a more substantial revision emphasizing hot topics for 1999.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 16 |
| technologies.csv | 17 |
| observations.csv | 25 |
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

Wayne Kernochan (1999). Internal Memo: Template for Next Round of Practice Summaries.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, market-overview
