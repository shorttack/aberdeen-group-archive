# Slow Growth For IT Spending In 2003

| Field | Value |
|-------|-------|
| Author | Gregg Keizer, Techweb News / InformationWeek |
| Date | 2003-01-03 |
| Type | news-article |
| Domain | IT-spending-outlook |
| License | CC-BY-4.0 |

## Abstract

InformationWeek article (Jan 3 2003) by Gregg Keizer summarizing Aberdeen Group's 2003 top tech trends forecast. Peter Kastner, Aberdeen's chief research officer, is the primary source: global IT spending up 4% in 2003 (up from <1% in 2002), back-end-loaded; outsourcing on-demand is the bright spot, driving deals like IBM-Deutsche Bank ($2.5B) and IBM-J.P. Morgan Chase ($5B); Kastner troubled by offshore outsourcing, calling it 'a horse of a completely different color and a potential economic threat to the livelihood of a lot of Americans.' Linux server growth 40% in 2003 (down from 50%+ in 2002); Linux desktop will still not break out and at best will overtake Apple at ~3% of enterprise market. Key Kastner aphorism: 'Ultimately, psychology and not technology will determine the growth rate for IT spending this year.'

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 5 |
| observations.csv | 10 |
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

Gregg Keizer, Techweb News / InformationWeek (2003). Slow Growth For IT Spending In 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, analyst-commentary
