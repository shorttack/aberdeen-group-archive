#!/usr/bin/env python3
"""
Archival Ingest Skill v13 - Validation and Demo Analysis Script
Study: Why You Need To Replace Those Windows 98 And NT Machines
Study ID: why-you-need-to-replace-those-windows-98-and-nt-ma-9b9622
Generated: 2026-03-15
"""

import csv
import json
import os
import sys
from pathlib import Path
from collections import Counter


def get_base_dir():
    """Determine the base directory of the data package."""
    script_dir = Path(__file__).resolve().parent
    return script_dir.parent


def load_csv(filepath):
    """Load a CSV file and return a list of dictionaries."""
    rows = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def validate_file_exists(filepath, label):
    """Check that a required file exists."""
    if filepath.exists():
        print(f"  [PASS] {label}: {filepath.name}")
        return True
    else:
        print(f"  [FAIL] {label}: {filepath.name} NOT FOUND")
        return False


def validate_csv_columns(rows, expected_columns, label):
    """Validate that CSV has the expected columns."""
    if not rows:
        print(f"  [FAIL] {label}: No rows found")
        return False
    actual_columns = set(rows[0].keys())
    expected_set = set(expected_columns)
    if expected_set == actual_columns:
        print(f"  [PASS] {label}: All {len(expected_columns)} columns present")
        return True
    else:
        missing = expected_set - actual_columns
        extra = actual_columns - expected_set
        if missing:
            print(f"  [FAIL] {label}: Missing columns: {missing}")
        if extra:
            print(f"  [WARN] {label}: Extra columns: {extra}")
        return not missing


def validate_foreign_keys(observations, entity_ids, tech_ids):
    """Validate that observation foreign keys reference valid entities/technologies."""
    errors = 0
    for obs in observations:
        eid = obs.get("entity_id", "").strip()
        tid = obs.get("tech_id", "").strip()
        if eid and eid not in entity_ids:
            print(f"  [FAIL] {obs['obs_id']}: entity_id '{eid}' not in entities.csv")
            errors += 1
        if tid and tid not in tech_ids:
            print(f"  [FAIL] {obs['obs_id']}: tech_id '{tid}' not in technologies.csv")
            errors += 1
    if errors == 0:
        print(f"  [PASS] All observation foreign keys are valid")
    return errors == 0


def validate_obs_id_format(observations, study_id):
    """Validate observation ID format."""
    prefix = f"{study_id}-OBS-"
    errors = 0
    for obs in observations:
        if not obs["obs_id"].startswith(prefix):
            print(f"  [FAIL] Invalid obs_id format: {obs['obs_id']}")
            errors += 1
    if errors == 0:
        print(f"  [PASS] All {len(observations)} observation IDs follow correct format")
    return errors == 0


def validate_datapackage(filepath):
    """Validate the datapackage.json structure."""
    with open(filepath, "r", encoding="utf-8") as f:
        pkg = json.load(f)

    errors = 0
    required_keys = ["name", "title", "version", "created", "resources", "licenses"]
    for key in required_keys:
        if key not in pkg:
            print(f"  [FAIL] datapackage.json missing key: {key}")
            errors += 1

    if pkg.get("created") == "2026-03-15":
        print(f"  [PASS] datapackage.json created date is correct")
    else:
        print(f"  [FAIL] datapackage.json created date: {pkg.get('created')}")
        errors += 1

    resource_names = [r["name"] for r in pkg.get("resources", [])]
    expected_resources = ["studies", "entities", "technologies", "observations", "codes"]
    for name in expected_resources:
        if name in resource_names:
            print(f"  [PASS] Resource '{name}' defined in datapackage.json")
        else:
            print(f"  [FAIL] Resource '{name}' missing from datapackage.json")
            errors += 1

    return errors == 0


def validate_schema_org(filepath):
    """Validate the schema_org.json structure."""
    with open(filepath, "r", encoding="utf-8") as f:
        schema = json.load(f)

    errors = 0
    if schema.get("@context") == "https://schema.org":
        print(f"  [PASS] schema_org.json @context is correct")
    else:
        print(f"  [FAIL] schema_org.json @context incorrect")
        errors += 1

    if schema.get("@type") == "ScholarlyArticle":
        print(f"  [PASS] schema_org.json @type is ScholarlyArticle")
    else:
        print(f"  [FAIL] schema_org.json @type: {schema.get('@type')}")
        errors += 1

    if schema.get("datePublished") == "2003-05-05":
        print(f"  [PASS] schema_org.json datePublished is correct")
    else:
        print(f"  [FAIL] schema_org.json datePublished: {schema.get('datePublished')}")
        errors += 1

    return errors == 0


def print_analysis(studies, entities, technologies, observations, codes):
    """Print a summary analysis of the data package contents."""
    print("\n" + "=" * 60)
    print("DATA PACKAGE ANALYSIS")
    print("=" * 60)

    # Study summary
    study = studies[0]
    print(f"\nStudy: {study['title']}")
    print(f"Author: {study['author']}")
    print(f"Date: {study['date']}")
    print(f"Type: {study['type']}")
    print(f"Importance: {study['importance']} | Relevance: {study['relevance']} | Prescience: {study['prescience']}")

    # Entity breakdown
    print(f"\nEntities: {len(entities)}")
    entity_types = Counter(e["entity_type"] for e in entities)
    for etype, count in entity_types.most_common():
        print(f"  {etype}: {count}")

    # Technology breakdown
    print(f"\nTechnologies: {len(technologies)}")
    tech_categories = Counter(t["category"] for t in technologies)
    for cat, count in tech_categories.most_common():
        print(f"  {cat}: {count}")

    lifecycle_current = Counter(t["lifecycle_current"] for t in technologies)
    print(f"\nCurrent lifecycle status:")
    for status, count in lifecycle_current.most_common():
        print(f"  {status}: {count}")

    # Observation breakdown
    print(f"\nObservations: {len(observations)}")
    obs_types = Counter(o["observation_type"] for o in observations)
    for otype, count in obs_types.most_common():
        print(f"  {otype}: {count}")

    confidence_levels = Counter(o["confidence"] for o in observations)
    print(f"\nConfidence distribution:")
    for level, count in confidence_levels.most_common():
        print(f"  {level}: {count}")

    methodology_codes = Counter(o["methodology_code"] for o in observations)
    print(f"\nMethodology codes:")
    for code, count in methodology_codes.most_common():
        print(f"  {code}: {count}")

    # Code definitions
    print(f"\nCode definitions: {len(codes)}")
    code_types = Counter(c["code_type"] for c in codes)
    for ctype, count in code_types.most_common():
        print(f"  {ctype}: {count}")


def main():
    """Run all validations and analysis."""
    base_dir = get_base_dir()
    study_id = "why-you-need-to-replace-those-windows-98-and-nt-ma-9b9622"

    print("=" * 60)
    print("ARCHIVAL INGEST SKILL v13 - VALIDATION REPORT")
    print(f"Study: {study_id}")
    print(f"Base directory: {base_dir}")
    print("=" * 60)

    # Phase 1: File existence
    print("\n--- Phase 1: File Existence ---")
    all_files_exist = True
    files_to_check = [
        (base_dir / "datapackage.json", "Data Package Descriptor"),
        (base_dir / "README.md", "README"),
        (base_dir / "data" / "studies.csv", "Studies CSV"),
        (base_dir / "data" / "entities.csv", "Entities CSV"),
        (base_dir / "data" / "technologies.csv", "Technologies CSV"),
        (base_dir / "data" / "observations.csv", "Observations CSV"),
        (base_dir / "data" / "codes.csv", "Codes CSV"),
        (base_dir / "schema" / "schema_org.json", "Schema.org JSON-LD"),
        (base_dir / "scripts" / "demo_analysis.py", "Demo Analysis Script"),
        (base_dir / "source" / "original_text.md", "Original Text"),
    ]
    for filepath, label in files_to_check:
        if not validate_file_exists(filepath, label):
            all_files_exist = False

    if not all_files_exist:
        print("\n[ABORT] Not all required files found. Fix missing files before proceeding.")
        sys.exit(1)

    # Phase 2: CSV Structure
    print("\n--- Phase 2: CSV Structure ---")
    studies = load_csv(base_dir / "data" / "studies.csv")
    entities = load_csv(base_dir / "data" / "entities.csv")
    technologies = load_csv(base_dir / "data" / "technologies.csv")
    observations = load_csv(base_dir / "data" / "observations.csv")
    codes = load_csv(base_dir / "data" / "codes.csv")

    validate_csv_columns(studies, [
        "study_id", "title", "author", "date", "type", "subject_domain",
        "methodology", "source_file", "abstract", "license", "importance",
        "importance_rationale", "relevance", "relevance_rationale",
        "prescience", "prescience_rationale"
    ], "studies.csv")

    validate_csv_columns(entities, [
        "entity_id", "entity_name", "entity_type", "sector", "status",
        "successor", "years_active", "study_id", "notes"
    ], "entities.csv")

    validate_csv_columns(technologies, [
        "tech_id", "tech_name", "category", "vendor", "era",
        "lifecycle_at_study", "lifecycle_current", "study_id", "notes"
    ], "technologies.csv")

    validate_csv_columns(observations, [
        "obs_id", "study_id", "entity_id", "tech_id", "observation_type",
        "year_observed", "metric_name", "metric_value", "confidence",
        "methodology_code", "source_page", "notes"
    ], "observations.csv")

    validate_csv_columns(codes, [
        "code_id", "code_type", "label", "definition"
    ], "codes.csv")

    # Phase 3: Row counts
    print("\n--- Phase 3: Row Counts ---")
    print(f"  Studies:      {len(studies)} record(s)")
    print(f"  Entities:     {len(entities)} record(s)")
    print(f"  Technologies: {len(technologies)} record(s)")
    print(f"  Observations: {len(observations)} record(s)")
    print(f"  Codes:        {len(codes)} record(s)")

    if len(studies) == 1:
        print("  [PASS] Exactly 1 study record")
    else:
        print(f"  [FAIL] Expected 1 study record, found {len(studies)}")

    if 25 <= len(observations) <= 35:
        print(f"  [PASS] Observations count ({len(observations)}) within target range 25-35")
    else:
        print(f"  [WARN] Observations count ({len(observations)}) outside target range 25-35")

    # Phase 4: Referential integrity
    print("\n--- Phase 4: Referential Integrity ---")
    entity_ids = {e["entity_id"] for e in entities}
    tech_ids = {t["tech_id"] for t in technologies}
    validate_foreign_keys(observations, entity_ids, tech_ids)
    validate_obs_id_format(observations, study_id)

    # Verify all observations reference the correct study_id
    bad_study_refs = [o for o in observations if o["study_id"] != study_id]
    if not bad_study_refs:
        print(f"  [PASS] All observations reference correct study_id")
    else:
        print(f"  [FAIL] {len(bad_study_refs)} observations reference wrong study_id")

    # Phase 5: JSON validation
    print("\n--- Phase 5: JSON Validation ---")
    validate_datapackage(base_dir / "datapackage.json")
    validate_schema_org(base_dir / "schema" / "schema_org.json")

    # Phase 6: Analysis
    print_analysis(studies, entities, technologies, observations, codes)

    print("\n" + "=" * 60)
    print("VALIDATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
