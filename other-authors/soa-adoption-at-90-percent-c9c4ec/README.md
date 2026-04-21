# SOA Adoption at 90 Percent?!

| Field | Value |
|-------|-------|
| Author | SYS-CON Media editorial (anonymous) |
| Date | 2006-07-15 |
| Type | editorial |
| Domain | SOA-enterprise-integration |
| License | CC-BY-4.0 |

## Abstract

SYS-CON Media editorial (mid-2006, au.sys-con.com print view) reacting with skepticism to Aberdeen Group's finding — reported in the benchmark study 'Enterprise Service Bus and SOA Middleware' — that '9 of every 10 companies are adopting or have adopted service-oriented architectures and will exit 2006 with SOA planning, design, and programming experience.' The editorial quotes Peter S. Kastner, Vice President and Research Director for Enterprise Integration at Aberdeen Group and the report's author: 'Redesigning business processes, high IT integration costs, and customization challenges are eating up 40% of the IT budget in integration expenditures. SOA is broadly seen as a real technology step forward, with the largest companies, who have the biggest integration problems, leading the way.' The editorial then lists Aberdeen's three distinct SOA adoption approaches (SOA 'light' — open source + standards for small companies; Enterprise SOA — suite software for mid-large installations; SOA ERP — entry via ERP extensions for mid-sized) and closes with a wry Aberdeen Group disclaimer about not being based in Aberdeen. The tone conveys reader skepticism toward the 90% number while legitimizing the underlying Aberdeen/Kastner analysis.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 6 |
| observations.csv | 8 |
| codes.csv | 25 |

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

SYS-CON Media editorial (anonymous) (2006). SOA Adoption at 90 Percent?!.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-commentary, analyst-report-summary
