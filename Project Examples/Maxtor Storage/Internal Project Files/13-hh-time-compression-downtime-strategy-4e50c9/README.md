# Time Compression - Downtime Strategy: Formulas and Business Case

| Field | Value |
|-------|-------|
| Author | David Hill (HH), Aberdeen Group |
| Date | 2003-01-01 |
| Type | case-analysis |
| Domain | enterprise-storage |
| License | CC-BY-4.0 |

## Abstract

Working document containing financial formulas and a detailed business case for demonstrating TCO savings from migrating from traditional tape-based nearline storage to a midline disk plus tape combination. Models downtime reduction for a large financial services company with 1 million customers by quantifying backup time savings and customer revenue impact. Provides specific dollar-per-GB pricing for online (HDS 9980V at $31.60/GB) midline ($9.30/GB) and nearline disk/tape systems.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 5 |
| observations.csv | 18 |
| codes.csv | 31 |

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

David Hill (HH), Aberdeen Group (2003). Time Compression - Downtime Strategy: Formulas and Business Case.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

financial-modeling, tco-analysis, benchmark
