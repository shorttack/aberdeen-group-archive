# IBM's Network Computing Solution: Energize Your Enterprise

**Study ID:** 1997-ibm’s-network-computing-solution----e74e8a
**Author:** Aberdeen Group
**Date:** 1997-06-01
**Type:** profile
**Subject Domain:** Network Computing / Enterprise IT Architecture
**License:** CC-BY-4.0

## Abstract

Aberdeen Group profiles IBM's comprehensive Network Computing Solution branded 'Energize Your Enterprise', comprising six product families: Personal Communications, Business Intelligence, Information Integration, Application Development, Systems Management, and Extended Transaction Services. The study assesses IBM's approach to helping enterprises migrate from legacy architectures to Intranets, Web-enabled applications, and n-tier client-server. Aberdeen evaluates key technologies including DB2, MQSeries, Tivoli, VisualAge, CICS/Encina, and IBM's AnyNet multiprotocol middleware. The study provides Aberdeen's framework for network computing evaluation and concludes IBM's integrated approach provides a superior migration path versus point-solution competitors.

## Ratings

| Dimension | Score (1-5) | Rationale |
|-----------|-------------|-----------|
| Importance | 3 | Comprehensive 1997 primary source documenting IBM's enterprise network computing architecture at its fullest articulation. Valuable as a snapshot of the complete IBM middleware and application portfolio and its positioning versus emerging Internet/Intranet architectures. Somewhat overlaps with ECF profile but broader in scope. |
| Relevance | 3 | Relevant to the history of enterprise IT architecture evolution from mainframe through client-server to web/Internet. Documents IBM's full stack response to the Internet challenge and provides context for understanding the IBM middleware portfolio that persists today (DB2, MQ, CICS, Tivoli). |
| Prescience | 3 | Aberdeen's framing of network computing benefits (cost savings, customer interfaces, electronic commerce) proved accurate. IBM's prediction that business intelligence and data integration would be critical was highly accurate. However, the specific IBM solution stack (AnyNet, specific product names) proved less durable than IBM hoped. Internet thin-client architecture won over n-tier client-server as predicted. |

## Dataset Contents

| File | Description | Rows |
|------|-------------|------|
| data/studies.csv | Study-level metadata | 1 |
| data/entities.csv | Organizations, products, people | 6 |
| data/technologies.csv | Technologies analyzed | 9 |
| data/observations.csv | Structured observations | 18 |
| data/codes.csv | Methodology codebook | 8 |

## Key Statistics

- **Entities:** 6
- **Technologies:** 9
- **Observations:** 18
- **Predictions:** 2
- **Actual Outcomes:** 5

## Source

Original text archived via Wayback Machine from aberdeen.com (1997).
Source document: `1997 IBM's Network Computing Solution_ _Energize Your Enterprise pr.pdf`

## How to Use

```python
import pandas as pd
obs = pd.read_csv("data/observations.csv")
preds = obs[obs["observation_type"] == "viability-prediction"]
outcomes = obs[obs["observation_type"] == "actual-outcome"]
```

See `scripts/demo_analysis.py` for a complete example.
