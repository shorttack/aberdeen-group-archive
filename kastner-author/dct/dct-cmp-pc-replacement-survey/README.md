# CMP Corporate PC Replacement Policy Survey

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-06-30 |
| Type | dct |
| Domain | dct |
| License | CC-BY-4.0 |

## Abstract

Survey instrument and results tracking corporate desktop and notebook replacement policies across U.S. IT buyers, comparing past policy against 'next 12 months' plans. Replacement interval bins: <18, 18-24, 24-30, 30-36, 36-42, 42-48, 48-54, >54 months, and 'when they break'. Instrument was fielded in partnership with CMP Media; this workbook contains the question framework and partial response tabulations that became inputs to Kastner's DCT corporate PC lifecycle commentary.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 0 |
| observations.csv | 4 |
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

Peter S. Kastner (2003). CMP Corporate PC Replacement Policy Survey.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

field-research
