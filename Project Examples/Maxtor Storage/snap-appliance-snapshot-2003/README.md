# AberdeenGroup SnapShot: Snap Appliance Inc.

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-10-15 |
| Type | case-analysis |
| Domain | enterprise-storage-NAS |
| License | CC-BY-4.0 |

## Abstract

This Aberdeen Group SnapShot profiles Snap Appliance Inc., the self-described number-one volume NAS provider, which was reborn as a private company in 2002 after being spun out of Quantum. The profile details Snap's product line spanning workgroup to enterprise NAS using inexpensive ATA disks, and explicitly maps Snap's coverage of Aberdeen's midline storage categories including staging, fixed content, consolidation, replication, and PC backup. The document positions Snap as a key validation of Aberdeen's midline disk storage thesis.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 19 |
| technologies.csv | 13 |
| observations.csv | 27 |
| codes.csv | 44 |

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

Peter S. Kastner (2003). AberdeenGroup SnapShot: Snap Appliance Inc..
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

vendor-profiling, competitive-analysis, product-analysis
