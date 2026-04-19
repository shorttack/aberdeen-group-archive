# PC Deals Weekly Update: April 20, 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-04-20 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

Last week, while gathering data for PC Deals, a window popped open at Dell's site inviting us to join "Dell Direct Deals." We begrudgingly entered our email, expecting for Dell to hound us with advertisements. But we were pleasantly wrong on that account. This past Thursday Dell emailed us an virtual coupon for $50 off any Dell Home System over $999, redeemable by typing the appropriate code in at checkout.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 15 |
| technologies.csv | 7 |
| observations.csv | 24 |
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

Peter S. Kastner (2003). PC Deals Weekly Update: April 20, 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
