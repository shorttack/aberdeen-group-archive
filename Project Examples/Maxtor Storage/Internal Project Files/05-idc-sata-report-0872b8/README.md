# Tired Storage and Capacity-Oriented Disk Drives (SATA) — Another Small Step Toward Data and Information Consolidation

| Field | Value |
|-------|-------|
| Author | Robert C. Gray, Dave Reinsel (IDC) |
| Date | 2003-11-01 |
| Type | market-study |
| Domain | enterprise-storage / SATA / tiered-storage |
| License | IDC report based on 50 in-depth executive interviews across 10 North American vertical markets examining enterprise acceptability of SATA/capacity-oriented disk drives in storage arrays. The study provides quantitative forecasts for SATA storage system revenues and HDD shipments 2003-2007 forecasting SATA will reach a quarter or more of storage array terabytes over time. Key findings include that compliance requirements are the primary driver for fixed-content adoption and that software management tools are the primary inhibitor for tiered-storage deployment. |

## Abstract

05-IDC-SATA-Report.txt

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 10 |
| observations.csv | 35 |
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

Robert C. Gray, Dave Reinsel (IDC) (2003). Tired Storage and Capacity-Oriented Disk Drives (SATA) — Another Small Step Toward Data and Information Consolidation.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

primary-research
