# Internet Architecture: Prescription For Success

**Aberdeen Group Technology Viewpoint | Volume 9, Number 8 | April 17, 1996**

> Note: The study_id `aberdeen-1996-computer-telephony-integration` reflects the original PDF filename; the actual document content is the Internet Architecture Viewpoint.

---

## Study Metadata

| Field | Value |
|-------|-------|
| Study ID | aberdeen-1996-computer-telephony-integration |
| Author | Aberdeen Group |
| Date | 1996-04-17 |
| Type | white-paper |
| Domain | internet-intranet-architecture |
| License | CC-BY-4.0 |
| Source | [Wayback Machine](https://web.archive.org/web/19970112010334/http://www.aberdeen.com:80/secure/viewpnts/v9n8/v9n8.htm) |

## Abstract

Aberdeen Group prescribes an enterprise Internet/Intranet architecture for 1996, arguing that long-term value lies in the Intranet rather than public Internet. The study recommends a scalable architecture combining TP-monitor-like middleware, 64-bit VLM server hardware, parallel-scalable RDBMSs, and second-generation CADEs. Aberdeen dismisses Java as immature and warns that enterprises without proper architectural foundations will find that short-term Internet success blocks long-term success.

## Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | high | Published at the apex of the first Internet boom; Aberdeen's architectural framework influenced thousands of IS decisions in 1996-1997. |
| Relevance | high | Core principles — TP-monitor-like middleware, separation of presentation from data tiers, metadata repositories — are directly ancestral to microservices, API gateways, and cloud-native architectures. |
| Prescience | high | Intranet-first thesis proved correct; Java skepticism accurate for 1996-1998; e-commerce transformation prediction fully verified; middleware centrality confirmed by modern architectures. |

## Data Tables

| Table | File | Rows |
|-------|------|------|
| Studies | data/studies.csv | 1 |
| Entities | data/entities.csv | 7 |
| Technologies | data/technologies.csv | 8 |
| Observations | data/observations.csv | 23 |
| Codes | data/codes.csv | 18 |

## Quick Load (Python)

```python
import pandas as pd
observations = pd.read_csv("data/observations.csv")
predictions = observations[observations.observation_type == "viability-prediction"]
outcomes = observations[observations.observation_type == "actual-outcome"]
print(f"Predictions: {len(predictions)}, Outcomes: {len(outcomes)}")
```

## Citation

> Aberdeen Group. (1996). *Internet Architecture: Prescription For Success*. Aberdeen Group Technology Viewpoint, Vol. 9, No. 8. Boston, MA. Archived: https://web.archive.org/web/19970112010334/http://www.aberdeen.com:80/secure/viewpnts/v9n8/v9n8.htm

DOI: [pending Zenodo deposit]
