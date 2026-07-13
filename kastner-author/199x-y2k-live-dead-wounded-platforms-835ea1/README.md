# Y2K Live, Dead & Wounded

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (Aberdeen Group) |
| Date | 1998 |
| Type | topic-analysis |
| Domain | Y2K-platform-viability |
| License | CC-BY-4.0 |

## Abstract

This four-slide Aberdeen Group deck classifies major enterprise platforms and application bases as likely "living," "dead," or "wounded" in the Year 2000 transition. It highlights IBM MVS, AS/400, AIX, HP-UX, Solaris, and Windows NT as likely survivors while flagging older IBM, HP 3000, Bull, Data General, Unisys, Wang, and legacy manufacturing environments as vulnerable or obsolete. A final slide reframes the taxonomy as a services-targeting guide by steering Y2K remediation effort toward attractive downstream customer segments and away from riskier or less desirable ones.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 19 |
| observations.csv | 22 |
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

Peter S. Kastner (Aberdeen Group) (1998). Y2K Live, Dead & Wounded.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, expert-opinion
