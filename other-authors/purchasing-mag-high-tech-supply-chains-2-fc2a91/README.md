# What's Happening in High-Tech Supply Chains

| Field | Value |
|-------|-------|
| Author | Purchasing Magazine staff |
| Date | 2003-11-20 |
| Type | trade-news |
| Domain | high-tech-supply-chain-recovery-2003 |
| License | CC-BY-4.0 |

## Abstract

Purchasing Magazine reviews late-2003 high-tech supply chain recovery. Government reports show 15.4% Q3-2003 annualized growth in software/equipment spending — the biggest jump since the 2000 bubble peak. Analyst Peter Kastner of Aberdeen Research rejects the figure, noting it isn't reflected in IT budgets or vendor revenues (single-digit growth at most). The piece also covers Intel's new Centrino bundle (Pentium M + wireless module) driving laptops past desktops.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 3 |
| observations.csv | 3 |
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

Purchasing Magazine staff (2003). What's Happening in High-Tech Supply Chains.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

trade-reporting, government-data-skepticism, expert-quote
