# Mac OS vs. Linux: Who's #2?

| Field | Value |
|-------|-------|
| Author | Bryan Chaffin and Vern Seward (The Mac Observer); Peter Kastner (secondary-source quote) |
| Date | 2004-08-11 |
| Type | press-article |
| Domain | desktop-os-market-share |
| License | CC-BY-4.0 |

## Abstract

The Mac Observer analytical piece reconciling competing claims about #2 desktop OS share between Mac OS X and Linux. Authors aggregate data from HP, IDC, Wired, Gartner, Google browser logs, and analyst commentary — including Peter Kastner's ~3% Mac share estimate (originally to Wired) as a secondary-source quote. Concludes that definitions matter: Linux installed seats (including piracy, embedded, preloaded non-Windows PCs) and active Mac desktop users are measured inconsistently.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 3 |
| observations.csv | 6 |
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

Bryan Chaffin and Vern Seward (The Mac Observer); Peter Kastner (secondary-source quote) (2004). Mac OS vs. Linux: Who's #2?.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

press-coverage, secondary-source-analysis, competitive-profiling
