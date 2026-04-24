# Tech Bucks Trend, Hack Threats Up

| Field | Value |
|-------|-------|
| Author | Wired staff |
| Date | 2002-12-01 |
| Type | news-article |
| Domain | it-spending-security-recession |
| License | CC-BY-4.0 |

## Abstract

Wired covers IDC's 2003 IT-spending forecast (6% growth) and competing analyst views. Aberdeen Group's Peter Kastner counters that 6% IT growth is 'totally unsustainable in this economy,' placing his own forecast at 3%. The article also covers IDC's ten-trend list including security, wireless networking, and tech as utility.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 3 |
| observations.csv | 5 |
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

Wired staff (2002). Tech Bucks Trend, Hack Threats Up.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, expert-quote-aggregation
