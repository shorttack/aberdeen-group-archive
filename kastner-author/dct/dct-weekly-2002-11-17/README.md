# PC Deals Weekly Analysis: November 17, 2002

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-11-17 |
| Type | dct |
| Domain | DCT-retail-pc-market |
| License | CC-BY-4.0 |

## Abstract

Intel's Pentium 4 at 3.06 GHz with Hyper-Threading (HT) technology arrived November 14th. HT adds a trivial number of transitors that add a measurable amount of performance boost for most users. Thus, P4 machines with HT will perform much more crisply than the implied boost from a 200 MHz speed-bump over yesterday's king of the chips, the 2.8 GHz P4.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 13 |
| technologies.csv | 9 |
| observations.csv | 21 |
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

Peter S. Kastner (2002). PC Deals Weekly Analysis: November 17, 2002.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-tracking, expert-opinion, price-tracking
