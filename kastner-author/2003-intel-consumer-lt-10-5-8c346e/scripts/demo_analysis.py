#!/usr/bin/env python3
"""
Validation and demo analysis script for:
  2003-intel-consumer-lt-10-5-8c346e
  LaGrande Technology: A Proposal for Consumer Market Research

Archival Ingest Skill v13
"""

import csv
import json
import os
import sys
from pathlib import Path
from collections import Counter

# Resolve package root relative to this script
PACKAGE_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PACKAGE_ROOT / "data"

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

EXPECTED_FILES = [
    "data/studies.csv",
    "data/entities.csv",
    "data/technologies.csv",
    "data/observations.csv",
    "data/codes.csv",
    "datapackage.json",
    "schema/schema_org.json",
    "README.md",
    "source/original_text.md",
    "scripts/demo_analysis.py",
]


def load_csv(filename):
    """Load a CSV file and return list of dicts."""
    filepath = DATA_DIR / filename
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def validate_file_existence():
    """Check all 10 expected files exist."""
    print("=" * 60)
    print("FILE EXISTENCE CHECK")
    print("=" * 60)
    all_ok = True
    for relpath in EXPECTED_FILES:
        full = PACKAGE_ROOT / relpath
        exists = full.exists()
        status = "OK" if exists else "MISSING"
        print(f"  [{status}] {relpath}")
        if not exists:
            all_ok = False
    return all_ok


def validate_studies():
    """Validate studies.csv."""
    print("\n" + "=" * 60)
    print("STUDIES VALIDATION")
    print("=" * 60)
    rows = load_csv("studies.csv")
    errors = []
    if len(rows) != 1:
        errors.append(f"Expected 1 study row, found {len(rows)}")
    row = rows[0]
    expected_id = "2003-intel-consumer-lt-10-5-8c346e"
    if row.get("study_id") != expected_id:
        errors.append(f"study_id mismatch: {row.get('study_id')} != {expected_id}")
    required_fields = [
        "study_id", "title", "author", "date", "type", "subject_domain",
        "methodology", "source_file", "abstract", "license",
        "importance", "importance_rationale", "relevance",
        "relevance_rationale", "prescience", "prescience_rationale",
    ]
    for field in required_fields:
        if not row.get(field):
            errors.append(f"Missing or empty field: {field}")
    # Validate scores are integers 1-10
    for score_field in ["importance", "relevance", "prescience"]:
        try:
            val = int(row.get(score_field, 0))
            if not (1 <= val <= 10):
                errors.append(f"{score_field} = {val}, expected 1-10")
        except ValueError:
            errors.append(f"{score_field} is not an integer: {row.get(score_field)}")
    if errors:
        for e in errors:
            print(f"  [FAIL] {e}")
    else:
        print(f"  [OK] 1 study record, all 16 fields present")
        print(f"  Study: {row['title']}")
        print(f"  Author: {row['author']}, Date: {row['date']}")
        print(f"  Scores: importance={row['importance']}, relevance={row['relevance']}, prescience={row['prescience']}")
    return len(errors) == 0


def validate_entities():
    """Validate entities.csv."""
    print("\n" + "=" * 60)
    print("ENTITIES VALIDATION")
    print("=" * 60)
    rows = load_csv("entities.csv")
    errors = []
    ids = [r["entity_id"] for r in rows]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate entity_id values found")
    for row in rows:
        if not row.get("entity_id", "").startswith("ENT-"):
            errors.append(f"Invalid entity_id format: {row.get('entity_id')}")
        if not row.get("entity_name"):
            errors.append(f"Missing entity_name for {row.get('entity_id')}")
    if errors:
        for e in errors:
            print(f"  [FAIL] {e}")
    else:
        print(f"  [OK] {len(rows)} entities, all IDs valid")
        type_counts = Counter(r["entity_type"] for r in rows)
        for t, c in sorted(type_counts.items()):
            print(f"    {t}: {c}")
    return len(errors) == 0


def validate_technologies():
    """Validate technologies.csv."""
    print("\n" + "=" * 60)
    print("TECHNOLOGIES VALIDATION")
    print("=" * 60)
    rows = load_csv("technologies.csv")
    errors = []
    ids = [r["tech_id"] for r in rows]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate tech_id values found")
    for row in rows:
        if not row.get("tech_id", "").startswith("TECH-"):
            errors.append(f"Invalid tech_id format: {row.get('tech_id')}")
    if errors:
        for e in errors:
            print(f"  [FAIL] {e}")
    else:
        print(f"  [OK] {len(rows)} technologies, all IDs valid")
        for r in rows:
            print(f"    {r['tech_id']}: {r['tech_name']} [{r['lifecycle_at_study']} -> {r['lifecycle_current']}]")
    return len(errors) == 0


def validate_observations():
    """Validate observations.csv."""
    print("\n" + "=" * 60)
    print("OBSERVATIONS VALIDATION")
    print("=" * 60)
    rows = load_csv("observations.csv")
    errors = []

    # Load valid entity and tech IDs
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    valid_entity_ids = {r["entity_id"] for r in entities}
    valid_tech_ids = {r["tech_id"] for r in technologies}

    obs_ids = [r["obs_id"] for r in rows]
    if len(obs_ids) != len(set(obs_ids)):
        errors.append("Duplicate obs_id values found")

    for row in rows:
        obs_id = row.get("obs_id", "")
        # Check obs_id format
        if not obs_id.startswith("OBS-"):
            errors.append(f"Invalid obs_id format: {obs_id}")
        # Check observation_type is canonical
        obs_type = row.get("observation_type", "")
        if obs_type not in CANONICAL_OBSERVATION_TYPES:
            errors.append(f"{obs_id}: invalid observation_type '{obs_type}'")
        # Check entity_id is single-valued (no commas)
        eid = row.get("entity_id", "")
        if "," in eid:
            errors.append(f"{obs_id}: entity_id contains comma (must be single-valued): {eid}")
        # Check entity_id exists
        if eid and eid not in valid_entity_ids:
            errors.append(f"{obs_id}: entity_id '{eid}' not found in entities.csv")
        # Check tech_id exists
        tid = row.get("tech_id", "")
        if tid and tid not in valid_tech_ids:
            errors.append(f"{obs_id}: tech_id '{tid}' not found in technologies.csv")

    # Count check
    if len(rows) < 15:
        errors.append(f"Only {len(rows)} observations; minimum target is 15")
    elif len(rows) > 30:
        errors.append(f"{len(rows)} observations; maximum target is 30")

    if errors:
        for e in errors:
            print(f"  [FAIL] {e}")
    else:
        print(f"  [OK] {len(rows)} observations, all valid")
        type_counts = Counter(r["observation_type"] for r in rows)
        print(f"  Observation type breakdown:")
        for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
            print(f"    {t}: {c}")
        conf_counts = Counter(r["confidence"] for r in rows)
        print(f"  Confidence breakdown:")
        for c, n in sorted(conf_counts.items()):
            print(f"    {c}: {n}")

    return len(errors) == 0


def validate_codes():
    """Validate codes.csv."""
    print("\n" + "=" * 60)
    print("CODES VALIDATION")
    print("=" * 60)
    rows = load_csv("codes.csv")
    errors = []
    code_ids = {r["code_id"] for r in rows}

    # Check methodology codes used in observations exist
    obs = load_csv("observations.csv")
    used_codes = {r["methodology_code"] for r in obs}
    missing = used_codes - code_ids
    if missing:
        errors.append(f"Methodology codes used in observations but not in codes.csv: {missing}")

    # Check observation types exist as codes
    for ot in CANONICAL_OBSERVATION_TYPES:
        if ot not in code_ids:
            errors.append(f"Canonical observation type '{ot}' not in codes.csv")

    if errors:
        for e in errors:
            print(f"  [FAIL] {e}")
    else:
        print(f"  [OK] {len(rows)} codes defined")
        type_counts = Counter(r["code_type"] for r in rows)
        for t, c in sorted(type_counts.items()):
            print(f"    {t}: {c}")

    return len(errors) == 0


def validate_datapackage():
    """Validate datapackage.json."""
    print("\n" + "=" * 60)
    print("DATAPACKAGE.JSON VALIDATION")
    print("=" * 60)
    errors = []
    filepath = PACKAGE_ROOT / "datapackage.json"
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            pkg = json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"Invalid JSON: {e}")
        for e in errors:
            print(f"  [FAIL] {e}")
        return False

    if pkg.get("name") != "2003-intel-consumer-lt-10-5-8c346e":
        errors.append(f"Package name mismatch: {pkg.get('name')}")
    resources = pkg.get("resources", [])
    expected_resources = {"studies", "entities", "technologies", "observations", "codes"}
    actual_resources = {r["name"] for r in resources}
    missing_res = expected_resources - actual_resources
    if missing_res:
        errors.append(f"Missing resources: {missing_res}")

    if errors:
        for e in errors:
            print(f"  [FAIL] {e}")
    else:
        print(f"  [OK] Valid JSON, {len(resources)} resources defined")
        for r in resources:
            print(f"    {r['name']}: {r['path']}")

    return len(errors) == 0


def validate_schema_org():
    """Validate schema_org.json."""
    print("\n" + "=" * 60)
    print("SCHEMA_ORG.JSON VALIDATION")
    print("=" * 60)
    errors = []
    filepath = PACKAGE_ROOT / "schema" / "schema_org.json"
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            schema = json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"Invalid JSON: {e}")
        for err in errors:
            print(f"  [FAIL] {err}")
        return False

    if schema.get("@type") != "Dataset":
        errors.append(f"@type should be 'Dataset', got '{schema.get('@type')}'")
    if not schema.get("@context"):
        errors.append("Missing @context")
    if schema.get("identifier") != "2003-intel-consumer-lt-10-5-8c346e":
        errors.append(f"Identifier mismatch: {schema.get('identifier')}")

    if errors:
        for e in errors:
            print(f"  [FAIL] {e}")
    else:
        print(f"  [OK] Valid Schema.org JSON-LD")
        print(f"    @type: {schema['@type']}")
        print(f"    name: {schema['name']}")
        print(f"    datePublished: {schema.get('datePublished')}")

    return len(errors) == 0


def demo_analysis():
    """Run a quick demo analysis."""
    print("\n" + "=" * 60)
    print("DEMO ANALYSIS")
    print("=" * 60)

    obs = load_csv("observations.csv")
    entities = load_csv("entities.csv")
    techs = load_csv("technologies.csv")

    # Predictions vs actuals
    predictions = [r for r in obs if r["observation_type"] == "viability-prediction"]
    actuals = [r for r in obs if r["observation_type"] == "actual-outcome"]

    print(f"\n  Predictions made: {len(predictions)}")
    for p in predictions:
        print(f"    {p['obs_id']}: {p['metric_name']} = {p['metric_value']}")

    print(f"\n  Actual outcomes verified: {len(actuals)}")
    for a in actuals:
        print(f"    {a['obs_id']}: {a['metric_name']} = {a['metric_value']} (year: {a['year_observed']})")

    # Technology lifecycle evolution
    print(f"\n  Technology lifecycle changes:")
    for t in techs:
        print(f"    {t['tech_name']}: {t['lifecycle_at_study']} -> {t['lifecycle_current']}")

    # Market data summary
    market = [r for r in obs if r["observation_type"] == "market-data"]
    print(f"\n  Market data points: {len(market)}")
    for m in market:
        print(f"    {m['metric_name']}: {m['metric_value']}")


def main():
    print("Archival Ingest Skill v13 -- Validation Report")
    print(f"Study: 2003-intel-consumer-lt-10-5-8c346e")
    print(f"Package root: {PACKAGE_ROOT}")
    print()

    results = {}
    results["files"] = validate_file_existence()
    results["studies"] = validate_studies()
    results["entities"] = validate_entities()
    results["technologies"] = validate_technologies()
    results["observations"] = validate_observations()
    results["codes"] = validate_codes()
    results["datapackage"] = validate_datapackage()
    results["schema_org"] = validate_schema_org()

    demo_analysis()

    # Summary
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    total = len(results)
    passed = sum(1 for v in results.values() if v)
    failed = total - passed
    for name, ok in results.items():
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}")

    print(f"\n  {passed}/{total} checks passed", end="")
    if failed:
        print(f", {failed} FAILED")
    else:
        print(" -- ALL CLEAR")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
