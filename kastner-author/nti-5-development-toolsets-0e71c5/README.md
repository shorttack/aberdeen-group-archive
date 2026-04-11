# Selecting and Using Advanced Software Toolsets

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner, John Logan, Thomas Willmott |
| Date | 1993-04-01 |
| Type | market-study |
| Domain | software-development |
| License | CC-BY-4.0 |

## Abstract

This Aberdeen Group workbook surveys the rapidly changing software development toolset landscape in 1993, presenting key field research findings from CIO interviews and ISV briefings. It identifies best-in-class tools across 3GLs, 4GLs, RDBMS-integrated tools, GUI builders, and CASE, and defines the three-layer architecture — presentation, business logic, data access — of strategic applications. The study evaluates client-server development readiness, positions emerging GUI tools from Powersoft, Gupta, and others, and previews object-oriented technology as a late-1990s mainstream prospect.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 33 |
| technologies.csv | 15 |
| observations.csv | 30 |
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

Peter S. Kastner, John Logan, Thomas Willmott (1993). Selecting and Using Advanced Software Toolsets.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, technology-assessment, vendor-profiling
