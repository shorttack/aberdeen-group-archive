# Win the Rebate Runaround

| Field | Value |
|-------|-------|
| Author | Jan Garkey |
| Date | 2004-04-19 |
| Type | news-feature |
| Domain | consumer-rebate-redemption-economics |
| License | CC-BY-4.0 |

## Abstract

Credit Union National Association (CUNA) consumer-finance writer Jan Garkey profiles the rebate-redemption mess in 2004. The piece anchors on Aberdeen Group EVP Peter Kastner's 40/40/20 estimate: only 40% of consumers submit rebates they're entitled to, 40% successfully redeem, and 20% have problems. Cites Philips Electronics N.A. case where >50,000 consumers experienced 6+ month delays on $20-$100 rebates Jan-2001 to Jan-2002, prompting FTC compulsion. Includes practical consumer guidance from Institute of Consumer Financial Education's Paul Richard.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 1 |
| observations.csv | 4 |
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

Jan Garkey (2004). Win the Rebate Runaround.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

consumer-finance-feature, expert-quote, case-study
