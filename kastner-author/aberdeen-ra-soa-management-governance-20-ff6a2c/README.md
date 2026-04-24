# Management and Governance: Planning for an Optimized SOA Application Lifecycle

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner and Rick Saia (Aberdeen Group) |
| Date | 2007-03-01 |
| Type | benchmark-report |
| Domain | soa-management-governance-application-lifecycle |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group benchmark report co-authored by Peter Kastner and Rick Saia (PKRS) examining the effectiveness of IT investments across operations management; design and operations governance; and underlying changes in project management, development, testing, and application lifecycle management tools for SOA. Survey of 200+ companies (Nov 2006-Jan 2007) finds that between a third and half of the 950 companies surveyed in 2006 are having serious difficulties getting SOA-enabled applications into stable deployment, with inadequate management/governance tools the predominant cause. Best-in-Class (top 20%) characteristics: 33% have >2 years SOA experience; 68% achieve positive SOA ROI vs. 77% of overall sample yet to see payback; design-time governance and re-use policy implemented; 80%+ have automated SOA operations and governance solutions.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 6 |
| observations.csv | 17 |
| codes.csv | 27 |

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

Peter S. Kastner and Rick Saia (Aberdeen Group) (2007). Management and Governance: Planning for an Optimized SOA Application Lifecycle.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

survey-benchmarking, best-practices-analysis, expert-opinion
