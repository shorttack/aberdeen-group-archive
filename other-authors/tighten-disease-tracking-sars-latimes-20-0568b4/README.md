# Tighten Disease Tracking (SARS editorial)

| Field | Value |
|-------|-------|
| Author | Los Angeles Times editorial board |
| Date | 2003-04-02 |
| Type | editorial |
| Domain | SARS-public-health-global-supply-chain-2003 |
| License | CC-BY-4.0 |

## Abstract

Los Angeles Times unsigned editorial (archived at UCLA School of Public Health bioterrorism site) urging tightened global disease-tracking during the 2003 SARS outbreak. The piece reports 1,804 cases across 17 countries and up to 62 deaths as of April 2003, criticizes China's incomplete WHO reporting, and cites Peter Kastner (Aberdeen) predicting that prolonged outbreak would disrupt Chinese manufacturing of electronics to Christmas toys. Notes Intel and HP had already closed Hong Kong offices.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 2 |
| observations.csv | 8 |
| codes.csv | 28 |

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

Los Angeles Times editorial board (2003). Tighten Disease Tracking (SARS editorial).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

editorial-opinion, policy-analysis
