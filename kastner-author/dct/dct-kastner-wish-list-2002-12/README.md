# Peter Kastner's Wish List

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-12-01 |
| Type | dct |
| Domain | dct |
| License | CC-BY-4.0 |

## Abstract

Kastner's personal 2002 holiday wish list of six digital consumer technology products: HP Scanjet 5500c, Dell Axim X5 Pocket PC, Viewsonic NextVision N6 PC-HDTV bridge, Gateway Profile 4 XL all-in-one, nVidia GeForce FX graphics card, and Davis Instruments Vantage Pro Plus weather station. Each item is framed as both a consumer product and an industry signal.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 13 |
| technologies.csv | 14 |
| observations.csv | 18 |
| codes.csv | 26 |

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

Peter S. Kastner (2002). Peter Kastner's Wish List.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

product-review, editorial
