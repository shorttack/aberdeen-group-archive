# IBM Corporation Across Six Decades of the Kastner Archive: Mainframe Survival, Platform Pivots, and the Services Transformation

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (assembled with Perplexity Computer using archival-ingest v16) |
| Date | 2026-05-17 |
| Type | topic-analysis |
| Domain | computing-industry-history |
| License | CC-BY-4.0 |

## Abstract

A longitudinal archive study of IBM Corporation across six decades of the Kastner IT Research Archive. IBM is the single most-referenced company in the archive — 1,054 observations across 174 distinct studies spanning 1967 to 2026, with 724 IBM-vendor technology rows. The study decomposes IBM coverage into eleven thematic threads (mainframe survival, AS/400 & midrange, OS/2 & PC exit, DB2 & software pivot, services transformation, Linux & open source bet, Watson & AI, hybrid cloud & Red Hat, quantum computing, TPC benchmarks, and Kastner direct engagements), computes per-thread confidence histograms with named exemplars and refutations, and audits how IBM's actual transformation mapped to Kastner's documented predictions. Headline finding: IBM's mainframe was documented as 'doomed' in 1987 yet remains the archive's most durable technology-survival story through 2026; the services pivot from 'Big Blue hardware' to the world's largest IT services firm was predicted correctly; Watson AI significantly underdelivered its 2013-era promises. The archive contains zero formally-tagged IBM refutations in the viability-prediction rows — a contrast with Intel's 9.7% refutation rate that reflects IBM's unique institutional durability as an analyst subject. This is the second longitudinal single-entity study in the archive, following the Intel builder template.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 16 |
| technologies.csv | 44 |
| observations.csv | 117 |
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

Peter S. Kastner (assembled with Perplexity Computer using archival-ingest v16) (2026). IBM Corporation Across Six Decades of the Kastner Archive: Mainframe Survival, Platform Pivots, and the Services Transformation.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

archive-mining,longitudinal-single-entity,prediction-vs-outcome-scorecard,thematic-thread-decomposition,wiki-driven-replication
