# Digital Debunks the NT/SMP Scalability Myth

**Study ID:** `aberdeen-1996-digital-debunks-ntsmp-scalability-myth`
**Archival Ingest Skill:** v13

## Study Metadata

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | November 22, 1996 |
| Type | market-study |
| Domain | server-computing-NT-SMP |
| License | CC-BY-4.0 |
| Source | Volume 9, Number 22, Aberdeen Market Viewpoint |

## Abstract

This Aberdeen Group Market Viewpoint argues that IT decision-makers should reconsider the widespread belief that Windows NT Server lacks SMP scalability beyond four processors. Using TPC-C benchmark data, Aberdeen demonstrates that Digital's 4-way Pentium Pro server achieves 6,712 tpmC at $65/tpmC, outperforming established midrange Unix and proprietary servers at a fraction of the cost. Aberdeen concludes that Microsoft's real strategy is performance clustering, not 8-way SMP scaling, and that Digital is optimally positioned to lead the NT midrange server market.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | high | Reframed the NT scalability debate at a critical juncture using TPC-certified data; influenced IT purchasing decisions for midrange server markets. |
| Relevance | medium | Price/performance analysis methodology using independent benchmarks remains applicable to cloud instance comparisons today; specific hardware references are dated. |
| Prescience | high | Core predictions accurate: 4-way NT dominated midrange, Wolfpack shipped on schedule, 8-way remained niche; Digital was acquired rather than winning independently. |

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study-level metadata |
| entities.csv | 11 | Organizations referenced |
| technologies.csv | 8 | Technologies assessed |
| observations.csv | 26 | Analytical observations |
| codes.csv | 21 | Controlled vocabulary |

## Load Example

```python
import pandas as pd
obs = pd.read_csv("data/observations.csv")
benchmarks = obs[obs["observation_type"] == "benchmark-result"]
print(benchmarks[["entity_id", "metric_name", "metric_value"]])
```

## Citation

> Aberdeen Group. (1996, November 22). *Digital Debunks the NT/SMP Scalability Myth*. Market Viewpoint Vol. 9 No. 22. Aberdeen Group, Inc. Boston, MA.
> Archived: https://web.archive.org/web/19970604112259/http://www.aberdeen.com:80/secure/viewpnts/v9n22/body.htm
> Dataset DOI: [pending Zenodo deposit]
