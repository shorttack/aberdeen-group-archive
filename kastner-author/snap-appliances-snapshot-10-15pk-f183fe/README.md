# Aberdeen Vendor SnapShot: Snap Appliance Inc.

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003 |
| Type | case-analysis |
| Domain | Network Attached Storage (NAS) / SMB/Enterprise Storage |
| License | CC-BY-4.0 |

## Abstract

Aberdeen vendor snapshot profile of Snap Appliance Inc. (formerly Meridian Data, then Quantum subsidiary), the number-one volume NAS provider with 130,000+ unit installed base. Covers product line from workgroup (Snap Server 1100/2200) through departmental (4100/4200/4500) and enterprise (SnapServer 14000) tiers, software partnerships, and ATA-based midline storage positioning.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 17 |
| technologies.csv | 17 |
| observations.csv | 21 |
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

Peter S. Kastner (2003). Aberdeen Vendor SnapShot: Snap Appliance Inc..
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Vendor profile; product analysis; qualitative assessment
