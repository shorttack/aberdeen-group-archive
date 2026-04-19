# Middleware/EAI Alternatives and Portera Pre-Integration (Draft Fragment)

| Field | Value |
|-------|-------|
| Author | Katherine Jones (Aberdeen Group) |
| Date | 2001-05-06 |
| Type | white-paper |
| Domain | enterprise-software/middleware-eai |
| License | CC-BY-4.0 |

## Abstract

Draft fragment from Katherine Jones to Tom Dwyer revising a section on middleware/EAI alternatives for the Aberdeen Oracle ROI white paper. Defines middleware, documents a Senior VP of Infrastructure's negative experience with EAI tooling, and analyzes Portera's pre-integrated bundle (Oracle Financials + PeopleSoft HR + Siebel CRM) as a 'buy pre-integrated' alternative.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 6 |
| observations.csv | 11 |
| codes.csv | 24 |

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

Katherine Jones (Aberdeen Group) (2001). Middleware/EAI Alternatives and Portera Pre-Integration (Draft Fragment).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review, industry-analysis, expert-opinion
