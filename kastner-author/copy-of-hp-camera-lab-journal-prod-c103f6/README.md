# Caveat Emptor: HP's Consumer IT Leadership Needs New Focus on Consumers

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2001-12-05 |
| Type | case-analysis |
| Domain | Consumer Electronics / Digital Cameras / Customer Support |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Lab Journal dated December 5, 2001. Kastner recounts a first-person experience evaluating HP's C315 digital camera through installation under Windows ME and then Windows XP. The report identifies a critical undocumented incompatibility: the HP photo transfer software shipped with the camera interferes with Windows XP's native camera support, causing photo transfer failures. HP's support web site does not document the workaround (not installing the bundled software), and the support technician was unaware of the issue. Aberdeen concludes HP's consumer IT leadership strategy requires improved process, simpler documentation, and better support to prevent costly support calls and consumer defection.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 6 |
| observations.csv | 16 |
| codes.csv | 30 |

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

Peter S. Kastner (2001). Caveat Emptor: HP's Consumer IT Leadership Needs New Focus on Consumers.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

First-person lab evaluation; real-product consumer experience testing with HP C315 digital camera
