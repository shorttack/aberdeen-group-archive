# Microsoft Split Will Hit Users' Pockets

| Field | Value |
|-------|-------|
| Author | Linda Leung (Computing UK / vnunet.com) |
| Date | 2000-06-09 |
| Type | news-article |
| Domain | antitrust-remedies |
| License | CC-BY-4.0 |

## Abstract

Computing UK article on an Aberdeen Group analysis projecting that the Jackson court's proposed break-up of Microsoft into separate OS and applications companies would cost customers worldwide approximately $6.8bn over 10 years in price hikes, and $43bn total including $20bn in added integration costs for enterprises. Peter Kastner argues the break-up would impose 'enormous friction, delay, and uncertainty' on IT adoption.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 3 |
| observations.csv | 8 |
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

Linda Leung (Computing UK / vnunet.com) (2000). Microsoft Split Will Hit Users' Pockets.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, cost-modeling
