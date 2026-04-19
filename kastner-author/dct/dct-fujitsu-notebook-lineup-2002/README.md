# Fujitsu Notebook Product Lineup Snapshot, Late 2002

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-12-01 |
| Type | dct |
| Domain | dct |
| License | CC-BY-4.0 |

## Abstract

Complete Fujitsu notebook product lineup snapshot circa late 2002, covering CELSIUS Mobile H Workstation variants (FPCM60101/60102), LifeBook C Series (C2210 variants), LifeBook E Series (E7110/E2010), LifeBook P Series ultra-portables, LifeBook S Series (S6010), and LifeBook T Series (T3010 tablet). Each entry captures MSRP, Mobile Pentium 4/Pentium III-M CPU, memory (DDR266), optical drives, HDD, networking (modem/LAN, optional 802.11b WLAN), display size, weight, OS (XP Home/Pro), warranty, and marketing positioning. Provides competitive baseline for Fujitsu's U.S. notebook presence during the HP Compaq / IBM ThinkPad duopoly era.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 7 |
| observations.csv | 8 |
| codes.csv | 23 |

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

Peter S. Kastner (2002). Fujitsu Notebook Product Lineup Snapshot, Late 2002.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

competitive-profiling
