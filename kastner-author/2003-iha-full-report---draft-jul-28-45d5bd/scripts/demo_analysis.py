#!/usr/bin/env python3
"""
Validation and analysis script for the Consumer Adoption of Memory Cards data package.

Study ID: 2003-iha-full-report---draft-jul-28-45d5bd
Archival Ingest Skill v13

Usage:
    python scripts/demo_analysis.py
"""

import csv
import json
import os
import sys
from collections import Counter
from pathlib import Path


# Resolve paths relative to this script's location
SCRIPT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = SCRIPT_DIR.parent
DATA_DIR = PACKAGE_DIR / "data"

CANONICAL_OBSERVATION_TYPES = {
    "strategy-classification",
    "viability-prediction",
    "actual-outcome",
    "technology-assessment",
    "benchmark-result",
    "framework-factor",
    "market-data",
    "expert-opinion",
}

EXPECTED_FILES = {
    "data/studies.csv": ["study_id", "title", "author", "date", "type", "subject_domain",
                         "methodology", "source_file", "abstract", "license", "importance",
                         "importance_rationale", "relevance", "relevance_rationale",
                         "prescience", "prescience_rationale"],
    "data/entities.csv": ["entity_id", "entity_name", "entity_type", "sector", "status",
                          "successor", "years_active", "study_id", "notes"],
    "data/technologies.csv": ["tech_id", "tech_name", "category", "vendor", "era",
                               "lifecycle_at_study", "lifecycle_current", "study_id", "notes"],
    "data/observations.csv": ["obs_id", "study_id", "entity_id", "tech_id", "observation_type",
                               "year_observed", "metric_name", "metric_value", "confidence",
                               "methodology_code", "source_page", "notes"],
    "data/codes.csv": ["code_id", "code_type", "label", "definition"],
}


def load_csv(filename):
    """Load a CSV file and return list of dicts."""
    filepath = PACKAGE_DIR / filename
    if not filepath.exists():
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def validate_file_existence():
    """Check that all expected files exist."""
    print("=" * 60)
    print("FILE EXISTENCE CHECK")
    print("=" * 60)
    all_ok = True
    for fname in EXPECTED_FILES:
        filepath = PACKAGE_DIR / fname
        exists = filepath.exists()
        status = "OK" if exists else "MISSING"
        print(f"  [{status}] {fname}")
        if not exists:
            all_ok = False

    # Check non-CSV files
    for extra in ["datapackage.json", "schema/schema_org.json", "README.md",
                  "source/original_text.md", "scripts/demo_analysis.py"]:
        filepath = PACKAGE_DIR / extra
        exists = filepath.exists()
        status = "OK" if exists else "MISSING"
        print(f"  [{status}] {extra}")
        if not exists:
            all_ok = False

    return all_ok


def validate_csv_headers():
    """Check that CSV files have the expected headers."""
    print("\n" + "=" * 60)
    print("CSV HEADER VALIDATION")
    print("=" * 60)
    all_ok = True
    for fname, expected_headers in EXPECTED_FILES.items():
        rows = load_csv(fname)
        if rows is None:
            print(f"  [SKIP] {fname} — file not found")
            all_ok = False
            continue
        if len(rows) == 0:
            print(f"  [WARN] {fname} — no data rows")
            continue
        actual_headers = list(rows[0].keys())
        if actual_headers == expected_headers:
            print(f"  [OK]   {fname} — {len(expected_headers)} columns match")
        else:
            missing = set(expected_headers) - set(actual_headers)
            extra = set(actual_headers) - set(expected_headers)
            print(f"  [FAIL] {fname}")
            if missing:
                print(f"         Missing columns: {missing}")
            if extra:
                print(f"         Extra columns: {extra}")
            all_ok = False
    return all_ok


def validate_observation_types():
    """Check that all observation types are canonical."""
    print("\n" + "=" * 60)
    print("OBSERVATION TYPE VALIDATION")
    print("=" * 60)
    observations = load_csv("data/observations.csv")
    if observations is None:
        print("  [SKIP] observations.csv not found")
        return False

    all_ok = True
    type_counts = Counter()
    for obs in observations:
        obs_type = obs.get("observation_type", "")
        type_counts[obs_type] += 1
        if obs_type not in CANONICAL_OBSERVATION_TYPES:
            print(f"  [FAIL] {obs['obs_id']}: invalid type '{obs_type}'")
            all_ok = False

    if all_ok:
        print("  [OK]   All observation types are canonical")

    print("\n  Observation type distribution:")
    for obs_type, count in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"    {obs_type}: {count}")

    return all_ok


def validate_obs_id_format():
    """Check that obs_id follows OBS-NNN format."""
    print("\n" + "=" * 60)
    print("OBS_ID FORMAT VALIDATION")
    print("=" * 60)
    observations = load_csv("data/observations.csv")
    if observations is None:
        print("  [SKIP] observations.csv not found")
        return False

    all_ok = True
    for obs in observations:
        obs_id = obs.get("obs_id", "")
        if not obs_id.startswith("OBS-") or not obs_id[4:].isdigit():
            print(f"  [FAIL] Invalid obs_id format: '{obs_id}'")
            all_ok = False

    if all_ok:
        print(f"  [OK]   All {len(observations)} obs_ids follow OBS-NNN format")
    return all_ok


def validate_foreign_keys():
    """Check referential integrity between CSVs."""
    print("\n" + "=" * 60)
    print("FOREIGN KEY VALIDATION")
    print("=" * 60)

    studies = load_csv("data/studies.csv")
    entities = load_csv("data/entities.csv")
    technologies = load_csv("data/technologies.csv")
    observations = load_csv("data/observations.csv")

    if any(x is None for x in [studies, entities, technologies, observations]):
        print("  [SKIP] One or more CSVs not found")
        return False

    study_ids = {r["study_id"] for r in studies}
    entity_ids = {r["entity_id"] for r in entities}
    tech_ids = {r["tech_id"] for r in technologies}

    all_ok = True

    # Check entity study_id references
    for ent in entities:
        if ent["study_id"] not in study_ids:
            print(f"  [FAIL] Entity {ent['entity_id']}: study_id '{ent['study_id']}' not in studies.csv")
            all_ok = False

    # Check technology study_id references
    for tech in technologies:
        if tech["study_id"] not in study_ids:
            print(f"  [FAIL] Tech {tech['tech_id']}: study_id '{tech['study_id']}' not in studies.csv")
            all_ok = False

    # Check observation references
    for obs in observations:
        if obs["study_id"] not in study_ids:
            print(f"  [FAIL] {obs['obs_id']}: study_id '{obs['study_id']}' not in studies.csv")
            all_ok = False
        if obs["entity_id"] not in entity_ids:
            print(f"  [FAIL] {obs['obs_id']}: entity_id '{obs['entity_id']}' not in entities.csv")
            all_ok = False
        if obs["tech_id"] not in tech_ids:
            print(f"  [FAIL] {obs['obs_id']}: tech_id '{obs['tech_id']}' not in technologies.csv")
            all_ok = False

    if all_ok:
        print("  [OK]   All foreign key references valid")
    return all_ok


def validate_single_valued_entity_ids():
    """Check that entity_id in observations is single-valued (no comma-separated lists)."""
    print("\n" + "=" * 60)
    print("SINGLE-VALUED ENTITY_ID VALIDATION")
    print("=" * 60)
    observations = load_csv("data/observations.csv")
    if observations is None:
        print("  [SKIP] observations.csv not found")
        return False

    all_ok = True
    for obs in observations:
        entity_id = obs.get("entity_id", "")
        if "," in entity_id:
            print(f"  [FAIL] {obs['obs_id']}: entity_id contains comma: '{entity_id}'")
            all_ok = False

    if all_ok:
        print("  [OK]   All entity_ids are single-valued")
    return all_ok


def validate_datapackage_json():
    """Check datapackage.json is valid JSON with required fields."""
    print("\n" + "=" * 60)
    print("DATAPACKAGE.JSON VALIDATION")
    print("=" * 60)
    filepath = PACKAGE_DIR / "datapackage.json"
    if not filepath.exists():
        print("  [SKIP] datapackage.json not found")
        return False

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            pkg = json.load(f)
    except json.JSONDecodeError as e:
        print(f"  [FAIL] Invalid JSON: {e}")
        return False

    all_ok = True
    for field in ["name", "title", "resources"]:
        if field not in pkg:
            print(f"  [FAIL] Missing required field: {field}")
            all_ok = False

    if "resources" in pkg:
        print(f"  [OK]   {len(pkg['resources'])} resources defined")
        for res in pkg["resources"]:
            print(f"         - {res.get('name', 'unnamed')}: {res.get('path', 'no path')}")

    if all_ok:
        print("  [OK]   datapackage.json is valid")
    return all_ok


def print_summary_statistics():
    """Print summary statistics for the data package."""
    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)

    studies = load_csv("data/studies.csv")
    entities = load_csv("data/entities.csv")
    technologies = load_csv("data/technologies.csv")
    observations = load_csv("data/observations.csv")
    codes = load_csv("data/codes.csv")

    if studies:
        study = studies[0]
        print(f"\n  Study: {study.get('title', 'N/A')}")
        print(f"  Author: {study.get('author', 'N/A')}")
        print(f"  Date: {study.get('date', 'N/A')}")
        print(f"  Importance: {study.get('importance', 'N/A')}/10")
        print(f"  Relevance: {study.get('relevance', 'N/A')}/10")
        print(f"  Prescience: {study.get('prescience', 'N/A')}/10")

    print(f"\n  Record counts:")
    print(f"    Studies:       {len(studies) if studies else 0}")
    print(f"    Entities:      {len(entities) if entities else 0}")
    print(f"    Technologies:  {len(technologies) if technologies else 0}")
    print(f"    Observations:  {len(observations) if observations else 0}")
    print(f"    Codes:         {len(codes) if codes else 0}")

    if entities:
        status_counts = Counter(e["status"] for e in entities)
        print(f"\n  Entity status distribution:")
        for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
            print(f"    {status}: {count}")

    if technologies:
        lifecycle_counts = Counter(t["lifecycle_current"] for t in technologies)
        print(f"\n  Technology current lifecycle distribution:")
        for lc, count in sorted(lifecycle_counts.items(), key=lambda x: -x[1]):
            print(f"    {lc}: {count}")

    if observations:
        confidence_counts = Counter(o["confidence"] for o in observations)
        print(f"\n  Observation confidence distribution:")
        for conf, count in sorted(confidence_counts.items(), key=lambda x: -x[1]):
            print(f"    {conf}: {count}")

        method_counts = Counter(o["methodology_code"] for o in observations)
        print(f"\n  Methodology code distribution:")
        for method, count in sorted(method_counts.items(), key=lambda x: -x[1]):
            print(f"    {method}: {count}")


def main():
    """Run all validations and print results."""
    print("Archival Data Package Validation")
    print(f"Study: 2003-iha-full-report---draft-jul-28-45d5bd")
    print(f"Package directory: {PACKAGE_DIR}")
    print()

    results = []
    results.append(("File Existence", validate_file_existence()))
    results.append(("CSV Headers", validate_csv_headers()))
    results.append(("Observation Types", validate_observation_types()))
    results.append(("Obs ID Format", validate_obs_id_format()))
    results.append(("Foreign Keys", validate_foreign_keys()))
    results.append(("Single-Valued Entity IDs", validate_single_valued_entity_ids()))
    results.append(("Datapackage JSON", validate_datapackage_json()))

    print_summary_statistics()

    print("\n" + "=" * 60)
    print("VALIDATION RESULTS")
    print("=" * 60)
    all_passed = True
    for name, passed in results:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {name}")
        if not passed:
            all_passed = False

    print()
    if all_passed:
        print("All validations PASSED.")
    else:
        print("Some validations FAILED. Review output above.")

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
