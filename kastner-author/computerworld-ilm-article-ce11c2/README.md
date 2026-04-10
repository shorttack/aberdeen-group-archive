# Waiting for ILM?

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2004-07-29 |
| Type | expert-report |
| Domain | Enterprise Storage / Information Lifecycle Management |
| License | CC-BY-4.0 |

## Abstract

Published in Computerworld on 29 July 2004, this advisory article argues that integrated cross-application ILM software is 4-5 years away from maturity but that enterprises should begin evolving toward ILM now using a six-step recipe: (1) centralize storage into SANs/NAS, (2) classify data across three axes (type/access/pool), (3) create lifecycle policies, (4) populate new applications on appropriate pools, (5) drive economies of scale via virtualization, (6) implement intelligent ILM circa 2008-2010. The article introduces the four-pool storage model (online FC/SCSI, midline, nearline, offline tape) and projects 45% annual storage growth driving a swing toward midline disk for reference data.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 9 |
| observations.csv | 16 |
| codes.csv | 33 |

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

Practitioner advisory; prescriptive six-step framework based on industry observation
