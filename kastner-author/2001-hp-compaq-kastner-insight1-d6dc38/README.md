# The HP-Compaq Merger: If There's the Will, There's a Way

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2001-09-06 |
| Type | expert-report |
| Domain | IT Industry; M&A; Enterprise Computing |
| License | CC-BY-4.0 |

## Abstract

Aberdeen InSight dated September 6, 2001 analyzing the proposed HP-Compaq merger. Kastner identifies customer concern about inward focus, product-line redundancy across servers, Unix, and services, and urges outward customer focus as the key to success. Warns that Dell, IBM, and Sun will benefit if HP-Compaq loses customer focus during integration.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 5 |
| observations.csv | 18 |
| codes.csv | 29 |

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

Peter S. Kastner (2001). The HP-Compaq Merger: If There's the Will, There's a Way.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Customer interviews; expert analysis
