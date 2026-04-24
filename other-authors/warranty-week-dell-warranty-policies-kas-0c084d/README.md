# Dell's Warranty Policies

| Field | Value |
|-------|-------|
| Author | Eric Arnum |
| Date | 2003-05-12 |
| Type | trade-publication-analysis |
| Domain | Dell-warranty-policies-PC-buying-criteria |
| License | CC-BY-4.0 |

## Abstract

Warranty Week analyzes Dell's warranty policies. Peter S. Kastner, executive vice president and chief research officer for the Consumer Digital Technology Practice at Aberdeen Group, recommends enterprise PC buyers seek minimum three-year basic warranties with next-business-day on-site repair. Aberdeen's PC reference model specifies a 2.4 GHz Pentium 4, 256 MB RAM, 40 GB drive. Dell's Dimension/Inspiron consumer lines were cut to one-year coverage; OptiPlex/Latitude business lines retain three-year terms — a $129-$199 differential.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 6 |
| observations.csv | 11 |
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

Eric Arnum (2003). Dell's Warranty Policies.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

trade-publication-analysis, financial-disclosure-review, expert-quote-aggregation
