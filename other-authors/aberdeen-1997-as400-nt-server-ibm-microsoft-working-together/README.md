# AS/400 And NT Server — IBM and Microsoft Working Together To Comprehensively Meet Real User Requirements

Aberdeen Group Archival Dataset — Frictionless Data Package v1.0.0

## Study Metadata

| Field | Value |
|-------|-------|
| study_id | `aberdeen-1997-as400-nt-server-ibm-microsoft-working-together` |
| author | Aberdeen Group |
| date | 1997-02-01 |
| type | white-paper |
| subject_domain | AS400, NT-Server, IBM, Microsoft, enterprise-computing |
| methodology | industry-analysis, competitive-profiling, expert-opinion |
| license | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |

## Abstract

Aberdeen Group documents the IBM-Microsoft agreement of late 1996 to integrate NT Server 4.0 into the IBM AS/400 Integrated PC Server, scheduled for general availability in Q1 1998. The study explains the technical architecture (Intel Pentium Pro 200MHz board in AS/400 slot, sharing disk/tape with OS/400), identifies the integration points (ODBC, common user profiles, file system integration), and concludes that both IBM and its AS/400 customers benefit substantially from the arrangement, enabling enterprise users to run AS/400 production applications alongside NT-based desktop applications in a unified, cost-efficient infrastructure.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | This Aberdeen Profile documented a landmark IBM-Microsoft agreement that settled a major mid-1990s platform war and directly shaped enterprise computing for thousands of AS/400 installations; published as the NT vs. AS/400 debate was at its peak, it provided the first independent analysis of the coexistence architecture. |
| **Relevance** | medium | The AS/400 platform survived and evolved into IBM i / IBM Power Systems — still active in 2025 — making this study's core prediction historically significant; the integration philosophy (coexistence over replacement) remains instructive for modern hybrid-cloud architects. |
| **Prescience** | high | Aberdeen's prediction that NT on AS/400 would benefit satellite offices and that AS/400 would retain production-application dominance proved correct; the platform survived multiple technology shifts and is still operational 28 years later as IBM i. |

## Data Tables

| File | Rows | Description |
|------|------|-------------|
| `data/studies.csv` | 1 | Study-level metadata (16-field v12 schema) |
| `data/entities.csv` | 5 | Organizations and institutions mentioned |
| `data/technologies.csv` | 11 | Technologies referenced |
| `data/observations.csv` | 20 | Extracted analytical observations |
| `data/codes.csv` | 24 | Controlled vocabulary |

**Observations by type:** actual-outcome: 3, benchmark-result: 2, expert-opinion: 3, market-data: 1, strategy-classification: 2, technology-assessment: 5, viability-prediction: 4

## Quick Load (Python)

```python
import pandas as pd

studies = pd.read_csv('data/studies.csv')
entities = pd.read_csv('data/entities.csv')
technologies = pd.read_csv('data/technologies.csv')
observations = pd.read_csv('data/observations.csv')
codes = pd.read_csv('data/codes.csv')

# Filter viability predictions
predictions = observations[observations['observation_type'] == 'viability-prediction']
outcomes = observations[observations['observation_type'] == 'actual-outcome']
print(f"Predictions: {len(predictions)}, Verified outcomes: {len(outcomes)}")
```

## Frictionless Validation

```bash
frictionless validate datapackage.json
```

## Run Demo Analysis

```bash
python scripts/demo_analysis.py
```

## Citation

```
Aberdeen Group. (1997). AS/400 And NT Server — IBM and Microsoft Working Together To Comprehensively Meet Real User Requirements.
Aberdeen Group Research Archive. Archived from: https://web.archive.org/
Processed: 2026-03-14. License: CC-BY-4.0.
DOI: [PENDING]
```

## Source

Original document archived via Wayback Machine. Full original text preserved in `source/original_text.md`.
