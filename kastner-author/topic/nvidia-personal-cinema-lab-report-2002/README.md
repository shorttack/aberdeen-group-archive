# nVidia Personal Cinema 1.0 — Aberdeen Lab Report

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-01-17 |
| Type | topic-analysis |
| Domain | topic/personal-pcs |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group laboratory feedback report to nVidia management on 16 hours of hands-on testing of the Personal Cinema 1.0 kit (Compro GeForce2 MX 400 graphics card with VIVO breakout box) on a Dell 8100 running Windows XP. Evaluates graphics, TV tuner via WinDVR, DVD playback via WinDVD, Ulead Video Wave 4, and Microsoft Movie Maker workflows, and recommends packaging, cabling, and software-install improvements.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 14 |
| observations.csv | 23 |
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

Peter S. Kastner (2002). nVidia Personal Cinema 1.0 — Aberdeen Lab Report.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

benchmarking, field-research, document-review
