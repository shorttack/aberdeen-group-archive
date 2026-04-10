# Outsourcing Application Development and Maintenance: Joining Cost Savings with IT Human Asset Management

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | November 2006 |
| Type | benchmark |
| Domain | IT Outsourcing / Application Development |
| License | CC-BY-4.0 |

## Abstract

This Aberdeen benchmark report examines the drivers, practices, and outcomes of outsourcing application development and maintenance (ADM) among ~125 global enterprises. Using Aberdeen's Competitive Framework (Best in Class / Industry Average / Laggard), the study finds that Best in Class organizations save 56% versus in-house development — more than twice Industry Average savings of 26%. Key findings include: application development/maintenance is the #1 IT outsourcing target (80% of respondents); India dominates as the outsourcing destination (46-55% of work); North American firms are more cost-sensitive than global peers; mid-size firms prioritize skill acquisition over savings; and near-shore arrangements are gaining popularity. The report was underwritten by IBM Global Services, Softtek, and Unisys.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 12 |
| observations.csv | 35 |
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

Aberdeen Group (Nove). Outsourcing Application Development and Maintenance: Joining Cost Savings with IT Human Asset Management.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Online survey of ~125 enterprises (September–October 2006); supplemented by qualitative interviews with select respondents; Aberdeen PACE and Competitive Framework applied
