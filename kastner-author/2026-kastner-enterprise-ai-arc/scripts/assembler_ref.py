#!/usr/bin/env python3
"""
Archival Ingest Skill v16 — Phase 2 Assembler & Utilities
"""

import csv
import json
import os
import sys
from collections import Counter
from datetime import date, datetime
from pathlib import Path

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
    {"code_id": "analytical-finding", "code_type": "observation_type", "label": "Analytical Finding", "definition": "Archive-mining result: a count, rate, or pattern finding"},
    {"code_id": "longitudinal-decomposition", "code_type": "observation_type", "label": "Longitudinal Decomposition", "definition": "Phase or period assignment in a single-entity longitudinal study"},
    {"code_id": "thematic-thread-decomposition", "code_type": "observation_type", "label": "Thematic Thread Decomposition", "definition": "Thread-level claim, population count, or named exemplar in a longitudinal study"},
    {"code_id": "industry-analysis", "code_type": "methodology", "label": "Industry Analysis", "definition": "Systematic analysis of industry structure and dynamics"},
    {"code_id": "competitive-profiling", "code_type": "methodology", "label": "Competitive Profiling", "definition": "Detailed comparison of competing entities"},
    {"code_id": "benchmarking", "code_type": "methodology", "label": "Benchmarking", "definition": "Comparison against industry standards or peers"},
    {"code_id": "field-research", "code_type": "methodology", "label": "Field Research", "definition": "Primary data collection via interviews or surveys"},
    {"code_id": "document-review", "code_type": "methodology", "label": "Document Review", "definition": "Analysis of existing documents and records"},
    {"code_id": "archive-mining", "code_type": "methodology", "label": "Archive Mining", "definition": "Extraction of patterns and statistics from the master CSV corpus"},
    {"code_id": "longitudinal-single-entity", "code_type": "methodology", "label": "Longitudinal Single-Entity", "definition": "Deep-dive study of one firm across all archive decades"},
    {"code_id": "thematic-thread-decomposition", "code_type": "methodology", "label": "Thematic Thread Decomposition", "definition": "Eleven-thread decomposition of entity coverage"},
    {"code_id": "prediction-vs-outcome-scorecard", "code_type": "methodology", "label": "Prediction vs Outcome Scorecard", "definition": "Tabulation of viability predictions against actual outcomes"},
    {"code_id": "oral-history", "code_type": "methodology", "label": "Oral History", "definition": "First-person spoken or written recollection of events"},
    {"code_id": "ai-dialog", "code_type": "methodology", "label": "AI Dialog", "definition": "Question-and-answer exchange between a human and an AI system"},
    {"code_id": "high", "code_type": "confidence", "label": "High Confidence", "definition": "Strong evidentiary basis; multiple corroborating sources"},
    {"code_id": "medium", "code_type": "confidence", "label": "Medium Confidence", "definition": "Reasonable basis but limited corroboration"},
    {"code_id": "low", "code_type": "confidence", "label": "Low Confidence", "definition": "Directional judgment with limited evidence"},
    {"code_id": "verified", "code_type": "confidence", "label": "Verified", "definition": "Confirmed by subsequent events or independent sources"},
    {"code_id": "refuted", "code_type": "confidence", "label": "Refuted", "definition": "Contradicted by subsequent events or independent sources"},
]

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

    print(f"Study: {studies[0][\'title\']}")
    print(f"Author: {studies[0][\'author\']}")
    print(f"Date: {studies[0][\'date\']}")
    print(f"Entities: {len(entities)}, Technologies: {len(techs)}, Observations: {len(obs)}")

    ent_ids = {e["entity_id"] for e in entities}
    tech_ids = {t["tech_id"] for t in techs}
    code_ids = {c["code_id"] for c in codes}
    errors = []
    for o in obs:
        if o["entity_id"] and o["entity_id"] not in ent_ids:
            errors.append(f"Missing entity: {o[\'entity_id\']} in {o[\'obs_id\']}")
        if o["tech_id"] and o["tech_id"] not in tech_ids:
            errors.append(f"Missing tech: {o[\'tech_id\']} in {o[\'obs_id\']}")
        if o["observation_type"] not in code_ids:
            errors.append(f"Missing code: {o[\'observation_type\']} in {o[\'obs_id\']}")

    if errors:
        print(f"VALIDATION ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
    else:
        print("Validation: PASSED")

if __name__ == "__main__":
    main()
'''

def _load_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def _write_csv(path, rows, fieldnames=None):
    if not rows:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", newline="", encoding="utf-8") as f:
            if fieldnames:
                w = csv.DictWriter(f, fieldnames=fieldnames)
                w.writeheader()
        return
    fieldnames = fieldnames or list(rows[0].keys())
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

def build_codes(study_dir):
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
    d = Path(study_dir) / "data"
    meta = _load_csv(d / "studies.csv")[0]
    ent_count = len(_load_csv(d / "entities.csv"))
    tech_count = len(_load_csv(d / "technologies.csv"))
    obs_count = len(_load_csv(d / "observations.csv"))
    code_count = len(_load_csv(d / "codes.csv"))
    readme = f"# {meta['title']}\n\n"
    readme += f"| Field | Value |\n|-------|-------|\n"
    readme += f"| Author | {meta['author']} |\n"
    readme += f"| Date | {meta['date']} |\n"
    readme += f"| Type | {meta['type']} |\n"
    readme += f"| Domain | {meta['subject_domain']} |\n"
    readme += f"| License | {meta['license']} |\n\n"
    readme += f"## Abstract\n\n{meta['abstract']}\n\n"
    readme += f"## Data Tables\n\n| Table | Rows |\n|-------|------|\n"
    readme += f"| studies.csv | 1 |\n| entities.csv | {ent_count} |\n"
    readme += f"| technologies.csv | {tech_count} |\n| observations.csv | {obs_count} |\n"
    readme += f"| codes.csv | {code_count} |\n\n"
    readme += f"## Load with Python\n\n```python\nimport pandas as pd\n"
    readme += f"studies = pd.read_csv('data/studies.csv')\n"
    readme += f"observations = pd.read_csv('data/observations.csv')\n```\n\n"
    readme += f"## Validate\n\n```bash\nfrictionless validate datapackage.json\n```\n\n"
    readme += f"## Citation\n\n{meta['author']} ({meta['date'][:4]}). {meta['title']}.\n"
    readme += f"Archived in Kastner Research Archive. DOI: [pending]\n\n"
    readme += f"## Methodology\n\n{meta['methodology']}\n"
    with open(Path(study_dir) / "README.md", "w") as f:
        f.write(readme)

def write_demo_analysis(study_dir):
    scripts_dir = Path(study_dir) / "scripts"
    scripts_dir.mkdir(parents=True, exist_ok=True)
    with open(scripts_dir / "demo_analysis.py", "w") as f:
        f.write(DEMO_TEMPLATE)

def build_original_text(study_dir, raw_text):
    d = Path(study_dir) / "data"
    meta = _load_csv(d / "studies.csv")[0]
    entities = _load_csv(d / "entities.csv")
    techs = _load_csv(d / "technologies.csv")
    obs = _load_csv(d / "observations.csv")

    ent_rows = "\n".join(
        f"| {e['entity_name']} | {e['entity_type']} | {e['status']} | {e['successor']} |"
        for e in entities
    )
    tech_rows = "\n".join(
        f"| {t['tech_name']} | {t['category']} | {t['vendor']} | {t['lifecycle_at_study']} | {t['lifecycle_current']} |"
        for t in techs
    )

    type_counts = Counter(o["observation_type"] for o in obs)
    breakdown = ", ".join(f"{k}: {v}" for k, v in type_counts.most_common())

    preds = [o for o in obs if o["observation_type"] == "viability-prediction"]
    prescience_md = "This study uses analytical-finding and thematic-thread-decomposition as primary observation types. See §6 for the prediction scorecard."
    if preds:
        prescience_md = f"See observations.csv: {len(preds)} viability-prediction rows."

    doc = f"# {meta['title']}\n\n"
    doc += f"> Archived from: {meta['source_file']}\n"
    doc += f"> Original publication date: {meta['date']}\n"
    doc += f"> Author: {meta['author']}\n\n---\n\n"
    doc += f"## Original Document Text\n\n{raw_text}\n\n---\n\n"
    doc += f"## Frictionless Data Package Metadata\n\n"
    doc += f"> Auto-generated by Archival Ingest Skill v16\n\n"
    doc += f"### Study Record\n\n| Field | Value |\n|-------|-------|\n"
    for k, v in meta.items():
        doc += f"| {k} | {v} |\n"
    doc += f"\n### Document Assessment\n\n"
    doc += f"| Dimension | Rating | Rationale |\n|-----------|--------|-----------|\n"
    doc += f"| **Importance** | {meta['importance']} | {meta['importance_rationale']} |\n"
    doc += f"| **Relevance** | {meta['relevance']} | {meta['relevance_rationale']} |\n"
    doc += f"| **Prescience** | {meta['prescience']} | {meta['prescience_rationale']} |\n"
    doc += f"\n### Prescience Detail\n\n{prescience_md}\n\n"
    doc += f"### Entities Referenced ({len(entities)})\n\n"
    doc += f"| Entity | Type | Status | Successor |\n|--------|------|--------|-----------|\n"
    doc += ent_rows + "\n"
    doc += f"\n### Technologies Referenced ({len(techs)})\n\n"
    doc += f"| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |\n"
    doc += f"|------------|----------|--------|---------------------|---------------------|\n"
    doc += tech_rows + "\n"
    doc += f"\n### Observation Summary\n\n- Total observations: {len(obs)}\n- By type: {breakdown}\n"

    source_dir = Path(study_dir) / "source"
    source_dir.mkdir(parents=True, exist_ok=True)
    with open(source_dir / "original_text.md", "w") as f:
        f.write(doc)

def assemble(study_dir, raw_text_file=None):
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

def validate(study_dirs):
    errors = []
    for study_dir in study_dirs:
        d = Path(study_dir) / "data"
        if not d.exists():
            errors.append(f"{study_dir}: data/ directory missing")
            continue
        ent_ids = {r["entity_id"] for r in _load_csv(d / "entities.csv")}
        tech_ids = {r["tech_id"] for r in _load_csv(d / "technologies.csv")}
        code_ids = {r["code_id"] for r in _load_csv(d / "codes.csv")}
        for row in _load_csv(d / "observations.csv"):
            if row["entity_id"] and row["entity_id"] not in ent_ids:
                errors.append(f"{study_dir}: Missing entity {row['entity_id']} in {row['obs_id']}")
            if row["tech_id"] and row["tech_id"] not in tech_ids:
                errors.append(f"{study_dir}: Missing tech {row['tech_id']} in {row['obs_id']}")
            if row["observation_type"] not in code_ids:
                errors.append(f"{study_dir}: Missing code {row['observation_type']} in {row['obs_id']}")
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

def cache_init(output_dir):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
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

def main():
    if len(sys.argv) < 2:
        print("Usage: assembler.py <command> [args]")
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
        validate(sys.argv[2:])
    elif cmd == "cache-init":
        cache_init(sys.argv[2])
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
