# Aberdeen Advisory Access Service (AAS) — Retainer Sales Kit

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 2000-01-01 |
| Type | employer-record |
| Domain | outbound-marketing |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group internal sales/marketing collateral for the Advisory Access Service (AAS) retainer offering. Documents client benefits, 3-tier deliverables (Core Access Deliverables for all clients, Six-Month Introductory AAS for new clients at $6K, Twelve-Month Multi-Day AAS), a full labor-rate pricing ladder from Associate ($10,200) through Executive ($21,000), sales scripts for cold-call prospecting, research-briefing close, and follow-up, plus a canonical objection-handling playbook distinguishing Aberdeen from Forrester/Gartner (subscription-style) by positioning Aberdeen as 'personal service that takes research and puts it into your company's exact context'.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 0 |
| observations.csv | 20 |
| codes.csv | 30 |

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

Aberdeen Group (2000). Aberdeen Advisory Access Service (AAS) — Retainer Sales Kit.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review, internal-sales-collateral
