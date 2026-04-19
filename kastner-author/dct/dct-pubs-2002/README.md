# Aberdeen Group DCT Publications Catalog, 2002

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-12-31 |
| Type | dct |
| Domain | dct |
| License | CC-BY-4.0 |

## Abstract

Catalog of 434 Aberdeen Group DCT (Digital Consumer Technology) publications issued during calendar year 2002, indexed by publication number, date, title, publication type (Profile, OnSite, Report, Impact, Perspective, InSight, Snapshot, etc.), and lead analyst. The catalog documents the productivity and editorial mix of the Aberdeen DCT practice during a peak year of PC industry transition and provides bibliographic provenance for any referenced Aberdeen publication from 2002.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 56 |
| technologies.csv | 0 |
| observations.csv | 28 |
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

Peter S. Kastner (2002). Aberdeen Group DCT Publications Catalog, 2002.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review
