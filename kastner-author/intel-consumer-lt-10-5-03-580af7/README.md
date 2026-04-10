# LaGrande Technology — A Proposal: Consumer Market Research for Intel LT

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-10-05 |
| Type | expert-report |
| Domain | Consumer PC Security / Trusted Computing |
| License | CC-BY-4.0 |

## Abstract

Letter and attached proposal from Peter S. Kastner (Aberdeen Group EVP Research) to Michael Ferron-Jones (Intel Desktop Platform Analyst Relations) dated October 5, 2003. Proposes a multi-phase market research program to evaluate consumer LaGrande Technology (LT) — Intel's hardware-based trusted computing platform. Aberdeen argues Intel is under-valuing the consumer LT opportunity, estimating >$150M annual revenue opportunity and 10M+ consumer units in 2006 at $100 retail uplift. Proposes 3-phase research (consumer qualitative, quantitative tracking, localized surveys) in US, Canada, Japan, Germany, UK, France, Italy, Brazil, Mexico. Research focuses on identity theft fear, privacy, trusted computing adoption drivers and barriers.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 3 |
| observations.csv | 22 |
| codes.csv | 31 |

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

Peter S. Kastner (2003). LaGrande Technology — A Proposal: Consumer Market Research for Intel LT.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Proposal document; qualitative consumer/business research; surveys; focus groups; IDIs
