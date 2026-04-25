# How PSA Was Codified: The Evolution of Professional Services Automation

| Field | Value |
|-------|-------|
| Author | Ryan Kelly |
| Date | 2025-03-04 |
| Type | category-creation-record |
| Domain | professional-services-automation |
| License | CC-BY-4.0 |

## Abstract

Ryan Kelly of SPI Research recounts how Dave Hofferberth, then a senior analyst at Aberdeen Group, published the seminal March 1999 whitepaper that named, structured, and codified Professional Services Automation (PSA) as a software category for the first time. The article documents the category's evolution through the early 2000s naming battles—with Gartner promoting SPO and PeopleSoft launching ESA—and its ultimate survival as the global standard adopted by Gartner by 2025. SPI Research's 2022 benchmark data across 88 firms demonstrates PSA's quantified financial impact, including an 8.2% utilization increase and $8.96M average revenue lift.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 15 |
| technologies.csv | 4 |
| observations.csv | 25 |
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

Ryan Kelly (2025). How PSA Was Codified: The Evolution of Professional Services Automation.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, market-history
