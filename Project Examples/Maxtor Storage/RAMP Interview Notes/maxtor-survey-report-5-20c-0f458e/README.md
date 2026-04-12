# Maxtor Survey Report (RAMP Results Presentation)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner; David Hill |
| Date | 2003-05-20 |
| Type | market-study |
| Domain | enterprise-storage / ATA-disk / midline-storage |
| License | CC-BY-4.0 |

## Abstract

Final 38-slide RAMP results presentation by Peter Kastner and David Hill for Maxtor Corporation, May 2003. Synthesizes findings from 70 telephone survey respondents and 5 face-to-face interviews (Timex, Applied Materials, State Street, Inovant/Visa, Kaiser Permanente) on enterprise willingness to adopt ATA (low-cost/midline) disk as a complementary storage tier. Key findings: 65% of enterprises use 60%+ of available storage; storage growth below vendor projections; 70% have read-only data but cannot easily identify it; 75% likely to purchase low-cost disk; backup/restore remains a major pain point. Key conclusions: MaXLine should be positioned as 'complementary' not 'substitute' storage; 'mid-line' is the correct market term; positioning should emphasize 'better than ATA' rather than 'less than SCSI'; disk-based backup/copy presents a major opportunity.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 30 |
| technologies.csv | 17 |
| observations.csv | 52 |
| codes.csv | 45 |

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

Peter S. Kastner; David Hill (2003). Maxtor Survey Report (RAMP Results Presentation).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

quantitative-survey, face-to-face-interview, market-research, statistical-analysis
