# Timing Your Move to Next Generation Operating Systems

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner, John Logan, Thomas Willmott |
| Date | 1993-02-01 |
| Type | market-study |
| Domain | operating-systems |
| License | CC-BY-4.0 |

## Abstract

This Aberdeen Group workbook presents a structured timing framework for IS executives evaluating the transition to next-generation operating systems in 1993. It identifies five key OS trends — single-to-multi-tasking, single-to-multi-threaded, LAN/desktop integration, GUI adoption, and distributed client-server progress — and analyzes hot spots across the Three-Tier Plus topology. The study evaluates Unix derivatives, desktop OS alternatives from Windows 3.1 to OS/2, Power PC, Windows NT, and Solaris, and concludes that Unix is the clear mid-range choice while 486/Windows or Macintosh remain the standard desktop buy through mid-1994.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 27 |
| technologies.csv | 19 |
| observations.csv | 30 |
| codes.csv | 28 |

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

Peter S. Kastner, John Logan, Thomas Willmott (1993). Timing Your Move to Next Generation Operating Systems.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, technology-assessment, vendor-profiling
