# PC Deals Weekly Update: March 16, 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-03-16 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

Intel's Centrino wireless notebook launch was the hot topic in the industry this week. We covered the launch from the corporate buyer's prospective in a Hot Topic. First, can you help us out?

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 15 |
| technologies.csv | 8 |
| observations.csv | 25 |
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

Peter S. Kastner (2003). PC Deals Weekly Update: March 16, 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
