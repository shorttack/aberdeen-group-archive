# The ESB in the Land of SOA

| Field | Value |
|-------|-------|
| Author | William Mougayar |
| Date | 2005-12-07 |
| Type | employer-record |
| Domain | ESB; SOA integration; enterprise middleware; vendor landscape |
| License | CC-BY-4.0 |

## Abstract

Aberdeen research note (5 pages) on the emergence of ESB as de-facto technology standard for integrating SOA infrastructure. Based on survey of 286 companies ('How SOA is Changing IT'): 60% of large company respondents are using or planning shared messaging services within 12 months; 76% implementing Web Services calls to existing applications; 73% implementing applications-related services. Kastner's three-phase ESB evolution framework: Message Bus (messaging) → Service Bus (orchestration) → Process Bus (mediation). Four-segment vendor landscape: ESB pioneers/SOA-specific, traditional EAI/EII players, platform vendors, process-centric integrators. Aberdeen conclusions: evaluate ESB extensibility; existing ESBs need to go beyond messaging to orchestration and mediation; don't neglect services registry and governance.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 29 |
| technologies.csv | 17 |
| observations.csv | 16 |
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

William Mougayar (2005). The ESB in the Land of SOA.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Aberdeen survey-based research note; survey of 286 companies 'How SOA is Changing IT'; vendor landscape analysis
