# DCT Segment Priorities Matrix (Home / Work / Mobile)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-11-01 |
| Type | dct |
| Domain | dct/segment-prioritization |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Personal IT / DCT segment-priorities matrix cross-tabulating four technology categories (Computers & Peripherals, Networking, Productivity Apps & Services, Leisure & Entertainment) against three contexts (Home, Work, Mobile). Captures priority rankings with analyst notes — including desktop-CPU 2.2->3.6 GHz 18-month roadmap, Pentium 4 laptop impact, 2002 as a 'banner year for home networks' caveated on wireless usability, and 2003 PC/TV/stereo integration outlook.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 16 |
| observations.csv | 21 |
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

Peter S. Kastner (2002). DCT Segment Priorities Matrix (Home / Work / Mobile).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis
