# PCs and Workstations: Vying for the 1990's Desktop

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner, John Logan, Thomas Willmott |
| Date | 1993-02-01 |
| Type | market-study |
| Domain | desktop-computing |
| License | CC-BY-4.0 |

## Abstract

This Aberdeen Group workbook analyzes the competitive landscape between Intel-powered PCs and RISC/Unix workstations for enterprise desktop dominance in the 1993-1996 timeframe. It defines workgroup computing requirements, compares platforms across client-server capability, networking, cost, application software, and multiuser compatibility, and evaluates supplier strategies from IBM, Apple, Compaq, Dell, Sun, HP, and operating system vendors. Aberdeen recommends workstations for technical/power users, low-end Unix workstations as NT contingency, Macs for functionality, and PCs for all other users through 1993.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 19 |
| technologies.csv | 14 |
| observations.csv | 29 |
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

Peter S. Kastner, John Logan, Thomas Willmott (1993). PCs and Workstations: Vying for the 1990's Desktop.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, technology-assessment, vendor-profiling
