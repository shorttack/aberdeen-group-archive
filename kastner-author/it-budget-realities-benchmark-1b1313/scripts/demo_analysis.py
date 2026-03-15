#!/usr/bin/env python3
"""
Demo Analysis Script for: The Strategic Enterprise IT Budget Realities Benchmark Report
Study ID: it-budget-realities-benchmark-1b1313
Archival Ingest Skill v13

Loads all 5 CSVs, prints summary statistics, validates referential integrity,
checks codes coverage, and cross-references predictions vs actual outcomes.
"""

import csv
import os
import sys
from collections import Counter
from pathlib import Path


def load_csv(filepath):
    """Load a CSV file and return list of dicts."""
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def main():
    # Determine base directory (script is in scripts/, data is in data/)
    script_dir = Path(__file__).resolve().parent
    base_dir = script_dir.parent
    data_dir = base_dir / "data"

    print("=" * 70)
    print("IT Budget Realities Benchmark Report - Demo Analysis")
    print("Study ID: it-budget-realities-benchmark-1b1313")
    print("=" * 70)

    # --- Load all CSVs ---
    print("\n[1] Loading CSV files...")
    try:
        studies = load_csv(data_dir / "studies.csv")
        entities = load_csv(data_dir / "entities.csv")
        technologies = load_csv(data_dir / "technologies.csv")
        observations = load_csv(data_dir / "observations.csv")
        codes = load_csv(data_dir / "codes.csv")
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    print(f"  studies.csv:      {len(studies)} row(s)")
    print(f"  entities.csv:     {len(entities)} row(s)")
    print(f"  technologies.csv: {len(technologies)} row(s)")
    print(f"  observations.csv: {len(observations)} row(s)")
    print(f"  codes.csv:        {len(codes)} row(s)")

    # --- Summary Statistics ---
    print("\n[2] Summary Statistics")
    print("-" * 40)

    if studies:
        s = studies[0]
        print(f"  Title:    {s['title']}")
        print(f"  Author:   {s['author']}")
        print(f"  Date:     {s['date']}")
        print(f"  Type:     {s['type']}")
        print(f"  Domain:   {s['subject_domain']}")
        print(f"  License:  {s['license']}")
        print(f"  Importance:  {s['importance']}")
        print(f"  Relevance:   {s['relevance']}")
        print(f"  Prescience:  {s['prescience']}")

    # Entity types
    entity_types = Counter(e["entity_type"] for e in entities)
    print(f"\n  Entity types:")
    for etype, count in entity_types.most_common():
        print(f"    {etype}: {count}")

    # Entity statuses
    entity_statuses = Counter(e["status"] for e in entities)
    print(f"\n  Entity statuses:")
    for status, count in entity_statuses.most_common():
        print(f"    {status}: {count}")

    # Technology categories
    tech_cats = Counter(t["category"] for t in technologies)
    print(f"\n  Technology categories:")
    for cat, count in tech_cats.most_common():
        print(f"    {cat}: {count}")

    # Technology lifecycle at study
    tech_lifecycle = Counter(t["lifecycle_at_study"] for t in technologies)
    print(f"\n  Technology lifecycle (at study):")
    for lc, count in tech_lifecycle.most_common():
        print(f"    {lc}: {count}")

    # Observation types
    obs_types = Counter(o["observation_type"] for o in observations)
    print(f"\n  Observation types:")
    for otype, count in obs_types.most_common():
        print(f"    {otype}: {count}")

    # Confidence levels
    conf_levels = Counter(o["confidence"] for o in observations)
    print(f"\n  Confidence levels:")
    for cl, count in conf_levels.most_common():
        print(f"    {cl}: {count}")

    # Methodology codes
    meth_codes = Counter(o["methodology_code"] for o in observations)
    print(f"\n  Methodology codes used:")
    for mc, count in meth_codes.most_common():
        print(f"    {mc}: {count}")

    # --- Referential Integrity ---
    print("\n[3] Referential Integrity Checks")
    print("-" * 40)
    errors = 0

    study_ids = {s["study_id"] for s in studies}
    entity_ids = {e["entity_id"] for e in entities}
    tech_ids = {t["tech_id"] for t in technologies}

    # Check entities reference valid study_id
    for e in entities:
        if e["study_id"] not in study_ids:
            print(f"  ERROR: Entity '{e['entity_id']}' references unknown study_id '{e['study_id']}'")
            errors += 1

    # Check technologies reference valid study_id
    for t in technologies:
        if t["study_id"] not in study_ids:
            print(f"  ERROR: Technology '{t['tech_id']}' references unknown study_id '{t['study_id']}'")
            errors += 1

    # Check observations reference valid study_id, entity_id, tech_id
    for o in observations:
        if o["study_id"] not in study_ids:
            print(f"  ERROR: Observation '{o['obs_id']}' references unknown study_id '{o['study_id']}'")
            errors += 1
        if o["entity_id"] and o["entity_id"] not in entity_ids:
            print(f"  ERROR: Observation '{o['obs_id']}' references unknown entity_id '{o['entity_id']}'")
            errors += 1
        if o["tech_id"] and o["tech_id"] not in tech_ids:
            print(f"  ERROR: Observation '{o['obs_id']}' references unknown tech_id '{o['tech_id']}'")
            errors += 1

    # Check observation obs_id uniqueness
    obs_id_list = [o["obs_id"] for o in observations]
    obs_id_dupes = [oid for oid, count in Counter(obs_id_list).items() if count > 1]
    if obs_id_dupes:
        for oid in obs_id_dupes:
            print(f"  ERROR: Duplicate obs_id '{oid}'")
            errors += 1

    if errors == 0:
        print("  All referential integrity checks PASSED")
    else:
        print(f"  {errors} referential integrity error(s) found")

    # --- Codes Coverage ---
    print("\n[4] Codes Coverage Check")
    print("-" * 40)
    code_ids = {c["code_id"] for c in codes}
    code_types = {c["code_type"]: [] for c in codes}
    for c in codes:
        code_types[c["code_type"]].append(c["code_id"])

    print(f"  Code types defined: {', '.join(sorted(code_types.keys()))}")
    for ct, cids in sorted(code_types.items()):
        print(f"    {ct}: {len(cids)} codes")

    # Check observation methodology_codes are defined
    missing_meth = set()
    for o in observations:
        if o["methodology_code"] and o["methodology_code"] not in code_ids:
            missing_meth.add(o["methodology_code"])
    if missing_meth:
        print(f"  WARNING: Methodology codes used but not in codes.csv: {missing_meth}")
    else:
        print("  All methodology codes in observations are defined in codes.csv")

    # Check observation_types are defined
    missing_obs_types = set()
    for o in observations:
        if o["observation_type"] and o["observation_type"] not in code_ids:
            missing_obs_types.add(o["observation_type"])
    if missing_obs_types:
        print(f"  WARNING: Observation types used but not in codes.csv: {missing_obs_types}")
    else:
        print("  All observation types in observations are defined in codes.csv")

    # Check confidence levels are defined
    missing_conf = set()
    for o in observations:
        if o["confidence"] and o["confidence"] not in code_ids:
            missing_conf.add(o["confidence"])
    if missing_conf:
        print(f"  WARNING: Confidence levels used but not in codes.csv: {missing_conf}")
    else:
        print("  All confidence levels in observations are defined in codes.csv")

    # --- Predictions vs Outcomes ---
    print("\n[5] Predictions vs Actual Outcomes Cross-Reference")
    print("-" * 40)

    predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]

    print(f"  Predictions found: {len(predictions)}")
    for p in predictions:
        print(f"    [{p['obs_id']}] {p['metric_name']}: {p['metric_value']}")

    print(f"\n  Actual outcomes found: {len(outcomes)}")
    for a in outcomes:
        print(f"    [{a['obs_id']}] {a['metric_name']}: {a['metric_value']}")

    # --- PACE Framework Analysis ---
    print("\n[6] PACE Framework Factors")
    print("-" * 40)

    pace_factors = [o for o in observations if o["observation_type"] == "framework-factor"]
    print(f"  PACE factors extracted: {len(pace_factors)}")
    for p in pace_factors:
        print(f"    {p['metric_name']}: {p['metric_value']}")

    # --- Benchmark Results ---
    print("\n[7] Benchmark Results (Competitive Framework)")
    print("-" * 40)

    benchmarks = [o for o in observations if o["observation_type"] == "benchmark-result"]
    print(f"  Benchmark results extracted: {len(benchmarks)}")
    for b in benchmarks:
        print(f"    {b['metric_name']}: {b['metric_value']}")

    # --- Strategy Classifications ---
    print("\n[8] Strategy Classifications")
    print("-" * 40)

    strategies = [o for o in observations if o["observation_type"] == "strategy-classification"]
    print(f"  Strategy classifications: {len(strategies)}")
    for s in strategies:
        print(f"    {s['metric_name']}: {s['metric_value'][:80]}...")

    # --- Final Summary ---
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    total_records = len(studies) + len(entities) + len(technologies) + len(observations) + len(codes)
    print(f"  Total records across all tables: {total_records}")
    print(f"  Referential integrity errors:    {errors}")
    print(f"  Package status:                  {'VALID' if errors == 0 else 'ERRORS FOUND'}")
    print("=" * 70)

    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
