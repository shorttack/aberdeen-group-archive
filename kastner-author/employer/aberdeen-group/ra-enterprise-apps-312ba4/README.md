# Achieving More Value from Enterprise Applications

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner, Aberdeen Group |
| Date | 2006-05 |
| Type | employer-record |
| Domain | Enterprise Application Integration/SOA |
| License | CC-BY-4.0 |

## Abstract

Enterprise application silos connected by inadequate integration software ('duct tape, chewing gum, and string'). If Industry Average IT ran at Best in Class cost-efficiency, $143 billion in 2006 savings would be generated; $20 billion readily achievable. SOA technologies (web services, XML, open middleware) seen by at least two-thirds of respondents as means to improve enterprise application integration. Survey covers discrete/process manufacturing, consumer, services, and government sectors. Aberdeen Competitive Framework used.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 21 |
| observations.csv | 82 |
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

Peter S. Kastner, Aberdeen Group (2006). Achieving More Value from Enterprise Applications.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Survey benchmark (online survey + telephone interviews; Jan-Mar 2006; Aberdeen PACE methodology; Aberdeen Competitive Framework)
