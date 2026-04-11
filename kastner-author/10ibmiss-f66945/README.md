# Ten Issues for IBM Mainframe MIS Executives

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1991-01-01 |
| Type | white-paper |
| Domain | mainframe-computing, enterprise-IT-management |
| License | CC-BY-4.0 |

## Abstract

This white paper identifies ten prioritized technology-related issues facing IBM mainframe MIS executives in the early 1990s, arguing that System/390 architecture constraints—rooted in 1960s batch-processing design—severely hamper cost reduction and agility demanded by corporate management. Kastner contends that IBM's failure to publish clear technology roadmaps leaves MIS planners in the dark, and that rising support costs and architectural limitations are driving mainframe customers to consider non-IBM alternatives such as Hewlett-Packard.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 17 |
| observations.csv | 30 |
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

Peter S. Kastner (1991). Ten Issues for IBM Mainframe MIS Executives.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, expert-opinion, competitive-analysis
