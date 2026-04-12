# Dell: Applying Its Business Value Model to Storage

| Field | Value |
|-------|-------|
| Author | David Hill; Peter S. Kastner |
| Date | 2004-05-01 |
| Type | case-analysis |
| Domain | enterprise-storage |
| License | CC-BY-4.0 |

## Abstract

This Aberdeen Group vendor profile examines how Dell applies its signature supply chain management and price/performance business model to enterprise storage in 2004. Co-authored by David Hill and Peter Kastner, the report covers the Dell|EMC CX product family (third-generation FC arrays), the new AX100 entry-level SATA SAN, Dell PowerVault NAS solutions, and Dell's software bundling and service integration strategies. Aberdeen concludes that Dell deserves a place at the business storage discussion table across all enterprise sizes.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 17 |
| technologies.csv | 18 |
| observations.csv | 36 |
| codes.csv | 40 |

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

David Hill; Peter S. Kastner (2004). Dell: Applying Its Business Value Model to Storage.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

vendor-profiling, competitive-analysis, product-analysis, financial-analysis
