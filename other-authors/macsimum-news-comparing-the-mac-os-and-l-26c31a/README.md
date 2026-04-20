# Comparing the Mac OS and Linux markets just doesn't work

| Field | Value |
|-------|-------|
| Author | Dennis Sellers (Macsimum News); Peter Kastner (secondary-source quote via Wired) |
| Date | 2004-08-15 |
| Type | press-article |
| Domain | desktop-os-market-share |
| License | CC-BY-4.0 |

## Abstract

Macsimum News opinion piece by Dennis Sellers arguing that Mac OS vs. Linux market-share comparisons are fundamentally apples-to-oranges. Draws on Peter Kastner's Wired-quoted ~3% Mac share / lower Linux share figure as a key datapoint; notes that Linux desktop installed-base counts often include PCs on which Windows is subsequently pirate-installed, distorting comparisons.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 2 |
| observations.csv | 4 |
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

Dennis Sellers (Macsimum News); Peter Kastner (secondary-source quote via Wired) (2004). Comparing the Mac OS and Linux markets just doesn't work.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

press-opinion, secondary-source-analysis
