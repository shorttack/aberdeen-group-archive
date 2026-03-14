# Aberdeen Picks The Right Tools for Year 2000

Aberdeen Group Archival Dataset — Frictionless Data Package v1.0.0

## Study Metadata

| Field | Value |
|-------|-------|
| study_id | `aberdeen-1997-picks-right-tools-year-2000` |
| author | Aberdeen Group |
| date | 1997-01-01 |
| type | white-paper |
| subject_domain | Year-2000-compliance, Y2K-tools, software-remediation |
| methodology | industry-analysis, expert-opinion |
| license | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |

## Abstract

This Technology Viewpoint (Vol. 10/No. 14) provides a brief but pointed overview of the Y2K problem's scale and complexity — 100 billion lines of code to check, 1,000+ person-years to manually inspect a large enterprise — and establishes Aberdeen's criteria for evaluating Y2K remediation tool vendors. Aberdeen emphasizes buyer skepticism toward Y2K solution hype while identifying the core technical and commercial attributes that distinguish credible Y2K tool suppliers.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | As a Technology Viewpoint briefing, this short piece was widely distributed to Aberdeen's subscriber base of IT buyers in early 1997 and served as a quick-reference guide for evaluating the flood of Y2K tool vendors entering the market at that time. |
| **Relevance** | low | Entirely historical; Y2K remediation tools and the problem they addressed are obsolete; retains minor archival value for historians of late-1990s enterprise software markets. |
| **Prescience** | medium | Aberdeen's scale estimates (100 billion lines of code, 1,000+ person-years) proved approximately correct — industry estimates converged around $100B in total spending; the prediction that buyer skepticism was warranted proved accurate as many Y2K tool vendors were indeed overstating effectiveness. |

## Data Tables

| File | Rows | Description |
|------|------|-------------|
| `data/studies.csv` | 1 | Study-level metadata (16-field v12 schema) |
| `data/entities.csv` | 1 | Organizations and institutions mentioned |
| `data/technologies.csv` | 3 | Technologies referenced |
| `data/observations.csv` | 10 | Extracted analytical observations |
| `data/codes.csv` | 24 | Controlled vocabulary |

**Observations by type:** actual-outcome: 2, expert-opinion: 2, market-data: 2, strategy-classification: 1, technology-assessment: 2, viability-prediction: 1

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
Aberdeen Group. (1997). Aberdeen Picks The Right Tools for Year 2000.
Aberdeen Group Research Archive. Archived from: https://web.archive.org/
Processed: 2026-03-14. License: CC-BY-4.0.
DOI: [PENDING]
```

## Source

Original document archived via Wayback Machine. Full original text preserved in `source/original_text.md`.
