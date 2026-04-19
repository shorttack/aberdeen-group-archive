# AMD's Acquisition of ATI: Upsetting the Equilibrium

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2006-07-27 |
| Type | market-alert |
| Domain | enterprise-computing |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group Market Alert by Peter S. Kastner (VP Enterprise Integration Research) analyzing AMD's $5.4B acquisition of ATI Technologies. Argues the deal upsets the four-way competitive equilibrium among AMD, ATI, Intel, and nVidia, and predicts less innovation and higher prices in enterprise volume servers and workstations. Kastner specifies buyer guidance for 2007-2008 planning: no immediate changes to purchasing, plan to test Windows XP/Vista on dual-core in Q1 2007, monitor Intel integrated graphics under Vista workload, and expects HP to gain and Dell to lose most among top-tier OEMs given Dell's Intel-only heritage.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 7 |
| observations.csv | 16 |
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

Peter S. Kastner (2006). AMD's Acquisition of ATI: Upsetting the Equilibrium.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, competitive-profiling
