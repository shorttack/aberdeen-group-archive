# Open Systems: A Technology Status Report

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner, John Logan, Thomas Willmott |
| Date | 1993-01-01 |
| Type | market-study |
| Domain | open-systems |
| License | CC-BY-4.0 |

## Abstract

This Aberdeen Group workbook provides a comprehensive status report on Open Systems as of January 1993, covering the transition from proprietary to open, distributed computing architectures. It assesses five key technology components — hardware microprocessors, systems software, application development toolsets, networking, and emerging architectures — and profiles major vendor positions and standards organizations. The study culminates in an ACTION framework for IS executives managing the organizational and economic challenges of open systems adoption.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 36 |
| technologies.csv | 20 |
| observations.csv | 29 |
| codes.csv | 27 |

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

Peter S. Kastner, John Logan, Thomas Willmott (1993). Open Systems: A Technology Status Report.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, technology-assessment, vendor-profiling
