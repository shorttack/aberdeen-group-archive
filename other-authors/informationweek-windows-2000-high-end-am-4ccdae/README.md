# Windows 2000: High-End Ambitions

| Field | Value |
|-------|-------|
| Author | Stuart J. Johnston, Mary Hayes |
| Date | 1999-04-19 |
| Type | news-feature |
| Domain | windows-2000-datacenter-scalability |
| License | CC-BY-4.0 |

## Abstract

InformationWeek Issue 730 (April 19, 1999) reports on Microsoft's plans for Windows 2000 Datacenter Server — the high-end SKU promised as Microsoft's most scalable server OS, supporting up to 32 processors and 64 GB RAM. Aberdeen Group CRO Peter Kastner is skeptical, predicting IT response will be 'call me when it's ready,' and benchmarks NT scalability against IBM mainframe's 95% boost-per-processor. Datacenter Server hadn't begun beta testing and wasn't due until 3 months after the Windows 2000 base release, itself delayed. Aberdeen survey of 240 IT decision-makers evaluating Windows 2000 found 89% plan to use it for email, 84% intranet hosting, 84% generic servers.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 6 |
| observations.csv | 5 |
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

Stuart J. Johnston, Mary Hayes (1999). Windows 2000: High-End Ambitions.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-feature, expert-quote-aggregation, customer-survey
