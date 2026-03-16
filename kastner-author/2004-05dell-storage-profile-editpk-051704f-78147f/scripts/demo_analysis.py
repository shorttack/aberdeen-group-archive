#!/usr/bin/env python3
"""
Demo analysis script for the Frictionless Data Package:
  Dell: Applying Its Business Value Model to Storage (Aberdeen Group, May 2004)

Study ID: 2004-05dell-storage-profile-editpk-051704f-78147f

This script demonstrates loading and analyzing the structured observations
extracted from the Aberdeen Group profile.
"""

import csv
import json
import os
from collections import Counter
from pathlib import Path


def load_csv(filepath):
    """Load a CSV file and return a list of dictionaries."""
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def main():
    # Determine package root (one level up from scripts/)
    script_dir = Path(__file__).resolve().parent
    package_dir = script_dir.parent

    print("=" * 72)
    print("FRICTIONLESS DATA PACKAGE ANALYSIS")
    print("Dell: Applying Its Business Value Model to Storage")
    print("Aberdeen Group, May 2004")
    print("=" * 72)
    print()

    # --- Load datapackage.json ---
    dp_path = package_dir / "datapackage.json"
    with open(dp_path, "r", encoding="utf-8") as f:
        datapackage = json.load(f)
    print(f"Package: {datapackage['name']}")
    print(f"Title:   {datapackage['title']}")
    print(f"Version: {datapackage['version']}")
    print(f"License: {datapackage['licenses'][0]['name']}")
    print()

    # --- Load all CSV data ---
    studies = load_csv(package_dir / "data" / "studies.csv")
    entities = load_csv(package_dir / "data" / "entities.csv")
    technologies = load_csv(package_dir / "data" / "technologies.csv")
    observations = load_csv(package_dir / "data" / "observations.csv")
    codes = load_csv(package_dir / "data" / "codes.csv")

    # --- Study Summary ---
    print("-" * 72)
    print("STUDY METADATA")
    print("-" * 72)
    study = studies[0]
    print(f"  Study ID:       {study['study_id']}")
    print(f"  Title:          {study['title']}")
    print(f"  Author:         {study['author']}")
    print(f"  Date:           {study['date']}")
    print(f"  Type:           {study['type']}")
    print(f"  Subject Domain: {study['subject_domain']}")
    print(f"  Methodology:    {study['methodology']}")
    print(f"  Importance:     {study['importance']}")
    print(f"  Relevance:      {study['relevance']}")
    print(f"  Prescience:     {study['prescience']}")
    print()

    # --- Entity Summary ---
    print("-" * 72)
    print(f"ENTITIES ({len(entities)} total)")
    print("-" * 72)
    entity_types = Counter(e["entity_type"] for e in entities)
    for etype, count in entity_types.most_common():
        print(f"  {etype}: {count}")
    print()
    for e in entities:
        print(f"  {e['entity_id']}: {e['entity_name']} ({e['entity_type']})")
    print()

    # --- Technology Summary ---
    print("-" * 72)
    print(f"TECHNOLOGIES ({len(technologies)} total)")
    print("-" * 72)
    tech_categories = Counter(t["category"] for t in technologies)
    for tcat, count in tech_categories.most_common():
        print(f"  {tcat}: {count}")
    print()
    for t in technologies:
        print(f"  {t['tech_id']}: {t['tech_name']} ({t['category']})")
    print()

    # --- Observation Analysis ---
    print("-" * 72)
    print(f"OBSERVATIONS ({len(observations)} total)")
    print("-" * 72)

    # By type
    obs_types = Counter(o["observation_type"] for o in observations)
    print("\n  By observation type:")
    for otype, count in obs_types.most_common():
        print(f"    {otype}: {count}")

    # By entity
    obs_entities = Counter(o["entity_id"] for o in observations if o["entity_id"])
    print("\n  By entity (top 5):")
    entity_lookup = {e["entity_id"]: e["entity_name"] for e in entities}
    for eid, count in obs_entities.most_common(5):
        ename = entity_lookup.get(eid, eid)
        print(f"    {ename} ({eid}): {count}")

    # By confidence
    obs_confidence = Counter(o["confidence"] for o in observations)
    print("\n  By confidence level:")
    for conf, count in obs_confidence.most_common():
        print(f"    {conf}: {count}")

    # --- Viability Predictions vs Actual Outcomes ---
    print()
    print("-" * 72)
    print("PREDICTION-OUTCOME PAIRS")
    print("-" * 72)
    predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]

    for pred in predictions:
        print(f"\n  PREDICTION ({pred['obs_id']}):")
        print(f"    {pred['metric_name']}: {pred['metric_value'][:100]}...")
        # Find corresponding outcome by matching tech_id
        matching_outcomes = [
            out for out in outcomes
            if out.get("tech_id") == pred.get("tech_id") and pred.get("tech_id")
        ]
        if not matching_outcomes:
            # Fall back: match by entity_id
            matching_outcomes = [
                out for out in outcomes
                if out.get("entity_id") == pred.get("entity_id")
                and out.get("tech_id", "") == pred.get("tech_id", "")
            ]
        for out in matching_outcomes:
            print(f"  OUTCOME ({out['obs_id']}):")
            print(f"    {out['metric_name']}: {out['metric_value'][:100]}...")
    print()

    # --- Benchmark Results ---
    print("-" * 72)
    print("BENCHMARK RESULTS")
    print("-" * 72)
    benchmarks = [o for o in observations if o["observation_type"] == "benchmark-result"]
    tech_lookup = {t["tech_id"]: t["tech_name"] for t in technologies}
    for b in benchmarks:
        tname = tech_lookup.get(b["tech_id"], "N/A")
        print(f"  {b['obs_id']} [{tname}]: {b['metric_value']}")
    print()

    # --- Codes Summary ---
    print("-" * 72)
    print(f"CONTROLLED VOCABULARY ({len(codes)} codes)")
    print("-" * 72)
    code_types = Counter(c["code_type"] for c in codes)
    for ct, count in code_types.most_common():
        print(f"  {ct}: {count} codes")
    print()

    # --- Validation ---
    print("-" * 72)
    print("VALIDATION CHECKS")
    print("-" * 72)

    # Check canonical observation types
    canonical_types = {
        "strategy-classification", "viability-prediction", "actual-outcome",
        "technology-assessment", "benchmark-result", "framework-factor",
        "market-data", "expert-opinion"
    }
    obs_type_values = set(o["observation_type"] for o in observations)
    invalid_types = obs_type_values - canonical_types
    if invalid_types:
        print(f"  FAIL: Non-canonical observation types found: {invalid_types}")
    else:
        print(f"  PASS: All {len(obs_type_values)} observation types are canonical")

    # Check assessment ratings are text values
    valid_ratings = {"high", "medium", "low", "not-applicable"}
    for rating_field in ["importance", "relevance", "prescience"]:
        val = study.get(rating_field, "")
        if val in valid_ratings:
            print(f"  PASS: {rating_field} = '{val}' (valid text rating)")
        else:
            print(f"  FAIL: {rating_field} = '{val}' (expected text rating)")

    # Check obs_id format
    bad_obs_ids = [o["obs_id"] for o in observations if not o["obs_id"].startswith("OBS-")]
    if bad_obs_ids:
        print(f"  FAIL: Invalid obs_id format: {bad_obs_ids}")
    else:
        print(f"  PASS: All {len(observations)} obs_ids use OBS-NNN format")

    # Check single-valued entity_id (no commas)
    multi_entity = [o["obs_id"] for o in observations if "," in o.get("entity_id", "")]
    if multi_entity:
        print(f"  FAIL: Multi-valued entity_id in: {multi_entity}")
    else:
        print("  PASS: All entity_id values are single-valued")

    # Check entity references
    valid_entities = {e["entity_id"] for e in entities}
    bad_refs = [
        o["obs_id"] for o in observations
        if o["entity_id"] and o["entity_id"] not in valid_entities
    ]
    if bad_refs:
        print(f"  FAIL: Invalid entity references in: {bad_refs}")
    else:
        print("  PASS: All entity references are valid")

    # Check tech references
    valid_techs = {t["tech_id"] for t in technologies}
    bad_tech_refs = [
        o["obs_id"] for o in observations
        if o["tech_id"] and o["tech_id"] not in valid_techs
    ]
    if bad_tech_refs:
        print(f"  FAIL: Invalid tech references in: {bad_tech_refs}")
    else:
        print("  PASS: All technology references are valid")

    # Check methodology codes
    valid_methods = {c["code_id"] for c in codes if c["code_type"] == "methodology_code"}
    bad_methods = [
        o["obs_id"] for o in observations
        if o["methodology_code"] and o["methodology_code"] not in valid_methods
    ]
    if bad_methods:
        print(f"  FAIL: Invalid methodology codes in: {bad_methods}")
    else:
        print(f"  PASS: All methodology codes are valid")

    # File count check
    expected_files = [
        "README.md", "datapackage.json",
        "data/studies.csv", "data/entities.csv", "data/technologies.csv",
        "data/observations.csv", "data/codes.csv",
        "schema/schema_org.json", "source/original_text.md",
        "scripts/demo_analysis.py"
    ]
    missing = [f for f in expected_files if not (package_dir / f).exists()]
    if missing:
        print(f"  FAIL: Missing files: {missing}")
    else:
        print(f"  PASS: All {len(expected_files)} expected files present")

    print()
    print("=" * 72)
    print("Analysis complete.")
    print("=" * 72)


if __name__ == "__main__":
    main()
