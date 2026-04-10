# Dell Asset Recovery Services: a Trustworthy Partner for Eliminating Aging IT Assets

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-07 |
| Type | white-paper |
| Domain | IT asset management / e-waste / asset recovery services |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group white paper commissioned by Dell examining the financial and legal risks of decommissioned IT equipment. Analyzes the seven steps of an IT asset end-of-life process with itemized cost breakdowns, argues that PC residual value declines 9.6% per month, estimates DIY disposal at $387+ per unit vs. Dell ARS at $49-$79 per unit, and recommends that enterprises disposing of 3,000+ PCs annually adopt a trusted asset recovery partner. Concludes that disposal costs exceed 25% of initial PC acquisition cost and are rising.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 5 |
| observations.csv | 21 |
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

Peter S. Kastner (2003). Dell Asset Recovery Services: a Trustworthy Partner for Eliminating Aging IT Assets.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Cost analysis and expert opinion; vendor-sponsored research with Aberdeen Group analysis
