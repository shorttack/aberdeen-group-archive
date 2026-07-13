# PyramidOLTP Overview

| Field | Value |
|-------|-------|
| Author | Wayne T. Kernochan; Robert J. Sakakeeney |
| Date | 1995 |
| Type | market-study |
| Domain | midrange-platforms |
| License | CC-BY-4.0 |

## Abstract

This Aberdeen Group presentation frames mid-1990s enterprise computing with its Three Tier Plus model and then profiles the leading commercial midrange RISC/UNIX suppliers. It combines market-share and revenue sizing with vendor-by-vendor strengths, challenges, and buying guidance for IBM, Hewlett-Packard, Digital Equipment, Sun Microsystems, and AT&T GIS/NCR. The deck is also notable for explicit forward-looking claims about RS/6000 momentum, UltraSPARC, Digital large in-memory databases, and NCR's Intel server role.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 15 |
| technologies.csv | 18 |
| observations.csv | 41 |
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

Wayne T. Kernochan; Robert J. Sakakeeney (1995). PyramidOLTP Overview.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, competitive-profiling, market-sizing
