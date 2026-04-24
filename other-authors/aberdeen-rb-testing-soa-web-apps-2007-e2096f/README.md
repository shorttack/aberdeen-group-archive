# Testing SOA and Web Services Applications: How Different Can It Be?

| Field | Value |
|-------|-------|
| Author | Perry Donham |
| Date | 2007-08-01 |
| Type | research-brief |
| Domain | soa-testing-qa-integration-orchestration |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group research brief by Perry Donham identifying the testing/QA challenges specific to SOA and web-services applications: unit and functional tests no longer suffice — integration and orchestration testing become critical, with performance and versioning adding further complexity. Brief draws on prior ESB/Middleware (July 2006), SOA Middleware (June 2007), and Modernizing Legacy (2007) Aberdeen research.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 5 |
| observations.csv | 5 |
| codes.csv | 25 |

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

Perry Donham (2007). Testing SOA and Web Services Applications: How Different Can It Be?.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

research-brief, best-practices-hypothesis
