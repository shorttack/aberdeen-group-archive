# RAMP Interview: Kaiser Permanente (Maxtor Midline Storage Study)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner, David Hill |
| Date | 2003-04-01 |
| Type | market-study |
| Domain | enterprise-storage / healthcare-IT / midline-disk-evaluation / EHR-migration |
| License | CC-BY-4.0 |

## Abstract

Face-to-face RAMP interview with Harvey Sietsema Jr., Applications Programming Manager at Kaiser Foundation Health Plan (Walnut Creek CA), capturing the healthcare IT perspective on storage purchasing for a primarily mainframe-centric organization. Kaiser's Management Data Repository (DB2/mainframe) served 2,200-3,000 users; the organization was mid-migration to the Epoch clinical system; HIPAA compliance was driving massive training; and regional fragmentation (northern vs. southern California operating separately) made enterprise storage planning infeasible. Sietsema's insight — 'applications are the tail that wags the storage dog' — captured how healthcare IT complexity would prevent systematic storage rationalization, making disk storage adoption opportunistic.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 10 |
| observations.csv | 33 |
| codes.csv | 34 |

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

Peter S. Kastner, David Hill (2003). RAMP Interview: Kaiser Permanente (Maxtor Midline Storage Study).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

ramp-interview, face-to-face, industry-analysis
