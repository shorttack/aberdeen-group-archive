#!/usr/bin/env python3
"""
Demo analysis script for the SARS May Impact Global Electronics Industry data package.
Study ID: 2003-sars2-hot-topic-deb75d

Loads all CSVs, validates referential integrity, checks codes, and prints summary statistics.
"""

import csv
import json
import sys
from collections import Counter
from pathlib import Path


def load_csv(filepath):
    """Load a CSV file and return list of dictionaries."""
    with open(filepath, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    # Determine base path (script is in scripts/, data is in data/)
    script_dir = Path(__file__).resolve().parent
    base_dir = script_dir.parent
    data_dir = base_dir / "data"

    print("=" * 70)
    print("SARS May Impact Global Electronics Industry")
    print("Study ID: 2003-sars2-hot-topic-deb75d")
    print("=" * 70)

    # --- Load all CSVs ---
    print("\n1. Loading data files...")
    studies = load_csv(data_dir / "studies.csv")
    entities = load_csv(data_dir / "entities.csv")
    technologies = load_csv(data_dir / "technologies.csv")
    observations = load_csv(data_dir / "observations.csv")
    codes = load_csv(data_dir / "codes.csv")

    print(f"   studies.csv:       {len(studies)} rows")
    print(f"   entities.csv:      {len(entities)} rows")
    print(f"   technologies.csv:  {len(technologies)} rows")
    print(f"   observations.csv:  {len(observations)} rows")
    print(f"   codes.csv:         {len(codes)} rows")

    # --- Validate datapackage.json exists ---
    print("\n2. Checking datapackage.json...")
    dp_path = base_dir / "datapackage.json"
    if dp_path.exists():
        with open(dp_path) as f:
            dp = json.load(f)
        print(f"   Package name: {dp['name']}")
        print(f"   Resources defined: {len(dp['resources'])}")
        resource_names = [r["name"] for r in dp["resources"]]
        print(f"   Resource names: {', '.join(resource_names)}")
    else:
        print("   WARNING: datapackage.json not found!")

    # --- Validate study IDs ---
    print("\n3. Validating referential integrity...")
    errors = []

    study_ids = {s["study_id"] for s in studies}
    entity_ids = {e["entity_id"] for e in entities}
    tech_ids = {t["tech_id"] for t in technologies}

    # Check entities reference valid study_ids
    for entity in entities:
        if entity["study_id"] not in study_ids:
            errors.append(f"Entity '{entity['entity_id']}' references unknown study_id '{entity['study_id']}'")

    # Check technologies reference valid study_ids
    for tech in technologies:
        if tech["study_id"] not in study_ids:
            errors.append(f"Technology '{tech['tech_id']}' references unknown study_id '{tech['study_id']}'")

    # Check observations reference valid study_ids, entity_ids, and tech_ids
    for obs in observations:
        if obs["study_id"] not in study_ids:
            errors.append(f"Observation '{obs['obs_id']}' references unknown study_id '{obs['study_id']}'")
        if obs["entity_id"] and obs["entity_id"] not in entity_ids:
            errors.append(f"Observation '{obs['obs_id']}' references unknown entity_id '{obs['entity_id']}'")
        if obs["tech_id"] and obs["tech_id"] not in tech_ids:
            errors.append(f"Observation '{obs['obs_id']}' references unknown tech_id '{obs['tech_id']}'")

    if errors:
        print(f"   ERRORS FOUND: {len(errors)}")
        for err in errors:
            print(f"     - {err}")
    else:
        print("   All references valid. No integrity errors found.")

    # --- Validate observation types against codes ---
    print("\n4. Validating observation types against codes...")
    valid_obs_types = {
        "strategy-classification", "viability-prediction", "actual-outcome",
        "technology-assessment", "benchmark-result", "framework-factor",
        "market-data", "expert-opinion"
    }
    code_obs_types = {c["code_id"] for c in codes if c["code_type"] == "observation_type"}

    obs_type_errors = []
    for obs in observations:
        if obs["observation_type"] not in valid_obs_types:
            obs_type_errors.append(f"Observation '{obs['obs_id']}' has invalid type '{obs['observation_type']}'")

    if obs_type_errors:
        print(f"   ERRORS: {len(obs_type_errors)}")
        for err in obs_type_errors:
            print(f"     - {err}")
    else:
        print("   All observation types are valid.")

    # Check codes table covers all valid types
    missing_in_codes = valid_obs_types - code_obs_types
    if missing_in_codes:
        print(f"   WARNING: observation types missing from codes.csv: {missing_in_codes}")
    else:
        print("   All 8 observation types defined in codes.csv.")

    # --- Validate confidence values ---
    print("\n5. Validating confidence values...")
    valid_confidence = {"high", "medium", "low", "verified"}
    conf_errors = []
    for obs in observations:
        if obs["confidence"] not in valid_confidence:
            conf_errors.append(f"Observation '{obs['obs_id']}' has invalid confidence '{obs['confidence']}'")
    if conf_errors:
        print(f"   ERRORS: {len(conf_errors)}")
        for err in conf_errors:
            print(f"     - {err}")
    else:
        print("   All confidence values are valid.")

    # --- Validate methodology codes ---
    print("\n6. Validating methodology codes...")
    valid_methods = {
        "industry-analysis", "competitive-profiling", "benchmarking",
        "field-research", "document-review", "statistical-analysis"
    }
    method_errors = []
    for obs in observations:
        if obs["methodology_code"] and obs["methodology_code"] not in valid_methods:
            method_errors.append(f"Observation '{obs['obs_id']}' has invalid methodology '{obs['methodology_code']}'")
    if method_errors:
        print(f"   ERRORS: {len(method_errors)}")
        for err in method_errors:
            print(f"     - {err}")
    else:
        print("   All methodology codes are valid.")

    # --- Summary statistics ---
    print("\n7. Observation summary by type:")
    type_counts = Counter(obs["observation_type"] for obs in observations)
    for obs_type, count in type_counts.most_common():
        print(f"   {obs_type}: {count}")

    print("\n8. Observations by confidence level:")
    conf_counts = Counter(obs["confidence"] for obs in observations)
    for conf, count in conf_counts.most_common():
        print(f"   {conf}: {count}")

    print("\n9. Entity status summary:")
    status_counts = Counter(e["status"] for e in entities)
    for status, count in status_counts.most_common():
        print(f"   {status}: {count}")

    # --- Prescience analysis: predictions vs outcomes ---
    print("\n10. Prescience analysis:")
    predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outcomes_2020_plus = [
        o for o in observations
        if o["observation_type"] == "actual-outcome" and o["year_observed"] and int(o["year_observed"]) >= 2020
    ]
    print(f"    Predictions made in 2003: {len(predictions)}")
    print(f"    Validated outcomes (2020+): {len(outcomes_2020_plus)}")

    print("\n    2003 Predictions:")
    for p in predictions:
        print(f"      {p['obs_id']}: {p['metric_name']} = {p['metric_value']}")

    print("\n    COVID-era Outcomes:")
    for o in outcomes_2020_plus:
        print(f"      {o['obs_id']}: {o['metric_name']} = {o['metric_value']}")

    # --- Final summary ---
    total_errors = len(errors) + len(obs_type_errors) + len(conf_errors) + len(method_errors)
    print("\n" + "=" * 70)
    if total_errors == 0:
        print("VALIDATION PASSED: All integrity checks passed with 0 errors.")
    else:
        print(f"VALIDATION FAILED: {total_errors} error(s) found.")
    print("=" * 70)

    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
