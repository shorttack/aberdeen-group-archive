# Aberdeen Group 'Harnessing the Megatrends of [the 90s]' MFA-CS-MIS deck (May 1993, Aberdeen institutional)

| Field | Value |
|-------|-------|
| Author | Aberdeen Group (no individual presenter named on extracted slides; copyright 1993 Aberdeen Group, Inc.) |
| Date | 1993-05 |
| Type | consulting-presentation-deck |
| Domain | enterprise-IT-strategy |
| License | CC-BY-4.0 |

## Abstract

Aberdeen's 1993 institutional megatrends framework. Headline: up to 50% of capital expenditure is now for IT; information is part of products and services; all employees are expected to be computer-comfortable; online data for real-time decisions is the standard, not the goal. 1992 Large Broker PC purchasing benchmark: 5,100 CPUs, $22.8M, 95,000 MIPS, 250 WMIPs. Mainframe-alternatives section: 'mainframes do not provide a differentiator'; 'consolidate data centers / cheap MIPS / outsource / freeze MIS budgets / downsize with replicated systems / non-MIS divisional installations.' Andy Grove (Intel CEO) WSJ Jan 18 1993 quote endorses integration-as-opportunity framing. Three-tier-plus persists from 1991 Logan deck and 1992 PSK SNR slides.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 5 |
| observations.csv | 7 |
| codes.csv | 31 |

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

Aberdeen Group (no individual presenter named on extracted slides; copyright 1993 Aberdeen Group, Inc.) (1993). Aberdeen Group 'Harnessing the Megatrends of [the 90s]' MFA-CS-MIS deck (May 1993, Aberdeen institutional).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Aberdeen Group consulting deck for an MFA-CS-MIS audience. Walks Enterprise Infrastructure (50% capex now IT) -> Users of IT -> Technology Advances -> 1992 Large Broker PC Purchases (95,000 MIPS / 5,100 CPUs / $22.8M / 250 WMIPs) -> Suppliers (less profitable; Computer Associates legacy-product model) -> MIS Role -> Enterprise Reactions -> Challenges -> Mainframe Alternatives -> Downsizing -> Enterprise Information Architecture -> Enterprise Topology ('Three-tier plus is state-of-the-art') -> Critical Technology Planning Areas. Cites Andy Grove WSJ quote 18 January 1993.
