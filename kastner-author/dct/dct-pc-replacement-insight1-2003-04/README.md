# PC Replacements: Lawyers, Auditors, and Common Sense Rules

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-04-24 |
| Type | dct |
| Domain | enterprise-pc/lifecycle-management |
| License | CC-BY-4.0 |

## Abstract

Aberdeen InSight arguing that the roughly 50 million Windows 98 / NT 4 corporate PCs still in service by mid-2003 should be accelerated off the desktop. Windows NT 4.x end-of-support (June 30, 2003) and Windows 98/SE (January 16, 2004) expose enterprises to unpatched security risk, auditor scrutiny, and potential negligence claims. Mid-2003 is framed as an auspicious PC replacement window anchored by Windows XP Pro SP1, Server 2003, Office 2003, Intel Springdale, Pentium 4 Hyper-Threading, and Centrino notebooks.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 11 |
| observations.csv | 21 |
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

Peter S. Kastner (2003). PC Replacements: Lawyers, Auditors, and Common Sense Rules.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, document-review
