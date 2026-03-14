# Unisys Clears the Path Ahead for A & OS 2200 Series Customers

**Aberdeen Group Company Profile | April 1996**

---

## Study Metadata

| Field | Value |
|-------|-------|
| Study ID | aberdeen-1996-unisys-clears-path-a-series-os2200 |
| Author | Aberdeen Group |
| Date | 1996-04-01 |
| Type | market-study |
| Domain | enterprise-servers-mainframe |
| License | CC-BY-4.0 |
| Source | [Wayback Machine](https://web.archive.org/web/19970112011840/http://www.aberdeen.com:80/secure/profiles/unisys_1/unisys1.htm) |

## Abstract

Aberdeen Group profiles Unisys ClearPath HMP (Heterogeneous Multi-Processing) servers, which combine CMOS versions of MCP/AS and OS 2200 enterprise systems with Intel-based Unix/NT SMP servers in a single cabinet. Aberdeen examines how ClearPath gives Unisys's 8,500+ mainframe customers a migration path to open client-server architectures while preserving existing investments. Unisys is transitioning from hardware to services, while hardware remains 40% of $6.2B in 1995 revenue.

## Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | high | ClearPath was pivotal for 8,500+ mid-to-large-range A Series and 1100/2200 customers evaluating mainframe migration strategies at a moment of maximum uncertainty. |
| Relevance | medium | Unisys ClearPath OS 2200 remains in active production use (deployable on AWS as of 2025); the mainframe-to-open-systems hybrid migration framework remains relevant for legacy modernization decisions. |
| Prescience | high | Aberdeen's ClearPath viability assessment proved correct over 28+ years; Unisys successfully transitioned to services; OS 2200 now runs on AWS (2025), validating the migration strategy endorsed in 1996. |

## Data Tables

| Table | File | Rows |
|-------|------|------|
| Studies | data/studies.csv | 1 |
| Entities | data/entities.csv | 5 |
| Technologies | data/technologies.csv | 6 |
| Observations | data/observations.csv | 20 |
| Codes | data/codes.csv | 18 |

## Quick Load (Python)

```python
import pandas as pd
observations = pd.read_csv("data/observations.csv")
print(observations[observations.observation_type.isin(["viability-prediction","actual-outcome"])][
    ["obs_id","year_observed","observation_type","metric_name"]
])
```

## Citation

> Aberdeen Group. (1996). *Unisys Clears the Path Ahead for A & OS 2200 Series Customers*. Aberdeen Group Company Profile. Boston, MA. Archived: https://web.archive.org/web/19970112011840/http://www.aberdeen.com:80/secure/profiles/unisys_1/unisys1.htm

DOI: [pending Zenodo deposit]
