# Sun Micro slammed as quarterly report disappoints

| Field | Value |
|-------|-------|
| Author | Rex Crum, CBS.MarketWatch.com |
| Date | 2003-07-23 |
| Type | news-article |
| Domain | server-market-public-companies |
| License | CC-BY-4.0 |

## Abstract

MarketWatch news story (Jul 23 2003, 5:51 p.m. EST) by Rex Crum reporting on Sun Microsystems' fiscal Q4 2003 results. Sun earnings dropped 80%, profit of $12M (breakeven EPS) vs $61M (2c EPS) year ago; revenue $2.98B down 13% from $3.42B; Thomson First Call consensus was 2c/$3.07B. Shares fell 92c to close at $3.85 on 239M shares (most active US stock that day). Analysts Kevin McCarthy (CSFB) and Toni Sacconaghi (Bernstein) were harshly critical. Peter Kastner, computer-hardware analyst with Aberdeen Group in Boston, provided the contrarian counter-balance: 'investors are likely to interpret Sun's results as being on the edge of respectability as the company has been hovering near breakeven for three quarters' and 'anyone who gives up on Sun would be making a big mistake, as they have a huge, loyal base of customers.' This is the end-of-day wrap-up; a companion pre-market MarketWatch story by Mike Tarsala that morning used the identical Kastner quote.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 3 |
| observations.csv | 7 |
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

Rex Crum, CBS.MarketWatch.com (2003). Sun Micro slammed as quarterly report disappoints.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

analyst-commentary, market-reaction-reporting
