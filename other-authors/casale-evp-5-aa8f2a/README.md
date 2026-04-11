# Hypergrowth Balance Sheets - Neglected Stepchildren?

| Field | Value |
|-------|-------|
| Author | Charles T. Casale |
| Date | 1983-01-07 |
| Type | market-study |
| Domain | tech-equity-analysis |
| License | CC-BY-4.0 |

## Abstract

EVP #5 in the Executive Viewpoint series analyzes balance sheet dynamics of a composite hypergrowth tech company (FTI), focusing on accounts receivable DSO expansion, inventory valuation asymmetry, and the distorting effect of end-of-quarter shipment concentration. Casale argues that apparent receivables deterioration is a symptom of loose operational cost control rather than credit quality issues, and that balance sheets are systematically underanalyzed by institutional investors focused on P/E ratios.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 2 |
| observations.csv | 21 |
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

Charles T. Casale (1983). Hypergrowth Balance Sheets - Neglected Stepchildren?.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, quantitative-analysis
