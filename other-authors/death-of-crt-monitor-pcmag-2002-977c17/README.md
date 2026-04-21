# The Death of the CRT Monitor

| Field | Value |
|-------|-------|
| Author | Cade Metz, PC Magazine |
| Date | 2002-11-01 |
| Type | news-article |
| Domain | pc-displays |
| License | CC-BY-4.0 |

## Abstract

PC Magazine / PCMag.com article (Nov 1 2002, Cade Metz) on the LCD-vs-CRT monitor transition. Peter Kastner, Aberdeen Group vice president and senior researcher, provides key market data: LCDs at 40% of desktop-display market with ~2M units/month at $800M revenue/month (average $400/unit). iSuppli/Stanford Resources' Rhonda Alexander offers more conservative 29% LCD share, with tracking from 3% (Q1 2000) → 5% (early 2001) → 21% (Jan 2002). Both analysts predict LCDs will outnumber CRTs as the standard PC monitor in 2003. Planar Systems' Rob Baumgartner addresses video-latency concerns. U Minn Carlson School professors Murtha and Lenway predict LCDs will outnumber CRTs 5:1 by 2006. Kastner's pre-CRO Aberdeen era (VP/senior researcher).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 13 |
| technologies.csv | 2 |
| observations.csv | 12 |
| codes.csv | 29 |

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

Cade Metz, PC Magazine (2002). The Death of the CRT Monitor.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-forecast, analyst-commentary
