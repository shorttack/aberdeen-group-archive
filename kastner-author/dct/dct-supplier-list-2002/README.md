# Digital Consumer Technology Supplier List (2002)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-01-23 |
| Type | dct |
| Domain | dct/supplier-taxonomy |
| License | CC-BY-4.0 |

## Abstract

Aberdeen's four-category taxonomy of the Digital Consumer Technology (DCT) supplier landscape as of early 2002, spanning PCs & peripherals, networks & automation, applications & services, and leisure & entertainment. Catalogs 150+ named suppliers organized by the analytical framework used in Aberdeen's DCT tracking program.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 26 |
| technologies.csv | 4 |
| observations.csv | 14 |
| codes.csv | 23 |

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

Peter S. Kastner (2002). Digital Consumer Technology Supplier List (2002).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis
