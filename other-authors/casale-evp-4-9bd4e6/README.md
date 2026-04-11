# Are Hypergrowth P&Ls Real? — Or Are You Seeing More Than You Paid For

| Field | Value |
|-------|-------|
| Author | Charles T. Casale |
| Date | 1983-01-06 |
| Type | market-study |
| Domain | tech-equity-analysis |
| License | CC-BY-4.0 |

## Abstract

Executive Viewpoint #4 analyzes the P&L implications of hypergrowth by introducing the Revenue Pull versus Cost Push framework and demonstrating with detailed quarterly financial tables for the fictional composite firm FTI. Casale shows how cost-push operations — where expenses run ahead of sales — can mask earnings quality deterioration even when EPS targets are met, because front-loaded costs require incremental revenue just to maintain margin, and the resulting pressure incentivizes GAAP-violating practices. The analysis previews balance sheet effects as the next analytical layer.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 1 |
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

Charles T. Casale (1983). Are Hypergrowth P&Ls Real? — Or Are You Seeing More Than You Paid For.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, quantitative-analysis, expert-opinion
