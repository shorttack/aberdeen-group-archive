# Eclipsys SunriseXA 3.3 Meets Subsecond Response Time Objective

**Frictionless Data Package** -- Aberdeen Group Historical Research Archive

---

## Study Metadata

| Field           | Value |
|-----------------|-------|
| **Study ID**    | `2004-eclipsys-auditor-report-4-3cd30c` |
| **Author**      | Peter S. Kastner |
| **Date**        | 2004-04-01 |
| **Type**        | benchmark |
| **Domain**      | healthcare-it |
| **Methodology** | benchmarking, statistical-analysis |
| **Source File** | `2004_Eclipsys_auditor_report_4.txt` |
| **License**     | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |

---

## Abstract

Aberdeen Group benchmark audit report confirming that Eclipsys SunriseXA 3.3 healthcare information system met subsecond response time objectives in a simulated 6,000-bed hospital environment. Using Mercury LoadRunner, the benchmark executed 65,637 transactions in one hour (exceeding 1,000 transactions per minute) representing 7,411 medical orders. Nearly all of 82 transaction types achieved subsecond response times, with exceptions only for batch patient order submissions. Database server CPU utilization peaked at only 40%, demonstrating significant headroom. Aberdeen concluded that Eclipsys successfully addressed response time issues identified in October 2003.

---

## Data Tables

| File | Rows | Description |
|------|------|-------------|
| `data/studies.csv` | 1 | Study metadata including assessment ratings and rationales |
| `data/entities.csv` | 10 | Organizations: Eclipsys, Unisys, Microsoft, Mercury Interactive, Intel, Aberdeen Group, Memorial Hermann, EMC, SAP, Allscripts |
| `data/technologies.csv` | 9 | Technologies: SunriseXA, Mercury LoadRunner, Unisys ES7000, Windows 2000 Data Center, SQL Server 2000, .NET Framework, Intel Xeon, HL7, EMC Fibre Channel Storage |
| `data/observations.csv` | 30 | Benchmark results, technology assessments, expert opinions, market data, actual outcomes |
| `data/codes.csv` | 24 | Controlled vocabulary: observation types, methodology codes, confidence levels, lifecycle stages |

### Observation Type Breakdown

| Type | Count |
|------|-------|
| benchmark-result | 19 |
| technology-assessment | 4 |
| expert-opinion | 3 |
| actual-outcome | 2 |
| market-data | 1 |
| strategy-classification | 1 |

---

## Key Benchmark Results

1. **65,637 transactions** executed in one steady-state hour at simulated 6,000-bed hospital peak load.

2. **7,411 total orders** during benchmark hour, far exceeding the 5,000 order/hour goal (2.27x the busiest hospital known to Eclipsys).

3. **Subsecond response times** for 4 of 5 transaction categories (averages and 99th percentiles); only administrative category exceeded due to doctor log-on data downloads.

4. **40% CPU utilization** on the database server, demonstrating significant headroom for even more intense workloads.

5. **721,158 transactions** in 12-hour overnight test, sustaining >1,000 transactions per minute with no system constraints.

6. **Only 8 of 82 transaction types** exceeded 1-second average response time, all involving batch/group patient order operations.

---

## Methodology Summary

Aberdeen Group conducted this benchmark audit using two primary methods:

- **Benchmarking**: Audited the execution of a Mercury LoadRunner hospital simulation benchmark at Eclipsys Corp. in Malvern, PA on March 2-3, 2004, including a one-hour steady-state test, 12-hour overnight test, isolation test, and slow-client test.
- **Statistical analysis**: Performed statistical analysis of response times across 82 transaction types grouped into five categories, computing averages, geometric means, and 99th percentiles.

---

## Load Example (Python / pandas)

```python
import pandas as pd
import os

BASE = "path/to/2004-eclipsys-auditor-report-4-3cd30c"

studies      = pd.read_csv(os.path.join(BASE, "data/studies.csv"))
entities     = pd.read_csv(os.path.join(BASE, "data/entities.csv"))
technologies = pd.read_csv(os.path.join(BASE, "data/technologies.csv"))
observations = pd.read_csv(os.path.join(BASE, "data/observations.csv"))
codes        = pd.read_csv(os.path.join(BASE, "data/codes.csv"))

# Example: All benchmark results
benchmarks = observations[observations["observation_type"] == "benchmark-result"]
print(benchmarks[["obs_id", "metric_name", "metric_value"]].to_string())

# Example: Technologies that are now obsolete
obsolete = technologies[technologies["lifecycle_current"] == "obsolete"]
print(obsolete[["tech_name", "era", "lifecycle_at_study"]].to_string())
```

---

## Frictionless Validation

```bash
# Install frictionless tools
pip install frictionless

# Validate the data package
frictionless validate path/to/2004-eclipsys-auditor-report-4-3cd30c/datapackage.json
```

---

## Demo Analysis

Run the validation and analysis script:

```bash
python scripts/demo_analysis.py
```

The script checks referential integrity, code coverage, observation type distribution, technology lifecycle summary, and entity status summary.

---

## Citation

> Kastner, P. S. (2004, April). *Eclipsys SunriseXA 3.3 Meets Subsecond Response Time Objective: A Benchmark Audit Report*. Aberdeen Group, Inc., Boston, MA. Dataset: 2004-eclipsys-auditor-report-4-3cd30c. License: CC-BY-4.0.

---

## Directory Structure

```
2004-eclipsys-auditor-report-4-3cd30c/
  README.md
  datapackage.json
  data/
    studies.csv
    entities.csv
    technologies.csv
    observations.csv
    codes.csv
  schema/
    schema_org.json
  source/
    original_text.md
  scripts/
    demo_analysis.py
```

---

*Processed by Archival Ingest Skill v13 on 2026-03-16.*
