#!/usr/bin/env python3
"""
Demo Analysis Script for Eclipsys SunriseXA 3.3 Benchmark Audit Report
Study ID: 2004-eclipsys-auditor-report-4-3cd30c

This script demonstrates loading and analyzing the Frictionless Data Package
generated from the Aberdeen Group benchmark audit report (April 2004).
"""

import csv
import os
import json
from collections import Counter
from pathlib import Path


def load_csv(filepath):
    """Load a CSV file and return a list of dictionaries."""
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def main():
    # Determine the base directory (parent of scripts/)
    base_dir = Path(__file__).resolve().parent.parent
    data_dir = base_dir / "data"

    print("=" * 70)
    print("Eclipsys SunriseXA 3.3 Benchmark Audit Report - Data Package Analysis")
    print("=" * 70)

    # --- Load study metadata ---
    studies = load_csv(data_dir / "studies.csv")
    study = studies[0]
    print(f"\nStudy: {study['title']}")
    print(f"Author: {study['author']}")
    print(f"Date: {study['date']}")
    print(f"Type: {study['type']}")
    print(f"Domain: {study['subject_domain']}")
    print(f"Methodology: {study['methodology']}")
    print(f"Assessment: importance={study['importance']}, "
          f"relevance={study['relevance']}, prescience={study['prescience']}")

    # --- Load and summarize entities ---
    entities = load_csv(data_dir / "entities.csv")
    print(f"\n--- Entities ({len(entities)} total) ---")
    entity_types = Counter(e["entity_type"] for e in entities)
    for etype, count in entity_types.most_common():
        print(f"  {etype}: {count}")
    for e in entities:
        status_str = f" [{e['status']}]" if e.get("status") else ""
        print(f"  - {e['entity_name']} ({e['entity_type']}){status_str}")

    # --- Load and summarize technologies ---
    technologies = load_csv(data_dir / "technologies.csv")
    print(f"\n--- Technologies ({len(technologies)} total) ---")
    tech_categories = Counter(t["category"] for t in technologies)
    for tcat, count in tech_categories.most_common():
        print(f"  {tcat}: {count}")
    for t in technologies:
        lifecycle = f" [{t['lifecycle_at_study']} -> {t['lifecycle_current']}]"
        print(f"  - {t['tech_name']} ({t['vendor']}){lifecycle}")

    # --- Load and analyze observations ---
    observations = load_csv(data_dir / "observations.csv")
    print(f"\n--- Observations ({len(observations)} total) ---")

    # Count by observation type
    obs_types = Counter(o["observation_type"] for o in observations)
    print("\nBy observation type:")
    for otype, count in obs_types.most_common():
        print(f"  {otype}: {count}")

    # Count by entity
    obs_entities = Counter(o["entity_id"] for o in observations if o["entity_id"])
    print("\nBy entity:")
    for eid, count in obs_entities.most_common():
        print(f"  {eid}: {count}")

    # Count by confidence
    obs_confidence = Counter(o["confidence"] for o in observations)
    print("\nBy confidence level:")
    for conf, count in obs_confidence.most_common():
        print(f"  {conf}: {count}")

    # Count by methodology
    obs_methodology = Counter(o["methodology_code"] for o in observations)
    print("\nBy methodology:")
    for meth, count in obs_methodology.most_common():
        print(f"  {meth}: {count}")

    # --- Benchmark results analysis ---
    print("\n--- Benchmark Performance Summary ---")
    benchmark_obs = [o for o in observations
                     if o["observation_type"] == "benchmark-result"]
    print(f"Total benchmark observations: {len(benchmark_obs)}")

    print("\nBenchmark Results:")
    print(f"  {'Metric':<45} {'Value':<35}")
    print(f"  {'-'*45} {'-'*35}")
    for obs in benchmark_obs:
        print(f"  {obs['metric_name']:<45} {obs['metric_value']:<35}")

    # --- Expert opinions ---
    print("\n--- Expert Opinions ---")
    expert_obs = [o for o in observations
                  if o["observation_type"] == "expert-opinion"]
    for o in expert_obs:
        print(f"  [{o['obs_id']}] {o['metric_name']}: {o['metric_value']}")

    # --- Actual outcomes ---
    print("\n--- Actual Outcomes (Post-Hoc) ---")
    outcomes = [o for o in observations
                if o["observation_type"] == "actual-outcome"]
    for o in outcomes:
        print(f"  [{o['obs_id']}] {o['entity_id']}: {o['metric_value']}")

    # --- Referential integrity checks ---
    print("\n--- Referential Integrity Checks ---")
    entity_ids = {e["entity_id"] for e in entities}
    tech_ids = {t["tech_id"] for t in technologies}
    study_ids = {s["study_id"] for s in studies}

    errors = []
    for obs in observations:
        if obs["study_id"] not in study_ids:
            errors.append(
                f"  {obs['obs_id']}: study_id '{obs['study_id']}' not found")
        if obs["entity_id"] and obs["entity_id"] not in entity_ids:
            errors.append(
                f"  {obs['obs_id']}: entity_id '{obs['entity_id']}' not found")
        if obs["tech_id"] and obs["tech_id"] not in tech_ids:
            errors.append(
                f"  {obs['obs_id']}: tech_id '{obs['tech_id']}' not found")

    for ent in entities:
        if ent["study_id"] not in study_ids:
            errors.append(
                f"  entity '{ent['entity_id']}': "
                f"study_id '{ent['study_id']}' not found")

    for tech in technologies:
        if tech["study_id"] not in study_ids:
            errors.append(
                f"  tech '{tech['tech_id']}': "
                f"study_id '{tech['study_id']}' not found")

    if errors:
        print(f"  ERRORS FOUND ({len(errors)}):")
        for err in errors:
            print(err)
    else:
        print("  All referential integrity checks passed.")

    # --- Validate observation types ---
    print("\n--- Observation Type Validation ---")
    valid_types = {
        "strategy-classification", "viability-prediction", "actual-outcome",
        "technology-assessment", "benchmark-result", "framework-factor",
        "market-data", "expert-opinion"
    }
    all_types = set(o["observation_type"] for o in observations)
    invalid = all_types - valid_types
    if invalid:
        print(f"  WARNING: Invalid observation types found: {invalid}")
    else:
        print(f"  All {len(all_types)} observation types are valid "
              f"canonical values.")

    # --- Load codes ---
    codes = load_csv(data_dir / "codes.csv")
    print(f"\n--- Codes ({len(codes)} total) ---")
    code_types = Counter(c["code_type"] for c in codes)
    for ctype, count in code_types.most_common():
        print(f"  {ctype}: {count}")

    # --- Validate datapackage.json ---
    dp_path = base_dir / "datapackage.json"
    if dp_path.exists():
        with open(dp_path, "r") as f:
            dp = json.load(f)
        print(f"\n--- Data Package Validation ---")
        print(f"  Name: {dp.get('name', 'N/A')}")
        print(f"  Resources: {len(dp.get('resources', []))}")
        for r in dp.get("resources", []):
            rpath = data_dir / os.path.basename(r.get("path", ""))
            exists = rpath.exists()
            status = "OK" if exists else "MISSING"
            print(f"    - {r.get('name', 'N/A')}: "
                  f"{r.get('path', 'N/A')} [{status}]")
    else:
        print(f"\n  datapackage.json not found at {dp_path}")

    print("\n" + "=" * 70)
    print("Analysis complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()
