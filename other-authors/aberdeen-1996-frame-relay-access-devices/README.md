# Frame Relay Access Devices

> Aberdeen Group Research Profile | 1996-06-01 | CC-BY-4.0

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | `aberdeen-1996-frame-relay-access-devices` |
| **Author** | Aberdeen Group |
| **Date** | 1996-06-01 |
| **License** | CC-BY-4.0 |
| **Source** | [Wayback Machine](https://web.archive.org/web/19970604113801/http://www.aberdeen.com:80/secure/profiles/netlink/netlink2.htm) |

## Abstract

This Aberdeen Group profile evaluates Netlink, Inc.'s family of Frame Relay Access Devices (FRADs) including TurboFRAD, OmniFRAD, NetFRAD, and the OmniLinx 8000 edge switch. The study examines the technical advantages of FRADs over routers for mixed SNA/LAN enterprise WAN environments, documents customer ROI through 20-25% leased-line cost savings, and predicts that frame relay will remain integral to the eventual ATM migration as an edge network.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Documented the FRAD vs. router decision at peak frame relay adoption; useful for understanding the SNA-to-IP transition period and WAN technology competitive dynamics of the mid-1990s. |
| **Relevance** | low | Frame relay and SNA are legacy protocols essentially replaced by MPLS, SD-WAN, and IP-native architectures; the study is primarily of historical interest for networking technology evolution. |
| **Prescience** | high | Aberdeen's prediction that frame relay would persist as an ATM edge network rather than being displaced proved accurate; ATM never displaced frame relay which coexisted until both were eventually superseded by MPLS/IP in the 2000s. |

## Data Tables

| File | Rows | Description |
|------|------|-------------|
| `data/studies.csv` | 1 | Study metadata with assessment ratings |
| `data/entities.csv` | 6 | Organizations and companies referenced |
| `data/technologies.csv` | 6 | Technologies mentioned |
| `data/observations.csv` | 18 | Extracted observations and predictions |
| `data/codes.csv` | 24 | Controlled vocabulary definitions |

**Observation types:** actual-outcome: 2; benchmark-result: 3; expert-opinion: 1; market-data: 2; strategy-classification: 1; technology-assessment: 7; viability-prediction: 2

## Quick Start (Python)

```python
import pandas as pd

obs = pd.read_csv("data/observations.csv")
entities = pd.read_csv("data/entities.csv")
techs = pd.read_csv("data/technologies.csv")

# Show predictions and outcomes
predictions = obs[obs["observation_type"] == "viability-prediction"]
outcomes = obs[obs["observation_type"] == "actual-outcome"]
print(f"Predictions: {len(predictions)}, Outcomes: {len(outcomes)}")
```

## Validation

```bash
frictionless validate datapackage.json
python scripts/demo_analysis.py
```

## Citation

```
Aberdeen Group. (1996). Frame Relay Access Devices. Aberdeen Group, Inc., Boston MA.
Archived: https://web.archive.org/web/19970604113801/http://www.aberdeen.com:80/secure/profiles/netlink/netlink2.htm
Dataset: https://github.com/kastner/aberdeen-archival/aberdeen-1996-frame-relay-access-devices
License: CC-BY-4.0
DOI: [PENDING — assign via Zenodo]
```

## Methodology

This profile was produced using Aberdeen Group's vendor assessment methodology combining:
- Industry analysis and competitive profiling
- Field research with enterprise customers
- Benchmarking against published TPC and industry standards (where applicable)

---
*Processed by Archival Ingest Skill v13 | 2026-03-14*
