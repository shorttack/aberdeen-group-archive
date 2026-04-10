# SARS May Impact Global Electronics Industry

| Field | Value |
|-------|-------|
| Author | Russ Craig and Peter Kastner |
| Date | 2003-04 |
| Type | topic-analysis |
| Domain | Electronics Manufacturing / Supply Chain / Semiconductors |
| License | CC-BY-4.0 |

## Abstract

Aberdeen hot topic analyzing the potential impact of the 2003 SARS epidemic on the global electronics industry, focusing on semiconductor manufacturing in Asia-Pacific (PRC, Taiwan, Hong Kong, Singapore), supply chain disruption risks, just-in-time logistics vulnerabilities, and investment implications for the trillion-dollar electronics sector.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 18 |
| technologies.csv | 5 |
| observations.csv | 25 |
| codes.csv | 31 |

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

Russ Craig and Peter Kastner (2003). SARS May Impact Global Electronics Industry.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Expert opinion; qualitative analysis of SARS outbreak geographic and industrial data
