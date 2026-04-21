# Tech's Best Hope: Pockets of Prosperity

| Field | Value |
|-------|-------|
| Author | Alex Salkever, BusinessWeek Online |
| Date | 2002-03-15 |
| Type | feature-article |
| Domain | IT-spending-forecast-2002 |
| License | CC-BY-4.0 |

## Abstract

BusinessWeek Online feature (March 15 2002) by Alex Salkever analyzing which tech segments will lead the post-dot-com recovery despite continuing telecom weakness. Peter Kastner, chief research officer at Aberdeen Group, provides the core Aberdeen 2002 forecast: total tech-sector revenues (hardware, software, IT services, excluding heavy telecom) will grow from $446.1 billion (2001) to $465.3 billion (2002), a 4.3% increase. Aberdeen projects IT services growing 5.6% ($173.9B -> $183.7B), software 6.7% ($93.7B -> $100B), and hardware only 1.7% ($178.4B -> $181.4B). Kastner calls the telecom-equipment segment 'an industry in nuclear winter.' He highlights Dell's two-hour inventory posture (supply-chain visibility) and IBM/EDS backlogs for ERP/CRM integration work at customers rolling out PeopleSoft, SAP, and Siebel. Merrill Lynch survey of 100 CIOs: most shifted spending-recovery expectations from 2002 into early 2003.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 14 |
| technologies.csv | 4 |
| observations.csv | 12 |
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

Alex Salkever, BusinessWeek Online (2002). Tech's Best Hope: Pockets of Prosperity.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

analyst-commentary, industry-analysis
