# How Aberdeen Sees the Storage Pyramid Evolving

| Field | Value |
|-------|-------|
| Author | David Hill, Aberdeen Group |
| Date | 2002-10-01 |
| Type | market-study |
| Domain | enterprise-storage |
| License | CC-BY-4.0 |

## Abstract

David Hill's Fall 2002 presentation establishing Aberdeen Group's analytical framework for the four-tier storage pyramid evolution. Introduces a content-centric approach to storage architecture based on four principles (ageing, freezing, accumulation, redundancy) and maps content types (structured/semi-structured/unstructured) to appropriate storage tiers. Provides foundational intellectual basis for the Pools of Storage and midline storage category initiative.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 6 |
| observations.csv | 22 |
| codes.csv | 33 |

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

David Hill, Aberdeen Group (2002). How Aberdeen Sees the Storage Pyramid Evolving.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, content-taxonomy, storage-tiering-framework
