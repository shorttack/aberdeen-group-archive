# Video Product Segmentation — Aberdeen DCT Market Map

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-03-01 |
| Type | dct |
| Domain | dct/consumer-video |
| License | CC-BY-4.0 |

## Abstract

Aberdeen DCT market-segmentation map of consumer PC video products across four feature categories: (1) digital/analog video capture, (2) TV-input to PC monitor, (3) TV-output to TV/stereo, and (4) combined TV + graphics card. Lists hardware and software suppliers per category with indicative pricing ($80 ATI TV Wonder up to $500 Radeon 8500DV) and captures the 2002 state of PC/TV convergence peripherals.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 20 |
| technologies.csv | 13 |
| observations.csv | 16 |
| codes.csv | 24 |

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

Peter S. Kastner (2002). Video Product Segmentation — Aberdeen DCT Market Map.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis
