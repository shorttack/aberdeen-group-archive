# AMD Beats Apple's G5 and Intel's P4

| Field | Value |
|-------|-------|
| Author | Jay Lyman, TechNewsWorld |
| Date | 2003-10-15 |
| Type | news-article |
| Domain | 64-bit-desktop-processors |
| License | CC-BY-4.0 |

## Abstract

TechNewsWorld article (Oct 15 2003, Jay Lyman) on PC World benchmarks showing AMD's Athlon 64 and dual Opteron processors beating Apple's Power Mac G5 and Intel's Pentium 4 on Word, Premiere 6, Quake III, and Photoshop 7.0.1. Aberdeen chief research officer Peter Kastner provides the central skeptical voice: 'Tune in a year from now, and then we'll have a better idea of how these chips run on real-world, 64-bit applications' — noting the PC World tests did not use 64-bit software, so 'users really aren't getting any benefit out of 64-bit instructions on Athlon or Apple.' Kastner calls Athlon 'a very competitive chip priced at a heady level for AMD' and predicts Apple developers will quickly optimize for 64-bit while Athlon64's market remains unclear pending 64-bit Windows XP. IDC's Shane Rau and Gartner's Martin Reynolds add benchmark-timing and memory-bandwidth context.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 14 |
| technologies.csv | 7 |
| observations.csv | 9 |
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

Jay Lyman, TechNewsWorld (2003). AMD Beats Apple's G5 and Intel's P4.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

product-analysis, benchmark-commentary, analyst-commentary
