# ClassMate PC Evaluation Notes

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2008-01-01 |
| Type | memoir |
| Domain | memoir/umpc-evaluation/emerging-markets |
| License | CC-BY-4.0 |

## Abstract

Kastner's detailed hands-on evaluation notes for the Intel Classmate PC (CMPC) — an ultra-mobile education PC — tested both in the United States and at a teacher's college in Jacmel, Haiti where teachers and K-12 students handled the device. Covers install quirks (50Hz/220v international power cable, WLAN activation gating), tutorial guide errata, operational issues (keyboard defaults, 7-inch screen real estate, standby battery), and extensive buggy behavior in the Mythware e-Learning Class v6.0 software. Concludes the hardware is a 'fine, workable device' for small hands, but Windows XP 'in silicon' carries high IT maintenance cost and the software is buggy but promising.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 5 |
| observations.csv | 26 |
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

Peter S. Kastner (2008). ClassMate PC Evaluation Notes.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

product-evaluation, field-testing, personal-recollection
