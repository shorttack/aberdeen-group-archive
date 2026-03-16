# SARS May Impact Global Electronics Industry

**Study ID:** `2003-sars2-hot-topic-deb75d`
**Authors:** Russ Craig; Peter Kastner
**Date:** 2003-03-28
**Type:** Hot Topic
**Publisher:** Aberdeen Group
**License:** CC-BY-4.0

## Abstract

Aberdeen Group hot topic report warning that the 2003 SARS outbreak could cause major disruptions to the global electronics supply chain concentrated in Asia Pacific. The report documents that Asia Pacific consumed 37% ($52B) of 2002 semiconductor production, with 85%+ of WiFi gear made in Taiwan and PRC. It catalogs facility closures (Motorola Singapore), travel bans (Compal), and corporate shutdowns (CTIC) already occurring, and warns that a PRC quarantine would mean nuclear winter for the semiconductor industry. The analysis identifies just-in-time manufacturing as inherently vulnerable to pandemic disruption and notes critical single-source dependencies on PRC components.

## Ratings

| Dimension | Rating | Summary |
|-----------|--------|---------|
| Importance | **high** | Discussed on NBC Nightly News within 24 hours of publication |
| Relevance | **high** | COVID-19 validated every concern raised |
| Prescience | **high** | Predictions proved dramatically correct during COVID-19 |

## Data Tables

| File | Description | Rows |
|------|-------------|------|
| `data/studies.csv` | Study metadata | 1 |
| `data/entities.csv` | Companies and organizations referenced | 17 |
| `data/technologies.csv` | Technologies and manufacturing processes | 6 |
| `data/observations.csv` | Coded observations, predictions, and outcomes | 33 |
| `data/codes.csv` | Code definitions for all coded fields | 34 |

## Supporting Files

| File | Description |
|------|-------------|
| `datapackage.json` | Frictionless Data Package descriptor |
| `schema/schema_org.json` | Schema.org JSON-LD metadata |
| `original_text.md` | Original document text with full metadata |
| `scripts/demo_analysis.py` | Python script for loading and validating data |

## Quick Start (Python)

```python
import csv
from pathlib import Path

base = Path("data")

# Load observations
with open(base / "observations.csv") as f:
    observations = list(csv.DictReader(f))

# Count by observation type
from collections import Counter
type_counts = Counter(obs["observation_type"] for obs in observations)
for obs_type, count in type_counts.most_common():
    print(f"  {obs_type}: {count}")

# Show predictions paired with outcomes
predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
outcomes = [o for o in observations if o["observation_type"] == "actual-outcome" and int(o["year_observed"]) >= 2020]

print(f"\nPredictions from 2003: {len(predictions)}")
print(f"Validated outcomes (2020+): {len(outcomes)}")
```

## Schema

All CSV files follow the schemas defined in `datapackage.json`. Key conventions:

- **entity_id**: Canonical lowercase hyphenated names (e.g., `sony`, `broadcom`)
- **tech_id**: Canonical lowercase hyphenated names (e.g., `wifi-802-11`, `just-in-time`)
- **obs_id**: Sequential format `OBS-001`, `OBS-002`, etc.
- **observation_type**: One of 8 standard values defined in `codes.csv`
- **confidence**: One of `high`, `medium`, `low`, `verified`

## Citation

Craig, R. and Kastner, P. (2003). "SARS May Impact Global Electronics Industry." Aberdeen Group Hot Topic Report, March 28, 2003. Data package: `2003-sars2-hot-topic-deb75d`.
