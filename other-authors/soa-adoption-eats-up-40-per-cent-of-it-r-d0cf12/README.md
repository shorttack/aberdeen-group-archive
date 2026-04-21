# SOA adoption eats up 40 per cent of IT resources

| Field | Value |
|-------|-------|
| Author | Andy McCue, silicon.com (CNET Networks UK) |
| Date | 2006-07-14 |
| Type | news-article |
| Domain | SOA-enterprise-integration |
| License | CC-BY-4.0 |

## Abstract

silicon.com news article (Fri Jul 14 2006) by Andy McCue reporting on the Aberdeen Group benchmark report 'Enterprise Service Bus and SOA Middleware.' The article opens: 'The high costs of migrating to a service-oriented architecture (SOA) can eat up 40 per cent of an organisation's IT budget.' Aberdeen surveyed 120+ IT and business professionals; 90% are adopting or have adopted SOA technologies, especially in large enterprises with more than $1bn in annual revenues. Peter S. Kastner, VP and research director for enterprise integration at Aberdeen Group, is cited with the same two quotes syndicated worldwide: 'SOA is broadly seen as a real technology step forward, with the largest companies — who have the biggest integration problems — leading the way' and 'Redesigning business processes, high IT integration costs, and customisation challenges are eating up 40 per cent of the IT budget in integration expenditures.' The article closes with Aberdeen's three SOA adoption approaches: SOA 'light' (open source + standards, small cos), Enterprise SOA (suite middleware, mid-large), SOA ERP (ERP-extension entry point). silicon.com was a CNET Networks UK property; the identical article was re-syndicated to ZDNet Asia on Jul 17 2006 — that version is skipped as syndication per skill §9 (see Batch 34 skip log).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 6 |
| observations.csv | 9 |
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

Andy McCue, silicon.com (CNET Networks UK) (2006). SOA adoption eats up 40 per cent of IT resources.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, analyst-report-summary
