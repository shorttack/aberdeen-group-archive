# SOA Middleware Takes the Lead: Picking Up Where Web Services Leaves Off

| Field | Value |
|-------|-------|
| Author | Perry Donham |
| Date | 2007-07-01 |
| Type | benchmark-report |
| Domain | soa-middleware-esb-integration |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group benchmark report by Perry Donham (Director, Enterprise Integration Research) on the evolution from web services to SOA middleware (ESB and related). Identifies how leading enterprises move beyond point-to-point web-services integration to mature SOA middleware platforms enabling reuse, governance, and operational management.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 3 |
| observations.csv | 3 |
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

Perry Donham (2007). SOA Middleware Takes the Lead: Picking Up Where Web Services Leaves Off.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

survey-benchmarking, best-practices-analysis
