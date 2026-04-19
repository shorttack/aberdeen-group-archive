# PC Deals Weekly Update: June 15, 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-06-15 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

Not all that much to comment on this week. With Father's Day past, the best deals are dwindling in number. We're not sure whether the normal lull in sales until back-to-school season starts in a month will mean retailers will lower prices or whether there will be fewer deals.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 14 |
| technologies.csv | 3 |
| observations.csv | 21 |
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

Peter S. Kastner (2003). PC Deals Weekly Update: June 15, 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
