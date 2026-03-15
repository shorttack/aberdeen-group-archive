# Industri-Matematik International Corp.: Strategic Solution for Fast-Moving, High-Volume Goods Industries

**Study ID:** 1997-industry-matematik-international-co-c398bc
**Author:** Aberdeen Group
**Date:** 1997-01-01
**Type:** profile
**Subject Domain:** ERP / Supply Chain Management / Order Fulfillment Software
**License:** CC-BY-4.0

## Abstract

Aberdeen Group profiles Industri-Matematik International Corp. (IMI / NASDAQ: IMIC), a Swedish supply chain software vendor targeting fast-moving, high-volume consumer and industrial goods. The study evaluates IMI's System ESS — a UNIX/NT-based three-tier client-server order fulfillment platform using Oracle as RDBMS and Trifox TRIMtools/VORTEX for database abstraction. Aberdeen analyzes IMI's pull-driven demand-chain management model, promotion management capabilities, and Internet Commerce Workbench (ICW). The study covers IMI's FY96 revenue of $40M (with $18M from North America, a 9x increase in two years), its 1996 IPO raising $33M, and its phased OO/Internet migration roadmap. Aberdeen concludes IMI's System ESS is best-in-class for CPG and wholesale distribution demand-chain.

## Ratings

| Dimension | Score (1-5) | Rationale |
|-----------|-------------|-----------|
| Importance | 4 | Primary source documenting a niche but significant ERP/SCM vendor at the moment of its IPO and peak visibility. IMI's demand-chain pull model was prescient — it prefigures modern demand-driven supply chain management. The study documents the 1990s ERP landscape and best-of-breed vs suite competition at a pivotal moment. |
| Relevance | 4 | Directly relevant to the history of supply chain software, ERP/SCM market evolution, and the best-of-breed vs integrated suite debate. IMI's survival and recent resurgence as a niche SCM provider make this study valuable for understanding durable specialized vendors. |
| Prescience | 4 | Aberdeen correctly identified demand-chain pull management as the future direction of supply chain (accurate: S&OP, demand sensing are now standard); Internet enabling of order management (accurate: B2B e-commerce); and need for object-oriented migration (accurate though IMI's specific path evolved). Aberdeen's recommendation to expand to pharma/healthcare proved partially correct. IMI survived the ERP consolidation wave as a specialist — as Aberdeen predicted for best-of-breed vendors. |

## Dataset Contents

| File | Description | Rows |
|------|-------------|------|
| data/studies.csv | Study-level metadata | 1 |
| data/entities.csv | Organizations, products, people | 11 |
| data/technologies.csv | Technologies analyzed | 10 |
| data/observations.csv | Structured observations | 20 |
| data/codes.csv | Methodology codebook | 8 |

## Key Statistics

- **Entities:** 11
- **Technologies:** 10
- **Observations:** 20
- **Predictions:** 2
- **Actual Outcomes:** 8

## Source

Original text archived via Wayback Machine from aberdeen.com (1997).
Source document: `1997 Industry-Matematik International Corp pr..pdf`

## How to Use

```python
import pandas as pd
obs = pd.read_csv("data/observations.csv")
preds = obs[obs["observation_type"] == "viability-prediction"]
outcomes = obs[obs["observation_type"] == "actual-outcome"]
```

See `scripts/demo_analysis.py` for a complete example.
