# The Composite Applications Benchmark Report: How SOA Standards Are Accelerating Business Change

| Field | Value |
|-------|-------|
| Author | Rick Saia and Peter S. Kastner, Aberdeen Group |
| Date | 2006-12 |
| Type | employer-record |
| Domain | SOA/Composite Applications |
| License | CC-BY-4.0 |

## Abstract

Application integration consumes ~40% of typical IT budget. Most enterprises have not fully implemented SOA but are building composite applications using web services standards (XML, SOAP, WS-*) to respond to line-of-business demands. Best in Class firms build apps in under 3 months and achieve >25% ROI. Survey of ~135 enterprises from manufacturing and services sectors. Aberdeen Competitive Framework used to segment Best in Class (20%), Industry Average (50%), and Laggards (30%).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 17 |
| observations.csv | 90 |
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

Rick Saia and Peter S. Kastner, Aberdeen Group (2006). The Composite Applications Benchmark Report: How SOA Standards Are Accelerating Business Change.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Survey benchmark (N~135 enterprises; online survey + telephone interviews; Oct-Dec 2006; Aberdeen Competitive Framework)
