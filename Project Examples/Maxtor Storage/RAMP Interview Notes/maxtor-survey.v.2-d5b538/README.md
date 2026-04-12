# Maxtor RAMP Disk Storage Usage Questionnaire v2

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner; David Hill (Aberdeen Group) |
| Date | 2003-03-01 |
| Type | market-study |
| Domain | enterprise-storage / disk-tiering / ILM |
| License | CC-BY-4.0 |

## Abstract

Refined second version of the Aberdeen Group telephone survey questionnaire for the Maxtor RAMP project. Streamlines the v1 instrument to 17 survey questions and a demographic section, with key enhancements: per-OS storage breakdowns (Q4.1-Q4.3) for mainframe / Windows / Unix separately, introduction of a 1-7 Likert willingness-to-tradeoff scale (Q9) testing three distinct cost-performance scenarios (50% cost reduction with lower availability; 30% with less availability; 30% with same availability), vendor engagement probing (Q10-Q11), restore frequency measurement (Q12), static data application identification (Q14), and a refined terminology awareness battery testing five terms. The instrument was used to collect data from approximately 70 enterprise IT decision-makers.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 10 |
| observations.csv | 30 |
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

Peter S. Kastner; David Hill (Aberdeen Group) (2003). Maxtor RAMP Disk Storage Usage Questionnaire v2.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

ramp-survey-design, telephone-survey, quantitative-research
