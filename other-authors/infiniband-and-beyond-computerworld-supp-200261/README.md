# To InfiniBand and beyond, cry firms

| Field | Value |
|-------|-------|
| Author | Carly Suppa |
| Date | 2002-08-13 |
| Type | news-article |
| Domain | data-center-interconnect-InfiniBand-2002 |
| License | CC-BY-4.0 |

## Abstract

Computerworld Australia feature on InfiniBand, a next-generation data-center interconnect operating at 2.5-10 Gbps (scaling to 30 Gbps) backed by 150+ firms in the InfiniBand Trade Association including IBM, Intel, Microsoft, Sun, and Dell. Draws on Aberdeen Group's 'InfiniBand Architecture: Planning the Next Generation Data Centre' white paper. Kastner (Aberdeen EVP/CRO) predicts InfiniBand 'will replace TCP/IP as the high-speed, server-to-server interconnect technology' with ISPs, ASPs and large web sites as initial targets.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 7 |
| observations.csv | 8 |
| codes.csv | 29 |

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

Carly Suppa (2002). To InfiniBand and beyond, cry firms.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, analyst-quote-aggregation
