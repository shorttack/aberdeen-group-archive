# System saves $ for thrifty night owls (AS&E ASEP time-of-day metering)

| Field | Value |
|-------|-------|
| Author | Minicomputer News staff |
| Date | 1979-06-21 |
| Type | news-article |
| Domain | utility-automation-energy-management |
| License | CC-BY-4.0 |

## Abstract

Minicomputer News (June 21, 1979) profiles the ASEP two-way power-line communications system developed by American Science & Engineering (AS&E) of Cambridge, Mass. to enable utility time-of-day metering. The system is controlled by a Data General Eclipse S-230 minicomputer with 256K core memory and is deployed by Florida Power, Florida Power and Light, Wisconsin Electric Power (154,000 homes), and utilities in Missouri, New Jersey, Minnesota and California. Article from Kastner's Arthur D. Little era (1972-1979); WEPco (Wisconsin Electric Power) appears in the filename suggesting this was an ADL client deliverable reference.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 4 |
| observations.csv | 12 |
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

Minicomputer News staff (1979). System saves $ for thrifty night owls (AS&E ASEP time-of-day metering).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, expert-quote
