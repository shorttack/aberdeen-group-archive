# AMD's Opteron at the One-Year Mark

| Field | Value |
|-------|-------|
| Author | Jay Lyman, TechNewsWorld |
| Date | 2004-04-22 |
| Type | news-article |
| Domain | 64-bit-server-processors |
| License | CC-BY-4.0 |

## Abstract

TechNewsWorld article (Apr 22 2004, Jay Lyman) marking the first anniversary of AMD's Opteron server processor and its 64-bit/32-bit x86 capability. HP, IBM, Sun, and Fujitsu Siemens all shipped Opteron-based servers in the first year. AMD VP Dirk Meyer claims Opteron transformed 64-bit from elite to pervasive; IDC's Vernon Turner credits OEMs with expanded x86 addressable market; AMD's Marty Seyer declares 32-bit-only servers 'obsolete.' Aberdeen chief research officer Peter Kastner offers the decisive Main Street take: 'Customers are saying that Opteron is a damn good chip at a great price, which has allowed HP and IBM to deliver value servers. Coming out of a recession, IT organizations are more value-conscious, and AMD has hit a sweet spot.' Kastner downplays 64-bit as the real driver — high-end 64-bit workloads have more processors than Opteron covers — and predicts Intel will match with its own 64-bit later this year.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 18 |
| technologies.csv | 4 |
| observations.csv | 8 |
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

Jay Lyman, TechNewsWorld (2004). AMD's Opteron at the One-Year Mark.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

anniversary-retrospective, analyst-commentary
