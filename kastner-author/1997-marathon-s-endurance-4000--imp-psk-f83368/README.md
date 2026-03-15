# Marathon's Endurance 4000: Bringing Fault Tolerance to NT Servers & Clusters

**Aberdeen Group Impact Brief | February 7, 1997**

## Study Metadata

| Field | Value |
|-------|-------|
| study_id | 1997-marathon's-endurance-4000--imp-psk-f83368 |
| title | Marathon's Endurance 4000: Bringing Fault Tolerance to NT Servers & Clusters |
| author | Peter S. Kastner |
| date | 1997-02-07 |
| type | impact-brief |
| subject_domain | server-high-availability |
| methodology | competitive-profiling, industry-analysis |
| source_file | 1997 Marathon's Endurance™ 4000_ imp PSK.pdf |
| license | CC-BY-4.0 |

## Abstract

Peter S. Kastner of Aberdeen Group evaluates Marathon Technologies' Endurance 4000, a hardware-based fault-tolerant solution for Windows NT servers. With NT increasingly hosting mission-critical applications, the study examines why Microsoft's forthcoming Wolfpack clustering software provides only minutes-level failover—inadequate for true mission-critical needs—while Marathon's Endurance 4000 provides continuous, transparent fault tolerance at 99.99% uptime for ~$24,995. The study concludes the Endurance 4000 is a well-architected breakthrough that creates a new 'fault-tolerant NT servers' category.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | high | First major analyst evaluation of hardware-based NT fault tolerance; Peter S. Kastner accurately identified the reliability gap in NT for mission-critical applications and positioned Marathon as a category-creating leader just as NT adoption was accelerating. |
| Relevance | medium | The architectural concepts (lock-step mirroring, hardware abstraction layer interception, campus-distance disaster recovery) are historically significant; modern high-availability architectures for VMs and containers evolved from these principles. |
| Prescience | high | Kastner correctly predicted the Endurance 4000 would become a 'breakaway leader' in fault-tolerant NT servers; Marathon survived, pivoted to software, and was acquired by Stratus Technologies in 2012 for its fault-tolerance IP. His critique of Wolfpack's 'minutes to recover' limitation proved accurate—MSCS v1 had serious reliability problems. |

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study metadata and assessments |
| entities.csv | 10 | Organizations referenced |
| technologies.csv | 6 | Technologies discussed |
| observations.csv | 21 | Extracted analytical observations |
| codes.csv | 21 | Controlled vocabulary |

## Quick Load (Python)

```python
import pandas as pd
obs = pd.read_csv("data/observations.csv")
print(obs.groupby("observation_type").size())
```

## Validation

```bash
frictionless validate datapackage.json
```

## Citation

Peter S. Kastner. (1997). *Marathon's Endurance 4000: Bringing Fault Tolerance to NT Servers & Clusters*. Aberdeen Group Impact Brief.
Archived: https://web.archive.org/web/19970604114333/http://www.aberdeen.com:80/secure/impacts/1997/mar/body.htm
License: CC-BY-4.0
