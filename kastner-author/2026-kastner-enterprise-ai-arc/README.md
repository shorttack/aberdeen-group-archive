# The Enterprise AI Arc: From XCON (1980) to Oracle 23ai (2024) — Forty-Four Years of AI-Adjacent Product Claims in the Kastner Archive

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (assembled with Perplexity Computer using archival-ingest v16) |
| Date | 2026-05-17 |
| Type | topic-analysis |
| Domain | computing-industry-history |
| License | CC-BY-4.0 |

## Abstract

A cross-entity longitudinal study tracing the continuous thread of AI-adjacent enterprise product claims documented in the Kastner IT Research Archive from 1980 through 2024. Synthesized from three completed longitudinal single-entity studies (IBM, Intel, Oracle) plus the broader 947-study master archive. The study decomposes the Enterprise AI Arc into eleven thematic threads: expert systems (1980–1995), early NLP and speech recognition (1986–2000), data mining and predictive analytics (1992–2005), document intelligence (1993–2005), agent architectures (1989–2010), computer vision and pattern recognition (1985–2005), IBM Deep Blue and competitive AI (1989–1997), IBM Watson and enterprise NLP (2006–2022), Oracle InterOffice to Oracle 23ai (1995–2024), Intel's AI hardware arc (2016–2024), and the LLM convergence (2017–2024). Each node is scored on specificity (1–5, mapping precision to modern LLM-era capability) and predictive distance (years to mainstream LLM-era delivery). Headline findings: Oracle InterOffice document summarization (1995) is the archive's highest-specificity contemporary forward-looking AI claim at 27-year predictive distance; XCON (1980) and MYCIN (1980) are the deepest historical AI anchors in the archive at 42-year distance; IBM ran the broadest pre-2000 commercial AI portfolio (speech, chess, data mining, NLP) of any company in the archive; the 1997 data mining cohort (IBM Intelligent Miner, Tandem ORDM, BusinessMiner) is the archive's densest AI cluster predating modern ML by 25 years. The enterprise AI arc is not a straight line — it is a series of capability surges followed by commercial failures, each advancing the underlying technology while the specific product vehicles collapsed. Every major LLM-era enterprise AI capability had a documented precursor in the Kastner archive at least fifteen years earlier.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 15 |
| technologies.csv | 30 |
| observations.csv | 78 |
| codes.csv | 33 |

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

Peter S. Kastner (assembled with Perplexity Computer using archival-ingest v16) (2026). The Enterprise AI Arc: From XCON (1980) to Oracle 23ai (2024) — Forty-Four Years of AI-Adjacent Product Claims in the Kastner Archive.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

archive-mining,longitudinal-cross-entity,prediction-vs-outcome-scorecard,thematic-thread-decomposition,wiki-driven-replication,specificity-scoring
