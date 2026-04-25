# Competitors Find Fault With Tolerant's Performance Claim — Tandem, Stratus argue Eternity performance figures

| Field | Value |
|-------|-------|
| Author | Paul E. Schindler Jr. (InformationWEEK staff) |
| Date | 1986-01-20 |
| Type | trade-press-article |
| Domain | transaction-processing-benchmarks |
| License | CC-BY-4.0 |

## Abstract

InformationWEEK page 22 (January 20, 1986) reports on a controversy over Tolerant Systems' Eternity transaction-processing performance claims. Tolerant claims its Eternity system at $23,800 per TPS beats Tandem ($42,200) and Stratus ($68,700) using TP1/ET1 (debit-credit) benchmark figures from Datapro and Omri Serlin's ITOM International newsletter. Tandem responds with internal numbers showing $20,800/TPS using configurations more comparable to Tolerant's. Serlin himself published Stratus internal figures showing $23,100/TPS. Serlin says 'these measurements are at best ambiguous and always the subject of intense controversy' and recommends users run their own benchmarks. Background: Tolerant Transaction Systems Inc. founder Eli Alon promised Unix-based fault-tolerant processing in 1985; firm dropped Alon and the word 'transaction' from its name. With release 5.0 of its Unix-like OS, Tolerant introduced multi-System-Building-Block (SBB) fault tolerance using National Semiconductor 32016 chips. Marketing director Shirley Henry says major vendors will resell Eternity. Confirms Tandem as market leader and Stratus as 'distant second-place competitor' in OLTP fault-tolerant computing.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 8 |
| observations.csv | 11 |
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

Paul E. Schindler Jr. (InformationWEEK staff) (1986). Competitors Find Fault With Tolerant's Performance Claim — Tandem, Stratus argue Eternity performance figures.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, expert-interview, vendor-data-analysis
