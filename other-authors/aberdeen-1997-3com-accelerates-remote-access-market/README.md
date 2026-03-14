# 3Com Accelerates into Remote Access Market

Aberdeen Group Archival Dataset — Frictionless Data Package v1.0.0

## Study Metadata

| Field | Value |
|-------|-------|
| study_id | `aberdeen-1997-3com-accelerates-remote-access-market` |
| author | Aberdeen Group |
| date | 1997-02-01 |
| type | white-paper |
| subject_domain | remote-access, enterprise-networking, ISDN, SOHO |
| methodology | industry-analysis, competitive-profiling, expert-opinion |
| license | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |

## Abstract

Aberdeen Group assesses 3Com Corporation's strategic expansion into the remote access market as of early 1997, following a year of acquisitions (Centrum, AccessWorks, Primary Access, Sonix) and product launches. The study describes the four market segments of remote access (enterprise, SOHO, individual user, ISP/carrier), evaluates 3Com's three solution families (AccessBuilder, NetBuilder, Impact), and concludes that while 3Com is not yet the market leader it has a logical and executable strategy, with its greatest strength in the SOHO segment and its channels as its most valuable competitive asset.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Published as 3Com was completing its transformative merger with USRobotics ($6.6B) in February 1997, this Profile provides a contemporaneous independent assessment of 3Com's remote access positioning at a pivotal moment in networking history. |
| **Relevance** | low | The specific remote access product lines and market dynamics are fully superseded; however the competitive-profiling methodology and four-segment market framework retain pedagogical value for market analysis courses. |
| **Prescience** | medium | Aberdeen correctly identified 3Com's channels as its greatest asset and the enterprise/ISP segment as the key challenge; however the prediction of 'increasing success' proved only partially correct — 3Com gained SOHO dominance via USRobotics modems but permanently struggled to win enterprise and carrier market share, and was ultimately acquired by HP in 2010. |

## Data Tables

| File | Rows | Description |
|------|------|-------------|
| `data/studies.csv` | 1 | Study-level metadata (16-field v12 schema) |
| `data/entities.csv` | 9 | Organizations and institutions mentioned |
| `data/technologies.csv` | 7 | Technologies referenced |
| `data/observations.csv` | 20 | Extracted analytical observations |
| `data/codes.csv` | 24 | Controlled vocabulary |

**Observations by type:** actual-outcome: 2, benchmark-result: 1, framework-factor: 4, market-data: 6, strategy-classification: 2, technology-assessment: 3, viability-prediction: 2

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
Aberdeen Group. (1997). 3Com Accelerates into Remote Access Market.
Aberdeen Group Research Archive. Archived from: https://web.archive.org/
Processed: 2026-03-14. License: CC-BY-4.0.
DOI: [PENDING]
```

## Source

Original document archived via Wayback Machine. Full original text preserved in `source/original_text.md`.
