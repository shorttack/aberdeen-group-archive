# Fault-Tolerant Market To Hit $2 Billion in '87 — trade press, 1987 (PSK at Stratus quoted)

| Field | Value |
|-------|-------|
| Author | S.K. (staff) |
| Date | 1987-01-01 |
| Type | press-article |
| Domain | fault-tolerant-computing-market-sizing |
| License | CC-BY-4.0 |

## Abstract

Trade-press article on the 1987 fault-tolerant computing market structure: "a two-man fight" between Marlboro MA-based Stratus Computer and Cupertino CA-based Tandem Computers, with IBM 'on the edge swinging but unable to land a solid punch.' Includes a '10-year forecast for disaster recovery services' bar chart by International Resource Development Inc. (Norwalk CT) showing total end-user revenue rising from $140M (1987) to $340M (1997). Article cites two competing 1987 FT market sizings: **Pete Kastner, manager of marketing development at Stratus**, predicts $2 billion in 1987 with 40-50% annual growth through 1990, citing financial services, brokerage, POS, and shop-floor applications as exploding categories; **International Resource Development** offers a more cautious $1B 1987 / $1.2B 1990 figure. Datquest's Van Weathers identifies two big developments: target-market expansion (POS, telecom) bringing in new vendors, and price/performance pressure pushing per-second-transaction costs down. Profiles Illinois Bell's Networker monitoring system (built on Parallel Computers fault-tolerant systems with battery backup), NCR's bread-and-butter POS push into FT at $25-45K, Tandem's new low-cost expandable-processor lineup, and Tolerant Systems Inc.'s Unix-based push at banking/telecom/manufacturing/federal.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 3 |
| observations.csv | 5 |
| codes.csv | 24 |

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

S.K. (staff) (1987). Fault-Tolerant Market To Hit $2 Billion in '87 — trade press, 1987 (PSK at Stratus quoted).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, market-sizing, expert-opinion
