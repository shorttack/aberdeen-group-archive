#!/usr/bin/env python3
"""
Archival Ingest Skill v16 — Phase 2 Assembler & Utilities

Handles all deterministic, zero-credit operations:
  - codes.csv generation (standard + study-specific codes)
  - datapackage.json generation
  - schema_org.json generation
  - README.md generation
  - demo_analysis.py template copy
  - source/original_text.md assembly (raw text + CSV metadata appendix)
  - Cross-study entity/technology reuse cache
  - Incremental web verification cache
  - Batch quality checks
  - Deferred field backfill

Usage:
  python scripts/assembler.py assemble <study_dir> [--raw-text-file <path>]
  python scripts/assembler.py validate <study_dir> [<study_dir2> ...]
  python scripts/assembler.py cache-init <output_dir>
  python scripts/assembler.py cache-lookup <output_dir> --entities <entity_ids_csv>
  python scripts/assembler.py cache-update <output_dir> --results <results_json>
  python scripts/assembler.py backfill <output_dir> --entity-results <json> --tech-results <json> --pred-results <json>
"""

import csv
import json
import os
import sys
from collections import Counter
from datetime import date, datetime
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
# Standard codes table — hardcoded, never changes per study
# ─────────────────────────────────────────────────────────────────────────────

STANDARD_CODES = [
    {"code_id": "strategy-classification", "code_type": "observation_type", "label": "Strategy Classification", "definition": "Categorization of an entity's business strategy"},
    {"code_id": "viability-prediction", "code_type": "observation_type", "label": "Viability Prediction", "definition": "Expert prediction of entity's long-term survival"},
    {"code_id": "actual-outcome", "code_type": "observation_type", "label": "Actual Outcome", "definition": "Verified historical outcome for an entity"},
    {"code_id": "technology-assessment", "code_type": "observation_type", "label": "Technology Assessment", "definition": "Evaluation of a technology's maturity or fitness"},
    {"code_id": "benchmark-result", "code_type": "observation_type", "label": "Benchmark Result", "definition": "Quantitative comparison against peers or standards"},
    {"code_id": "framework-factor", "code_type": "observation_type", "label": "Framework Factor", "definition": "One component of a multi-factor analytical framework"},
    {"code_id": "market-data", "code_type": "observation_type", "label": "Market Data", "definition": "Quantitative market statistic"},
    {"code_id": "expert-opinion", "code_type": "observation_type", "label": "Expert Opinion", "definition": "Qualitative professional judgment"},
    {"code_id": "personal-recollection", "code_type": "observation_type", "label": "Personal Recollection", "definition": "First-person memory or anecdote from Kastner"},
    {"code_id": "ai-exchange", "code_type": "observation_type", "label": "AI Exchange", "definition": "A question posed by Kastner and the AI response extracted as a structured observation"},
    {"code_id": "topic-insight", "code_type": "observation_type", "label": "Topic Insight", "definition": "An analytical claim or framework point within a technology topic deep-dive"},
    {"code_id": "industry-analysis", "code_type": "methodology", "label": "Industry Analysis", "definition": "Systematic analysis of industry structure and dynamics"},
    {"code_id": "competitive-profiling", "code_type": "methodology", "label": "Competitive Profiling", "definition": "Detailed comparison of competing entities"},
    {"code_id": "benchmarking", "code_type": "methodology", "label": "Benchmarking", "definition": "Comparison against industry standards or peers"},
    {"code_id": "field-research", "code_type": "methodology", "label": "Field Research", "definition": "Primary data collection via interviews or surveys"},
    {"code_id": "document-review", "code_type": "methodology", "label": "Document Review", "definition": "Analysis of existing documents and records"},
    {"code_id": "statistical-analysis", "code_type": "methodology", "label": "Statistical Analysis", "definition": "Quantitative data analysis with statistical methods"},
    {"code_id": "oral-history", "code_type": "methodology", "label": "Oral History", "definition": "First-person spoken or written recollection of events"},
    {"code_id": "ai-dialog", "code_type": "methodology", "label": "AI Dialog", "definition": "Question-and-answer exchange between a human and an AI system"},
    {"code_id": "high", "code_type": "confidence", "label": "High Confidence", "definition": "Strong evidentiary basis; multiple corroborating sources"},
    {"code_id": "medium", "code_type": "confidence", "label": "Medium Confidence", "definition": "Reasonable basis but limited corroboration"},
    {"code_id": "low", "code_type": "confidence", "label": "Low Confidence", "definition": "Directional judgment with limited evidence"},
    {"code_id": "verified", "code_type": "confidence", "label": "Verified", "definition": "Confirmed by subsequent events or independent sources"},
]

# ─────────────────────────────────────────────────────────────────────────────
# Fixed schema definitions for datapackage.json
# ─────────────────────────────────────────────────────────────────────────────

RESOURCE_SCHEMAS = {
    "studies": [
        {"name": "study_id", "type": "string"}, {"name": "title", "type": "string"},
        {"name": "author", "type": "string"}, {"name": "date", "type": "date"},
        {"name": "type", "type": "string"}, {"name": "subject_domain", "type": "string"},
        {"name": "methodology", "type": "string"}, {"name": "source_file", "type": "string"},
        {"name": "abstract", "type": "string"}, {"name": "license", "type": "string"},
        {"name": "importance", "type": "string"}, {"name": "importance_rationale", "type": "string"},
        {"name": "relevance", "type": "string"}, {"name": "relevance_rationale", "type": "string"},
        {"name": "prescience", "type": "string"}, {"name": "prescience_rationale", "type": "string"},
    ],
    "entities": [
        {"name": "entity_id", "type": "string"}, {"name": "entity_name", "type": "string"},
        {"name": "entity_type", "type": "string"}, {"name": "sector", "type": "string"},
        {"name": "status", "type": "string"}, {"name": "successor", "type": "string"},
        {"name": "years_active", "type": "string"}, {"name": "study_id", "type": "string"},
        {"name": "notes", "type": "string"},
    ],
    "technologies": [
        {"name": "tech_id", "type": "string"}, {"name": "tech_name", "type": "string"},
        {"name": "category", "type": "string"}, {"name": "vendor", "type": "string"},
        {"name": "era", "type": "string"}, {"name": "lifecycle_at_study", "type": "string"},
        {"name": "lifecycle_current", "type": "string"}, {"name": "study_id", "type": "string"},
        {"name": "notes", "type": "string"},
    ],
    "observations": [
        {"name": "obs_id", "type": "string"}, {"name": "study_id", "type": "string"},
        {"name": "entity_id", "type": "string"}, {"name": "tech_id", "type": "string"},
        {"name": "observation_type", "type": "string"}, {"name": "year_observed", "type": "year"},
        {"name": "metric_name", "type": "string"}, {"name": "metric_value", "type": "string"},
        {"name": "confidence", "type": "string"}, {"name": "methodology_code", "type": "string"},
        {"name": "source_page", "type": "string"}, {"name": "notes", "type": "string"},
    ],
    "codes": [
        {"name": "code_id", "type": "string"}, {"name": "code_type", "type": "string"},
        {"name": "label", "type": "string"}, {"name": "definition", "type": "string"},
    ],
}

# ─────────────────────────────────────────────────────────────────────────────
# demo_analysis.py template — identical across all studies
# ─────────────────────────────────────────────────────────────────────────────

DEMO_TEMPLATE = '''#!/usr/bin/env python3
"""Validation and summary script for a single Frictionless Data Package."""
import csv, os, sys
from collections import Counter

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    data = os.path.join(base, "..", "data")

    def load(name):
        with open(os.path.join(data, name)) as f:
            return list(csv.DictReader(f))

    studies = load("studies.csv")
    entities = load("entities.csv")
    techs = load("technologies.csv")
    obs = load("observations.csv")
    codes = load("codes.csv")

    print(f"Study: {studies[0]['title']}")
    print(f"Author: {studies[0]['author']}")
    print(f"Date: {studies[0]['date']}")
    print(f"Entities: {len(entities)}, Technologies: {len(techs)}, Observations: {len(obs)}")

    ent_ids = {e["entity_id"] for e in entities}
    tech_ids = {t["tech_id"] for t in techs}
    code_ids = {c["code_id"] for c in codes}
    errors = []
    for o in obs:
        if o["entity_id"] and o["entity_id"] not in ent_ids:
            errors.append(f"Missing entity: {o['entity_id']} in {o['obs_id']}")
        if o["tech_id"] and o["tech_id"] not in tech_ids:
            errors.append(f"Missing tech: {o['tech_id']} in {o['obs_id']}")
        if o["observation_type"] not in code_ids:
            errors.append(f"Missing code: {o['observation_type']} in {o['obs_id']}")

    preds = [o for o in obs if o["observation_type"] == "viability-prediction"]
    actuals = [o for o in obs if o["observation_type"] == "actual-outcome"]
    if preds:
        verified = [a for a in actuals if a["confidence"] == "verified"]
        print(f"Predictions: {len(preds)}, Verified outcomes: {len(verified)}")
        if verified:
            print(f"Prediction accuracy: {len(verified)/len(preds)*100:.0f}%")

    if errors:
        print(f"VALIDATION ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
    else:
        print("Validation: PASSED")

if __name__ == "__main__":
    main()
'''

# ─────────────────────────────────────────────────────────────────────────────
# Helper: read a CSV into list of dicts
# ─────────────────────────────────────────────────────────────────────────────

def _load_csv(path):
    if not Path(path).exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _write_csv(path, rows, fieldnames=None):
    if not rows:
        return
    fieldnames = fieldnames or list(rows[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 2: Per-Study Assembly (zero AI credits)
# ═══════════════════════════════════════════════════════════════════════════════

def build_codes(study_dir):
    """Step 7: Write codes.csv from standard table + study-specific codes."""
    obs_path = Path(study_dir) / "data" / "observations.csv"
    codes = list(STANDARD_CODES)
    known_ids = {c["code_id"] for c in codes}
    if obs_path.exists():
        for row in _load_csv(obs_path):
            for field in ("observation_type", "methodology_code"):
                val = row.get(field, "")
                if val and val not in known_ids:
                    codes.append({
                        "code_id": val,
                        "code_type": field.replace("_code", ""),
                        "label": val.replace("-", " ").title(),
                        "definition": f"Study-specific code: {val}",
                    })
                    known_ids.add(val)
    _write_csv(Path(study_dir) / "data" / "codes.csv", codes,
               ["code_id", "code_type", "label", "definition"])


def build_datapackage(study_dir):
    """Step 8: Generate datapackage.json from studies.csv row 1."""
    meta = _load_csv(Path(study_dir) / "data" / "studies.csv")[0]
    pkg = {
        "name": meta["study_id"],
        "title": meta["title"],
        "description": meta["abstract"],
        "version": "1.0.0",
        "created": date.today().isoformat(),
        "licenses": [{"name": "CC-BY-4.0", "path": "https://creativecommons.org/licenses/by/4.0/"}],
        "contributors": [{"title": meta["author"], "role": "author"}],
        "resources": [
            {"name": k, "path": f"data/{k}.csv", "schema": {"fields": v}}
            for k, v in RESOURCE_SCHEMAS.items()
        ],
    }
    with open(Path(study_dir) / "datapackage.json", "w") as f:
        json.dump(pkg, f, indent=2)


def build_schema_org(study_dir):
    """Step 9: Generate schema_org.json."""
    meta = _load_csv(Path(study_dir) / "data" / "studies.csv")[0]
    schema = {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": meta["title"],
        "description": meta["abstract"],
        "creator": {"@type": "Person", "name": meta["author"]},
        "datePublished": meta["date"],
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "distribution": [
            {"@type": "DataDownload", "encodingFormat": "text/csv",
             "contentUrl": "data/observations.csv"}
        ],
        "variableMeasured": [
            "strategy-classification", "viability-prediction",
            "technology-assessment", "benchmark-result",
        ],
    }
    schema_dir = Path(study_dir) / "schema"
    schema_dir.mkdir(parents=True, exist_ok=True)
    with open(schema_dir / "schema_org.json", "w") as f:
        json.dump(schema, f, indent=2)


def build_readme(study_dir):
    """Step 10: Generate README.md from CSV data."""
    d = Path(study_dir) / "data"
    meta = _load_csv(d / "studies.csv")[0]
    ent_count = len(_load_csv(d / "entities.csv"))
    tech_count = len(_load_csv(d / "technologies.csv"))
    obs_count = len(_load_csv(d / "observations.csv"))
    code_count = len(_load_csv(d / "codes.csv"))
    readme = f"""# {meta['title']}

| Field | Value |
|-------|-------|
| Author | {meta['author']} |
| Date | {meta['date']} |
| Type | {meta['type']} |
| Domain | {meta['subject_domain']} |
| License | {meta['license']} |

## Abstract

{meta['abstract']}

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | {ent_count} |
| technologies.csv | {tech_count} |
| observations.csv | {obs_count} |
| codes.csv | {code_count} |

## Load with Python

```python
import pandas as pd
studies = pd.read_csv('data/studies.csv')
observations = pd.read_csv('data/observations.csv')
```

## Validate

```bash
frictionless validate datapackage.json
```

## Citation

{meta['author']} ({meta['date'][:4]}). {meta['title']}.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

{meta['methodology']}
"""
    with open(Path(study_dir) / "README.md", "w") as f:
        f.write(readme)


def write_demo_analysis(study_dir):
    """Step 11: Copy the demo_analysis.py template."""
    scripts_dir = Path(study_dir) / "scripts"
    scripts_dir.mkdir(parents=True, exist_ok=True)
    with open(scripts_dir / "demo_analysis.py", "w") as f:
        f.write(DEMO_TEMPLATE)


def build_original_text(study_dir, raw_text):
    """Step 12: Assemble original_text.md from raw text + CSV metadata."""
    d = Path(study_dir) / "data"
    meta = _load_csv(d / "studies.csv")[0]
    entities = _load_csv(d / "entities.csv")
    techs = _load_csv(d / "technologies.csv")
    obs = _load_csv(d / "observations.csv")

    # Entity table
    ent_rows = "\n".join(
        f"| {e['entity_name']} | {e['entity_type']} | {e['status']} | {e['successor']} |"
        for e in entities
    )
    # Technology table
    tech_rows = "\n".join(
        f"| {t['tech_name']} | {t['category']} | {t['vendor']} | {t['lifecycle_at_study']} | {t['lifecycle_current']} |"
        for t in techs
    )

    # Prescience detail
    preds = [o for o in obs if o["observation_type"] == "viability-prediction"]
    actuals = [o for o in obs if o["observation_type"] == "actual-outcome"]
    if preds:
        prescience_md = ""
        for i, p in enumerate(preds, 1):
            prescience_md += f"\n**Prediction {i}:** {p['metric_name']}\n"
            prescience_md += f"- **Claimed:** {p['metric_value']}\n"
            prescience_md += f"- **Year:** {p['year_observed']}\n"
            prescience_md += f"- **Confidence at time:** {p['confidence']}\n"
            match = next(
                (a for a in actuals
                 if (a.get("entity_id") and a["entity_id"] == p.get("entity_id"))
                 or (a.get("tech_id") and a["tech_id"] == p.get("tech_id"))),
                None,
            )
            if match:
                prescience_md += f"\n**Actual Outcome {i}:** {match['metric_name']}\n"
                prescience_md += f"- **Result:** {match['metric_value']}\n"
                prescience_md += f"- **Confidence:** {match['confidence']}\n"
                prescience_md += f"- **Notes:** {match['notes']}\n"
    else:
        prescience_md = "This study did not make forward-looking claims."

    # Observation breakdown
    type_counts = Counter(o["observation_type"] for o in obs)
    breakdown = ", ".join(f"{k}: {v}" for k, v in type_counts.most_common())

    doc = f"""# {meta['title']}

> Archived from: {meta['source_file']}
> Original publication date: {meta['date']}
> Author: {meta['author']}

---

## Original Document Text

{raw_text}

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | {meta['study_id']} |
| title | {meta['title']} |
| author | {meta['author']} |
| date | {meta['date']} |
| type | {meta['type']} |
| subject_domain | {meta['subject_domain']} |
| methodology | {meta['methodology']} |
| source_file | {meta['source_file']} |
| license | {meta['license']} |

### Abstract

{meta['abstract']}

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | {meta['importance']} | {meta['importance_rationale']} |
| **Relevance** | {meta['relevance']} | {meta['relevance_rationale']} |
| **Prescience** | {meta['prescience']} | {meta['prescience_rationale']} |

### Prescience Detail

{prescience_md}

### Entities Referenced ({len(entities)})

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
{ent_rows}

### Technologies Referenced ({len(techs)})

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
{tech_rows}

### Observation Summary

- Total observations: {len(obs)}
- By type: {breakdown}
"""
    source_dir = Path(study_dir) / "source"
    source_dir.mkdir(parents=True, exist_ok=True)
    with open(source_dir / "original_text.md", "w") as f:
        f.write(doc)


def assemble(study_dir, raw_text_file=None):
    """Run all Phase 2 steps for a single study. Zero AI credits."""
    raw_text = ""
    if raw_text_file and Path(raw_text_file).exists():
        raw_text = Path(raw_text_file).read_text(encoding="utf-8", errors="replace")
    elif (Path(study_dir) / "source" / "_raw_text.txt").exists():
        raw_text = (Path(study_dir) / "source" / "_raw_text.txt").read_text(
            encoding="utf-8", errors="replace"
        )

    build_codes(study_dir)
    build_datapackage(study_dir)
    build_schema_org(study_dir)
    build_readme(study_dir)
    write_demo_analysis(study_dir)
    build_original_text(study_dir, raw_text)
    print(f"Phase 2 assembly complete: {study_dir}")


# ═══════════════════════════════════════════════════════════════════════════════
# BATCH QUALITY CHECKS (per-batch, not per-study)
# ═══════════════════════════════════════════════════════════════════════════════

def validate(study_dirs):
    """Run referential integrity and completeness checks across studies."""
    errors = []
    for study_dir in study_dirs:
        d = Path(study_dir) / "data"
        if not d.exists():
            errors.append(f"{study_dir}: data/ directory missing")
            continue

        # Tolerate missing CSVs: report and skip (some legacy studies lack codes.csv)
        for required in ("entities.csv", "technologies.csv", "observations.csv", "studies.csv"):
            if not (d / required).exists():
                errors.append(f"{study_dir}: required file '{required}' missing")
        ent_ids = {r.get("entity_id", "") for r in _load_csv(d / "entities.csv")}
        tech_ids = {r.get("tech_id", "") for r in _load_csv(d / "technologies.csv")}
        codes_rows = _load_csv(d / "codes.csv")
        code_ids = {r.get("code_id", "") for r in codes_rows}
        codes_present = bool(codes_rows)

        for row in _load_csv(d / "observations.csv"):
            if row.get("entity_id") and row["entity_id"] not in ent_ids:
                errors.append(f"{study_dir}: Missing entity {row['entity_id']} in {row.get('obs_id','')}")
            if row.get("tech_id") and row["tech_id"] not in tech_ids:
                errors.append(f"{study_dir}: Missing tech {row['tech_id']} in {row.get('obs_id','')}")
            if codes_present and row.get("observation_type") not in code_ids:
                errors.append(f"{study_dir}: Missing code {row['observation_type']} in {row.get('obs_id','')}")

        meta = _load_csv(d / "studies.csv")
        if meta:
            for field in ("study_id", "title", "author", "date", "type"):
                if not meta[0].get(field):
                    errors.append(f"{study_dir}: Empty required field '{field}'")

    if errors:
        print(f"VALIDATION: {len(errors)} error(s) found")
        for e in errors:
            print(f"  [REVIEW] {e}")
    else:
        print(f"VALIDATION: {len(study_dirs)} studies — all PASSED")
    return errors


# ═══════════════════════════════════════════════════════════════════════════════
# T3-B: CROSS-STUDY ENTITY / TECHNOLOGY REUSE CACHE
# ═══════════════════════════════════════════════════════════════════════════════

def cache_init(output_dir):
    """Initialize or load the known-entity and known-technology caches."""
    output = Path(output_dir)
    ent_cache = output / "_known_entities.csv"
    tech_cache = output / "_known_technologies.csv"

    if not ent_cache.exists():
        _write_csv(ent_cache, [], ["entity_id", "entity_name", "entity_type",
                                    "sector", "status", "successor", "years_active",
                                    "notes", "source_studies"])
        print(f"Created: {ent_cache}")
    else:
        count = len(_load_csv(ent_cache))
        print(f"Loaded: {ent_cache} ({count} known entities)")

    if not tech_cache.exists():
        _write_csv(tech_cache, [], ["tech_id", "tech_name", "category", "vendor",
                                     "era", "lifecycle_at_study", "lifecycle_current",
                                     "notes", "source_studies"])
        print(f"Created: {tech_cache}")
    else:
        count = len(_load_csv(tech_cache))
        print(f"Loaded: {tech_cache} ({count} known technologies)")


def cache_lookup(output_dir, entity_ids=None, tech_ids=None):
    """Look up known entities/technologies. Returns JSON dict of matches."""
    output = Path(output_dir)
    result = {"known_entities": {}, "known_technologies": {}}

    ent_cache = output / "_known_entities.csv"
    if ent_cache.exists() and entity_ids:
        for row in _load_csv(ent_cache):
            if row["entity_id"] in entity_ids:
                result["known_entities"][row["entity_id"]] = row

    tech_cache = output / "_known_technologies.csv"
    if tech_cache.exists() and tech_ids:
        for row in _load_csv(tech_cache):
            if row["tech_id"] in tech_ids:
                result["known_technologies"][row["tech_id"]] = row

    print(json.dumps(result, indent=2))
    return result


def cache_update_from_study(output_dir, study_dir):
    """Merge a study's entities and technologies into the reuse cache."""
    output = Path(output_dir)
    d = Path(study_dir) / "data"

    # Update entity cache
    ent_cache_path = output / "_known_entities.csv"
    known = {}
    if ent_cache_path.exists():
        for row in _load_csv(ent_cache_path):
            known[row["entity_id"]] = row

    study_id = _load_csv(d / "studies.csv")[0]["study_id"]
    for row in _load_csv(d / "entities.csv"):
        eid = row["entity_id"]
        if eid in known:
            # Append study_id to source_studies
            sources = known[eid].get("source_studies", "")
            if study_id not in sources:
                known[eid]["source_studies"] = f"{sources},{study_id}".strip(",")
            # Update status if we have a better value
            if row["status"] not in ("[DEFERRED]", "unknown", "") and known[eid]["status"] in ("[DEFERRED]", "unknown", ""):
                known[eid]["status"] = row["status"]
                known[eid]["successor"] = row.get("successor", "")
        else:
            known[eid] = {
                "entity_id": eid,
                "entity_name": row["entity_name"],
                "entity_type": row["entity_type"],
                "sector": row["sector"],
                "status": row["status"],
                "successor": row.get("successor", ""),
                "years_active": row.get("years_active", ""),
                "notes": row.get("notes", ""),
                "source_studies": study_id,
            }

    _write_csv(ent_cache_path, list(known.values()),
               ["entity_id", "entity_name", "entity_type", "sector", "status",
                "successor", "years_active", "notes", "source_studies"])

    # Update technology cache
    tech_cache_path = output / "_known_technologies.csv"
    known_tech = {}
    if tech_cache_path.exists():
        for row in _load_csv(tech_cache_path):
            known_tech[row["tech_id"]] = row

    for row in _load_csv(d / "technologies.csv"):
        tid = row["tech_id"]
        if tid in known_tech:
            sources = known_tech[tid].get("source_studies", "")
            if study_id not in sources:
                known_tech[tid]["source_studies"] = f"{sources},{study_id}".strip(",")
            if row.get("lifecycle_current") not in ("[DEFERRED]", "unknown", "") \
               and known_tech[tid].get("lifecycle_current") in ("[DEFERRED]", "unknown", ""):
                known_tech[tid]["lifecycle_current"] = row["lifecycle_current"]
        else:
            known_tech[tid] = {
                "tech_id": tid,
                "tech_name": row["tech_name"],
                "category": row["category"],
                "vendor": row["vendor"],
                "era": row.get("era", ""),
                "lifecycle_at_study": row.get("lifecycle_at_study", ""),
                "lifecycle_current": row.get("lifecycle_current", ""),
                "notes": row.get("notes", ""),
                "source_studies": study_id,
            }

    _write_csv(tech_cache_path, list(known_tech.values()),
               ["tech_id", "tech_name", "category", "vendor", "era",
                "lifecycle_at_study", "lifecycle_current", "notes", "source_studies"])

    print(f"Cache updated from {study_dir}: {len(known)} entities, {len(known_tech)} technologies")


# ═══════════════════════════════════════════════════════════════════════════════
# T3-C: INCREMENTAL WEB VERIFICATION CACHE
# ═══════════════════════════════════════════════════════════════════════════════

def web_cache_path(output_dir):
    return Path(output_dir) / "_web_cache.json"


def web_cache_load(output_dir):
    """Load the web verification cache, or create empty."""
    p = web_cache_path(output_dir)
    if p.exists():
        with open(p) as f:
            cache = json.load(f)
        print(f"Web cache loaded: {len(cache.get('entities', {}))} entities, "
              f"{len(cache.get('technologies', {}))} technologies, "
              f"{len(cache.get('predictions', {}))} predictions verified")
        return cache
    return {"entities": {}, "technologies": {}, "predictions": {},
            "last_updated": None}


def web_cache_save(output_dir, cache):
    """Persist the web verification cache."""
    cache["last_updated"] = datetime.utcnow().isoformat()
    with open(web_cache_path(output_dir), "w") as f:
        json.dump(cache, f, indent=2)
    print(f"Web cache saved: {web_cache_path(output_dir)}")


def web_cache_needs_verification(output_dir, entity_ids=None, tech_ids=None, pred_ids=None):
    """Return lists of IDs that are NOT already in the cache."""
    cache = web_cache_load(output_dir)
    result = {
        "entities_needed": [eid for eid in (entity_ids or []) if eid not in cache["entities"]],
        "technologies_needed": [tid for tid in (tech_ids or []) if tid not in cache["technologies"]],
        "predictions_needed": [pid for pid in (pred_ids or []) if pid not in cache["predictions"]],
    }
    total = sum(len(v) for v in result.values())
    cached = (len(entity_ids or []) + len(tech_ids or []) + len(pred_ids or [])) - total
    print(f"Cache hits: {cached}, Needs verification: {total}")
    print(json.dumps(result, indent=2))
    return result


def web_cache_store(output_dir, entity_results=None, tech_results=None, pred_results=None):
    """Store web verification results into the cache."""
    cache = web_cache_load(output_dir)
    if entity_results:
        cache["entities"].update(entity_results)
    if tech_results:
        cache["technologies"].update(tech_results)
    if pred_results:
        cache["predictions"].update(pred_results)
    web_cache_save(output_dir, cache)


# ═══════════════════════════════════════════════════════════════════════════════
# BACKFILL: Apply deferred web results to all study CSVs
# ═══════════════════════════════════════════════════════════════════════════════

def backfill(output_dir, entity_results=None, tech_results=None, pred_results=None):
    """Update [DEFERRED] fields across all study directories."""
    entity_results = entity_results or {}
    tech_results = tech_results or {}
    pred_results = pred_results or {}
    updated_studies = 0

    for study_dir in sorted(Path(output_dir).iterdir()):
        if not study_dir.is_dir() or study_dir.name.startswith("_"):
            continue
        d = study_dir / "data"
        if not d.exists():
            continue

        changed = False

        # Backfill entities
        ent_path = d / "entities.csv"
        if ent_path.exists():
            rows = _load_csv(ent_path)
            for row in rows:
                if row["status"] == "[DEFERRED]" and row["entity_id"] in entity_results:
                    r = entity_results[row["entity_id"]]
                    row["status"] = r.get("status", "unknown")
                    row["successor"] = r.get("successor", "")
                    changed = True
            if changed:
                _write_csv(ent_path, rows)

        # Backfill technologies
        tech_path = d / "technologies.csv"
        if tech_path.exists():
            rows = _load_csv(tech_path)
            for row in rows:
                if row.get("lifecycle_current") == "[DEFERRED]" and row["tech_id"] in tech_results:
                    row["lifecycle_current"] = tech_results[row["tech_id"]]
                    changed = True
            if changed:
                _write_csv(tech_path, rows)

        # Backfill prediction outcomes
        obs_path = d / "observations.csv"
        if obs_path.exists():
            rows = _load_csv(obs_path)
            for row in rows:
                if (row["observation_type"] == "actual-outcome"
                        and row["confidence"] == "[DEFERRED]"
                        and row["obs_id"] in pred_results):
                    r = pred_results[row["obs_id"]]
                    row["metric_value"] = r.get("outcome", "[UNVERIFIED]")
                    row["confidence"] = r.get("confidence", "low")
                    row["notes"] = r.get("notes", "")
                    changed = True
            if changed:
                _write_csv(obs_path, rows)

        # Clean up remaining [DEFERRED] → unknown
        if ent_path.exists():
            rows = _load_csv(ent_path)
            for row in rows:
                if row["status"] == "[DEFERRED]":
                    row["status"] = "unknown"
                    row["notes"] = (row.get("notes", "") + " [REVIEW]").strip()
            _write_csv(ent_path, rows)

        if changed:
            updated_studies += 1
            # Regenerate original_text.md with backfilled data
            raw_path = study_dir / "source" / "_raw_text.txt"
            raw_text = raw_path.read_text(encoding="utf-8", errors="replace") if raw_path.exists() else ""
            build_original_text(str(study_dir), raw_text)

    print(f"Backfill complete: {updated_studies} studies updated")


# ═══════════════════════════════════════════════════════════════════════════════
# CLI DISPATCHER
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "assemble":
        study_dir = sys.argv[2]
        raw_text_file = None
        if "--raw-text-file" in sys.argv:
            idx = sys.argv.index("--raw-text-file")
            raw_text_file = sys.argv[idx + 1]
        assemble(study_dir, raw_text_file)

    elif cmd == "validate":
        study_dirs = sys.argv[2:]
        validate(study_dirs)

    elif cmd == "cache-init":
        cache_init(sys.argv[2])

    elif cmd == "cache-update":
        cache_update_from_study(sys.argv[2], sys.argv[3])

    elif cmd == "cache-lookup":
        output_dir = sys.argv[2]
        # Parse --entities and --techs flags
        entity_ids = set()
        tech_ids = set()
        if "--entities" in sys.argv:
            idx = sys.argv.index("--entities")
            entity_ids = set(sys.argv[idx + 1].split(","))
        if "--techs" in sys.argv:
            idx = sys.argv.index("--techs")
            tech_ids = set(sys.argv[idx + 1].split(","))
        cache_lookup(output_dir, entity_ids, tech_ids)

    elif cmd == "web-cache-init":
        cache = web_cache_load(sys.argv[2])
        web_cache_save(sys.argv[2], cache)

    elif cmd == "web-cache-check":
        output_dir = sys.argv[2]
        entity_ids = tech_ids = pred_ids = []
        if "--entities" in sys.argv:
            idx = sys.argv.index("--entities")
            entity_ids = sys.argv[idx + 1].split(",")
        if "--techs" in sys.argv:
            idx = sys.argv.index("--techs")
            tech_ids = sys.argv[idx + 1].split(",")
        if "--preds" in sys.argv:
            idx = sys.argv.index("--preds")
            pred_ids = sys.argv[idx + 1].split(",")
        web_cache_needs_verification(output_dir, entity_ids, tech_ids, pred_ids)

    elif cmd == "web-cache-store":
        output_dir = sys.argv[2]
        results_file = sys.argv[3]
        with open(results_file) as f:
            results = json.load(f)
        web_cache_store(output_dir,
                        results.get("entities"), results.get("technologies"),
                        results.get("predictions"))

    elif cmd == "backfill":
        output_dir = sys.argv[2]
        results_file = sys.argv[3]
        with open(results_file) as f:
            results = json.load(f)
        backfill(output_dir,
                 results.get("entities"), results.get("technologies"),
                 results.get("predictions"))

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
