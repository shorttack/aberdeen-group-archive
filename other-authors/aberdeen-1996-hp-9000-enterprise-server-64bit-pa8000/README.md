# HP 9000 Enterprise Server Performance Leadership Again: The 64-bit PA-8000 Has Arrived

**Aberdeen Group | September 17, 1996 | Archival Dataset**

---

## Study Metadata

| Field | Value |
|-------|-------|
| Study ID | aberdeen-1996-hp-9000-enterprise-server-64bit-pa8000 |
| Author | Aberdeen Group |
| Date | 1996-09-17 |
| Type | market-study |
| Domain | unix-enterprise-servers |
| License | CC-BY-4.0 |
| Source | [Wayback Machine](https://web.archive.org/web/19970112011513/http://www.aberdeen.com:80/secure/profiles/hp9000/hp9000.htm) |

## Abstract

Aberdeen Group evaluates HP's September 1996 announcement of PA-8000-based HP 9000 enterprise servers, documenting benchmark performance results (K460 at 12,321 tpmC — a 2.5x improvement over its PA-7200 predecessor) and positioning HP's PRISM framework as the standard for Unix enterprise server selection. The study asserts HP's competitive superiority over IBM, Sun, and Digital in the Unix server market, and outlines HP's roadmap through PA-8200, PA-8500, and eventual Merced processor transitions.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | high | Documented the first PA-8000 TPC-C benchmark results for HP 9000 servers at a pivotal moment in Unix server competition; the 2.5x generation-over-generation performance leap and pricing data were significant inputs for IS decision-makers in 1996. |
| Relevance | low | The specific benchmarks and processors are entirely obsolete; the HP 9000/PA-RISC platform was discontinued in 2003. The study retains archival value for understanding 1990s Unix server competitive dynamics. |
| Prescience | medium | HP's short-term performance roadmap (PA-8200, PA-8500) proved accurate, but the long-term Merced/Itanium transition was delayed until 2001 and ultimately failed commercially; HP 9000 was discontinued in 2003. |

---

## Data Tables

| Table | File | Rows |
|-------|------|------|
| Studies | data/studies.csv | 1 |
| Entities | data/entities.csv | 9 |
| Technologies | data/technologies.csv | 10 |
| Observations | data/observations.csv | 27 |
| Codes | data/codes.csv | 18 |

---

## Quick Load (Python)

```python
import pandas as pd
base = "."
obs = pd.read_csv(f"{base}/data/observations.csv")
print(obs[obs["observation_type"]=="benchmark-result"][["metric_name","metric_value"]])
```

## Validation

```bash
frictionless validate datapackage.json
python scripts/demo_analysis.py
```

---

## Citation

> Aberdeen Group. (1996, September 17). *HP 9000 Enterprise Server Performance Leadership Again: The 64-bit PA-8000 Has Arrived*. Aberdeen Group, Boston, MA.
> Archived: https://web.archive.org/web/19970112011513/http://www.aberdeen.com:80/secure/profiles/hp9000/hp9000.htm
> Dataset DOI: [pending Zenodo deposit]

---

*Processed by Archival Ingest Skill v13 | 2026-03-14*
