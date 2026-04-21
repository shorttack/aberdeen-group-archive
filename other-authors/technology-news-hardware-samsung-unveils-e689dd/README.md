# Samsung Unveils Fastest Mobile CPU on the Market

| Field | Value |
|-------|-------|
| Author | Jay Lyman, TechNewsWorld |
| Date | 2003-07-21 |
| Type | news-article |
| Domain | mobile-handheld-processors |
| License | CC-BY-4.0 |

## Abstract

TechNewsWorld article (Jul 21 2003, Jay Lyman) on Samsung's 533 MHz S3C2440 mobile processor (ARM920T core, 32-bit RISC, 0.13 micron, 1.3V), claimed as world's fastest mobile CPU — besting Intel's XScale top-end 400 MHz. S3C2440 targets mobile phones and PDAs with features including camera interfaces, LCDs, USB, touch screens; supports Windows CE, Palm OS, Symbian, Linux; built-in flash boot-loader. Aberdeen chief research officer Peter Kastner provides the strategic read: the S3C2440 will speed and enhance handheld functions such as encrypting e-mail and compressing digital images — but Samsung 'might have difficulty getting the new processor into phones and PDAs other than its own. Breaking into this market is fairly difficult.' Kastner cites proprietary architectures from Nokia and other device-maker commitments as barriers: '400-million-unit-per-year mobile business takes more than a fast processor.' Yankee Group's John Jackson: microprocessing power isn't everything; power management and memory-subsystem access matter equally.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 7 |
| observations.csv | 7 |
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

Jay Lyman, TechNewsWorld (2003). Samsung Unveils Fastest Mobile CPU on the Market.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

product-launch-analysis, analyst-commentary
