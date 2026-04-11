# Software Market Dynamics

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1995 |
| Type | white-paper |
| Domain | software-market-analysis |
| License | CC-BY-4.0 |

## Abstract

This presentation by Peter S. Kastner, Vice President at Aberdeen Group, surveys mid-1990s software market dynamics across five domains: operating systems, database management, client-server application development, client-server application solutions, and enterprise information systems management. Kastner argues that software is evolving faster than typical enterprises can absorb change, and identifies key market transitions and investment opportunities in areas such as RDBMS growth, Windows NT ascendancy, and EISM consolidation.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 16 |
| observations.csv | 30 |
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

Peter S. Kastner (1995). Software Market Dynamics.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, expert-opinion, trend-analysis
