#!/usr/bin/env python3
"""
Demo Analysis & Validation Script
Frictionless Data Package: ie-appendix-lane-qa-research-e594cb

Research Findings: The Role of Professional Services Suppliers' Internal
Quality Assurance Organizations in Large-scale Systems Integration Engagements
Stephen Lane, Aberdeen Group, June 1999

This script validates the data package structure, checks referential integrity
across all 5 CSVs, validates code usage, and reports results.
"""

import csv
import json
import os
import sys
from collections import Counter
from pathlib import Path

# Canonical observation types -- the ONLY valid values
CANONICAL_OBS_TYPES = {
    "strategy-classification",
    "viability-prediction",
    "actual-outcome",
    "technology-assessment",
    "benchmark-result",
    "framework-factor",
    "market-data",
    "expert-opinion",
}

# Valid confidence levels
VALID_CONFIDENCE = {"high", "medium", "low", "verified"}

# Valid methodology codes
VALID_METHODOLOGY = {
    "industry-analysis",
    "competitive-profiling",
    "benchmarking",
    "field-research",
    "document-review",
    "statistical-analysis",
}

# Valid assessment ratings
VALID_RATINGS = {"high", "medium", "low", "not-applicable"}

# Expected files in the data package
EXPECTED_FILES = [
    "README.md",
    "datapackage.json",
    "data/studies.csv",
    "data/entities.csv",
    "data/technologies.csv",
    "data/observations.csv",
    "data/codes.csv",
    "schema/schema_org.json",
    "source/original_text.md",
    "scripts/demo_analysis.py",
]


def find_package_root():
    """Find the data package root directory."""
    script_dir = Path(__file__).resolve().parent
    package_root = script_dir.parent
    if (package_root / "datapackage.json").exists():
        return package_root
    cwd = Path.cwd()
    if (cwd / "datapackage.json").exists():
        return cwd
    print("ERROR: Cannot find datapackage.json. Run from the package root directory.")
    sys.exit(1)


def validate_file_structure(root):
    """Validate that all expected files exist."""
    print("=" * 60)
    print("FILE STRUCTURE VALIDATION")
    print("=" * 60)
    all_ok = True
    for f in EXPECTED_FILES:
        path = root / f
        exists = path.exists()
        status = "OK" if exists else "MISSING"
        if exists:
            size = path.stat().st_size
            print(f"  [{status}] {f} ({size:,} bytes)")
        else:
            print(f"  [{status}] {f}")
            all_ok = False
    print()
    return all_ok


def load_csv(root, filename):
    """Load a CSV file and return rows as list of dicts."""
    filepath = root / "data" / filename
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def validate_studies(root):
    """Validate studies.csv content."""
    print("=" * 60)
    print("STUDIES VALIDATION")
    print("=" * 60)
    rows = load_csv(root, "studies.csv")
    errors = []

    if len(rows) != 1:
        errors.append(f"Expected 1 study row, got {len(rows)}")
    study = rows[0]

    print(f"  Study ID:    {study['study_id']}")
    print(f"  Title:       {study['title'][:70]}...")
    print(f"  Author:      {study['author']}")
    print(f"  Date:        {study['date']}")
    print(f"  Type:        {study['type']}")
    print(f"  Domain:      {study['subject_domain']}")
    print(f"  Methodology: {study['methodology']}")
    print(f"  License:     {study['license']}")

    # Validate assessment ratings are text values
    for dim in ["importance", "relevance", "prescience"]:
        val = study[dim]
        if val not in VALID_RATINGS:
            errors.append(f"{dim} = '{val}' (must be one of {VALID_RATINGS})")
        else:
            print(f"  {dim.capitalize():12s}: {val}")

    field_count = len(study)
    print(f"  Fields:      {field_count} (expected 16)")
    if field_count != 16:
        errors.append(f"Expected 16 fields, got {field_count}")

    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
    print()
    return len(errors) == 0


def validate_entities(root):
    """Validate entities.csv content."""
    print("=" * 60)
    print("ENTITIES VALIDATION")
    print("=" * 60)
    rows = load_csv(root, "entities.csv")
    errors = []

    print(f"  Total entities: {len(rows)}")
    print(f"  Fields per row: {len(rows[0])}")

    # Check entity_id format (must be canonical lowercase hyphenated, not ENT-NNN)
    for r in rows:
        eid = r["entity_id"]
        if eid.startswith("ENT-") and eid[4:].isdigit():
            errors.append(f"entity_id '{eid}' uses ENT-NNN format; must be canonical lowercase hyphenated name")
        if eid != eid.lower():
            errors.append(f"entity_id '{eid}' is not lowercase")

    # Entity type breakdown
    type_counts = Counter(r["entity_type"] for r in rows)
    print(f"  Entity type breakdown:")
    for t, c in sorted(type_counts.items()):
        print(f"    {t}: {c}")

    # Status breakdown
    status_counts = Counter(r["status"] for r in rows)
    print(f"  Status breakdown:")
    for s, c in sorted(status_counts.items()):
        print(f"    {s}: {c}")

    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
    print()
    return len(errors) == 0


def validate_technologies(root):
    """Validate technologies.csv content."""
    print("=" * 60)
    print("TECHNOLOGIES VALIDATION")
    print("=" * 60)
    rows = load_csv(root, "technologies.csv")
    errors = []

    print(f"  Total technologies: {len(rows)}")

    # Check tech_id format (must be canonical lowercase hyphenated, not TECH-NNN)
    for r in rows:
        tid = r["tech_id"]
        if tid.startswith("TECH-") and tid[5:].isdigit():
            errors.append(f"tech_id '{tid}' uses TECH-NNN format; must be canonical lowercase hyphenated name")
        if tid != tid.lower():
            errors.append(f"tech_id '{tid}' is not lowercase")

    for r in rows:
        print(f"    {r['tech_id']}: {r['tech_name']} [{r['category']}] "
              f"({r['lifecycle_at_study']} -> {r['lifecycle_current']})")

    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
    print()
    return len(errors) == 0


def validate_observations(root):
    """Validate observations.csv content and referential integrity."""
    print("=" * 60)
    print("OBSERVATIONS VALIDATION")
    print("=" * 60)
    rows = load_csv(root, "observations.csv")
    errors = []

    print(f"  Total observations: {len(rows)}")
    print(f"  Fields per row: {len(rows[0])}")

    # Load reference tables
    entities = load_csv(root, "entities.csv")
    entity_ids = {e["entity_id"] for e in entities}
    techs = load_csv(root, "technologies.csv")
    tech_ids = {t["tech_id"] for t in techs}

    # Validate observation types
    type_counts = Counter()
    for r in rows:
        obs_type = r["observation_type"]
        type_counts[obs_type] += 1
        if obs_type not in CANONICAL_OBS_TYPES:
            errors.append(f"{r['obs_id']} has invalid observation_type: '{obs_type}'")

    print(f"  Observation type breakdown:")
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        valid = "OK" if t in CANONICAL_OBS_TYPES else "INVALID"
        print(f"    [{valid}] {t}: {c}")

    # Validate obs_id format (OBS-NNN)
    for r in rows:
        obs_id = r["obs_id"]
        if not obs_id.startswith("OBS-"):
            errors.append(f"{obs_id} does not start with 'OBS-'")

    # Validate confidence values
    for r in rows:
        conf = r["confidence"]
        if conf not in VALID_CONFIDENCE:
            errors.append(f"{r['obs_id']} has invalid confidence: '{conf}' (must be one of {VALID_CONFIDENCE})")

    # Validate methodology codes
    for r in rows:
        meth = r["methodology_code"]
        if meth and meth not in VALID_METHODOLOGY:
            errors.append(f"{r['obs_id']} has invalid methodology_code: '{meth}' (must be one of {VALID_METHODOLOGY})")

    # Validate entity_id is single-valued (no commas)
    for r in rows:
        if r["entity_id"] and "," in r["entity_id"]:
            errors.append(f"{r['obs_id']} has comma-separated entity_id: '{r['entity_id']}'")

    # Validate entity_id and tech_id foreign key references
    for r in rows:
        if r["entity_id"] and r["entity_id"] not in entity_ids:
            errors.append(f"{r['obs_id']} references unknown entity_id: '{r['entity_id']}'")
        if r["tech_id"] and r["tech_id"] not in tech_ids:
            errors.append(f"{r['obs_id']} references unknown tech_id: '{r['tech_id']}'")

    if errors:
        print(f"\n  VALIDATION ERRORS ({len(errors)}):")
        for e in errors:
            print(f"    ERROR: {e}")
    else:
        print(f"\n  All observation types are canonical: PASS")
        print(f"  All obs_ids use OBS-NNN format: PASS")
        print(f"  All confidence values are valid text: PASS")
        print(f"  All methodology codes are standard: PASS")
        print(f"  All entity_ids are single-valued: PASS")
        print(f"  All foreign key references valid: PASS")

    print()
    return len(errors) == 0


def validate_codes(root):
    """Validate codes.csv content."""
    print("=" * 60)
    print("CODES VALIDATION")
    print("=" * 60)
    rows = load_csv(root, "codes.csv")
    errors = []

    print(f"  Total codes: {len(rows)}")

    type_counts = Counter(r["code_type"] for r in rows)
    print(f"  Code type breakdown:")
    for t, c in sorted(type_counts.items()):
        print(f"    {t}: {c}")

    # Verify all 8 observation types are defined
    obs_type_codes = {r["code_id"] for r in rows if r["code_type"] == "observation_type"}
    missing_obs_types = CANONICAL_OBS_TYPES - obs_type_codes
    if missing_obs_types:
        errors.append(f"Missing observation_type codes: {missing_obs_types}")

    # Verify all confidence levels are defined
    conf_codes = {r["code_id"] for r in rows if r["code_type"] == "confidence"}
    missing_conf = VALID_CONFIDENCE - conf_codes
    if missing_conf:
        errors.append(f"Missing confidence codes: {missing_conf}")

    # Verify all methodology codes are defined
    meth_codes = {r["code_id"] for r in rows if r["code_type"] == "methodology_code"}
    missing_meth = VALID_METHODOLOGY - meth_codes
    if missing_meth:
        errors.append(f"Missing methodology codes: {missing_meth}")

    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
    else:
        print(f"  All 8 observation types defined: PASS")
        print(f"  All 4 confidence levels defined: PASS")
        print(f"  All 6 methodology codes defined: PASS")

    print()
    return len(errors) == 0


def validate_datapackage_json(root):
    """Validate datapackage.json structure."""
    print("=" * 60)
    print("DATAPACKAGE.JSON VALIDATION")
    print("=" * 60)
    errors = []

    with open(root / "datapackage.json", "r") as f:
        pkg = json.load(f)

    print(f"  Name:      {pkg.get('name')}")
    print(f"  Version:   {pkg.get('version')}")
    print(f"  Resources: {len(pkg.get('resources', []))}")

    expected_resources = {"studies", "entities", "technologies", "observations", "codes"}
    actual_resources = {r["name"] for r in pkg.get("resources", [])}
    missing = expected_resources - actual_resources
    if missing:
        errors.append(f"Missing resources: {missing}")

    for res in pkg.get("resources", []):
        fields = len(res.get("schema", {}).get("fields", []))
        print(f"    {res['name']}: {res['path']} ({fields} fields)")

    # Check confidence enum uses text values
    obs_resource = next((r for r in pkg["resources"] if r["name"] == "observations"), None)
    if obs_resource:
        conf_field = next((f for f in obs_resource["schema"]["fields"] if f["name"] == "confidence"), None)
        if conf_field:
            enum_vals = set(conf_field.get("constraints", {}).get("enum", []))
            if "CONF-HIGH" in enum_vals:
                errors.append("confidence enum uses CONF-HIGH format; must use text values (high, medium, low, verified)")

    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
    print()
    return len(errors) == 0


def validate_schema_org(root):
    """Validate schema_org.json structure."""
    print("=" * 60)
    print("SCHEMA.ORG JSON-LD VALIDATION")
    print("=" * 60)
    errors = []

    with open(root / "schema" / "schema_org.json", "r") as f:
        schema = json.load(f)

    print(f"  @type:         {schema.get('@type')}")
    print(f"  name:          {schema.get('name', '')[:60]}...")
    print(f"  identifier:    {schema.get('identifier')}")
    print(f"  datePublished: {schema.get('datePublished')}")
    print(f"  keywords:      {len(schema.get('keywords', []))} items")
    print(f"  distributions: {len(schema.get('distribution', []))} items")

    if schema.get("@type") != "Dataset":
        errors.append(f"@type should be 'Dataset', got '{schema.get('@type')}'")
    if not schema.get("@context"):
        errors.append("Missing @context")

    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
    print()
    return len(errors) == 0


def demo_analysis(root):
    """Run a brief analysis on the extracted observations."""
    print("=" * 60)
    print("DEMO ANALYSIS: Key Findings")
    print("=" * 60)

    observations = load_csv(root, "observations.csv")
    entities = load_csv(root, "entities.csv")
    entity_map = {e["entity_id"]: e["entity_name"] for e in entities}

    # Framework factors by firm
    framework = [r for r in observations if r["observation_type"] == "framework-factor"]
    print(f"\n  Framework Factors: {len(framework)}")
    for f in framework:
        name = entity_map.get(f["entity_id"], f["entity_id"] or "(cross-firm)")
        print(f"    {f['obs_id']}: {name} -- {f['metric_name']}")

    # Technology assessments
    tech_assess = [r for r in observations if r["observation_type"] == "technology-assessment"]
    print(f"\n  Technology Assessments: {len(tech_assess)}")
    for t in tech_assess:
        name = entity_map.get(t["entity_id"], t["entity_id"] or "(industry-level)")
        print(f"    {t['obs_id']}: {name} -- {t['metric_name']}")

    # Expert opinions
    opinions = [r for r in observations if r["observation_type"] == "expert-opinion"]
    print(f"\n  Expert Opinions: {len(opinions)}")
    for o in opinions:
        name = entity_map.get(o["entity_id"], o["entity_id"] or "(industry-level)")
        print(f"    {o['obs_id']}: {name} -- {o['metric_value'][:80]}")

    # Acquired entities
    acquired = [e for e in entities if e["status"] == "acquired"]
    print(f"\n  Entities Subsequently Acquired: {len(acquired)}")
    for a in acquired:
        print(f"    {a['entity_name']} -> {a['successor']} ({a['years_active']})")

    # Firms by entity type
    vendors = [e for e in entities if e["entity_type"] == "vendor"]
    print(f"\n  Vendor Firms Profiled: {len(vendors)}")
    for v in vendors:
        print(f"    {v['entity_name']} [{v['status']}]")

    print()


def main():
    root = find_package_root()
    print(f"\nData Package Root: {root}\n")

    results = []
    results.append(("File Structure", validate_file_structure(root)))
    results.append(("datapackage.json", validate_datapackage_json(root)))
    results.append(("schema_org.json", validate_schema_org(root)))
    results.append(("studies.csv", validate_studies(root)))
    results.append(("entities.csv", validate_entities(root)))
    results.append(("technologies.csv", validate_technologies(root)))
    results.append(("observations.csv", validate_observations(root)))
    results.append(("codes.csv", validate_codes(root)))

    demo_analysis(root)

    # Summary
    print("=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    all_pass = True
    for name, passed in results:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {name}")
        if not passed:
            all_pass = False

    if all_pass:
        print("\n  All validations passed successfully.")
    else:
        print("\n  Some validations failed. Review errors above.")

    print()
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
