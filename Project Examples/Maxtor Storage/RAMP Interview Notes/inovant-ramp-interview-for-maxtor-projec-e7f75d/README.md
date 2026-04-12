# RAMP Interview: Inovant / Visa (Maxtor Midline Storage Study)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner, David Hill |
| Date | 2003-04-01 |
| Type | market-study |
| Domain | enterprise-storage / financial-sector-storage / midline-disk-evaluation |
| License | CC-BY-4.0 |

## Abstract

Face-to-face RAMP interview with Paul Orleman, Department Head for Direct Exchange Infrastructure at Inovant (Visa's technology subsidiary), capturing the financial-sector perspective on ATA midline storage adoption. Inovant operated 20TB with 30% utilization, 95% Fibre Channel, and rated willingness to adopt low-cost disk at only 2/7 due to extreme SLA requirements for member bank transactions. The credit card dispute image application (10TB, 50% read-only, DB2) represented a major static-data use case that theoretically suited lower-cost storage but was protected by availability requirements too stringent to permit migration.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 12 |
| observations.csv | 34 |
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

Peter S. Kastner, David Hill (2003). RAMP Interview: Inovant / Visa (Maxtor Midline Storage Study).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

ramp-interview, face-to-face, industry-analysis
