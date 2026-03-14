# Network Appliance: Data Appliances for Commercial Network Computing

**Aberdeen Group Company Profile | November 1996**

---

## Study Metadata

| Field | Value |
|-------|-------|
| Study ID | aberdeen-1996-network-appliance-data-appliances |
| Author | Aberdeen Group |
| Date | 1996-11-01 |
| Type | market-study |
| Domain | network-attached-storage |
| License | CC-BY-4.0 |
| Source | [Wayback Machine](https://web.archive.org/web/19970604113423/http://www.aberdeen.com:80/secure/profiles/netapp/body.htm) |

## Abstract

Aberdeen Group profiles Network Appliance (NetApp) as a pioneer in network-attached storage (NAS) for commercial computing environments. The study examines NetApp's filer hardware (F220, F330, F540), Data ONTAP software with WAFL file system, and multiprotocol support (NFS, CIFS, HTTP). Aberdeen concludes NetApp is well-positioned to capitalize on the shift from application-server-based storage to dedicated network-attached data servers, citing revenue growth from $2M (1994) to $47M (FY1996) approaching $100M.

## Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | high | Aberdeen identified NetApp at the precise moment the NAS market was emerging as a distinct category; the "data appliance" framing helped define the NAS segment. |
| Relevance | high | NetApp remains a leading data infrastructure company (NASDAQ: NTAP, ~$6.3B revenue FY2024); NAS architectural principles underpin modern cloud storage design. |
| Prescience | high | Aberdeen predicted $100M FY1997 revenue (actual was ~$166M); CIFS/HTTP multiprotocol support proved foundational to NetApp's 30-year market leadership. |

## Data Tables

| Table | File | Rows |
|-------|------|------|
| Studies | data/studies.csv | 1 |
| Entities | data/entities.csv | 6 |
| Technologies | data/technologies.csv | 7 |
| Observations | data/observations.csv | 22 |
| Codes | data/codes.csv | 18 |

## Observation Types

| Type | Count |
|------|-------|
| strategy-classification | 2 |
| technology-assessment | 3 |
| market-data | 3 |
| viability-prediction | 4 |
| actual-outcome | 5 |
| framework-factor | 2 |
| expert-opinion | 1 |
| benchmark-result | 0 |
| **Total** | **22** |

## Quick Load (Python)

```python
import pandas as pd
observations = pd.read_csv("data/observations.csv")
revenue_data = observations[observations.observation_type == "market-data"]
print(revenue_data[["year_observed", "metric_name", "metric_value"]])
```

## Citation

> Aberdeen Group. (1996). *Network Appliance: Data Appliances for Commercial Network Computing*. Aberdeen Group Company Profile. Boston, MA. Archived: https://web.archive.org/web/19970604113423/http://www.aberdeen.com:80/secure/profiles/netapp/body.htm

DOI: [pending Zenodo deposit]
