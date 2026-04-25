# Stratus Internal Benchmark Tuning Guide: TP-1 Results on XA600/XA400/FT200 (Stratus Internal Use Only, 1985)

| Field | Value |
|-------|-------|
| Author | Stratus Computer (internal engineering documentation) |
| Date | 1985 |
| Type | internal-engineering-document |
| Domain | transaction-processing/benchmark-tuning |
| License | CC-BY-4.0 |

## Abstract

Stratus Computer 1985 internal-use-only benchmark tuning guide documenting Stratus's internal TP-1 (transaction-processing) benchmark and the tuned performance results for three Stratus production systems: XA600 (5.0 tps with 2.1s avg / 3.3s 90th-percentile response, 80% CPU + 40% disk utilization, 3 duplexed D108 disks + 8 MB + 6 servers + 2 requesters with 80 tasks each); XA400 (3.4 tps, 1.8s avg / 2.7s 90th-percentile, 80% CPU + 25% disk, 8 MB + 3 Fuji disks + 4 servers + 2 requesters with 55 tasks); FT200 (1.7 tps, 2.1s avg / 3.5s 90th-percentile, 85% CPU + 18% disk, 8 MB + 2 Fuji disks + 1 requester with 55 tasks, server priority above requester). The guide describes TP1 as a PL/1 + COBOL requester/server simulation with parameterized indexed reads (5/tx), indexed rewrites (2/tx), sequential log writes (1/tx), 5,000-cycle requester CPU loop and 200-cycle server loop, 30-second sleep with +/-5s deviation, no screen I/O, no comms. Observations note task metering had no measurable effect, cache utilization significantly impacts performance, and multiple server copies improve performance. This document is the technical complement to the 1986 Stratus ET1 corpus (Batch 25 study #6+#7) — TP1 was the Stratus internal benchmark before ET1 became the industry standard.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 1 |
| technologies.csv | 6 |
| observations.csv | 5 |
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

Stratus Computer (internal engineering documentation) (1985). Stratus Internal Benchmark Tuning Guide: TP-1 Results on XA600/XA400/FT200 (Stratus Internal Use Only, 1985).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

internal-engineering-tuning-guide
