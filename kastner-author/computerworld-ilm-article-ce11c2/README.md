# Waiting for ILM?

Frictionless Data Package for a Computerworld published column (July 2004) by Peter S. Kastner presenting a six-step recipe for enterprise adoption of Information Lifecycle Management (ILM).

## Metadata

| Field | Value |
|-------|-------|
| **Study ID** | `computerworld-ilm-article-ce11c2` |
| **Title** | Waiting for ILM? |
| **Author** | Peter S. Kastner |
| **Date** | 2004-07-29 |
| **Type** | article |
| **Subject Domain** | enterprise-storage |
| **Methodology** | industry-analysis, document-review |
| **License** | CC-BY-4.0 |
| **Source File** | `Computerworld ILM article.txt` |

## Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Practical ILM adoption guide published in a major trade publication; useful six-step framework but not groundbreaking research |
| **Relevance** | high | Tiered storage and data lifecycle management are more relevant than ever with cloud storage tiers, compliance requirements, and enterprise data governance |
| **Prescience** | high | Correctly predicted ILM software maturity timeline of 2008-2010; correctly predicted midline/capacity tier dominance; four-pool model maps to modern cloud storage tiers |

## Abstract

Computerworld published column by Aberdeen Group co-founder Peter S. Kastner presenting a six-step recipe for enterprise adoption of Information Lifecycle Management (ILM). Argues that while cross-application ILM management software is four to five years away (circa 2008-2009), organizations should not wait but should proactively evolve toward ILM. Prescribes centralizing storage on SANs and NAS, creating pools on three axes (data type, use frequency, storage tier), establishing lifecycle policies, populating applications on appropriate pools during five-year refresh cycles, driving economies of scale through virtualization and automation, and finally implementing intelligent ILM-based storage by 2008-2010. Introduces a four-pool storage model: online dynamic (FC/SCSI), midline (25% cost), nearline buffered (D2D backup), and offline (tape for DR). Projects 45% annual storage growth and warns of litigation liability from offline tapes.

## Data Summary

| Resource | File | Rows | Description |
|----------|------|------|-------------|
| Studies | `data/studies.csv` | 1 | Study metadata with 16 fields including assessment ratings |
| Entities | `data/entities.csv` | 7 | Organizations referenced in the study |
| Technologies | `data/technologies.csv` | 8 | Storage technologies analyzed |
| Observations | `data/observations.csv` | 31 | Structured observations extracted from the study |
| Codes | `data/codes.csv` | 18 | Code definitions for observation types, confidence levels, and methodologies |

### Observation Type Breakdown

| Type | Count | Description |
|------|-------|-------------|
| technology-assessment | 7 | Storage technology evaluations (SAN, NAS, FC/SCSI, midline, D2D, tape, ILM software) |
| framework-factor | 6 | Six-step ILM adoption recipe |
| actual-outcome | 5 | Post-study validated outcomes (ILM maturity, cloud tiers, tape persistence, automation, midline dominance) |
| viability-prediction | 4 | Forward-looking predictions about ILM, midline, D2D, and automation |
| market-data | 4 | Storage growth, cost ratios, admin reduction, data composition |
| strategy-classification | 3 | Four-pool model, three-axis classification, ILM definition |
| expert-opinion | 2 | Compliance warning and adoption urgency |

## File Structure

```
computerworld-ilm-article-ce11c2/
  README.md                    # This file
  datapackage.json             # Frictionless Data Package descriptor
  data/
    studies.csv                # Study metadata (1 row, 16 fields)
    entities.csv               # Referenced entities (7 rows, 9 fields)
    technologies.csv           # Referenced technologies (8 rows, 9 fields)
    observations.csv           # Extracted observations (31 rows, 12 fields)
    codes.csv                  # Code definitions (18 rows, 4 fields)
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

# Find the six-step framework
framework = [r for r in observations if r["observation_type"] == "framework-factor"]
print(f"\nSix-Step ILM Recipe:")
for f_obs in framework:
    print(f"  {f_obs['metric_name']}: {f_obs['metric_value'][:80]}...")

# Find prediction-outcome pairs
predictions = [r for r in observations if r["observation_type"] == "viability-prediction"]
outcomes = [r for r in observations if r["observation_type"] == "actual-outcome"]
print(f"\nPredictions: {len(predictions)}, Outcomes: {len(outcomes)}")
```

## Validation

Run the validation script to check data package integrity:

```bash
cd computerworld-ilm-article-ce11c2
python scripts/demo_analysis.py
```

## Key Findings

1. **Six-step ILM recipe**: Centralize storage, create pools on three axes, create lifecycle policies, populate apps on pools, drive economies of scale, implement intelligent ILM
2. **Four-pool storage model**: Online dynamic (FC/SCSI), midline (25% cost), nearline buffered (D2D backup), offline (tape DR)
3. **45% annual storage growth**: Driving massive swing toward midline/capacity tier storage
4. **ILM software timeline**: Cross-application management software predicted to mature circa 2008-2010
5. **80% admin reduction**: Expected when ILM policy management software reaches maturity
6. **Litigation liability**: Offline backup tapes represent enormous legal exposure

## Prescience Highlights

The article's predictions proved remarkably accurate:
- **ILM maturity timeline**: Cross-application storage management did mature by 2008-2010 (EMC, IBM, Symantec delivered platforms)
- **Midline dominance**: SATA/NL-SAS/object storage became the dominant enterprise storage by volume; flash replaced FC/SCSI for performance
- **Four-pool model validated by cloud**: AWS S3 tiers (Standard/Infrequent/Glacier/Deep Archive) map directly to the four-pool model
- **Automation impact**: Software-defined storage and cloud managed services increased TB-per-admin ratios by orders of magnitude
- **Tape persists**: Tape retained niche for cold storage and compliance despite disk-to-disk backup dominance

## Citation

> Kastner, Peter S. "Waiting for ILM?" Computerworld, July 29, 2004.

## License

CC-BY-4.0 -- Creative Commons Attribution 4.0 International

---

*Generated by Archival Ingest Skill v13 on 2026-03-16*
