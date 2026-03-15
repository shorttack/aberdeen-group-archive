# IBM's NT Strategy: Moving NT Upscale with Enterprise-grade Solutions, Middleware, and Services

**Study ID:** 1997-ibm’s-nt-strategy-strat-pr-b93817
**Author:** Aberdeen Group
**Date:** 1997-06-01
**Type:** profile
**Subject Domain:** Operating Systems / Enterprise Computing Strategy
**License:** CC-BY-4.0

## Abstract

Aberdeen Group profiles IBM Software Solutions Division's Windows NT strategy, analyzing IBM's major strategic pivot from OS/2 competition to NT enablement. The study covers IBM's stated goal of NT market leadership by year-end 1998, its competitive positioning versus Compaq (~35% share) and HP (~16% share), and its portfolio of NT-optimized products: Lotus Notes/Domino, DB2 Universal Database, Tivoli TME, ADSM storage management, Communications Server, Transaction Server (CICS for NT + Transarc Encina), VisualAge tools, and MQSeries middleware. Aberdeen concludes IBM is well-positioned for enterprise NT due to its service infrastructure and mature application portfolio.

## Ratings

| Dimension | Score (1-5) | Rationale |
|-----------|-------------|-----------|
| Importance | 4 | Documents a historically significant strategic reversal: IBM formally abandoning its OS/2 vs NT ideological battle and embracing NT. This is a primary source for understanding how Microsoft NT achieved enterprise dominance and IBM's subsequent enterprise middleware strategy. The study also documents 1997 NT license volume, competitive market shares, and IBM's services positioning that prefigures Global Services growth. |
| Relevance | 4 | Directly relevant to the OS wars history of the 1990s, IBM's strategic transformation, and the competitive dynamics between IBM, Compaq, HP, and Microsoft. Documents the precise moment IBM shifted from adversary to NT enabler — a pivotal inflection point. |
| Prescience | 4 | Aberdeen correctly predicted: IBM would not become NT market leader (Compaq retained dominance through 1999, then Dell surpassed); Compaq would struggle with enterprise services (Compaq acquired DEC 1998, then HP acquired Compaq 2002); Java would become popular development environment; MQSeries would become enterprise standard (IBM MQ active today). Less accurate: predicting IBM would be NT leader by 1998 — IBM remained 3rd behind Compaq and Dell. |

## Dataset Contents

| File | Description | Rows |
|------|-------------|------|
| data/studies.csv | Study-level metadata | 1 |
| data/entities.csv | Organizations, products, people | 9 |
| data/technologies.csv | Technologies analyzed | 12 |
| data/observations.csv | Structured observations | 21 |
| data/codes.csv | Methodology codebook | 8 |

## Key Statistics

- **Entities:** 9
- **Technologies:** 12
- **Observations:** 21
- **Predictions:** 6
- **Actual Outcomes:** 6

## Source

Original text archived via Wayback Machine from aberdeen.com (1997).
Source document: `1997 IBM's NT Strategy strat pr.pdf`

## How to Use

```python
import pandas as pd
obs = pd.read_csv("data/observations.csv")
preds = obs[obs["observation_type"] == "viability-prediction"]
outcomes = obs[obs["observation_type"] == "actual-outcome"]
```

See `scripts/demo_analysis.py` for a complete example.
