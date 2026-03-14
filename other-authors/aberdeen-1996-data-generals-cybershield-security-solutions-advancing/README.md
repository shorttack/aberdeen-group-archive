# Data General's Cybershield: Security Solutions for Advancing Business on the Net

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | `aberdeen-1996-data-generals-cybershield-security-solutions-advancing` |
| **Author** | Aberdeen Group |
| **Date** | 1996-12-01 |
| **Type** | market-study |
| **Domain** | internet-security |
| **License** | CC-BY-4.0 |
| **Source File** | 1996 Data Generals CyberShield security solutions advancing.pdf |

## Abstract

Aberdeen Group profiles Data General's Cybershield security platform, an integrated suite built on the B2-level secure DG/UX operating system (B2SO), designed to protect enterprise Intranets and electronic commerce applications. The study documents IS executives' concerns about network security and the inadequacy of standalone firewalls, then validates Cybershield's ability to segregate users, applications, and data with minimal performance impact. Aberdeen recommends Cybershield as a superior alternative to component-based point solutions for IS executives deploying Internet-facing business applications.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Published at a pivotal moment when enterprise internet security was nascent; Cybershield's B2-level OS security model anticipated modern zero-trust concepts, and Aberdeen's identification of firewall limitations proved prescient. Impact was limited by DG's niche market position. |
| **Relevance** | medium | The study's conceptual framework—integrated security over component point-solutions, role-based access controls, compartmentalized network security—directly anticipates modern zero-trust architecture principles, making the analytical framework relevant even though the specific products are obsolete. |
| **Prescience** | medium | Aberdeen correctly identified that integrated security platforms would outperform component firewalls, and that e-commerce security would require OS-level controls—predictions validated by industry evolution. However, DG itself failed to sustain the market position predicted. |

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study-level metadata with assessments |
| entities.csv | 6 | Organizations referenced in the study |
| technologies.csv | 7 | Technologies referenced in the study |
| observations.csv | 22 | Extracted analytical observations |
| codes.csv | 18 | Controlled vocabulary definitions |

### Observations by Type

| Type | Count |
|------|-------|
| actual-outcome | 3 |
| benchmark-result | 2 |
| expert-opinion | 3 |
| framework-factor | 3 |
| market-data | 2 |
| strategy-classification | 2 |
| technology-assessment | 4 |
| viability-prediction | 3 |

## Quick Start

```python
import pandas as pd, os
base = os.path.dirname(os.path.abspath(__file__))
observations = pd.read_csv(os.path.join(base, "data/observations.csv"))
print(observations.groupby("observation_type").size())
```

## Validation

```bash
frictionless validate datapackage.json
```

## Citation

> Aberdeen Group. (1996). *Data General's Cybershield: Security Solutions for Advancing Business on the Net*. Aberdeen Group, Inc., Boston, Massachusetts.
> Archived: https://web.archive.org/web/19970604113358/http://www.aberdeen.com:80/secure/profiles/dgcyb/dgcyber2.htm
> Dataset DOI: [pending Zenodo deposit]

## Methodology

industry-analysis, competitive-profiling, field-research
