# Desktop PCs in Decline as Notebooks Surge

| Field | Value |
|-------|-------|
| Author | Jay Lyman, TechNewsWorld |
| Date | 2004-01-15 |
| Type | news-article |
| Domain | pc-form-factor-shift |
| License | CC-BY-4.0 |

## Abstract

TechNewsWorld article (Jan 15 2004, Jay Lyman) covering a new Meta Group research report predicting that by 2006 only 45% of corporate users will primarily use a desktop PC, 40% will primarily use a notebook or tablet, and 15% will rely on thin clients or other information appliances. Aberdeen Group chief research officer Peter Kastner summarizes the retail evidence: consumer and corporate notebook computers are 'flying off the shelves,' making mobile PCs the fastest growing segment. IDC analyst Alan Promisel forecasts U.S. notebooks at 47% of PC shipments by 2007, stabilizing near 50%. Meta Group VP Steve Kleynhans predicts by 2007 users will interact with at least four distinct devices daily — home PC, smart TV, work PC, mobile — forcing software vendors toward information-synchronization and roaming apps.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 6 |
| observations.csv | 11 |
| codes.csv | 27 |

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

Jay Lyman, TechNewsWorld (2004). Desktop PCs in Decline as Notebooks Surge.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-forecast, analyst-commentary
