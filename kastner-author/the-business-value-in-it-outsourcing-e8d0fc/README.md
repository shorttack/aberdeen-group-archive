# The Business Value in IT Outsourcing

Frictionless Data Package for an Aberdeen Group research brief (June 2006) by Peter S. Kastner hypothesizing that IT outsourcing engagements fall into three maturity tiers and identifying key drivers and challenges to outsourcing success.

## Metadata

| Field | Value |
|-------|-------|
| **Study ID** | `the-business-value-in-it-outsourcing-e8d0fc` |
| **Title** | The Business Value in IT Outsourcing |
| **Author** | Aberdeen Group (Peter S. Kastner) |
| **Date** | 2006-06-01 |
| **Type** | research-brief |
| **Subject Domain** | it-outsourcing |
| **Methodology** | industry-analysis, field-research, benchmarking |
| **License** | CC-BY-4.0 |
| **Source File** | `The Business Value in IT Outsourcing.pdf` |

## Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Establishes a useful maturity framework for IT outsourcing success with specific hypothesized percentages; draws on Aberdeen's extensive survey base of 2,000+ companies on IT organizational maturity |
| **Relevance** | medium | IT outsourcing governance challenges (SLAs, change management, metrics alignment) remain highly relevant in 2024; the maturity model approach is still used by advisory firms for outsourcing assessments |
| **Prescience** | medium | The hypothesis that most outsourcing contracts run sub-optimally proved broadly accurate; industry surveys consistently show 40-60% dissatisfaction rates with IT outsourcing arrangements through the 2010s and 2020s |

## Abstract

Aberdeen Group research brief by Peter S. Kastner hypothesizing that IT outsourcing engagements fall into three maturity tiers: approximately 30% seriously misaligned, 50-66% sub-optimal, and only 5-10% driving full anticipated business value. The brief announces a planned benchmark report examining why outsourcing projects become sub-optimal and how companies can maximize business value, drawing on surveys of 2,000+ companies on IT maturity.

## Data Summary

| Resource | File | Rows | Description |
|----------|------|------|-------------|
| Studies | `data/studies.csv` | 1 | Study metadata with 16 fields including assessment ratings |
| Entities | `data/entities.csv` | 2 | Organizations referenced in the study |
| Technologies | `data/technologies.csv` | 8 | Technologies and frameworks analyzed |
| Observations | `data/observations.csv` | 35 | Structured observations extracted from the study |
| Codes | `data/codes.csv` | 43 | Code definitions for observation types, confidence levels, methodologies, and assessment ratings |

### Observation Type Breakdown

| Type | Count | Description |
|------|-------|-------------|
| framework-factor | 14 | Five outsourcing drivers and nine challenge areas for sub-optimal outsourcing |
| market-data | 5 | Maturity tier percentages, survey base size, tracking timeline |
| actual-outcome | 4 | Aberdeen acquisitions, outsourcing dissatisfaction confirmed, governance confirmed |
| benchmark-result | 3 | ROI measurement frequency across best-in-class, average, and laggard tiers |
| technology-assessment | 3 | SOA, enterprise integration, and BPO assessments |
| viability-prediction | 2 | Outsourcing dissatisfaction and governance importance predictions |
| strategy-classification | 2 | Outsourcing scope range and research approach classification |
| expert-opinion | 2 | Universal failure learning and maturity spectrum hypothesis |

## File Structure

```
the-business-value-in-it-outsourcing-e8d0fc/
  README.md                    # This file
  datapackage.json             # Frictionless Data Package descriptor
  data/
    studies.csv                # Study metadata (1 row, 16 fields)
    entities.csv               # Referenced entities (2 rows, 9 fields)
    technologies.csv           # Referenced technologies (8 rows, 9 fields)
    observations.csv           # Extracted observations (35 rows, 12 fields)
    codes.csv                  # Code definitions (43 rows, 4 fields)
  schema/
    schema_org.json            # Schema.org JSON-LD Dataset metadata
  source/
    original_text.md           # Full original document text with metadata appendix
  scripts/
    demo_analysis.py           # Validation and analysis script
```

## Quick Start with Python

```python
import csv
from collections import Counter

# Load observations
with open("data/observations.csv") as f:
    observations = list(csv.DictReader(f))

print(f"Total observations: {len(observations)}")

# Count by type
type_counts = Counter(r["observation_type"] for r in observations)
for obs_type, count in sorted(type_counts.items(), key=lambda x: -x[1]):
    print(f"  {obs_type}: {count}")

# Find framework factors (outsourcing drivers and challenge areas)
factors = [r for r in observations if r["observation_type"] == "framework-factor"]
print(f"\nFramework Factors: {len(factors)}")
for f in factors:
    print(f"  {f['metric_name']}: {f['metric_value'][:80]}...")

# Find maturity tier data
market = [r for r in observations if r["observation_type"] == "market-data"]
print(f"\nMaturity Tier Data:")
for m in market:
    print(f"  {m['metric_name']}: {m['metric_value'][:80]}...")

# Load entities and check acquisition status
with open("data/entities.csv") as f:
    entities = list(csv.DictReader(f))

acquired = [e for e in entities if e["status"] == "acquired"]
print(f"\nEntities subsequently acquired: {len(acquired)}")
for a in acquired:
    print(f"  {a['entity_name']} -> {a['successor']}")
```

## Validation

Run the validation script to check data package integrity:

```bash
cd the-business-value-in-it-outsourcing-e8d0fc
python scripts/demo_analysis.py
```

## Key Findings

1. **Three maturity tiers**: ~30% of IT outsourcing engagements are seriously misaligned, 50-66% run sub-optimally, and only 5-10% drive full anticipated business value
2. **Five outsourcing drivers**: Core competencies, cost savings, resource constraints, time-to-market, and culture wars
3. **Nine challenge areas**: SLAs, governance, preparation, transition, operations, change management, pricing, conflict resolution, and metrics
4. **IT maturity correlation**: ROI measurement frequency used as proxy for outsourcing readiness -- best-in-class companies measure ROI after every change
5. **Universal learning curve**: No company has outsourced IT without learning painful lessons

## Prescience Highlights

The study's hypotheses proved broadly accurate:
- **Outsourcing dissatisfaction rates**: Industry surveys through the 2010s and 2020s consistently show 40-60% dissatisfaction with IT outsourcing, validating the 50-66% sub-optimal hypothesis
- **Governance as differentiator**: Outsourcing governance frameworks became standard practice, with advisory firms (Gartner, ISG, Everest Group) building entire practices around governance maturity models
- **Aberdeen Group** itself was acquired by Harte-Hanks in 2007 and later by Spiceworks Ziff Davis, though the brand continued as a research resource

## Citation

> Aberdeen Group (Peter S. Kastner). "The Business Value in IT Outsourcing: Getting and Keeping IT Outsourcing Projects on Track to Business Value." Research Brief. Boston, MA: Aberdeen Group, June 2006.

## License

CC-BY-4.0 -- Creative Commons Attribution 4.0 International

---

*Generated by Archival Ingest Skill v13 on 2026-03-16*
