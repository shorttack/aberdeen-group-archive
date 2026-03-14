# IBM's OS/2 Warp Server: The Whole is Greater Than the Sum of the Parts

**Aberdeen Group Product Viewpoint — February 19, 1996**

## Study Metadata

| Field | Value |
|-------|-------|
| Study ID | aberdeen-1996-ibm-os2-warp-server |
| Author | Aberdeen Group |
| Date | 1996-02-19 |
| Type | product-viewpoint |
| Domain | server-network-operating-systems |
| License | CC-BY-4.0 |
| Importance | medium |
| Relevance | low |
| Prescience | low |

## Abstract

Aberdeen Group evaluates IBM's newly released OS/2 Warp Server, arguing it combines the networking strengths of Novell NetWare with the application strengths of Microsoft NT Server plus integrated directory and security services via a DCE-based Directory and Security Server (DSS) add-on. The study contends that OS/2 Warp Server is at least a year ahead of competitors in delivering an integrated, enterprise-wide NOS with objects, distributed directory services, and network security.

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study-level metadata with assessment ratings |
| entities.csv | 12 | Organizations mentioned in the study |
| technologies.csv | 10 | Technologies evaluated |
| observations.csv | 25 | Structured analytical observations |
| codes.csv | 24 | Controlled vocabulary definitions |

## Quick Load (Python)

```python
import pandas as pd
obs = pd.read_csv('data/observations.csv')
ents = pd.read_csv('data/entities.csv')
techs = pd.read_csv('data/technologies.csv')
print(obs['observation_type'].value_counts())
```

## Validation

```bash
frictionless validate datapackage.json
```

## Citation

Aberdeen Group. (1996). *IBM's OS/2 Warp Server: The Whole is Greater Than the Sum of the Parts*
(Volume 9, Number 4). Aberdeen Group, Boston MA.
Archived: https://web.archive.org/web/19970112010601/http://www.aberdeen.com:80/secure/viewpnts/v9n4/v9n4.htm
DOI: [pending Zenodo deposit]

## Methodology

Industry analysis, competitive profiling, and field research (interviews with LAN administrators and beta users).
Assessment covers OS/2 Warp Server product features, DCE-based Directory and Security Server, and competitive positioning
versus Novell NetWare 4.x, Microsoft NT Server 3.5x, and Banyan VINES.
