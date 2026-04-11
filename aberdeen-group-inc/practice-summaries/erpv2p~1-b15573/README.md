# Enterprise Resource Planning: 1998 Practice Summary

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-05-01 |
| Type | other-research |
| Domain | ERP |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group's 1998 ERP market practice summary covering the worldwide ERP software market at $17.7 billion, dominated by SAP (33%), Oracle (10%), J.D. Edwards (7%), PeopleSoft (6%), and Baan (5%). The report introduces Aberdeen's Infinite Resource Planning (IRP) model as the next evolution beyond ERP, driven by three convergent technologies: object orientation, network-centric architectures, and the Internet. Supplier profiles cover Baan, IMI, i2 Technologies, Infinium, J.D. Edwards, Lawson Software, Marcam Solutions, Oracle, PeopleSoft, SAP, and QAD, with Aberdeen assessments of each vendor's competitive position and trajectory.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 29 |
| technologies.csv | 29 |
| observations.csv | 32 |
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

Aberdeen Group (1998). Enterprise Resource Planning: 1998 Practice Summary.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, market-overview
