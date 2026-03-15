# IBM Network Computing: Enterprise Communications Family

**Study ID:** 1997-ibm-s-enterprise-communications-fam-14559a
**Author:** Aberdeen Group
**Date:** 1997-06-01
**Type:** profile
**Subject Domain:** Enterprise Networking / Communications Software
**License:** CC-BY-4.0

## Abstract

Aberdeen Group evaluates IBM's Enterprise Communications Family, a suite of communications software for enterprise network computing. The study assesses IBM's advanced multiprotocol support (AnyNet/MPTN) and High Performance Routing (HPR) technologies, covering products including Communications Server (CS/2, CS/NT, CS/AIX, OS/400, CS/MVS) and Personal Communications. Aberdeen concludes that IBM's approach delivers scalability, flexibility, and ease of SNA-to-TCP/IP migration for enterprises transitioning to network computing architectures.

## Ratings

| Dimension | Score (1-5) | Rationale |
|-----------|-------------|-----------|
| Importance | 3 | Represents a transitional moment in IBM's networking stack — the strategic pivot from SNA-centric to TCP/IP-aware multiprotocol architectures. Important as a primary source on the SNA deprecation trajectory and AnyNet/MPTN technology decisions. |
| Relevance | 3 | Directly relevant to the history of enterprise networking transitions from SNA to TCP/IP. Documents IBM's technical strategy at a critical juncture and provides benchmark context for evaluating communications middleware choices of the era. |
| Prescience | 4 | Aberdeen accurately predicted that TCP/IP would displace SNA; that multiprotocol bridging would be a transitional strategy; that HPR dynamic routing features anticipate modern SDN concepts; and that ATM would not displace TCP/IP long-term. The call to place ECF 'high on lists to buy' was overstated — SNA was sunset by IBM within a decade. |

## Dataset Contents

| File | Description | Rows |
|------|-------------|------|
| data/studies.csv | Study-level metadata | 1 |
| data/entities.csv | Organizations, products, people | 5 |
| data/technologies.csv | Technologies analyzed | 8 |
| data/observations.csv | Structured observations | 18 |
| data/codes.csv | Methodology codebook | 8 |

## Key Statistics

- **Entities:** 5
- **Technologies:** 8
- **Observations:** 18
- **Predictions:** 4
- **Actual Outcomes:** 4

## Source

Original text archived via Wayback Machine from aberdeen.com (1997).
Source document: `1997 IBM_s Enterprise Communications Family pr.pdf`

## How to Use

```python
import pandas as pd
obs = pd.read_csv("data/observations.csv")
preds = obs[obs["observation_type"] == "viability-prediction"]
outcomes = obs[obs["observation_type"] == "actual-outcome"]
```

See `scripts/demo_analysis.py` for a complete example.
