# Corporate Notebook Lineup Snapshot, January 2003

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-01-15 |
| Type | dct |
| Domain | dct |
| License | CC-BY-4.0 |

## Abstract

Two-sheet (Business and Consumer) snapshot of corporate notebook lineups as of January 2003, profiling HP Compaq Evo N800v / Evo 1000c / N610c / N410c, IBM ThinkPad T30 / X30, and parallel consumer configurations across three form-factor bands (Standard, Thin & Light, Value). Each entry captures manufacturer online price, street price (e.g., CDW), processor (Mobile Pentium 4-M or Pentium III-M), screen size, memory, HDD, optical drive, weight, warranty, OS (Windows XP Pro), Office XP Pro availability, and street-site source.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 4 |
| observations.csv | 11 |
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

Peter S. Kastner (2003). Corporate Notebook Lineup Snapshot, January 2003.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

competitive-profiling
