#!/usr/bin/env python3
"""
Demo Analysis & Validation Script
Frictionless Data Package: dct-oct.-4-hot-topic-7c1af3

New Consumer Electronics Categories Appear in Time for Christmas
Russ Craig & Peter Kastner, October 2003
"""

import csv
import json
import sys
from collections import Counter
from pathlib import Path

# Resolve paths relative to this script's location
SCRIPT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = SCRIPT_DIR.parent
DATA_DIR = PACKAGE_DIR / "data"

ERRORS = []


def load_csv(filename):
    """Load a CSV file and return a list of dictionaries."""
    filepath = DATA_DIR / filename
    if not filepath.exists():
        msg = f"File not found: {filepath}"
        ERRORS.append(msg)
        print(f"  ERROR: {msg}")
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def print_section(title, char="="):
    """Print a formatted section header."""
    print(f"\n{char * 60}")
    print(f"  {title}")
    print(f"{char * 60}")


def validate_columns(filename, data, required_columns):
    """Validate that required columns are present in the data."""
    if not data:
        ERRORS.append(f"{filename}: No data loaded")
        return False
    actual = set(data[0].keys())
    missing = set(required_columns) - actual
    if missing:
        msg = f"{filename}: Missing required columns: {sorted(missing)}"
        ERRORS.append(msg)
        print(f"  ERROR: {msg}")
        return False
    print(f"  OK: {filename} has all {len(required_columns)} required columns")
    return True


def analyze_study():
    """Display study metadata."""
    print_section("STUDY METADATA")
    studies = load_csv("studies.csv")
    if not studies:
        return
    study = studies[0]
    print(f"  Title:      {study['title']}")
    print(f"  Study ID:   {study['study_id']}")
    print(f"  Author:     {study['author']}")
    print(f"  Date:       {study['date']}")
    print(f"  Type:       {study['type']}")
    print(f"  Domain:     {study['subject_domain']}")
    print(f"  License:    {study['license']}")
    print()
    print(f"  Importance: {study['importance']}")
    print(f"    -> {study['importance_rationale'][:100]}...")
    print(f"  Relevance:  {study['relevance']}")
    print(f"    -> {study['relevance_rationale'][:100]}...")
    print(f"  Prescience: {study['prescience']}")
    print(f"    -> {study['prescience_rationale'][:100]}...")


def analyze_entities():
    """Analyze entities in the study."""
    print_section("ENTITY ANALYSIS")
    entities = load_csv("entities.csv")
    required = ["entity_id", "entity_name", "entity_type", "sector",
                 "status", "successor", "years_active", "study_id", "notes"]
    validate_columns("entities.csv", entities, required)
    print(f"  Total entities: {len(entities)}")
    print()

    # Count by status
    status_counts = Counter(e["status"] for e in entities)
    print("  Entity Status Distribution:")
    for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
        print(f"    {status:<15} {count:>3}")
    print()

    # Count by entity_type
    type_counts = Counter(e["entity_type"] for e in entities)
    print("  Entity Type Distribution:")
    for etype, count in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"    {etype:<20} {count:>3}")
    print()

    # List entities with status
    print("  Entity Roster:")
    for e in entities:
        successor_tag = f" -> {e['successor']}" if e.get("successor") else ""
        print(f"    [{e['status']:<10}] {e['entity_name']:<40} {e['years_active']}{successor_tag}")


def analyze_technologies():
    """Analyze technologies in the study."""
    print_section("TECHNOLOGY ANALYSIS")
    technologies = load_csv("technologies.csv")
    required = ["tech_id", "tech_name", "category", "vendor", "era",
                 "lifecycle_at_study", "lifecycle_current", "study_id", "notes"]
    validate_columns("technologies.csv", technologies, required)
    print(f"  Total technologies: {len(technologies)}")
    print()

    # Show technology evolution
    print("  Technology Lifecycle Evolution (at study -> current):")
    for t in technologies:
        print(f"    {t['tech_name'][:40]:<42} {t['lifecycle_at_study']:<12} -> {t['lifecycle_current']}")
    print()

    # Count by category
    cat_counts = Counter(t["category"] for t in technologies)
    print("  Technology Categories:")
    for cat, count in sorted(cat_counts.items(), key=lambda x: -x[1]):
        print(f"    {cat:<25} {count:>3}")


def analyze_observations():
    """Analyze observations in the study."""
    print_section("OBSERVATION ANALYSIS")
    observations = load_csv("observations.csv")
    required = ["obs_id", "study_id", "entity_id", "tech_id",
                 "observation_type", "year_observed", "metric_name",
                 "metric_value", "confidence", "methodology_code",
                 "source_page", "notes"]
    validate_columns("observations.csv", observations, required)
    print(f"  Total observations: {len(observations)}")
    print()

    # Count by observation_type
    type_counts = Counter(o["observation_type"] for o in observations)
    print("  Observation Type Distribution:")
    for otype, count in sorted(type_counts.items(), key=lambda x: -x[1]):
        bar = "#" * count
        print(f"    {otype:<25} {count:>3}  {bar}")
    print()

    # Count by confidence
    conf_counts = Counter(o["confidence"] for o in observations)
    print("  Confidence Distribution:")
    for conf, count in sorted(conf_counts.items(), key=lambda x: -x[1]):
        print(f"    {conf:<15} {count:>3}")
    print()

    # Count by methodology_code
    meth_counts = Counter(o["methodology_code"] for o in observations)
    print("  Methodology Code Distribution:")
    for meth, count in sorted(meth_counts.items(), key=lambda x: -x[1]):
        print(f"    {meth:<25} {count:>3}")
    print()

    # Observations per entity
    entity_counts = Counter(o["entity_id"] for o in observations if o["entity_id"])
    print("  Observations per Entity:")
    for entity, count in sorted(entity_counts.items(), key=lambda x: -x[1]):
        print(f"    {entity:<35} {count:>3}")
    print()

    # Show actual outcomes
    print("  Actual Outcomes (retrospective verification):")
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    for o in outcomes:
        entity_tag = f"[{o['entity_id']}]" if o["entity_id"] else "[general]"
        print(f"    {entity_tag:<35} {o['notes'][:70]}...")


def analyze_codes():
    """Analyze code definitions."""
    print_section("CODE DEFINITIONS")
    codes = load_csv("codes.csv")
    required = ["code_id", "code_type", "label", "definition"]
    validate_columns("codes.csv", codes, required)
    print(f"  Total codes: {len(codes)}")
    print()

    # Group by code_type
    type_groups = {}
    for c in codes:
        code_type = c["code_type"]
        if code_type not in type_groups:
            type_groups[code_type] = []
        type_groups[code_type].append(c)

    for code_type, items in sorted(type_groups.items()):
        print(f"  {code_type} ({len(items)} codes):")
        for item in items:
            print(f"    {item['code_id']:<30} {item['label']}")
        print()


def validate_package():
    """Validate the data package descriptor and cross-references."""
    print_section("PACKAGE VALIDATION")
    descriptor_path = PACKAGE_DIR / "datapackage.json"
    if not descriptor_path.exists():
        msg = "datapackage.json not found"
        ERRORS.append(msg)
        print(f"  ERROR: {msg}")
        return

    with open(descriptor_path, "r", encoding="utf-8") as f:
        descriptor = json.load(f)

    print(f"  Package name:    {descriptor.get('name', 'N/A')}")
    print(f"  Package version: {descriptor.get('version', 'N/A')}")
    print(f"  Resources:       {len(descriptor.get('resources', []))}")
    print()

    # Validate that all resource files exist
    all_valid = True
    for resource in descriptor.get("resources", []):
        filepath = PACKAGE_DIR / resource["path"]
        exists = filepath.exists()
        status = "OK" if exists else "MISSING"
        if not exists:
            all_valid = False
            ERRORS.append(f"Resource file missing: {resource['path']}")
        rows = 0
        if exists:
            with open(filepath, "r", encoding="utf-8") as f:
                rows = sum(1 for _ in f) - 1  # subtract header
        print(f"    [{status:<7}] {resource['path']:<30} ({rows} rows)")

    print()
    if all_valid:
        print("  All resource files present and accessible.")
    else:
        print("  WARNING: Some resource files are missing!")

    # Validate schema column names match CSV headers
    print()
    print("  Schema-CSV Column Validation:")
    for resource in descriptor.get("resources", []):
        filepath = PACKAGE_DIR / resource["path"]
        if not filepath.exists():
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            csv_headers = next(reader)
        schema_fields = [fld["name"] for fld in resource["schema"]["fields"]]
        if csv_headers == schema_fields:
            print(f"    [OK     ] {resource['name']}: headers match schema")
        else:
            missing_in_csv = set(schema_fields) - set(csv_headers)
            extra_in_csv = set(csv_headers) - set(schema_fields)
            msg = f"{resource['name']}: header mismatch"
            if missing_in_csv:
                msg += f" missing={sorted(missing_in_csv)}"
            if extra_in_csv:
                msg += f" extra={sorted(extra_in_csv)}"
            ERRORS.append(msg)
            print(f"    [ERROR  ] {msg}")

    # Cross-validate observation types against codes
    print()
    observations = load_csv("observations.csv")
    codes = load_csv("codes.csv")
    valid_obs_types = {c["code_id"] for c in codes if c["code_type"] == "observation_type"}
    used_obs_types = {o["observation_type"] for o in observations}
    invalid_types = used_obs_types - valid_obs_types
    if invalid_types:
        msg = f"Invalid observation types found: {invalid_types}"
        ERRORS.append(msg)
        print(f"  WARNING: {msg}")
    else:
        print(f"  All {len(used_obs_types)} observation types are valid codes.")

    # Cross-validate confidence levels against codes
    valid_conf = {c["code_id"] for c in codes if c["code_type"] == "confidence"}
    used_conf = {o["confidence"] for o in observations}
    invalid_conf = used_conf - valid_conf
    if invalid_conf:
        msg = f"Invalid confidence levels found: {invalid_conf}"
        ERRORS.append(msg)
        print(f"  WARNING: {msg}")
    else:
        print(f"  All {len(used_conf)} confidence levels are valid codes.")

    # Cross-validate methodology codes against codes
    valid_meth = {c["code_id"] for c in codes if c["code_type"] == "methodology_code"}
    used_meth = {o["methodology_code"] for o in observations}
    invalid_meth = used_meth - valid_meth
    if invalid_meth:
        msg = f"Invalid methodology codes found: {invalid_meth}"
        ERRORS.append(msg)
        print(f"  WARNING: {msg}")
    else:
        print(f"  All {len(used_meth)} methodology codes are valid codes.")

    # Cross-validate entity_id references in observations
    entities = load_csv("entities.csv")
    valid_entity_ids = {e["entity_id"] for e in entities}
    used_entity_ids = {o["entity_id"] for o in observations if o["entity_id"]}
    invalid_entities = used_entity_ids - valid_entity_ids
    if invalid_entities:
        msg = f"Invalid entity_id references in observations: {sorted(invalid_entities)}"
        ERRORS.append(msg)
        print(f"  WARNING: {msg}")
    else:
        print(f"  All {len(used_entity_ids)} entity references are valid.")

    # Cross-validate tech_id references in observations
    technologies = load_csv("technologies.csv")
    valid_tech_ids = {t["tech_id"] for t in technologies}
    used_tech_ids = {o["tech_id"] for o in observations if o["tech_id"]}
    invalid_techs = used_tech_ids - valid_tech_ids
    if invalid_techs:
        msg = f"Invalid tech_id references in observations: {sorted(invalid_techs)}"
        ERRORS.append(msg)
        print(f"  WARNING: {msg}")
    else:
        print(f"  All {len(used_tech_ids)} technology references are valid.")


def price_comparison():
    """Special analysis: Price comparison of video solutions."""
    print_section("SPECIAL ANALYSIS: 2003 Portable Video Price Comparison")
    print()
    print("  Product                        Base    Total   Video Storage")
    print("  " + "-" * 56)
    print("  ZVUE Player (Hand Held Ent.)   $99     ~$149   256MB SD = 4hrs")
    print("  Sony UX40 Clie Stack           $599    $1,359  1GB MSPro = 4hrs")
    print("  Expected Panasonic/Sony        $300    $300+   TBD")
    print("  Roku HD1000                    $500    $570+   Multi-card + WiFi")
    print()
    print("  Price ratio (Sony/ZVUE): 13.6x for equivalent video storage")
    print("  The ZVUE represented a >90% cost reduction vs Sony's solution.")


def main():
    """Run all analyses."""
    print("=" * 60)
    print("  FRICTIONLESS DATA PACKAGE ANALYSIS")
    print("  Study: New Consumer Electronics Categories Appear")
    print("         in Time for Christmas")
    print("  ID:    dct-oct.-4-hot-topic-7c1af3")
    print("  Date:  2003-10-04")
    print("=" * 60)

    validate_package()
    analyze_study()
    analyze_entities()
    analyze_technologies()
    analyze_observations()
    analyze_codes()
    price_comparison()

    print_section("ANALYSIS COMPLETE", "=")
    if ERRORS:
        print(f"  FAILED: {len(ERRORS)} validation error(s):")
        for err in ERRORS:
            print(f"    - {err}")
        print()
        sys.exit(1)
    else:
        print("  All 5 CSV resources loaded and analyzed successfully.")
        print("  All validation checks passed.")
        print(f"  Package directory: {PACKAGE_DIR}")
        print()


if __name__ == "__main__":
    main()
