# Aberdeen Group Launch Process Questionnaire (Template for Sun Best Practices Study)

| Field | Value |
|-------|-------|
| Author | Aberdeen Group (Peter Kastner, project lead) |
| Date | 2002-06-01 |
| Type | employer-record |
| Domain | product-marketing/launch-process-benchmarking/methodology |
| License | CC-BY-4.0 |

## Abstract

Template questionnaire used by Aberdeen to interview the 5 companies whose responses form Study 8 ('Best Practices in Hardware and Software Industry Product Launch Process'). Contains prompts on launch organization, reporting, lead times (12 task categories), and materials delivery methods (7 methods across 7 material categories). Explicitly names 'Peter Kastner, Executive Vice President, Research at 617 854-5221' as contact of record — significant biographical confirmation of Kastner's Aberdeen title and direct line during 2002.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 1 |
| observations.csv | 6 |
| codes.csv | 23 |

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

Aberdeen Group (Peter Kastner, project lead) (2002). Aberdeen Group Launch Process Questionnaire (Template for Sun Best Practices Study).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review, research-instrument
