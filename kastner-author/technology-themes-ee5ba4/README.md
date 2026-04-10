# IT Technology Themes and Trends

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-2004 |
| Type | topic-analysis |
| Domain | Enterprise IT / Technology Trends |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group analysis of 10 major technology themes shaping enterprise IT: IT deflation and server pricing pressure, storage market transformation via ILM, empowered consumers driving retail IT, best-of-breed consolidation, ROI-driven IT purchasing, IT over-buying and rationalization, consumer power reshaping supply chains, real-time consumer tracking, wireless laptop adoption barriers, enterprise management in web services environments, and Sarbanes-Oxley/Basel II compliance costs.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 12 |
| observations.csv | 21 |
| codes.csv | 28 |

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

Peter S. Kastner (2003). IT Technology Themes and Trends.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Analyst commentary; survey reference (750,000 business computer buyers); qualitative assessment
