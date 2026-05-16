# A Worked Example: Quantifying Analyst Prescience Using the Kastner IT Research Archive

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (subject/reviewer) and Perplexity Computer (methodology architect) |
| Date | 2026-05-16 |
| Type | topic-analysis |
| Domain | research-methodology |
| License | CC-BY-4.0 |

## Abstract

This 2026 methodology-demonstration study uses the 933-study Kastner IT Research Archive (19,175 structured observations, 466 high-prescience studies) as a primary-source research instrument to develop and apply a reproducible methodology for attributing economic value to analyst prescience. Across 15 inclusion-threshold themes, the study triangulates every market-size anchor against three or more independent sources with at least one primary source (IDC, Gartner, SEC 10-K, BLS), then applies a share-of-prescience discount based on lead time, contrarian position, and specificity. The worked example yields $10.9 trillion cumulative net-attributed value in 2026 USD (sensitivity band $8.8T-$13.4T), demonstrating that the archive supports rigorous third-party-replicable research. The result and the methodology are both intended for hostile peer review.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 15 |
| technologies.csv | 18 |
| observations.csv | 98 |
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

Peter S. Kastner (subject/reviewer) and Perplexity Computer (methodology architect) (2026). A Worked Example: Quantifying Analyst Prescience Using the Kastner IT Research Archive.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis,attribution-modeling,sensitivity-analysis,primary-source-triangulation,reproducibility-framework
