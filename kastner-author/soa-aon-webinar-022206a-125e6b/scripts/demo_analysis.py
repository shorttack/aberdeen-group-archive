#!/usr/bin/env python3
"""
demo_analysis.py — Validation and analysis script for Archival Ingest Skill v13 package.

Study: Enterprise Integration Technology: Aberdeen Group's Market Trends & Research for 2006
Study ID: soa-aon-webinar-022206a-125e6b
Created: 2026-03-15
"""

import csv
import json
import os
import sys
from pathlib import Path


def get_package_root():
    """Determine the package root directory."""
    script_dir = Path(__file__).resolve().parent
    return script_dir.parent


def validate_csv(filepath, expected_columns, resource_name):
    """Validate a CSV file exists, has expected columns, and return row count."""
    errors = []
    row_count = 0

    if not filepath.exists():
        errors.append(f"MISSING: {filepath}")
        return 0, errors

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            actual_columns = reader.fieldnames or []

            # Check column names
            missing_cols = set(expected_columns) - set(actual_columns)
            extra_cols = set(actual_columns) - set(expected_columns)

            if missing_cols:
                errors.append(f"{resource_name}: missing columns: {missing_cols}")
            if extra_cols:
                errors.append(f"{resource_name}: unexpected columns: {extra_cols}")

            # Count rows and check for empty required fields
            for row in reader:
                row_count += 1

        if row_count == 0:
            errors.append(f"{resource_name}: no data rows found")

    except Exception as e:
        errors.append(f"{resource_name}: read error: {e}")

    return row_count, errors


def validate_json(filepath, resource_name):
    """Validate a JSON file exists and is parseable."""
    errors = []

    if not filepath.exists():
        errors.append(f"MISSING: {filepath}")
        return None, errors

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data, errors
    except json.JSONDecodeError as e:
        errors.append(f"{resource_name}: JSON parse error: {e}")
        return None, errors


def validate_package():
    """Run full package validation."""
    root = get_package_root()
    all_errors = []
    stats = {}

    print("=" * 70)
    print("Archival Ingest Skill v13 — Package Validation")
    print(f"Study ID: soa-aon-webinar-022206a-125e6b")
    print(f"Package root: {root}")
    print("=" * 70)

    # 1. Validate datapackage.json
    print("\n[1/7] Validating datapackage.json...")
    dp_data, dp_errors = validate_json(root / "datapackage.json", "datapackage.json")
    all_errors.extend(dp_errors)
    if dp_data:
        print(f"  Name: {dp_data.get('name', 'N/A')}")
        print(f"  Version: {dp_data.get('version', 'N/A')}")
        print(f"  Created: {dp_data.get('created', 'N/A')}")
        print(f"  Resources: {len(dp_data.get('resources', []))}")
        print("  OK")
    else:
        print("  FAILED")

    # 2. Validate studies.csv
    print("\n[2/7] Validating data/studies.csv...")
    studies_cols = [
        "study_id", "title", "author", "date", "type", "subject_domain",
        "methodology", "source_file", "abstract", "license", "importance",
        "importance_rationale", "relevance", "relevance_rationale",
        "prescience", "prescience_rationale"
    ]
    count, errs = validate_csv(root / "data" / "studies.csv", studies_cols, "studies.csv")
    all_errors.extend(errs)
    stats["studies"] = count
    print(f"  Records: {count}")
    print(f"  Columns: {len(studies_cols)}")
    print("  OK" if not errs else "  FAILED")

    # 3. Validate entities.csv
    print("\n[3/7] Validating data/entities.csv...")
    entities_cols = [
        "entity_id", "entity_name", "entity_type", "sector", "status",
        "successor", "years_active", "study_id", "notes"
    ]
    count, errs = validate_csv(root / "data" / "entities.csv", entities_cols, "entities.csv")
    all_errors.extend(errs)
    stats["entities"] = count
    print(f"  Records: {count}")
    print(f"  Columns: {len(entities_cols)}")
    print("  OK" if not errs else "  FAILED")

    # 4. Validate technologies.csv
    print("\n[4/7] Validating data/technologies.csv...")
    tech_cols = [
        "tech_id", "tech_name", "category", "vendor", "era",
        "lifecycle_at_study", "lifecycle_current", "study_id", "notes"
    ]
    count, errs = validate_csv(root / "data" / "technologies.csv", tech_cols, "technologies.csv")
    all_errors.extend(errs)
    stats["technologies"] = count
    print(f"  Records: {count}")
    print(f"  Columns: {len(tech_cols)}")
    print("  OK" if not errs else "  FAILED")

    # 5. Validate observations.csv
    print("\n[5/7] Validating data/observations.csv...")
    obs_cols = [
        "obs_id", "study_id", "entity_id", "tech_id", "observation_type",
        "year_observed", "metric_name", "metric_value", "confidence",
        "methodology_code", "source_page", "notes"
    ]
    count, errs = validate_csv(root / "data" / "observations.csv", obs_cols, "observations.csv")
    all_errors.extend(errs)
    stats["observations"] = count
    print(f"  Records: {count}")
    print(f"  Columns: {len(obs_cols)}")
    print("  OK" if not errs else "  FAILED")

    # 6. Validate codes.csv
    print("\n[6/7] Validating data/codes.csv...")
    codes_cols = ["code_id", "code_type", "label", "definition"]
    count, errs = validate_csv(root / "data" / "codes.csv", codes_cols, "codes.csv")
    all_errors.extend(errs)
    stats["codes"] = count
    print(f"  Records: {count}")
    print(f"  Columns: {len(codes_cols)}")
    print("  OK" if not errs else "  FAILED")

    # 7. Validate schema_org.json
    print("\n[7/7] Validating schema/schema_org.json...")
    schema_data, schema_errors = validate_json(
        root / "schema" / "schema_org.json", "schema_org.json"
    )
    all_errors.extend(schema_errors)
    if schema_data:
        print(f"  @type: {schema_data.get('@type', 'N/A')}")
        print(f"  identifier: {schema_data.get('identifier', 'N/A')}")
        print("  OK")
    else:
        print("  FAILED")

    # Check supporting files
    print("\n" + "-" * 70)
    print("Supporting Files:")
    for rel_path in ["source/original_text.md", "README.md", "scripts/demo_analysis.py"]:
        full_path = root / rel_path
        exists = full_path.exists()
        size = full_path.stat().st_size if exists else 0
        status = f"OK ({size:,} bytes)" if exists else "MISSING"
        print(f"  {rel_path}: {status}")

    # Referential integrity checks
    print("\n" + "-" * 70)
    print("Referential Integrity Checks:")

    # Load observation foreign keys
    obs_entity_ids = set()
    obs_tech_ids = set()
    obs_study_ids = set()
    obs_type_codes = set()
    obs_method_codes = set()
    obs_conf_codes = set()

    obs_path = root / "data" / "observations.csv"
    if obs_path.exists():
        with open(obs_path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("entity_id"):
                    obs_entity_ids.add(row["entity_id"])
                if row.get("tech_id"):
                    obs_tech_ids.add(row["tech_id"])
                if row.get("study_id"):
                    obs_study_ids.add(row["study_id"])
                if row.get("observation_type"):
                    obs_type_codes.add(row["observation_type"])
                if row.get("methodology_code"):
                    obs_method_codes.add(row["methodology_code"])
                if row.get("confidence"):
                    obs_conf_codes.add(row["confidence"])

    # Load valid entity IDs
    valid_entity_ids = set()
    ent_path = root / "data" / "entities.csv"
    if ent_path.exists():
        with open(ent_path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                valid_entity_ids.add(row["entity_id"])

    # Load valid tech IDs
    valid_tech_ids = set()
    tech_path = root / "data" / "technologies.csv"
    if tech_path.exists():
        with open(tech_path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                valid_tech_ids.add(row["tech_id"])

    # Load valid study IDs
    valid_study_ids = set()
    study_path = root / "data" / "studies.csv"
    if study_path.exists():
        with open(study_path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                valid_study_ids.add(row["study_id"])

    # Load valid codes
    valid_codes = set()
    codes_path = root / "data" / "codes.csv"
    if codes_path.exists():
        with open(codes_path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                valid_codes.add(row["code_id"])

    # Check entity FK
    orphan_entities = obs_entity_ids - valid_entity_ids
    if orphan_entities:
        msg = f"  Entity FK: FAIL — orphan IDs: {orphan_entities}"
        print(msg)
        all_errors.append(msg)
    else:
        print(f"  Entity FK: OK ({len(obs_entity_ids)} referenced, all valid)")

    # Check tech FK
    orphan_techs = obs_tech_ids - valid_tech_ids
    if orphan_techs:
        msg = f"  Tech FK: FAIL — orphan IDs: {orphan_techs}"
        print(msg)
        all_errors.append(msg)
    else:
        print(f"  Tech FK: OK ({len(obs_tech_ids)} referenced, all valid)")

    # Check study FK
    orphan_studies = obs_study_ids - valid_study_ids
    if orphan_studies:
        msg = f"  Study FK: FAIL — orphan IDs: {orphan_studies}"
        print(msg)
        all_errors.append(msg)
    else:
        print(f"  Study FK: OK ({len(obs_study_ids)} referenced, all valid)")

    # Check codes
    orphan_types = obs_type_codes - valid_codes
    orphan_methods = obs_method_codes - valid_codes
    orphan_confs = obs_conf_codes - valid_codes

    if orphan_types:
        msg = f"  Observation type codes: FAIL — unknown: {orphan_types}"
        print(msg)
        all_errors.append(msg)
    else:
        print(f"  Observation type codes: OK ({len(obs_type_codes)} used, all defined)")

    if orphan_methods:
        msg = f"  Methodology codes: FAIL — unknown: {orphan_methods}"
        print(msg)
        all_errors.append(msg)
    else:
        print(f"  Methodology codes: OK ({len(obs_method_codes)} used, all defined)")

    if orphan_confs:
        msg = f"  Confidence codes: FAIL — unknown: {orphan_confs}"
        print(msg)
        all_errors.append(msg)
    else:
        print(f"  Confidence codes: OK ({len(obs_conf_codes)} used, all defined)")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  Studies:       {stats.get('studies', 0)} records")
    print(f"  Entities:      {stats.get('entities', 0)} records")
    print(f"  Technologies:  {stats.get('technologies', 0)} records")
    print(f"  Observations:  {stats.get('observations', 0)} records")
    print(f"  Codes:         {stats.get('codes', 0)} records")

    total_records = sum(stats.values())
    print(f"  Total records: {total_records}")

    if all_errors:
        print(f"\n  ERRORS: {len(all_errors)}")
        for err in all_errors:
            print(f"    - {err}")
        print("\n  RESULT: FAIL")
        return 1
    else:
        print(f"\n  ERRORS: 0")
        print("\n  RESULT: PASS")
        return 0


def run_analysis():
    """Run basic analytical queries on the extracted data."""
    root = get_package_root()

    print("\n" + "=" * 70)
    print("ANALYSIS: SOA Adoption & KPI Data")
    print("=" * 70)

    obs_path = root / "data" / "observations.csv"
    if not obs_path.exists():
        print("  Cannot run analysis: observations.csv not found")
        return

    observations = []
    with open(obs_path, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            observations.append(row)

    # SOA adoption statistics
    print("\n--- Current SOA Adoption Distribution (2006) ---")
    adoption_obs = [
        o for o in observations
        if o["metric_name"].startswith("current_adoption_")
    ]
    for obs in sorted(adoption_obs, key=lambda x: x["obs_id"]):
        name = obs["metric_name"].replace("current_adoption_", "").replace("_", " ")
        print(f"  {name:>20s}: {obs['metric_value']}")

    # Top motives
    print("\n--- Top Motives Driving SOA Adoption ---")
    motive_obs = [
        o for o in observations
        if "motive" in o["metric_name"] or "top_motive" in o["metric_name"]
    ]
    for obs in sorted(motive_obs, key=lambda x: x["obs_id"]):
        name = obs["metric_name"].replace("top_motive_", "").replace("motive_", "").replace("_", " ")
        print(f"  {name:>40s}: {obs['metric_value']}")

    # KPI benchmarks
    print("\n--- Best-in-Class vs Average KPIs ---")
    kpi_obs = [
        o for o in observations
        if o["observation_type"] == "OT-KPI"
    ]
    for obs in sorted(kpi_obs, key=lambda x: x["obs_id"]):
        name = obs["metric_name"].replace("_", " ")
        print(f"  {name:>45s}: {obs['metric_value']}")

    # Market data
    print("\n--- Aberdeen Group Market Reach ---")
    market_obs = [
        o for o in observations
        if o["observation_type"] == "OT-MRKT"
    ]
    for obs in sorted(market_obs, key=lambda x: x["obs_id"]):
        name = obs["metric_name"].replace("_", " ")
        print(f"  {name:>45s}: {obs['metric_value']}")

    # Technology lifecycle summary
    print("\n--- Technology Lifecycle Summary ---")
    tech_path = root / "data" / "technologies.csv"
    if tech_path.exists():
        with open(tech_path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                print(
                    f"  {row['tech_name']:>45s}: "
                    f"{row['lifecycle_at_study']:>10s} (2006) -> "
                    f"{row['lifecycle_current']:<10s} (current)"
                )


if __name__ == "__main__":
    exit_code = validate_package()
    if exit_code == 0:
        run_analysis()
    sys.exit(exit_code)
