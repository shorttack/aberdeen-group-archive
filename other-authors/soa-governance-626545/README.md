# Management and Governance: Planning for an Optimized SOA Application Lifecycle

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 2007-03 |
| Type | employer-record |
| Domain | SOA governance; SOA operations management; application lifecycle management |
| License | CC-BY-4.0 |

## Abstract

24-page Aberdeen Group benchmark report examining effectiveness of IT investments in three SOA lifecycle areas: operations management, design/operations governance, and project/development/ALM tools. Survey of 200+ companies across geographies and industries. Between one-third and half of 950 companies surveyed in 2006 had serious deployment difficulties. Best-in-Class (top 20%) distinguish themselves through experience (33% with >2 years SOA), positive ROI (68%), design-time governance implementation, and automated management/governance solutions (>80%). Three SOA strategies identified: SOA Lite (50%), Enterprise SOA (30%), ERP SOA (20%).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 1 |
| technologies.csv | 5 |
| observations.csv | 26 |
| codes.csv | 29 |

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

Aberdeen Group (2007). Management and Governance: Planning for an Optimized SOA Application Lifecycle.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

survey; benchmark; n=200+ companies; qualitative interviews; Nov 2006–Jan 2007
