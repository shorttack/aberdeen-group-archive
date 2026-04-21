# Systems Management: Delayed Promise

| Field | Value |
|-------|-------|
| Author | Stuart J. Johnston with Monua Janah, InformationWeek #694 |
| Date | 1998-08-03 |
| Type | feature-article |
| Domain | systems-management-zero-admin |
| License | CC-BY-4.0 |

## Abstract

InformationWeek issue #694 feature (Aug 3 1998) by Stuart J. Johnston with Monua Janah analyzing the state of Microsoft's Zero Administration Windows (ZAW) initiative nearly two years after its announcement. Core thesis: the pieces are falling into place — Windows-based terminals (HP), Terminal Server edition of Windows NT 4.0, Systems Management Server 2.0 in final testing — but the plan still hinges on the delayed Windows NT 5.0 (later Windows 2000). Peter Kastner, Aberdeen Group analyst, provides the key skeptical quote: full benefits of Zero Administration accrue only to companies with homogeneous NT 5.0 environments, so cost savings 'will happen very slowly, in an evolutionary fashion' as companies upgrade. Additional reporting by Mary Hayes and Caryn Gillooly. Article captures the 1998 moment when NT 5.0's delays and the thin-client/terminal strategy dominated the IT systems-management conversation.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 5 |
| observations.csv | 6 |
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

Stuart J. Johnston with Monua Janah, InformationWeek #694 (1998). Systems Management: Delayed Promise.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, vendor-commentary, analyst-commentary
