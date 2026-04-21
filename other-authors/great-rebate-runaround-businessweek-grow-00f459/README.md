# The Great Rebate Runaround

| Field | Value |
|-------|-------|
| Author | Brian Grow (with Rishi Chhatwal), BusinessWeek |
| Date | 2005-12-05 |
| Type | news-article |
| Domain | consumer-rebates-regulation |
| License | CC-BY-4.0 |

## Abstract

BusinessWeek cover story (Dec 5 2005, Brian Grow with Rishi Chhatwal) that became the canonical exposé of the U.S. mail-in rebate industry. Peter S. Kastner, then director of consulting firm Vericours Inc., provides the pivotal 40% statistic: 'fully 40% of all rebates never get redeemed because consumers fail to apply for them or their applications are rejected,' translating into more than $2B of extra revenue per year for retailers and suppliers. Aberdeen's Paula Rosenblum adds: 'anything less than 100% redemption is free money.' The article details industry lingo (breakage, slippage), TCA's 10-35% expected redemption rates, TiVo's $5M rebate-expense reduction from 50,000 of 104,000 subscribers failing to redeem, Massachusetts suing Young America for $43M in uncashed checks, NY AG Spitzer settling with Samsung for $200K over apartment-address rules, California SB (Figueroa) vetoed by Gov. Schwarzenegger, consumer complaints to BBB tripled 2001-2004 (964 to 3,641), and Best Buy / Staples transitions away from mail-in rebates. Kastner's Vericours affiliation here (not Aberdeen) is notable — this is his post-Aberdeen consulting/advisory period.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 38 |
| technologies.csv | 3 |
| observations.csv | 14 |
| codes.csv | 34 |

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

Brian Grow (with Rishi Chhatwal), BusinessWeek (2005). The Great Rebate Runaround.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

investigative-journalism, industry-analysis, expert-opinion
