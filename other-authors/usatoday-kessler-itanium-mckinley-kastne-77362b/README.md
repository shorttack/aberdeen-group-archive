# Intel Antes Up $1B on Success of Itanium Line (USA Today)

| Field | Value |
|-------|-------|
| Author | Michelle Kessler (USA Today) |
| Date | 2002-03-01 |
| Type | trade-press-feature |
| Domain | semiconductor/Itanium-IA-64/server-chip-strategy |
| License | CC-BY-4.0 |

## Abstract

Michelle Kessler's USA Today story (1 March 2002) on Intel's Itanium line and the McKinley successor preview. Reports $1 billion six-year HP+Intel Itanium investment, $1000-$4000 chip pricing, and the chicken-and-egg software adoption problem caused by Itanium's 64-bit architecture incompatibility with 32-bit Intel. Quotes Aberdeen Group's Peter Kastner: 'Intel and H-P are holding a party, and nobody's coming.' Notes Intel's reported backup plan to develop a 64-bit version of its 32-bit processor line (foreshadowing AMD64/x86-64 response and Intel's eventual EM64T). Cites HP+Compaq merger as additional Itanium-volume risk.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 5 |
| observations.csv | 11 |
| codes.csv | 33 |

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

Michelle Kessler (USA Today) (2002). Intel Antes Up $1B on Success of Itanium Line (USA Today).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

press-feature-with-analyst-quotes
