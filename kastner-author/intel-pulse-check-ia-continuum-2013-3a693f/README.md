# Pulse Check: How Intel is Scaling to Meet the Decade's Opportunities

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2013-06-02 |
| Type | topic-analysis |
| Domain | semiconductors-intel |
| License | CC-BY-4.0 |

## Abstract

Kastner blog analysis of Intel's IA (Intel Architecture) scaling strategy — the 'silicon gene-splicing' approach of creating IA variants for every computing tier from embedded SoCs, Atom smartphones, Core desktops/notebooks, to Xeon datacenter and PHI HPC. Projects the 2010s TAM at nearly 1B processors per year, rising to 2B+ by decade end. Reviews Haswell/Baytrail SoCs, Avoton Atom for micro-servers, and challenges around software delivery, sub-10nm scaling, missed-iPhone, and mobile-vs-PC substitution dynamics. Includes a personal recollection of advising NCR and Sequent on 486-based servers in the 1990s.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 16 |
| observations.csv | 24 |
| codes.csv | 35 |

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

Peter S. Kastner (2013). Pulse Check: How Intel is Scaling to Meet the Decade's Opportunities.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, market-sizing, product-roadmap-analysis
