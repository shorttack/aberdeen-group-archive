# Tech Investor: Is SARS sickening tech?

| Field | Value |
|-------|-------|
| Author | Eric Hellweg, CNN/Money |
| Date | 2003-04-10 |
| Type | column-opinion |
| Domain | supply-chain-pandemic-risk |
| License | CC-BY-4.0 |

## Abstract

CNN/Money Tech Investor column (Apr 10 2003) by Eric Hellweg on SARS impact on the tech industry. Early-outbreak fears: Intel canceled developer conferences in Beijing and Taipei; Sun postponed Shanghai conference; Motorola briefly closed a Singapore factory; Microchip Technology blamed SARS for a Q1 earnings warning; First Albany analyst Auguste Richard cut 2003 semiconductor revenue growth forecast from 8% to zero. Peter Kastner — coauthor of an Aberdeen Group SARS report and Aberdeen's chief research officer — had already tempered his own initial dire predictions by the column date. Kastner: 'Goods are moving freely, and we haven't seen changes in commodity spot prices, which might indicate a decrease in supply.' Key prescient Kastner China-supply-chain warning: 'Tech companies, which heretofore had rushed to outsource to China because of the quality and low cost, are now rethinking whether they can put all their high-tech eggs in the China basket... This isn't the first time China has stiff-armed the world on a major global health issue.'

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 3 |
| observations.csv | 8 |
| codes.csv | 28 |

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

Eric Hellweg, CNN/Money (2003). Tech Investor: Is SARS sickening tech?.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

analyst-commentary, macro-commentary
