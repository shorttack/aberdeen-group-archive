# Stratus ET1 Functional Specification (May 1, 1986) and Stratus Transaction Processing Benchmarks (June 26, 1986) — Consolidated Stratus 1986 ET1 Corpus

| Field | Value |
|-------|-------|
| Author | Stratus Computer (engineering and benchmark documents) |
| Date | 1986 |
| Type | internal-engineering-corpus |
| Domain | transaction-processing/benchmark-methodology |
| License | CC-BY-4.0 |

## Abstract

Two-document Stratus 1986 ET1 corpus consolidating: (1) the Stratus ET1 Functional Specification (May 1, 1986) — Stratus's internal definition of the Anon-et-al ET1 'debit-credit' transaction (Read X.25, Read+Rewrite Account/Teller/Branch, Write History sequential, Write X.25 acknowledgement; 1,000 branches, 10K tellers, 10M accounts, 100 tps peak); explicitly clarifies that 'TP1 (Stratus internal) and ET1 are NOT the same benchmark or even a variation' — TP1 was Stratus's earlier internal benchmark, not based on ET1 or debit-credit, with different I/O profile and different database; vendor comparisons based on TP1-vs-ET1 results are 'invalid'. (2) Stratus Transaction Processing Benchmarks (June 26, 1986) — Stratus's official ET1 benchmark results, framed within a broader critique of MIPS and Whetstone benchmarks for OLTP, a quantitative TP1-vs-ET1 comparison (TP1 does ~4x as many physical I/Os as ET1; logical I/O ratio 7:8 but physical I/O ratio dominates due to small relative file caching), and detailed ET1 benchmark methodology (PL1 requester/server with Stratus TPF; 85%/15% local-vs-remote branch traffic model; multimodule dispatch). This corpus is Stratus's direct response to the 1985 Tandem TXP ET1 marketing barrage (Batch 25 study #6 / Serlin FTSN-33).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 5 |
| observations.csv | 7 |
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

Stratus Computer (engineering and benchmark documents) (1986). Stratus ET1 Functional Specification (May 1, 1986) and Stratus Transaction Processing Benchmarks (June 26, 1986) — Consolidated Stratus 1986 ET1 Corpus.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

vendor-engineering-spec-plus-benchmark-results
