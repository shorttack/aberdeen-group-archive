# Waiting for ILM?

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2004-07-29 |
| Type | expert-report |
| Domain | enterprise-storage |
| License | CC-BY-4.0 |

## Abstract

Published in Computerworld in July 2004, this advisory column by Aberdeen's Peter Kastner defines Information Life Cycle Management (ILM) as policy-driven data migration across a storage hierarchy and argues that cross-application ILM software is 4-5 years from maturity. Kastner provides a practical six-step recipe for enterprises to begin ILM adoption immediately using a four-pool storage model (Online/Midline/Nearline/Offline). The article predicts that mature ILM software arriving circa 2008-2010 will reduce storage-related production hours by 80%.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 10 |
| observations.csv | 32 |
| codes.csv | 37 |

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

Peter S. Kastner (2004). Waiting for ILM?.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, expert-opinion, storage-architecture
