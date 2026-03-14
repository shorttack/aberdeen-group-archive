# ManageWORKS 2.2 Market Profile

**Study ID:** `aberdeen-1996-dec-manageworks-22`
**Archival Ingest Skill:** v13

## Study Metadata

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | March 1996 |
| Type | market-study |
| Domain | LAN-management-software |
| License | CC-BY-4.0 |
| Source File | 1996 DEC - ManageWORKS 2.2 pr.pdf |

## Abstract

This Aberdeen Group product profile evaluates Digital Equipment Corporation's ManageWORKS 2.2, a multi-NOS LAN management platform designed for site and workgroup environments of 10 to 800 nodes. The study assesses ManageWORKS' architecture, partner ecosystem, and competitive positioning against McAfee and Symantec's Norton Administrator for Networks, concluding that its open, partner-extensible approach is unique in the market. Aberdeen highlights the product's advantage in enabling best-of-breed integrations across disparate network operating systems.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | medium | Documented an early 1990s LAN management platform at a pivotal moment in multi-NOS administration; Aberdeen endorsement carried weight, but ManageWORKS was niche. |
| Relevance | low | ManageWORKS 2.2 and the multi-NOS LAN management category are obsolete; architectures (NetWare, LAN Manager, PATHWORKS) have been entirely replaced. |
| Prescience | medium | Aberdeen's claim of open platform uniqueness was partly correct short-term, but the platform was discontinued after DEC's 1998 acquisition by Compaq. |

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study-level metadata |
| entities.csv | 11 | Organizations referenced |
| technologies.csv | 8 | Technologies assessed |
| observations.csv | 20 | Analytical observations |
| codes.csv | 21 | Controlled vocabulary |

## Load Example

```python
import pandas as pd
obs = pd.read_csv("data/observations.csv")
entities = pd.read_csv("data/entities.csv")
print(obs.groupby("observation_type").size())
```

## Frictionless Validation

```bash
frictionless validate datapackage.json
```

## Citation

> Aberdeen Group. (1996, March). *ManageWORKS 2.2 Market Profile*. Aberdeen Group, Inc. Boston, MA.
> Archived: https://web.archive.org/web/19970112012044/http://www.aberdeen.com:80/secure/profiles/decmgwk/decmgwk.htm
> Dataset DOI: [pending Zenodo deposit]

## Methodology

Industry analysis and competitive profiling based on vendor documentation and Aberdeen analyst review.
