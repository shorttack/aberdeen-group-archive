# Tandem TopGun ET1 Benchmark Analysis — Kastner-authored Stratus + DEC memos

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (with Raphael Frommer, Clark Hodder, Stratus, Aug 1987); Peter S. Kastner (DEC Corporate Systems Group, 13 January 1988) |
| Date | 1987-08-11/1988-01-13 |
| Type | internal-engineering-memo |
| Domain | fault-tolerant-OLTP-benchmarks |
| License | CC-BY-4.0 |

## Abstract

Two PSK-authored memos covering the same Tandem TopGun ET1 benchmark across employer transitions: the August 1987 Stratus 'Working Document on the NonStop SQL Benchmark' (co-authored with Raphael Frommer and Clark Hodder, addressed to Bill Foster, Bob Freiburghouse and the Stratus engineering leadership) dissecting Tandem's 32-VLX 208-tps TopGun result; and the January 1988 DEC Corporate Systems Group memo applying the same analysis to plot Digital's response. PSK enumerates Tandem's 'go-fast tricks' (Pathway hacks, TMF buffering, file partitioning so all branch records sit on one ATB disk, mirrored disks worth ~5%, intelligent X.25 cluster controllers, relaxed 90%/2-sec response criterion vs the original 95%/1-sec, randomized arrival times) and concludes Tandem's 8-VLX baseline would deliver ~10-15 tps under conservative ET1 conditions — meaning Stratus and Digital are 'not nearly as bad as corporate mythology would have us believe.' The memo is a rare document of PSK actively analyzing competitive benchmarks across two employers in five months.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 10 |
| observations.csv | 10 |
| codes.csv | 34 |

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

Peter S. Kastner (with Raphael Frommer, Clark Hodder, Stratus, Aug 1987); Peter S. Kastner (DEC Corporate Systems Group, 13 January 1988) (1987). Tandem TopGun ET1 Benchmark Analysis — Kastner-authored Stratus + DEC memos.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Primary-source PSK-authored technical memos analyzing Tandem 32-VLX TopGun benchmark (208 tps) — first as Stratus marketing-support manager (Aug 1987 working document), then as DEC Corporate Systems Group (Jan 1988) re-applying the analysis to a Digital response.
