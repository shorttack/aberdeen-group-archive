# Outsourcing Application Development and Maintenance: Joining Cost Savings with IT Human Asset Management

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 2006-11 |
| Type | employer-record |
| Domain | IT outsourcing / application development |
| License | CC-BY-4.0 |

## Abstract

Survey of ~125 enterprises on outsourcing application development and maintenance (ADM). Finds that Best in Class organizations save 56% vs. 26% for Industry Average on outsourced work. Top drivers: reduce IT operating costs (75%) and enable IT professionals to focus on strategic tasks (63%). India dominates (46% of development work), but near-shore alternatives gaining ground. Mid-market firms prioritize expertise gain over cost savings. Underwritten by IBM Global Services, Softtek, and Unisys.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 8 |
| observations.csv | 80 |
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

Aberdeen Group (2006). Outsourcing Application Development and Maintenance: Joining Cost Savings with IT Human Asset Management.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Survey-based benchmark (N~125); Aberdeen Competitive Framework (Best in Class/Industry Average/Laggard); online survey Sep-Oct 2006 supplemented by executive interviews
