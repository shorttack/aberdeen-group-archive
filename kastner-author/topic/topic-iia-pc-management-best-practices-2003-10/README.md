# PC Management Best Practices: A Study of the Total Cost of Operation, Risk, Security, and Audit

| Field | Value |
|-------|-------|
| Author | Mark Salamasick, Charles Le Grand |
| Date | 2003-10-07 |
| Type | topic-analysis |
| Domain | enterprise-pcs |
| License | CC-BY-4.0 |

## Abstract

IIA Research Foundation rough-draft report (Oct 7, 2003) authored by Mark Salamasick (University of Texas at Dallas) and Charles Le Grand (IIA AVP Technology Practices). Based on 221 GAIN flash-survey responses plus the July 2003 IIA Technology Audit Forum where Peter Kastner of Aberdeen Group was keynote speaker. Organized around the COSO Internal Control Integrated Framework and SAC model; covers business risk and insurance, Sarbanes-Oxley/HIPAA/GLBA compliance, information security and appropriate use, business continuity, software management, and PC TCO. Cites Kastner's research extensively on PC fleet TCO ($8k-$9k per seat), 20-25% cost reduction through best practices, 70-80% of TCO in operations, 40 million desktops running outdated OSes, and standardized images.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 30 |
| technologies.csv | 24 |
| observations.csv | 40 |
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

Mark Salamasick, Charles Le Grand (2003). PC Management Best Practices: A Study of the Total Cost of Operation, Risk, Security, and Audit.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, survey-research, forum-research
