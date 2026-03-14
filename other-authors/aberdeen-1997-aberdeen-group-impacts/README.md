# Aberdeen Group Impacts: Technology Briefings 1997

Aberdeen Group Archival Dataset — Frictionless Data Package v1.0.0

## Study Metadata

| Field | Value |
|-------|-------|
| study_id | `aberdeen-1997-aberdeen-group-impacts` |
| author | Aberdeen Group |
| date | 1997-01-01 |
| type | market-study |
| subject_domain | enterprise-networking, telecommunications, ERP, IT-infrastructure |
| methodology | industry-analysis, competitive-profiling, expert-opinion |
| license | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |

## Abstract

This document is an index and abstract listing of Aberdeen Group's 'Impacts' research briefings published across 1997, covering networking, telecommunications, ERP, and IT-infrastructure vendors. Each entry summarizes a one-to-two page rapid-analysis product assessing specific vendor announcements or technology developments. The listing spans approximately 35 individual impact reports from February through January 1998.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | As a catalogue index of Aberdeen's rapid-analysis products, this document provides a snapshot of the technology topics that enterprise IT buyers considered most significant during 1997; its value is contextual rather than analytical. |
| **Relevance** | low | Individual company-specific briefings from 1997 have limited applicability today; primarily of archival interest for historians of 1990s networking and ERP markets. |
| **Prescience** | not-applicable | This is an index document without forward-looking claims; no predictions to evaluate. |

## Data Tables

| File | Rows | Description |
|------|------|-------------|
| `data/studies.csv` | 1 | Study-level metadata (16-field v12 schema) |
| `data/entities.csv` | 14 | Organizations and institutions mentioned |
| `data/technologies.csv` | 5 | Technologies referenced |
| `data/observations.csv` | 15 | Extracted analytical observations |
| `data/codes.csv` | 24 | Controlled vocabulary |

**Observations by type:** market-data: 1, strategy-classification: 5, technology-assessment: 9

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
Aberdeen Group. (1997). Aberdeen Group Impacts: Technology Briefings 1997.
Aberdeen Group Research Archive. Archived from: https://web.archive.org/
Processed: 2026-03-14. License: CC-BY-4.0.
DOI: [PENDING]
```

## Source

Original document archived via Wayback Machine. Full original text preserved in `source/original_text.md`.
