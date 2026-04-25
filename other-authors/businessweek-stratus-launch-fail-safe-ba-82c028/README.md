# A Fail-Safe Entry That's a Bargain (Stratus Computer launch coverage)

| Field | Value |
|-------|-------|
| Author | BusinessWeek (McGraw-Hill) |
| Date | 1981-11-16 |
| Type | trade-press-launch-feature |
| Domain | fault-tolerant-computing/Stratus-vs-Tandem |
| License | CC-BY-4.0 |

## Abstract

BusinessWeek's 16 November 1981 launch feature on Stratus Computer Inc. as a fail-safe-computing competitor to Tandem. Quotes Stratus president William E. Foster, IDC consultant John C. Hart, Cupertino consultant David E. Gold, ADL's Norman S. Zimbel, Tandem software-VP Dennis L. McEvoy, IVP managing partner Reid W. Dennis, and Dataquest's Richard J. Matlack. Establishes Stratus's $148K starting price vs Tandem's ~$264K, projects $5B fault-tolerant market by 1985, and notes Tandem's 142% three-year sales CAGR to $109M in 1980. Pre-Aberdeen industry-context artifact (Aberdeen founded 1988); Kastner joined Stratus in early 1980s as a marketing/sales-support hire — this story covers the era and company that became formative for him.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 21 |
| technologies.csv | 4 |
| observations.csv | 12 |
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

BusinessWeek (McGraw-Hill) (1981). A Fail-Safe Entry That's a Bargain (Stratus Computer launch coverage).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

press-feature-with-analyst-quotes
