# Intel Corporation Across Five Decades of the Kastner Archive: Technology Emergence, Decline, and the x86 Market Calls

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (assembled with Perplexity Computer using archival-ingest v18) |
| Date | 2026-05-17 |
| Type | topic-analysis |
| Domain | computing-industry-history |
| License | CC-BY-4.0 |

## Abstract

A longitudinal archive study of Intel Corporation across five decades of the Kastner IT Research Archive. Intel is the most-observed single company in the archive — 562 observations across 102 distinct studies spanning 1990 to 2026, with 472 Intel-vendor technology rows. The study decomposes Intel coverage into eleven thematic threads (x86 ascension, Itanium, P4 GHz race, Centrino, tick-tock cadence, smartphone failure, manycore/Xeon Phi, vPro security, Atom/embedded, AI compute, foundry pivot), computes per-thread confidence histograms with named exemplars and refutations, and audits how Intel's actual growth mapped to Kastner's documented x86 market projections. Headline finding: every dated numeric named-winner Kastner projection about Intel x86 markets (1981, 1988, 1993) was verified or remains in-flight; the seven refuted outcomes in the Intel observation set are predominantly Intel-issued promises (Itanium 7x performance, consumer LaGrande, Atom smartphone success, tick-tock cadence post-2016) that the archive tracked and adjudicated. This is the third archive-as-protagonist study, the first longitudinal single-entity study, and it validates ARG-1 / ARG-2 / ARG-10 from the core arguments framework against the strongest possible test subject — a single firm operating in maximally competitive markets across half a century. Refutation rate within the Intel set (9.7%) is 26x the archive baseline (0.37%); reading honestly, Intel's predictive surface is harder because the firm itself is the protagonist of computing-industry competition. Refutations are preserved, not suppressed.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 18 |
| technologies.csv | 26 |
| observations.csv | 98 |
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

Peter S. Kastner (assembled with Perplexity Computer using archival-ingest v18) (2026). Intel Corporation Across Five Decades of the Kastner Archive: Technology Emergence, Decline, and the x86 Market Calls.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

archive-mining,longitudinal-single-entity,prediction-vs-outcome-scorecard,thematic-thread-decomposition,wiki-driven-replication
