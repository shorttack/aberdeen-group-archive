# Maxtor Midline Storage Interactive Demo (Adobe Flash)

| Field | Value |
|-------|-------|
| Author | Aberdeen Group / Maxtor Corporation |
| Date | 2003 |
| Type | consulting-report |
| Domain | Enterprise Storage / Interactive Sales Tool |
| License | CC-BY-4.0 |

## Abstract

Macromedia Flash 6 (SWF) interactive demo of the enterprise storage hierarchy, illustrating where Maxtor midline storage fits between high-end Fibre Channel storage and low-end desktop drives. Created circa 2003 by Aberdeen Group as a sales/marketing tool for Maxtor CMO Stephen DiFranco's midline storage initiative. Binary file; text extraction not possible. Represents an early and innovative use of interactive analyst content as a sales enablement tool.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 2 |
| observations.csv | 5 |
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

Aberdeen Group / Maxtor Corporation (2003). Maxtor Midline Storage Interactive Demo (Adobe Flash).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Interactive Flash animation; binary SWF file; metadata-only extraction
