# Tiger Responds to Security Warnings

| Field | Value |
|-------|-------|
| Author | Ian Betteridge |
| Date | 2005-04-29 |
| Type | news-article |
| Domain | Mac-OS-X-Tiger-security-posture-2005 |
| License | CC-BY-4.0 |

## Abstract

eWEEK article reporting Mac OS X 10.4 'Tiger' launch features (Kerberos VPN, stealth-mode firewall, Safe Downloads, secure virtual memory) in the context of analyst warnings that Apple's rising market share will attract more attackers. Kastner (Vericours Inc. director) cites the Symantec Internet Security Threat Report figure of 37/1,403 new vulnerabilities involving Apple in H2 2004 and argues severity and organizational impact remain much lower than Microsoft's.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 7 |
| observations.csv | 8 |
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

Ian Betteridge (2005). Tiger Responds to Security Warnings.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, analyst-quote-aggregation
