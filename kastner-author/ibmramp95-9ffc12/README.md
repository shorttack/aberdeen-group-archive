# IBM RS/6000 SP RAMP: Market Research Proposal

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1995-10-17 |
| Type | consulting-report |
| Domain | parallel-computing, commercial-HPC, market-research |
| License | CC-BY-4.0 |

## Abstract

This proposal outlines a dual-objective Aberdeen Group market research engagement for IBM's RS/6000 SP parallel system: producing a commercial customer case-study white paper for the IBM sales force, while simultaneously investigating evidence that the SP has been mis-sold at some accounts with unrealistically high customer expectations. Aberdeen proposes structured telephone and face-to-face interviews with SP commercial customers to surface best-practice application profiles and, where present, diagnose the extent of any customer dissatisfaction problem before it becomes a broader issue for IBM.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 6 |
| observations.csv | 12 |
| codes.csv | 23 |

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

Peter S. Kastner (1995). IBM RS/6000 SP RAMP: Market Research Proposal.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

field-interviews, customer-satisfaction-research, white-paper-development, proposal
