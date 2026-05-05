# Why Aberdeen Group is Focusing on Enterprise IT Integration

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2006-02-23 |
| Type | employer-record |
| Domain | Enterprise IT integration; SOA; megatrends; programmer productivity; RTBI; mobility; datacenter; knowledge worker productivity |
| License | CC-BY-4.0 |

## Abstract

Dated/published version of the Aberdeen Enterprise IT Integration practice launch perspective. Kastner identifies six megatrends driving IT integration opportunity: (1) Programmer productivity stuck at 1970s levels — legacy spaghetti code; SOA/composite applications/BPM as solutions; best-in-class frees 15% of IT budget with lower maintenance costs. (2) SOA and Web Services will constitute majority of development by ~2010. (3) Deconstruction of processing at core and edge — datacenter as JBOR; SANs; blade servers; virtualization; grid computing. (4) Mobility is the norm — technically mature in 2006 but enterprises have tepid reactive strategy. (5) Real-Time Business Intelligence (RTBI) — gradual replumbing creates new opportunities; EII as augmentation to data warehouses. (6) Knowledge Worker productivity — collaboration, messaging, smart phones, laptops, enterprise portals, CRM/ERP improvements. Bottom line: act tactically but build strategically; focus on IT investment synergy. February 23, 2006 dateline confirms this as the formal published version of the perspective.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 16 |
| observations.csv | 18 |
| codes.csv | 32 |

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

Peter S. Kastner (2006). Why Aberdeen Group is Focusing on Enterprise IT Integration.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Aberdeen Perspective. Analyst opinion/megatrend analysis based on approximately two decades of market research observation. No survey data cited.
