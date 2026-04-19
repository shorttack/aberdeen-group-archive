# Aberdeen Group Semiconductor Research Practice Definition (2002)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-03-01 |
| Type | topic-analysis |
| Domain | semiconductor,industry-structure,enabling-technology |
| License | CC-BY-4.0 |

## Abstract

Formal definition of Aberdeen Group's Semiconductor Research Practice: focus on enabling semiconductor technologies for emerging digital markets (MEMS, photonics, software-defined radios, NPUs, UWB), a taxonomy of semiconductor ecosystem trends (design, fabrication, test), and detailed target account lists spanning 36+ firms (Agere, AMD, ARM, ATI, Broadcom, IBM, Intel, Nvidia, Samsung, Sony, TSMC, etc.). Captures the 2001 semiconductor downturn context (-32% to $132B WW revenue) and a forward-looking view of fabless trends, design/NRE cost inflation ($10M+ per device), 300mm facility cost ($2.7B), verification engineering dominance (70% of cycle), DFT, SoC test, and molecular/Plastic-Logic disruption candidates.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 39 |
| technologies.csv | 21 |
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

Peter S. Kastner (2002). Aberdeen Group Semiconductor Research Practice Definition (2002).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis,document-review
