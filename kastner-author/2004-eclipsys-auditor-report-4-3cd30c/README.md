# Eclipsys SunriseXA 3.3 Meets Subsecond Response Time Objective

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2004-04 |
| Type | benchmark |
| Domain | Healthcare information systems / clinical software performance benchmarking |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group audit report commissioned by Eclipsys Corp. to independently verify performance benchmarks for SunriseXA Release 3.3, a healthcare clinical information system. Benchmark simulated a 6,000-bed hospital at peak load (5,000 orders/hour, 2.27x the busiest known real hospital rate), executing 65,637 transactions in one steady-state hour via Mercury LoadRunner. Results confirmed subsecond response times for 4 of 5 transaction categories; only administrative log-on (multi-patient download) and batch group-order transactions exceeded 1 second. Database server CPU utilization was only 40% at peak. Aberdeen concludes Eclipsys successfully resolved response time issues identified in October 2003.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 11 |
| observations.csv | 21 |
| codes.csv | 29 |

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

Peter S. Kastner (2004). Eclipsys SunriseXA 3.3 Meets Subsecond Response Time Objective.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Independent audit of vendor-conducted benchmark; Mercury LoadRunner load simulation; 1-hour and 12-hour sustained load tests; isolation and slow-client tests
