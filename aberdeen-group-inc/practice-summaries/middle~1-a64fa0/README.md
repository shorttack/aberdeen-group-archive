# Middleware Technology: 1998 Practice Summary

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-05-01 |
| Type | other-research |
| Domain | middleware |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group's 1998 practice summary covering the middleware technology market, analyzing gateways, TP monitors, RPCs, messaging, ORBs, data access tools, EAI solutions, and application servers as distinct middleware categories. The report sizes the middleware market at approximately $6 billion by 2000, identifies the CORBA vs. DCOM standards battle as a critical industry question, and provides supplier abstracts for thirteen vendors including BEA Systems, IBM, Microsoft, TIBCO, and CrossWorlds. Key findings include that no vendor had yet delivered a fully integrated middleware solution and that market consolidation was underway.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 17 |
| technologies.csv | 14 |
| observations.csv | 23 |
| codes.csv | 30 |

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

Aberdeen Group (1998). Middleware Technology: 1998 Practice Summary.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, market-overview
