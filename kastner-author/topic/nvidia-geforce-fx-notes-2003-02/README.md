# nVidia GeForce FX Product-Line Briefing Notes

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-02-21 |
| Type | topic-analysis |
| Domain | topic/personal-pcs |
| License | CC-BY-4.0 |

## Abstract

Briefing notes from an nVidia product-line meeting with Brian Burke and Todd Reddick covering the GeForce FX NV30/NV31/NV34 lineup — targets, process (TSMC 0.13 micron / 0.15 micron), memory (DDR1/DDR2), AGP 8x, DirectX 9 support, NV35 high-end future, and SKU positioning versus ATI Radeon 9500 and prior GeForce Ti 4200/MX 440 parts. Includes pricing of $99 (NV34) to $399 (NV30/5800) and April ship timing.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 15 |
| observations.csv | 20 |
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

Peter S. Kastner (2003). nVidia GeForce FX Product-Line Briefing Notes.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

field-research, industry-analysis
