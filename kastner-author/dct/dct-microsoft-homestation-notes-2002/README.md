# Microsoft HomeStation — Analyst Briefing Notes

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-02-15 |
| Type | dct |
| Domain | dct/home-platform-strategy |
| License | CC-BY-4.0 |

## Abstract

Briefing notes on Microsoft's HomeStation concept — a home-server platform bridging traditional PC with home stereo and TV, built on Xbox hardware with Windows XP 2.0 (codename Longwood) replacing Windows 2000, Terminal Server support to drive Mira tablets and remote controls, and nVidia TV-tuner integration. Freestyle is the HomeStation UI (demoed at CES 2002). Frames Microsoft as a $1.5B hardware player via mice, WebTV, and Xbox — and HomeStation as a stealth path to become a major PC vendor.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 11 |
| observations.csv | 15 |
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

Peter S. Kastner (2002). Microsoft HomeStation — Analyst Briefing Notes.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

field-research, industry-analysis
