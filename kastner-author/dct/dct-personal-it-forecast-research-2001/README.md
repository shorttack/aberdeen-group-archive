# Personal IT Forecast Research Compendium (2000-2001)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2001-08-08 |
| Type | dct |
| Domain | PC-forecasting,DCT |
| License | CC-BY-4.0 |

## Abstract

A curated research compendium assembled by Peter S. Kastner capturing key PC and semiconductor market forecasts from Dataquest, IDC, Merrill Lynch, TechWeb, and Japanese industry sources during the 2000-2001 PC downturn. Covers worldwide PC shipment declines, U.S. market contraction, DRAM price collapse, Japan/Asia growth, and Kastner's own dissent [PSK disagrees] on Rambus DRAM demand expectations. Source material for Aberdeen's Personal IT practice forecasting work.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 48 |
| technologies.csv | 18 |
| observations.csv | 38 |
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

Peter S. Kastner (2001). Personal IT Forecast Research Compendium (2000-2001).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis,document-review,market-tracking
