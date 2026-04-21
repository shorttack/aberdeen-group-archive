# Gateway Goes Gigabit, Wireless

| Field | Value |
|-------|-------|
| Author | Kirk L. Kroeker, TechNewsWorld |
| Date | 2004-04-06 |
| Type | news-article |
| Domain | enterprise-networking-smb |
| License | CC-BY-4.0 |

## Abstract

TechNewsWorld article (Apr 6 2004, Kirk L. Kroeker) on Gateway's entry into enterprise networking with the 7200/7400/7600 Series Layer 2 managed and unmanaged network switches (based on Broadcom switch silicon) and the Gateway 7000 Series Wi-Fi access points (802.11g / 802.11a+g, Intel IPX422 processor, PoE, RADIUS, VLAN). Launched 'in the aftermath of a major announcement about shutting all its retail stores' — Gateway exiting brick-and-mortar after eMachines acquisition. Aberdeen EVP and chief research officer Peter Kastner provides the strategic framing: 'In both their price and functionality, Gateway is taking a disruptive approach with these two new wireless [access points]. Many wireless vendors are ignoring the pleas of small- and medium-sized businesses, who desire enterprise security and much more simplicity in setup. SMBs clearly stand to benefit from these new Gateway [access points].' IDC's Maximilian Flisi: managed switches priced competitively and may be a lead purchase driver.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 8 |
| observations.csv | 6 |
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

Kirk L. Kroeker, TechNewsWorld (2004). Gateway Goes Gigabit, Wireless.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

product-launch-analysis, analyst-commentary
