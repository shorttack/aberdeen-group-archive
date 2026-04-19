# World IT Spending 2002-2005: Timing the Recovery

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 2002-04-01 |
| Type | market-study |
| Domain | global-it-spending |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group's April 2002 forecast of worldwide IT spending through 2005, modeling the post-dot-com recovery path across regions (North America, Europe, Latin America, Asia-Pacific, Middle East/Africa) and categories (hardware, software, services). The report projects a return to growth from the 2001 trough and serves as the demand-side companion to Aberdeen's Sun AS/400 RAMP engagement. Includes CAGR projections by customer size (Small 1-99, Medium 100-999, Large 1000+, Government).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 0 |
| observations.csv | 27 |
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

Aberdeen Group (2002). World IT Spending 2002-2005: Timing the Recovery.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, market-forecasting, regional-segmentation
