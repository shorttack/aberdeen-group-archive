# Comdex 2003: Sun Microsystems sets new, aggressive strategy

| Field | Value |
|-------|-------|
| Author | Kim Peterson, The Seattle Times |
| Date | 2003-11-18 |
| Type | news-article |
| Domain | server-vendor-strategy |
| License | CC-BY-4.0 |

## Abstract

Seattle Times article (Nov 18 2003, Kim Peterson) reporting Scott McNealy's Comdex 2003 keynote where Sun unveiled two aggressive pivots: (1) Sun Fire servers using AMD Opteron processors, and (2) a strategic partnership with China Standard Software for Java Desktop System rollout to 200 million Chinese desktops at $100/user. Sun was then in deep trouble — $286M Q4 FY03 loss, 2+ years of revenue declines, stock at $4.08. Peter Kastner of The Aberdeen Group frames the Opteron move as a direct IBM challenge: 'Sun can use AMD's Opteron to compete directly against IBM in the head-to-head Opteron battle for price-conscious buyers of high-performance computers.' He also notes the customer-retention angle. Yankee Group's Dana Gardner highlights the novel nation-level sales strategy: 'It's a lot easier to sell to a whole country vis-a-vis a government than it is to go company by company.'

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 16 |
| technologies.csv | 6 |
| observations.csv | 8 |
| codes.csv | 27 |

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

Kim Peterson, The Seattle Times (2003). Comdex 2003: Sun Microsystems sets new, aggressive strategy.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

event-reporting, analyst-commentary
