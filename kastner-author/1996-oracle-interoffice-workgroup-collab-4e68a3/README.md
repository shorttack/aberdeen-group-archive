# If Workgroup Collaboration is a Problem, How Are We Going to Collaborate With the World?

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1996 |
| Type | market-study |
| Domain | workgroup-collaboration |
| License | CC-BY-4.0 |

## Abstract

This Aberdeen Group presentation frames mid-1990s groupware as a rapidly growing market that is about to expand beyond departmental messaging into enterprise, intranet, and internet-enabled collaboration. It mixes market sizing and adoption data with Peter Kastner's guidance on strategy, requirements, best practices, and ROI. The deck also serves as a vendor-facing assessment of Oracle InterOffice as an extensible, server-centric collaboration platform positioned for that transition.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 18 |
| technologies.csv | 11 |
| observations.csv | 42 |
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

Peter S. Kastner (1996). If Workgroup Collaboration is a Problem, How Are We Going to Collaborate With the World?.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, expert-opinion, market-sizing
