# RAMP Interview: Applied Materials (Maxtor Midline Storage Study)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner, David Hill |
| Date | 2003-04-01 |
| Type | market-study |
| Domain | enterprise-storage / midline-disk-evaluation |
| License | CC-BY-4.0 |

## Abstract

Face-to-face RAMP interview with Bill Foley, Director of Computing & Intranet Services at Applied Materials (Santa Clara CA), documenting enterprise storage practices and willingness-to-adopt ATA/low-cost disk alternatives. Applied Materials operated 16-20TB of Windows storage with 80% DAS / 20% SAN, rating high willingness for capacity at lower cost (6/7) but zero willingness for any availability reduction (1/7). The interview surfaced a foundational insight: IT managers perceive applications and availability holistically, making even marginal reliability trade-offs unacceptable — a signal that positioned the midline storage market.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 13 |
| observations.csv | 33 |
| codes.csv | 35 |

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

Peter S. Kastner, David Hill (2003). RAMP Interview: Applied Materials (Maxtor Midline Storage Study).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

ramp-interview, face-to-face, industry-analysis
