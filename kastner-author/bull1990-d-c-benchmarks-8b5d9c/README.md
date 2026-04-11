# Bull DPS 9000/7000 Debit-Credit Benchmark and Cooperative Processing Proposal

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1989-05-04 |
| Type | consulting-report |
| Domain | OLTP-benchmarking, hardware-performance-analysis |
| License | CC-BY-4.0 |

## Abstract

This consolidated proposal letter revises and combines three Aberdeen Group engagements for Bull HN Information Systems covering Debit-Credit benchmark auditing for the DPS 9000 and DPS 7000 servers, and a cooperative processing benchmark study. Aberdeen proposes to audit Bull's internal benchmark results against industry disclosure guidelines and then publish findings to validate Bull's price-performance claims in the commercial OLTP market. The letter consolidates scope and reduces combined fees to $77,000 to capture efficiencies from running all three projects in parallel.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 6 |
| observations.csv | 15 |
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

Peter S. Kastner (1989). Bull DPS 9000/7000 Debit-Credit Benchmark and Cooperative Processing Proposal.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

benchmark-auditing, competitive-analysis, proposal-development
