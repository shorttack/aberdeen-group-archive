# Restructure plans weigh on Gateway

| Field | Value |
|-------|-------|
| Author | Rex Crum, CBS.MarketWatch.com |
| Date | 2003-01-06 |
| Type | news-article |
| Domain | PC-manufacturer-restructuring |
| License | CC-BY-4.0 |

## Abstract

CBS.MarketWatch.com news (2003-01-06) on Gateway's share-price reaction after CEO Ted Waitt said the financially troubled PC maker would reshuffle management and unveil a new business strategy following weak holiday sales. Stock closed at $3.30, down 4.6% on 2.3M volume, after Waitt's WSJ interview. Peter Kastner, chief research officer with the Aberdeen Group, assesses the situation: 'It looks to us as if Gateway's whole business model is on the boardroom table.' The article documents Gateway's Q3 2002 loss ($50M, 15c/share), 21% revenue decline (from $1.41B to $1.12B), lowered full-year guidance ($4.3-4.5B vs $4.5-5B), IDC's #3 US PC shipments ranking, 272 retail stores under expiring leases, and the November 2002 pivot into consumer electronics (100+ new digital products including a $2,999 42-inch plasma TV).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 2 |
| observations.csv | 10 |
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

Rex Crum, CBS.MarketWatch.com (2003). Restructure plans weigh on Gateway.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, analyst-commentary
