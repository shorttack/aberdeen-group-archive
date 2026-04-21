# Intel Targets SMBs With Revamped vPro

| Field | Value |
|-------|-------|
| Author | Mark Long, Data Storage Today / CIO Today Network |
| Date | 2008-09-23 |
| Type | news-article |
| Domain | PC-manageability-SMB |
| License | CC-BY-4.0 |

## Abstract

Data Storage Today / CIO Today Network article (Sep 23 2008) by Mark Long on Intel's 2008 revamp of the vPro business-PC platform, now targeting small and medium businesses with limited IT staff. New features: automated PC maintenance/repair/security, Remote Alert (PC calls for help autonomously even when off), IT Director dashboard for fleets under 25 PCs, Intel-Symantec patch-compliance partnership, and full manageability outside the firewall for laptops in the field. Peter Kastner, vice president and research director at Aberdeen Group, is the primary analyst voice: 'No matter where in the world the device is, the corporate laptops that workers take home or on business trips are all now manageable, fixable, and diagnosable. As long as you can get to a network, vPro and related technology can help to solve the problem.' On TCO: Kastner cites major service companies' prior measurements of $700-$3,000/PC/year pre-vPro; post-vPro figures are under $500/PC/year on the low end and under $2,000 on the high end — 'a huge savings that can go right to the bottom line.' Also quoted: Matthew Wilkins (principal analyst, iSuppli) and Kevin Unbedacht (Symantec).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 4 |
| observations.csv | 8 |
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

Mark Long, Data Storage Today / CIO Today Network (2008). Intel Targets SMBs With Revamped vPro.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, analyst-commentary
