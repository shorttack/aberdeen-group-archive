# Apple Ships Hot PowerMac G5

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-06-23 |
| Type | dct |
| Domain | dct |
| License | CC-BY-4.0 |

## Abstract

Hot Topic piece on Apple's Power Mac G5 launch. Analyzes SPEC CPU 2000 benchmark claims (G5 2.0 GHz beats Xeon and P4 in floating point, loses integer; dual-G5 beats both in integer and floating point), the 64-bit marketing claim relative to Alpha/HP-PA/PowerPC/Sun/Itanium 2 predecessors, the $3998 configuration with ATI 9800 Pro and Apple 17in Studio Display, PCI-X and 8x AGP I/O, USB/FireWire 800/gigabit Ethernet. Concludes G5 is legitimate workstation competitor but an Apple-base renovation rather than a PC-attack product.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 20 |
| observations.csv | 19 |
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

Peter S. Kastner (2003). Apple Ships Hot PowerMac G5.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

product-review, competitive-analysis
