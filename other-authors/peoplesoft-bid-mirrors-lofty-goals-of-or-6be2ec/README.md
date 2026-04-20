# PeopleSoft Bid Mirrors Lofty Goals of Oracle Chief

| Field | Value |
|-------|-------|
| Author | Steve Lohr (The New York Times) |
| Date | 2003-06-11 |
| Type | news-article |
| Domain | enterprise-software-ma |
| License | CC-BY-4.0 |

## Abstract

New York Times Business section feature (June 11, 2003) by Steve Lohr analyzing Oracle's $5.1B hostile bid for PeopleSoft in the context of Larry Ellison's ambition to replicate Microsoft's desktop dominance in the corporate data center. Peter S. Kastner (director of research, Aberdeen Group) provides the key analytical frame: the enterprise software market is 'way too complex, with way too many suppliers in the corporate kitchen,' and consolidation is needed. Kastner further argues 'Microsoft is heading inexorably upstream' and that keeping Microsoft from gaining data center share is a crucial strategic objective for Oracle.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 13 |
| technologies.csv | 7 |
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

Steve Lohr (The New York Times) (2003). PeopleSoft Bid Mirrors Lofty Goals of Oracle Chief.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, competitive-profiling, expert-opinion
