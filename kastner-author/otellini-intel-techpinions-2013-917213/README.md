# On the Impact of Paul Otellini's CEO Years at Intel (Tech.pinions, Published Version)

| Field | Value |
|-------|-------|
| Author | Peter Kastner |
| Date | 2013-04-28 |
| Type | topic-analysis |
| Domain | semiconductors-intel |
| License | CC-BY-4.0 |

## Abstract

Published Tech.pinions column by Peter Kastner assessing the 40-year Intel career and 8-year CEO tenure (2005-2013) of Paul Otellini, organized across four dimensions: technology (tick-tock model, multi-core, High-K metal gate, 3D tri-gate, performance-per-watt), growth (BRIC geographies, mobile, software via McAfee and Wind River, intelligent systems), competition (AMD retake, ARM mobile threat), and finance (revenue up 60% to ~$53B; dividend initiation). Notes the missed-iPhone cost to Intel and the new emerging devices division.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 14 |
| technologies.csv | 12 |
| observations.csv | 22 |
| codes.csv | 32 |

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

Peter Kastner (2013). On the Impact of Paul Otellini's CEO Years at Intel (Tech.pinions, Published Version).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, executive-profile, longitudinal-review
