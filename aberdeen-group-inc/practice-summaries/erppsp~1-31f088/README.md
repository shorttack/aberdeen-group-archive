# ERP Professional Services: 1998 Practice Summary

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-05-01 |
| Type | other-research |
| Domain | ERP-professional-services |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group's 1998 practice summary covering the ERP professional services market, classifying providers into OEMs (Compaq, HP), ISVs (SAP, Oracle, J.D. Edwards, PeopleSoft, Baan), and Independent Professional Services Providers (IPSPs) including Big Six consultancies and specialist firms. The report categorizes ERP services into Planning, Implementation, Project Management, and Lifecycle Support, and profiles 14 suppliers with competitive assessments. Key findings highlight declining implementation costs due to new methodologies, Y2K-driven ERP adoption, and growing merger/acquisition activity among IPSPs.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 30 |
| technologies.csv | 16 |
| observations.csv | 30 |
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

Aberdeen Group (1998). ERP Professional Services: 1998 Practice Summary.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, market-overview
