#!/usr/bin/env python3
"""
Demo Analysis & Validation Script
Frictionless Data Package: 2010-intel-vpro-daily-globe-6f615e

2010 Business Computers Leave the Starting Gate
Peter S. Kastner, February 2010
"""

import csv
import json
import os
import sys
from collections import Counter
from pathlib import Path

CANONICAL_OBS_TYPES = {
    "strategy-classification", "viability-prediction", "actual-outcome",
    "technology-assessment", "benchmark-result", "framework-factor",
    "market-data", "expert-opinion",
}
VALID_CONFIDENCE = {"high", "medium", "low", "verified"}
VALID_METHODOLOGY = {
    "industry-analysis", "competitive-profiling", "benchmarking",
    "field-research", "document-review", "statistical-analysis",
}
VALID_RATINGS = {"high", "medium", "low", "not-applicable"}

STUDY_ID = "2010-intel-vpro-daily-globe-6f615e"

EXPECTED_FILES = [
    "datapackage.json",
    "README.md",
    "data/studies.csv",
    "data/entities.csv",
    "data/technologies.csv",
    "data/observations.csv",
    "data/codes.csv",
    "schema/schema_org.json",
    "source/original_text.md",
    "scripts/demo_analysis.py",
]

# Column definitions for each CSV
STUDIES_COLUMNS = [
    "study_id", "title", "author", "date", "type", "subject_domain",
    "methodology", "source_file", "abstract", "license", "importance",
    "importance_rationale", "relevance", "relevance_rationale",
    "prescience", "prescience_rationale",
]
ENTITIES_COLUMNS = [
    "entity_id", "entity_name", "entity_type", "sector", "status",
    "successor", "years_active", "study_id", "notes",
]
TECHNOLOGIES_COLUMNS = [
    "tech_id", "tech_name", "category", "vendor", "era",
    "lifecycle_at_study", "lifecycle_current", "study_id", "notes",
]
OBSERVATIONS_COLUMNS = [
    "obs_id", "study_id", "entity_id", "tech_id", "observation_type",
    "year_observed", "metric_name", "metric_value", "confidence",
    "methodology_code", "source_page", "notes",
]
CODES_COLUMNS = [
    "code_id", "code_type", "label", "definition",
]


def find_package_root():
    """Find the package root directory."""
    script_dir = Path(__file__).resolve().parent
    # Script is in scripts/, so package root is one level up
    pkg_root = script_dir.parent
    if (pkg_root / "datapackage.json").exists():
        return pkg_root
    # Try current working directory
    cwd = Path.cwd()
    if (cwd / "datapackage.json").exists():
        return cwd
    print("ERROR: Cannot find package root (no datapackage.json found)")
    sys.exit(1)


def load_csv(filepath):
    """Load a CSV file and return list of dicts."""
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def validate_files_present(pkg_root):
    """Check that all 10 expected files are present."""
    print("=" * 60)
    print("FILE PRESENCE CHECK")
    print("=" * 60)
    errors = 0
    for rel_path in EXPECTED_FILES:
        full_path = pkg_root / rel_path
        if full_path.exists():
            print(f"  PASS  {rel_path}")
        else:
            print(f"  FAIL  {rel_path} -- MISSING")
            errors += 1
    print(f"\nFiles: {len(EXPECTED_FILES) - errors}/{len(EXPECTED_FILES)} present")
    return errors


def validate_csv_columns(data, expected_columns, name):
    """Validate CSV has expected columns."""
    if not data:
        print(f"  FAIL  {name} -- no data rows")
        return 1
    actual = list(data[0].keys())
    if actual != expected_columns:
        missing = set(expected_columns) - set(actual)
        extra = set(actual) - set(expected_columns)
        msg = []
        if missing:
            msg.append(f"missing: {missing}")
        if extra:
            msg.append(f"extra: {extra}")
        print(f"  FAIL  {name} columns -- {'; '.join(msg)}")
        return 1
    print(f"  PASS  {name} columns ({len(expected_columns)} fields)")
    return 0


def validate_studies(studies):
    """Validate studies.csv content."""
    errors = 0
    if len(studies) != 1:
        print(f"  FAIL  studies.csv -- expected 1 row, got {len(studies)}")
        errors += 1
    study = studies[0]
    if study["study_id"] != STUDY_ID:
        print(f"  FAIL  study_id mismatch: {study['study_id']}")
        errors += 1
    for field in ["importance", "relevance", "prescience"]:
        val = study.get(field, "")
        if val not in VALID_RATINGS:
            print(f"  FAIL  studies.{field} = '{val}' not in {VALID_RATINGS}")
            errors += 1
        else:
            print(f"  PASS  studies.{field} = '{val}'")
    return errors


def validate_entities(entities):
    """Validate entities.csv content."""
    errors = 0
    entity_ids = set()
    for ent in entities:
        eid = ent["entity_id"]
        entity_ids.add(eid)
        # Check lowercase-hyphenated format
        if eid != eid.lower() or " " in eid:
            print(f"  FAIL  entity_id '{eid}' not lowercase-hyphenated")
            errors += 1
        if ent["study_id"] != STUDY_ID:
            print(f"  FAIL  entity '{eid}' has wrong study_id: {ent['study_id']}")
            errors += 1
    print(f"  PASS  {len(entities)} entities loaded, IDs: {sorted(entity_ids)}")
    return errors, entity_ids


def validate_technologies(techs):
    """Validate technologies.csv content."""
    errors = 0
    tech_ids = set()
    for tech in techs:
        tid = tech["tech_id"]
        tech_ids.add(tid)
        # Check lowercase-hyphenated format
        if tid != tid.lower() or " " in tid:
            print(f"  FAIL  tech_id '{tid}' not lowercase-hyphenated")
            errors += 1
        if tech["study_id"] != STUDY_ID:
            print(f"  FAIL  tech '{tid}' has wrong study_id: {tech['study_id']}")
            errors += 1
    print(f"  PASS  {len(techs)} technologies loaded, IDs: {sorted(tech_ids)}")
    return errors, tech_ids


def validate_observations(observations, entity_ids, tech_ids):
    """Validate observations.csv content."""
    errors = 0
    obs_ids = set()

    for obs in observations:
        oid = obs["obs_id"]
        obs_ids.add(oid)

        # Check obs_id format
        if not oid.startswith("OBS-") or len(oid) != 7:
            print(f"  FAIL  obs_id '{oid}' not in OBS-NNN format")
            errors += 1

        # Check study_id
        if obs["study_id"] != STUDY_ID:
            print(f"  FAIL  {oid} has wrong study_id: {obs['study_id']}")
            errors += 1

        # Check observation_type
        otype = obs["observation_type"]
        if otype not in CANONICAL_OBS_TYPES:
            print(f"  FAIL  {oid} observation_type '{otype}' not canonical")
            errors += 1

        # Check confidence
        conf = obs["confidence"]
        if conf not in VALID_CONFIDENCE:
            print(f"  FAIL  {oid} confidence '{conf}' not valid")
            errors += 1

        # Check methodology_code
        meth = obs["methodology_code"]
        if meth not in VALID_METHODOLOGY:
            print(f"  FAIL  {oid} methodology_code '{meth}' not valid")
            errors += 1

        # Check entity_id referential integrity
        eid = obs["entity_id"]
        if eid and eid not in entity_ids:
            print(f"  FAIL  {oid} entity_id '{eid}' not in entities.csv")
            errors += 1

        # Check tech_id referential integrity
        tid = obs["tech_id"]
        if tid and tid not in tech_ids:
            print(f"  FAIL  {oid} tech_id '{tid}' not in technologies.csv")
            errors += 1

        # Check entity_id is single-valued (no commas)
        if "," in eid:
            print(f"  FAIL  {oid} entity_id '{eid}' contains comma (must be single-valued)")
            errors += 1

    # Summary
    type_counts = Counter(obs["observation_type"] for obs in observations)
    conf_counts = Counter(obs["confidence"] for obs in observations)
    meth_counts = Counter(obs["methodology_code"] for obs in observations)

    print(f"\n  Observation count: {len(observations)}")
    print(f"  Unique obs_ids: {len(obs_ids)}")
    print(f"\n  By observation_type:")
    for otype in sorted(CANONICAL_OBS_TYPES):
        count = type_counts.get(otype, 0)
        print(f"    {otype}: {count}")
    print(f"\n  By confidence:")
    for conf in sorted(VALID_CONFIDENCE):
        count = conf_counts.get(conf, 0)
        print(f"    {conf}: {count}")
    print(f"\n  By methodology_code:")
    for meth in sorted(VALID_METHODOLOGY):
        count = meth_counts.get(meth, 0)
        print(f"    {meth}: {count}")

    return errors


def validate_codes(codes):
    """Validate codes.csv content."""
    errors = 0
    code_types = Counter(c["code_type"] for c in codes)

    # Check that all 8 observation_type codes are present
    obs_type_codes = {c["code_id"] for c in codes if c["code_type"] == "observation_type"}
    missing_obs = CANONICAL_OBS_TYPES - obs_type_codes
    if missing_obs:
        print(f"  FAIL  Missing observation_type codes: {missing_obs}")
        errors += 1
    else:
        print(f"  PASS  All 8 observation_type codes present")

    # Check that all 4 confidence codes are present
    conf_codes = {c["code_id"] for c in codes if c["code_type"] == "confidence"}
    missing_conf = VALID_CONFIDENCE - conf_codes
    if missing_conf:
        print(f"  FAIL  Missing confidence codes: {missing_conf}")
        errors += 1
    else:
        print(f"  PASS  All 4 confidence codes present")

    # Check that all 6 methodology_code codes are present
    meth_codes = {c["code_id"] for c in codes if c["code_type"] == "methodology_code"}
    missing_meth = VALID_METHODOLOGY - meth_codes
    if missing_meth:
        print(f"  FAIL  Missing methodology_code codes: {missing_meth}")
        errors += 1
    else:
        print(f"  PASS  All 6 methodology_code codes present")

    print(f"\n  Code type distribution:")
    for ct, count in code_types.most_common():
        print(f"    {ct}: {count}")
    print(f"  Total codes: {len(codes)}")

    return errors


def validate_datapackage(pkg_root):
    """Validate datapackage.json structure."""
    errors = 0
    dp_path = pkg_root / "datapackage.json"
    with open(dp_path, encoding="utf-8") as f:
        dp = json.load(f)

    if dp.get("name") != STUDY_ID:
        print(f"  FAIL  datapackage.json name '{dp.get('name')}' != '{STUDY_ID}'")
        errors += 1
    else:
        print(f"  PASS  datapackage.json name matches study_id")

    resources = dp.get("resources", [])
    resource_names = {r["name"] for r in resources}
    expected_resources = {"studies", "entities", "technologies", "observations", "codes"}
    if resource_names != expected_resources:
        print(f"  FAIL  resources mismatch: {resource_names} vs {expected_resources}")
        errors += 1
    else:
        print(f"  PASS  All 5 resources defined")

    # Check each resource has a schema
    for r in resources:
        if "schema" not in r:
            print(f"  FAIL  resource '{r['name']}' missing schema")
            errors += 1
        elif "fields" not in r["schema"]:
            print(f"  FAIL  resource '{r['name']}' schema missing fields")
            errors += 1
        else:
            print(f"  PASS  resource '{r['name']}' has schema with {len(r['schema']['fields'])} fields")

    return errors


def validate_schema_org(pkg_root):
    """Validate schema_org.json structure."""
    errors = 0
    schema_path = pkg_root / "schema" / "schema_org.json"
    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)

    if schema.get("@type") != "Dataset":
        print(f"  FAIL  schema_org.json @type != 'Dataset'")
        errors += 1
    else:
        print(f"  PASS  schema_org.json @type = 'Dataset'")

    if schema.get("identifier") != STUDY_ID:
        print(f"  FAIL  schema_org.json identifier mismatch")
        errors += 1
    else:
        print(f"  PASS  schema_org.json identifier matches study_id")

    return errors


def main():
    """Run all validations."""
    pkg_root = find_package_root()
    print(f"\nPackage root: {pkg_root}")
    print(f"Study ID: {STUDY_ID}")
    print()

    total_errors = 0

    # 1. File presence
    total_errors += validate_files_present(pkg_root)

    # 2. CSV column validation
    print("\n" + "=" * 60)
    print("CSV COLUMN VALIDATION")
    print("=" * 60)

    studies = load_csv(pkg_root / "data" / "studies.csv")
    entities = load_csv(pkg_root / "data" / "entities.csv")
    techs = load_csv(pkg_root / "data" / "technologies.csv")
    observations = load_csv(pkg_root / "data" / "observations.csv")
    codes = load_csv(pkg_root / "data" / "codes.csv")

    total_errors += validate_csv_columns(studies, STUDIES_COLUMNS, "studies")
    total_errors += validate_csv_columns(entities, ENTITIES_COLUMNS, "entities")
    total_errors += validate_csv_columns(techs, TECHNOLOGIES_COLUMNS, "technologies")
    total_errors += validate_csv_columns(observations, OBSERVATIONS_COLUMNS, "observations")
    total_errors += validate_csv_columns(codes, CODES_COLUMNS, "codes")

    # 3. Studies validation
    print("\n" + "=" * 60)
    print("STUDIES VALIDATION")
    print("=" * 60)
    total_errors += validate_studies(studies)

    # 4. Entities validation
    print("\n" + "=" * 60)
    print("ENTITIES VALIDATION")
    print("=" * 60)
    ent_errors, entity_ids = validate_entities(entities)
    total_errors += ent_errors

    # 5. Technologies validation
    print("\n" + "=" * 60)
    print("TECHNOLOGIES VALIDATION")
    print("=" * 60)
    tech_errors, tech_ids = validate_technologies(techs)
    total_errors += tech_errors

    # 6. Observations validation
    print("\n" + "=" * 60)
    print("OBSERVATIONS VALIDATION")
    print("=" * 60)
    total_errors += validate_observations(observations, entity_ids, tech_ids)

    # 7. Codes validation
    print("\n" + "=" * 60)
    print("CODES VALIDATION")
    print("=" * 60)
    total_errors += validate_codes(codes)

    # 8. datapackage.json validation
    print("\n" + "=" * 60)
    print("DATAPACKAGE.JSON VALIDATION")
    print("=" * 60)
    total_errors += validate_datapackage(pkg_root)

    # 9. schema_org.json validation
    print("\n" + "=" * 60)
    print("SCHEMA_ORG.JSON VALIDATION")
    print("=" * 60)
    total_errors += validate_schema_org(pkg_root)

    # Final summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Studies:       {len(studies)} row(s)")
    print(f"  Entities:      {len(entities)} row(s)")
    print(f"  Technologies:  {len(techs)} row(s)")
    print(f"  Observations:  {len(observations)} row(s)")
    print(f"  Codes:         {len(codes)} row(s)")
    print(f"\n  Total errors:  {total_errors}")

    if total_errors == 0:
        print("\n  ALL VALIDATIONS PASSED")
    else:
        print(f"\n  VALIDATION FAILED with {total_errors} error(s)")

    return total_errors


if __name__ == "__main__":
    sys.exit(main())
