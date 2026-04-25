# Rochester Business Journal — 'Computer resellers suffering while many delay upgrades' (Kathy Quinn Thomas; PSK Aberdeen Group quoted, 2002-07-05)

| Field | Value |
|-------|-------|
| Author | Kathy Quinn Thomas (Rochester Business Journal staff) |
| Date | 2002-07-05 |
| Type | regional-trade-press |
| Domain | PC-reseller-channel |
| License | CC-BY-4.0 |

## Abstract

RBJ's July 5 2002 piece chronicles the post-bubble PC channel slump in Rochester NY. PSK quoted: 'The replacement PC market is driven by price, as buyers see little to differentiate individual brands. The global recession last year led to a decline in sales, even as industry overcapacity drove prices lower.' Local VARs cited (Brite Computers $16.7M / 45 employees; Soyata Computers $7.2M / 27 employees; Manchester Technologies $10M local / 22 employees). Q1-2002 worldwide PC shipments 31.4M (vs 32.2M Q1-2001, -2.5%). Apple/AMD/Intel all cut earnings forecasts mid-June 2002. Gartner: 'Consider it a respite, not a turning point.' eTForecasts: 175M PCs in U.S. in 2001. Joseph Osha (Merrill Lynch): 'It's hard for things in general to get better if PCs are still bad.'

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 14 |
| technologies.csv | 1 |
| observations.csv | 7 |
| codes.csv | 29 |

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

Kathy Quinn Thomas (Rochester Business Journal staff) (2002). Rochester Business Journal — 'Computer resellers suffering while many delay upgrades' (Kathy Quinn Thomas; PSK Aberdeen Group quoted, 2002-07-05).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Rochester Business Journal weekly cover-package on the local VAR/reseller slump as the 1990s 3-year PC replacement cycle stretched. Quotes PSK as 'technology analyst with Boston's Aberdeen Group Inc.' on replacement-PC market dynamics.
