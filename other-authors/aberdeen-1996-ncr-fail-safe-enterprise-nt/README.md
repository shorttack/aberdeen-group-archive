# NCR: Finally a Fail-Safe Choice For Enterprise NT

**Aberdeen Group Technology Viewpoint | Volume 9, Number 11 | May 25, 1996**

---

## Study Metadata

| Field | Value |
|-------|-------|
| Study ID | aberdeen-1996-ncr-fail-safe-enterprise-nt |
| Author | Aberdeen Group |
| Date | 1996-05-25 |
| Type | market-study |
| Domain | enterprise-NT-OLTP |
| License | CC-BY-4.0 |
| Source | [Wayback Machine](https://web.archive.org/web/19961023173805/http://www.aberdeen.com:80/secure/viewpnts/v9n11/v9n11.htm) |

## Abstract

Aberdeen Group evaluates NCR's Windows NT Server products for mission-critical OLTP applications based on user interviews with early adopters. The study finds that NCR's LifeKeeper, TOP END, and WorldMark servers address NT's enterprise weaknesses in reliability, scalability, and manageability. Aberdeen concludes that NCR has delivered on its 1994 promise and is a "fail-safe choice" for NT-based OLTP deployment in retail, finance, telecom, and transportation industries.

## Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | high | Published at pivotal moment when NT challenged Unix/mainframes; NCR was the leading enterprise NT integrator and this Viewpoint shaped 1996 early-adopter decisions. |
| Relevance | medium | NT-specific product details are obsolete, but the RAS evaluation framework for OS platform transitions remains applicable to modern cloud/edge migration decisions. |
| Prescience | high | NT SMP scalability predictions (8 CPUs by fall 1996, 12-16 by mid-1997) proved largely accurate; Windows NT's enterprise dominance for OLTP by 2000 materialized as predicted. |

## Data Tables

| Table | File | Rows |
|-------|------|------|
| Studies | data/studies.csv | 1 |
| Entities | data/entities.csv | 5 |
| Technologies | data/technologies.csv | 7 |
| Observations | data/observations.csv | 20 |
| Codes | data/codes.csv | 18 |

## Observation Types

| Type | Count |
|------|-------|
| strategy-classification | 1 |
| technology-assessment | 2 |
| benchmark-result | 1 |
| market-data | 2 |
| viability-prediction | 4 |
| actual-outcome | 4 |
| framework-factor | 4 |
| expert-opinion | 1 |
| **Total** | **20** |

## Quick Load (Python)

```python
import pandas as pd

studies = pd.read_csv("data/studies.csv")
entities = pd.read_csv("data/entities.csv")
technologies = pd.read_csv("data/technologies.csv")
observations = pd.read_csv("data/observations.csv")
codes = pd.read_csv("data/codes.csv")

# Predictions vs outcomes
predictions = observations[observations.observation_type == "viability-prediction"]
outcomes = observations[observations.observation_type == "actual-outcome"]
print(f"Predictions: {len(predictions)}, Outcomes: {len(outcomes)}")
```

## Frictionless Validation

```bash
frictionless validate datapackage.json
```

## Citation

> Aberdeen Group. (1996). *NCR: Finally a Fail-Safe Choice For Enterprise NT*. Aberdeen Group Technology Viewpoint, Vol. 9, No. 11. Boston, MA. Archived: https://web.archive.org/web/19961023173805/http://www.aberdeen.com:80/secure/viewpnts/v9n11/v9n11.htm

DOI: [pending Zenodo deposit]

## Methodology

Field research via user interviews with early NCR/NT OLTP adopters in retail, finance, telecommunications, and transportation. Supplemented by vendor briefings and Aberdeen industry analysis. NCR commissioned the study as a progress-check on its 1994 enterprise NT commitment.
