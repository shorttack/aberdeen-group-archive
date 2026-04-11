# Linuxcare, Inc. -- Enterprise Service and Support for All Things Linux

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 1999-11-01 |
| Type | white-paper |
| Domain | Linux-enterprise-services |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group profiles Linuxcare, Inc., a San Francisco-based specialist in enterprise Linux service and support founded in 1998. The report evaluates Linuxcare's four service pillars -- technical support, professional services, education/training, and benchmarking/certification -- and its partnerships with Dell, IBM, Sun, and TurboLinux. Aberdeen concludes Linuxcare has proven viability as a Linux expertise source but faces challenges scaling headcount and quality assurance.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 14 |
| technologies.csv | 6 |
| observations.csv | 20 |
| codes.csv | 28 |

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

Peter S. Kastner / Aberdeen Group (1999). Linuxcare, Inc. -- Enterprise Service and Support for All Things Linux.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

competitive-profiling, industry-analysis, customer-interviews
