# Debunking the NT/SMP Scalability Myth

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | `aberdeen-1996-debunking-ntsmp-scalability-myth` |
| **Author** | Aberdeen Group |
| **Date** | 1996-11-26 |
| **Type** | white-paper |
| **Domain** | server-computing |
| **License** | CC-BY-4.0 |
| **Source File** | 1996 debunking NTSMP scalability myth.pdf |

## Abstract

Aberdeen Group's November 1996 Viewpoint argues that IS decision-makers should reconsider Windows NT's SMP scalability limitations, framing them as a deliberate Microsoft market strategy rather than an engineering constraint. Using TPC-C benchmark data, Aberdeen demonstrates that 4-way NT servers had already reached mid-range performance levels (6,712 tpmC at $65/tpmC), and projects NT will achieve 16,000 tpmC on 4-way platforms by 1998 while NT performance clusters will exceed 20,000 tpmC by early 1999. The study positions NT as an irresistible force in the mid-range server market based on price/performance momentum.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Published at a pivotal inflection point in the mid-range server market, this Viewpoint directly challenged conventional wisdom that NT could not compete with Unix and proprietary SMP systems. Aberdeen's TPC-C analysis was highly influential in legitimizing NT for enterprise IS planning in 1997-1998. |
| **Relevance** | medium | The analytical framework—using transaction benchmarks to segment server markets and project performance trajectories—remains methodologically sound and applicable to current cloud/on-premises performance debates. The specific hardware predictions are dated but the market dynamics analysis transfers well. |
| **Prescience** | high | Aberdeen's core predictions proved largely accurate: NT/Windows Server did dominate the mid-range market by 2000-2002 (IDC data confirms), 4-way NT performance exceeded 16,000 tpmC by 1998 (Microsoft/Compaq TPC-C results), and NT availability clusters (Wolfpack/MSCS) shipped in 1997. Performance cluster prediction at 20,000+ tpmC was also validated. |

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study-level metadata with assessments |
| entities.csv | 10 | Organizations referenced in the study |
| technologies.csv | 7 | Technologies referenced in the study |
| observations.csv | 24 | Extracted analytical observations |
| codes.csv | 18 | Controlled vocabulary definitions |

### Observations by Type

| Type | Count |
|------|-------|
| actual-outcome | 3 |
| benchmark-result | 4 |
| expert-opinion | 3 |
| framework-factor | 3 |
| market-data | 1 |
| strategy-classification | 2 |
| technology-assessment | 3 |
| viability-prediction | 5 |

## Key TPC-C Benchmark Data (1996)

| System | Processors | tpmC | $/tpmC | Year |
|--------|-----------|------|--------|------|
| Compaq ProLiant 5000 (NT 4.0 / SQL Server 6.5) | 4 | 6,712 | $65 | Nov 1996 |
| DEC AlphaServer 5/35 (Unix) | 32 | ~20,000 | $305 | 1996 |
| HP 9000 EPS30 (Unix clustered) | 48 | ~25,000 | $396 | 1996 |

## Quick Start

```python
import pandas as pd, os
base = os.path.dirname(os.path.abspath(__file__))
observations = pd.read_csv(os.path.join(base, "data/observations.csv"))
benchmarks = observations[observations["observation_type"] == "benchmark-result"]
print(benchmarks[["metric_name", "metric_value", "year_observed"]])
```

## Validation

```bash
frictionless validate datapackage.json
```

## Citation

> Aberdeen Group. (1996, November 26). *Debunking the NT/SMP Scalability Myth*. Aberdeen Group Market Viewpoint, Vol. 9, No. 20.
> Archived: https://web.archive.org/web/19970604112307/http://www.aberdeen.com:80/secure/viewpnts/v9n20/body.htm
> Dataset DOI: [pending Zenodo deposit]

## Methodology

industry-analysis, benchmarking, competitive-profiling
