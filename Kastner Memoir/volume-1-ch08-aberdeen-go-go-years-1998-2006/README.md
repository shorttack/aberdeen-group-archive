# Chapter 8: The Go-Go Years — Aberdeen at Scale (1998–2006)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2026-05-14 |
| Type | memoir |
| Domain | memoir/volume-1 |
| License | CC-BY-4.0 |

## Abstract

Peter S. Kastner chronicles Aberdeen Group's transformation from a boutique partnership into a venture-backed research firm employing up to 150 analysts during the internet boom, and its subsequent collapse and recovery following the dot-com crash. The chapter details audited revenue and profit figures from 1997 to 2006, the firm's methodological evolution (benchmark research, TCO models, best-practices frameworks), key analytical predictions (SOA, open-source enterprise adoption, consumerization of IT), the CEO transition to Jamie Bedard, and the October 2006 acquisition by Harte-Hanks for $42 million just before the financial crisis.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 18 |
| technologies.csv | 21 |
| observations.csv | 126 |
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

Peter S. Kastner (2026). Chapter 8: The Go-Go Years — Aberdeen at Scale (1998–2006).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

oral-history
