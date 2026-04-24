# The Retail Business Intelligence Benchmark Studies: Hypothesis and Survey

| Field | Value |
|-------|-------|
| Author | Paula Rosenblum |
| Date | 2006-03-01 |
| Type | research-design-deck |
| Domain | retail-business-intelligence-predictive-analytics |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group internal research-design deck by Paula Rosenblum (Retail practice) introducing the hypothesis and survey design for an upcoming Retail Business Intelligence Benchmark Study. Hypothesis: advanced BI including predictive analytics improves retailer top and bottom-line performance across assortment, price, promotion planning, and enterprise-wide scorecarding. Targets GMMs, VPs of Store Operations, VPs of Supply Chain, and CIOs in retail. Planned publication May 30, 2006.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 3 |
| observations.csv | 6 |
| codes.csv | 25 |

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

Paula Rosenblum (2006). The Retail Business Intelligence Benchmark Studies: Hypothesis and Survey.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

research-design, hypothesis-formulation, sample-targeting
