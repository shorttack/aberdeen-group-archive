#!/usr/bin/env python3
"""
demo_analysis.py - Validates and analyzes the Frictionless Data Package
for study 2003-intel-centrino-pk-04050a (Intel Centrino opinion piece by Peter S. Kastner).

Usage:
    python scripts/demo_analysis.py

Requires: Python 3.7+ (standard library only; pandas optional)
"""

import os
import sys
import json
import csv
from pathlib import Path
from collections import Counter

# Determine the package root (one level up from scripts/)
PACKAGE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PACKAGE_DIR / "data"

# Expected schema definitions
EXPECTED_SCHEMAS = {
    "studies.csv": [
        "study_id", "title", "author", "date", "type", "subject_domain",
        "methodology", "source_file", "abstract", "license", "importance",
        "importance_rationale", "relevance", "relevance_rationale",
        "prescience", "prescience_rationale"
    ],
    "entities.csv": [
        "entity_id", "entity_name", "entity_type", "sector", "status",
        "successor", "years_active", "study_id", "notes"
    ],
    "technologies.csv": [
        "tech_id", "tech_name", "category", "vendor", "era",
        "lifecycle_at_study", "lifecycle_current", "study_id", "notes"
    ],
    "observations.csv": [
        "obs_id", "study_id", "entity_id", "tech_id", "observation_type",
        "year_observed", "metric_name", "metric_value", "confidence",
        "methodology_code", "source_page", "notes"
    ],
    "codes.csv": [
        "code_id", "code_type", "label", "definition"
    ]
}

CANONICAL_OBSERVATION_TYPES = {
    "strategy-classification", "viability-prediction", "actual-outcome",
    "technology-assessment", "benchmark-result", "framework-factor",
    "market-data", "expert-opinion"
}

errors = []
warnings = []


def load_csv(filename):
    """Load a CSV file and return rows as list of dicts."""
    filepath = DATA_DIR / filename
    if not filepath.exists():
        errors.append(f"MISSING FILE: {filepath}")
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def print_section(title):
    """Print a section header."""
    print(f"\n{'=' * 65}")
    print(f"  {title}")
    print(f"{'=' * 65}")


def validate_schema(filename, rows):
    """Validate CSV column headers match expected schema."""
    expected = EXPECTED_SCHEMAS.get(filename, [])
    if not rows:
        errors.append(f"EMPTY: {filename} has no data rows")
        return False
    actual = list(rows[0].keys())
    if actual != expected:
        missing = set(expected) - set(actual)
        extra = set(actual) - set(expected)
        if missing:
            errors.append(f"SCHEMA {filename}: missing columns: {missing}")
        if extra:
            errors.append(f"SCHEMA {filename}: unexpected columns: {extra}")
        return False
    return True


def validate_observations(observations, entities, technologies):
    """Validate observation records against constraints."""
    entity_ids = {e["entity_id"] for e in entities}
    tech_ids = {t["tech_id"] for t in technologies}

    for obs in observations:
        obs_id = obs.get("obs_id", "?")

        # Check observation_type is canonical
        obs_type = obs.get("observation_type", "")
        if obs_type not in CANONICAL_OBSERVATION_TYPES:
            errors.append(
                f"OBS {obs_id}: invalid observation_type '{obs_type}'. "
                f"Must be one of: {sorted(CANONICAL_OBSERVATION_TYPES)}"
            )

        # Check entity_id is single-valued (no commas)
        entity_id = obs.get("entity_id", "")
        if "," in entity_id:
            errors.append(
                f"OBS {obs_id}: entity_id must be single-valued, "
                f"found comma-separated: '{entity_id}'"
            )

        # Check foreign key references
        if entity_id and entity_id not in entity_ids:
            errors.append(
                f"OBS {obs_id}: entity_id '{entity_id}' not found in entities.csv"
            )

        tech_id = obs.get("tech_id", "")
        if tech_id and tech_id not in tech_ids:
            errors.append(
                f"OBS {obs_id}: tech_id '{tech_id}' not found in technologies.csv"
            )

        # Check obs_id format
        if not obs_id.startswith("OBS-"):
            errors.append(f"OBS {obs_id}: obs_id must start with 'OBS-'")

        # Check confidence values
        confidence = obs.get("confidence", "")
        if confidence not in ("high", "medium", "low"):
            warnings.append(
                f"OBS {obs_id}: unexpected confidence value '{confidence}'"
            )


def main():
    print_section("Frictionless Data Package Validation & Analysis")
    print(f"  Study: 2003-intel-centrino-pk-04050a")
    print(f"  Package directory: {PACKAGE_DIR}")

    # Load all CSVs
    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")
    codes = load_csv("codes.csv")

    # --- Schema Validation ---
    print_section("1. Schema Validation")
    for filename in EXPECTED_SCHEMAS:
        rows = {"studies.csv": studies, "entities.csv": entities,
                "technologies.csv": technologies, "observations.csv": observations,
                "codes.csv": codes}[filename]
        ok = validate_schema(filename, rows)
        status = "PASS" if ok else "FAIL"
        print(f"  {filename:25s}  {len(rows):3d} rows  [{status}]")

    # --- Study Overview ---
    print_section("2. Study Overview")
    if studies:
        study = studies[0]
        print(f"  Title:          {study.get('title', 'N/A')}")
        print(f"  Author:         {study.get('author', 'N/A')}")
        print(f"  Date:           {study.get('date', 'N/A')}")
        print(f"  Type:           {study.get('type', 'N/A')}")
        print(f"  Subject Domain: {study.get('subject_domain', 'N/A')}")
        print(f"  Methodology:    {study.get('methodology', 'N/A')}")
        print(f"  Ratings:        Importance={study.get('importance', 'N/A')}/10, "
              f"Relevance={study.get('relevance', 'N/A')}/10, "
              f"Prescience={study.get('prescience', 'N/A')}/10")

    # --- Entity Summary ---
    print_section(f"3. Entities ({len(entities)} total)")
    for ent in entities:
        print(f"  {ent.get('entity_id', '?'):8s}  "
              f"{ent.get('entity_name', '?'):30s}  "
              f"[{ent.get('entity_type', '?')}]  "
              f"status={ent.get('status', '?')}")

    # --- Technology Summary ---
    print_section(f"4. Technologies ({len(technologies)} total)")
    for tech in technologies:
        print(f"  {tech.get('tech_id', '?'):9s}  "
              f"{tech.get('tech_name', '?'):35s}  "
              f"[{tech.get('category', '?')}]")
        print(f"            lifecycle: {tech.get('lifecycle_at_study', '?')} -> "
              f"{tech.get('lifecycle_current', '?')}")

    # --- Observation Validation ---
    print_section("5. Observation Validation")
    validate_observations(observations, entities, technologies)

    # --- Observation Type Distribution ---
    print_section(f"6. Observations ({len(observations)} total)")
    type_counts = Counter(obs.get("observation_type", "") for obs in observations)
    print("  By type:")
    for t, count in type_counts.most_common():
        bar = "#" * count
        print(f"    {t:28s}  {count:2d}  {bar}")

    # Verify count is in range 15-30
    total_obs = len(observations)
    if total_obs < 15:
        warnings.append(f"Observation count ({total_obs}) below recommended minimum of 15")
    elif total_obs > 30:
        warnings.append(f"Observation count ({total_obs}) above recommended maximum of 30")
    print(f"\n  Total: {total_obs} (target range: 15-30)")

    # --- Confidence Distribution ---
    conf_counts = Counter(obs.get("confidence", "") for obs in observations)
    print("\n  By confidence:")
    for c, count in conf_counts.most_common():
        print(f"    {c:10s}  {count:2d}")

    # --- Prescience Analysis ---
    print_section("7. Prescience Analysis: Predictions vs Actual Outcomes")
    predictions = [o for o in observations
                   if o.get("observation_type") == "viability-prediction"]
    outcomes = [o for o in observations
                if o.get("observation_type") == "actual-outcome"]
    print(f"  Predictions: {len(predictions)}")
    print(f"  Outcomes:    {len(outcomes)}")

    for pred in predictions:
        print(f"\n  PREDICTION ({pred['obs_id']}): "
              f"{pred.get('notes', pred.get('metric_name', ''))[:90]}")
    for out in outcomes:
        print(f"\n  OUTCOME    ({out['obs_id']}): "
              f"{out.get('notes', out.get('metric_name', ''))[:90]}")

    # --- Benchmark Results ---
    print_section("8. Key Quantitative Claims (Benchmark Results)")
    benchmarks = [o for o in observations
                  if o.get("observation_type") == "benchmark-result"]
    entity_lookup = {e["entity_id"]: e for e in entities}
    for bm in benchmarks:
        ent = entity_lookup.get(bm.get("entity_id"), {})
        ent_name = ent.get("entity_name", bm.get("entity_id", "?"))
        print(f"  [{bm['obs_id']}] {bm.get('metric_name', '?')} = "
              f"{bm.get('metric_value', '?')}")
        print(f"          Source: {ent_name} | Confidence: {bm.get('confidence', '?')}")

    # --- Code Summary ---
    print_section(f"9. Code Definitions ({len(codes)} codes)")
    code_type_counts = Counter(c.get("code_type", "") for c in codes)
    for ct, count in sorted(code_type_counts.items()):
        print(f"  {ct:25s}  {count} codes")

    # --- Datapackage.json Validation ---
    print_section("10. Datapackage.json Validation")
    dp_path = PACKAGE_DIR / "datapackage.json"
    if dp_path.exists():
        with open(dp_path, "r") as f:
            dp = json.load(f)
        print(f"  Package name:    {dp.get('name', 'N/A')}")
        print(f"  Version:         {dp.get('version', 'N/A')}")
        print(f"  Resources:       {len(dp.get('resources', []))}")
        for res in dp.get("resources", []):
            res_path = PACKAGE_DIR / res["path"]
            exists = res_path.exists()
            status = "OK" if exists else "MISSING"
            print(f"    {res['name']:20s}  {res['path']:30s}  [{status}]")
            if not exists:
                errors.append(f"DATAPACKAGE: resource '{res['name']}' "
                              f"path '{res['path']}' does not exist")
    else:
        errors.append("MISSING: datapackage.json not found")

    # --- Schema.org Validation ---
    print_section("11. Schema.org JSON-LD Validation")
    schema_path = PACKAGE_DIR / "schema" / "schema_org.json"
    if schema_path.exists():
        with open(schema_path, "r") as f:
            schema = json.load(f)
        print(f"  @type:       {schema.get('@type', 'N/A')}")
        print(f"  identifier:  {schema.get('identifier', 'N/A')}")
        print(f"  keywords:    {len(schema.get('keywords', []))}")
        print(f"  distributions: {len(schema.get('distribution', []))}")
        print(f"  [PASS]")
    else:
        errors.append("MISSING: schema/schema_org.json not found")

    # --- Original Text Validation ---
    print_section("12. Source Document Validation")
    text_path = PACKAGE_DIR / "source" / "original_text.md"
    if text_path.exists():
        with open(text_path, "r") as f:
            text = f.read()
        has_header = "# Intel's Centrino" in text
        has_archive_note = "Archived from:" in text
        has_metadata = "Frictionless Data Package Metadata" in text
        has_kastner = "--Peter S Kastner" in text
        print(f"  Header present:         {'YES' if has_header else 'NO'}")
        print(f"  Archive note present:   {'YES' if has_archive_note else 'NO'}")
        print(f"  Kastner signoff:        {'YES' if has_kastner else 'NO'}")
        print(f"  Metadata section:       {'YES' if has_metadata else 'NO'}")
        print(f"  Total length:           {len(text)} chars")
        if not has_header:
            errors.append("ORIGINAL_TEXT: missing document header")
        if not has_kastner:
            errors.append("ORIGINAL_TEXT: missing author signoff")
    else:
        errors.append("MISSING: source/original_text.md not found")

    # --- Final Report ---
    print_section("VALIDATION SUMMARY")
    print(f"  Errors:   {len(errors)}")
    print(f"  Warnings: {len(warnings)}")

    if errors:
        print("\n  ERRORS:")
        for e in errors:
            print(f"    [ERROR] {e}")

    if warnings:
        print("\n  WARNINGS:")
        for w in warnings:
            print(f"    [WARN]  {w}")

    if not errors:
        print("\n  All validations PASSED.")
    else:
        print(f"\n  {len(errors)} validation(s) FAILED.")

    print(f"\n{'=' * 65}")
    print("  Analysis complete.")
    print(f"{'=' * 65}\n")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
