# Technical Workstations: 1998 Practice Summary

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-05-01 |
| Type | other-research |
| Domain | technical-workstations |
| License | Aberdeen Group's 1998 practice summary covering standalone Unix and Windows NT technical workstations used for CAD/MCAD/CAE/DCC/animation/scientific visualization and decision-support. The document profiles market leaders (HP Sun IBM SGI for Unix; HP Compaq Dell Digital IBM Intergraph for NT) and provides key findings including NT growing at 30%+ annually, Unix maintaining high-end dominance for 4-5 more years, and the emerging use of workstations as data visualization decision-support tools. HP is identified as the overall combined-platform market leader for 1997. |

## Abstract

WORKST~1.DOC

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 18 |
| technologies.csv | 15 |
| observations.csv | 20 |
| codes.csv | 26 |

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

Aberdeen Group (1998). Technical Workstations: 1998 Practice Summary.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis
