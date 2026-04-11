# DocuCorp Consulting Project Plan (Aberdeen Group, ~June 2000)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 2000-06-01 |
| Type | consulting-report |
| Domain | enterprise-document-management, consulting-methodology |
| License | CC-BY-4.0 |

## Abstract

This project plan details a multi-phase Aberdeen Group management consulting engagement for DocuCorp, a document management software vendor, beginning with a two-day on-site Discovery phase in Dallas to interview managers across sales, R&D, support, and professional services, followed by a presentation of preliminary findings to DocuCorp's executive team. Subsequent phases include competitive analysis, strategic positioning recommendations, and delivery of a final report, with the overall goal of helping DocuCorp optimize its market position, organizational structure, and go-to-market strategy.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 0 |
| observations.csv | 11 |
| codes.csv | 25 |

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

Peter S. Kastner / Aberdeen Group (2000). DocuCorp Consulting Project Plan (Aberdeen Group, ~June 2000).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

management-consulting, field-interviews, competitive-analysis, strategic-planning
