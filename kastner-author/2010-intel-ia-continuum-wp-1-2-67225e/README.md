# Intel's IA Continuum Strategy Anticipates a Much Broader Computing Market

**Frictionless Data Package** for an Aberdeen Group white paper by Peter S. Kastner (circa February 2010).

| Field | Value |
|-------|-------|
| Study ID | `2010-intel-ia-continuum-wp-1-2-67225e` |
| Author | Peter S. Kastner |
| Date | 2010-02-01 |
| Type | white-paper |
| Domain | semiconductor-strategy |
| License | CC-BY-4.0 |

## Overview

This data package captures structured observations from a white paper analyzing Intel's "IA Continuum" strategy for the 2010s decade. The paper examines how Intel planned to expand its IA (Intel Architecture) instruction set across the full computing spectrum -- from Atom-powered smartphones and consumer electronics to Xeon-based datacenter and HPC systems. The analysis covers Intel's product roadmap (Atom, Core i3/i5/i7, Xeon, Itanium), software strategy (Moblin/MeeGo, Wind River), R&D projects (Larrabee, Terascale), and market challenges.

## Assessment Ratings

| Dimension | Rating | Summary |
|-----------|--------|---------|
| **Importance** | high | Comprehensive analysis of Intel's decade-defining IA Continuum strategy at a critical inflection point |
| **Relevance** | high | Intel's datacenter/server dominance proved lasting; continuum concept anticipated IoT and edge computing |
| **Prescience** | medium | Server/datacenter predictions highly accurate; mobile/smartphone predictions failed as ARM dominated |

## Package Contents

```
2010-intel-ia-continuum-wp-1-2-67225e/
  README.md                    This file
  datapackage.json             Frictionless Data Package descriptor
  data/
    studies.csv                Study metadata (1 row, 16 columns)
    entities.csv               17 organizations referenced in the study
    technologies.csv           18 technologies discussed
    observations.csv           50 coded observations, predictions, and outcomes
    codes.csv                  18 code definitions
  schema/
    schema_org.json            Schema.org JSON-LD metadata
  source/
    original_text.md           Full text of lines 1-122 with metadata appendix
  scripts/
    demo_analysis.py           Validation and analysis script
```

## Key Entities

Intel, AMD, NVIDIA, ARM Holdings, Nokia, Apple, Microsoft, Salesforce, TSMC, Aberdeen Group, Dell, Acer, HP, Lenovo, Google, Wind River, IBM

## Key Technologies

Atom, Core i3/i5/i7, Xeon, Itanium, Moblin, MeeGo, Wi-Fi, PCI Express, Larrabee, Terascale, Nehalem-EX, Westmere, vPro, SSD, InfiniBand, Cloud Computing

## Validation

Run the validation script:

```bash
cd 2010-intel-ia-continuum-wp-1-2-67225e
python3 scripts/demo_analysis.py
```

## Hindsight Notes

Key predictions and their outcomes:

- **Datacenter/Server (accurate):** Intel maintained 90%+ server CPU market share through most of the 2010s. Server processor volumes more than doubled as predicted.
- **Cloud Computing (accurate):** Became the dominant IT paradigm, far exceeding 2010 expectations.
- **SSD Adoption (accurate):** Rapid datacenter adoption occurred as predicted by mid-decade.
- **Smartphone/Atom (failed):** Intel Atom never gained meaningful smartphone market share. ARM architecture dominated mobile entirely. Intel cancelled mobile Atom in 2016.
- **Larrabee (cancelled, concept validated):** Never shipped as a product. Technology evolved into Xeon Phi. GPU computing became massive market but NVIDIA dominated with CUDA.
- **MeeGo/Moblin (failed):** Only one phone (Nokia N9) shipped. Nokia abandoned MeeGo for Windows Phone in 2011. Platform forked into Tizen and Sailfish OS.
- **Wind River:** Intel sold Wind River to TPG Capital in 2018 after 9 years of ownership.
