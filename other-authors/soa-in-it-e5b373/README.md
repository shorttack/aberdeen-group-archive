# The SOA in IT Benchmark Report: What CIOs Should Know about How SOA Is Changing IT

| Field | Value |
|-------|-------|
| Author | Aberdeen Group (institutional; William Mougayar, VP & Service Director, IT Research) |
| Date | 2005-12 |
| Type | employer-record |
| Domain | SOA Adoption/CIO Strategy |
| License | CC-BY-4.0 |

## Abstract

Foundational SOA benchmark establishing early adoption landscape. CIO dilemma: SOA offers compelling case but business benefits largely untapped. SOA here but not widely distributed: only 16% have >24 months experience. Aberdeen bullish: predicts Global 2000 companies can save $53 billion from IT budgets as SOA reduces software implementation costs over 5 years. BIC companies spend 29.6% of IT budgets on innovation vs 18.5% average; BIC spend only 12.4% on software maintenance vs 27.3% average. Survey of 284 companies; three categories: Laggards (<12 months SOA experience), Cautious Adopters (12-24 months), Experienced Adopters (>24 months).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 19 |
| observations.csv | 121 |
| codes.csv | 32 |

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

Aberdeen Group (institutional; William Mougayar, VP & Service Director, IT Research) (2005). The SOA in IT Benchmark Report: What CIOs Should Know about How SOA Is Changing IT.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Survey benchmark (N=284 companies; online survey + telephone/email interviews; November 2005; Accela Communications survey partner; Aberdeen Competitive Framework)
