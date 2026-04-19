# Kastner Personal IDF Notes — Consumer Spending, Extreme Edition, Prescott, BTX, DTCP

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-09-16 |
| Type | memoir |
| Domain | personal-notes/intel-idf |
| License | CC-BY-4.0 |

## Abstract

Short handwritten-style notes by Peter Kastner captured at an Intel IDF (content indicates Fall 2003 — Pentium 4 Extreme Edition launch, 90nm Prescott demo with PCI Express graphics, BTX (Balanced Technology Extended) 'Bigwater' form factor, iCube Korea MPEG2-to-MPEG4 on-the-fly compression, DTCP-over-IP content protection). Preserved as memoir — fragment of Kastner's in-session notetaking practice.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 7 |
| observations.csv | 8 |
| codes.csv | 24 |

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

Peter S. Kastner (2003). Kastner Personal IDF Notes — Consumer Spending, Extreme Edition, Prescott, BTX, DTCP.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

oral-history, document-review
