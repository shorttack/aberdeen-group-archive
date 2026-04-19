# Asian Virus Casts Shadow Over Supply Chain: SARS Impact on Asia/Pacific Semiconductor and Electronics Manufacturing

| Field | Value |
|-------|-------|
| Author | Russ Craig; Peter S. Kastner |
| Date | 2003-04-16 |
| Type | white-paper |
| Domain | electronics-supply-chain |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group analyst report (Russ Craig and Peter Kastner) excerpted by PlanetAnalog/EBN on April 16, 2003, examining the potential impact of the SARS epidemic on the PRC- and Taiwan-centered global electronics supply chain. The authors quantify Asia/Pacific's 37% share of 2002 semiconductor consumption ($52B), document early SARS clusters in Guangdong, Shenzhen, Guangzhou, Hong Kong, Singapore, and Taiwan, and assess the vulnerability of dependable component supply — particularly for no-second-source items like PRC-made AC/DC power supplies — should quarantines extend. The report ends with a prescient warning that investor confidence in the PRC will take years to rebuild given government opacity about the outbreak.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 21 |
| technologies.csv | 7 |
| observations.csv | 20 |
| codes.csv | 31 |

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

Russ Craig; Peter S. Kastner (2003). Asian Virus Casts Shadow Over Supply Chain: SARS Impact on Asia/Pacific Semiconductor and Electronics Manufacturing.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, supply-chain-analysis, risk-assessment
