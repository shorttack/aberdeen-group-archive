# EE Times: Stratus Challenges Tandem in Fault-Tolerant Computing — Pete Kastner on Self-Checking Hardware Strategy (May 1982)

| Field | Value |
|-------|-------|
| Author | EE Times (Electronic Engineering Times) staff |
| Date | 1982-05 |
| Type | trade-press-feature |
| Domain | fault-tolerant-computing/competitive-strategy |
| License | CC-BY-4.0 |

## Abstract

May 1982 Electronic Engineering Times feature on the maturing fault-tolerant computer market. Tandem Computers retains a roughly six-year lead but must expect upstart competition. Pete Kastner — quoted as 'manager of marketing development at Stratus' — argues that Stratus has 'taken a piece' out of Tandem's market with the Stratus/32 and that the Stratus self-checking-hardware-pair architecture is superior because: (a) all redundancy is in hardware (every component is self-checking each cycle), and (b) data paths remain in 16-bit mode unlike Tandem's NonStop II competing system. Kastner promises faster transaction throughput and the ability to support 'all the memory they need — up to a million kbytes'. The article also quotes investment banker Larry Roberts (whose firm backed both Stratus and Synapse Computer) and alludes to Synapse president Mark Leslie's perspective on 32-bit FT systems. This is the second-earliest Kastner Stratus quote in the archive (after the March 1982 Eagle-Tribune piece) and the first to use his 'manager of marketing development' title.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 5 |
| observations.csv | 6 |
| codes.csv | 27 |

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

EE Times (Electronic Engineering Times) staff (1982). EE Times: Stratus Challenges Tandem in Fault-Tolerant Computing — Pete Kastner on Self-Checking Hardware Strategy (May 1982).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-reporter-with-vendor-and-vc-quotes
