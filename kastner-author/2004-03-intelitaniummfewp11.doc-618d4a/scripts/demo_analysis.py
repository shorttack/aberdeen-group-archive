#!/usr/bin/env python3
"""
Demo Analysis Script for Aberdeen Group Itanium White Paper Data Package
study_id: 2004-03-intelitaniummfewp11.doc-618d4a

This script demonstrates how to load and analyze the Frictionless Data Package
for the Aberdeen Group study on Intel Itanium readiness for mainframe workloads.

Usage:
    python scripts/demo_analysis.py

Requirements:
    Python 3.7+ with standard library (csv, json, collections)
"""

import csv
import json
import os
from collections import Counter
from pathlib import Path


def get_base_dir():
    """Get the base directory of the data package."""
    script_dir = Path(__file__).resolve().parent
    return script_dir.parent


def load_csv(filename):
    """Load a CSV file and return a list of dictionaries."""
    filepath = get_base_dir() / "data" / filename
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def load_datapackage():
    """Load and return the datapackage.json metadata."""
    filepath = get_base_dir() / "datapackage.json"
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def print_separator(title):
    """Print a formatted section separator."""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}")


def analyze_study_metadata():
    """Display study metadata and ratings."""
    print_separator("STUDY METADATA")
    studies = load_csv("studies.csv")
    study = studies[0]
    print(f"  Title:      {study['title']}")
    print(f"  Author:     {study['author']}")
    print(f"  Date:       {study['date']}")
    print(f"  Type:       {study['type']}")
    print(f"  Domain:     {study['subject_domain']}")
    print(f"  Methodology:{study['methodology']}")
    print(f"  License:    {study['license']}")
    print()
    print(f"  Importance:  {study['importance']:>6}  - {study['importance_rationale']}")
    print(f"  Relevance:   {study['relevance']:>6}  - {study['relevance_rationale']}")
    print(f"  Prescience:  {study['prescience']:>6}  - {study['prescience_rationale']}")


def analyze_entities():
    """Analyze and display entity information."""
    print_separator("ENTITIES ANALYSIS")
    entities = load_csv("entities.csv")
    print(f"  Total entities: {len(entities)}")
    print()

    # Group by status
    status_counts = Counter(e["status"] for e in entities)
    print("  By Status:")
    for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
        print(f"    {status:<15} {count}")

    # Group by entity_type
    type_counts = Counter(e["entity_type"] for e in entities)
    print("\n  By Type:")
    for etype, count in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"    {etype:<20} {count}")

    # List acquired/dissolved entities
    print("\n  Acquired/Dissolved Entities:")
    for e in entities:
        if e["status"] in ("acquired", "dissolved", "restructured"):
            successor = f" -> {e['successor']}" if e["successor"] else ""
            print(f"    {e['entity_name']:<25} ({e['status']}{successor})")


def analyze_technologies():
    """Analyze and display technology information."""
    print_separator("TECHNOLOGIES ANALYSIS")
    technologies = load_csv("technologies.csv")
    print(f"  Total technologies: {len(technologies)}")
    print()

    print("  Lifecycle Comparison (study time vs. current):")
    print(f"    {'Technology':<25} {'At Study':<15} {'Current':<15}")
    print(f"    {'-' * 25} {'-' * 15} {'-' * 15}")
    for t in technologies:
        print(f"    {t['tech_name']:<25} {t['lifecycle_at_study']:<15} {t['lifecycle_current']:<15}")

    # Count discontinued
    discontinued = [t for t in technologies if t["lifecycle_current"] == "discontinued"]
    print(f"\n  Technologies discontinued since study: {len(discontinued)}")
    for t in discontinued:
        print(f"    - {t['tech_name']} ({t['era']})")


def analyze_observations():
    """Analyze and display observation statistics."""
    print_separator("OBSERVATIONS ANALYSIS")
    observations = load_csv("observations.csv")
    print(f"  Total observations: {len(observations)}")
    print()

    # By observation type
    type_counts = Counter(o["observation_type"] for o in observations)
    print("  By Observation Type:")
    for otype, count in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"    {otype:<30} {count:>3}")

    # By confidence level
    conf_counts = Counter(o["confidence"] for o in observations)
    print("\n  By Confidence Level:")
    for conf, count in sorted(conf_counts.items(), key=lambda x: -x[1]):
        print(f"    {conf:<15} {count:>3}")

    # By methodology
    method_counts = Counter(o["methodology_code"] for o in observations)
    print("\n  By Methodology:")
    for method, count in sorted(method_counts.items(), key=lambda x: -x[1]):
        print(f"    {method:<25} {count:>3}")

    # Predictions vs Outcomes
    print_separator("PREDICTIONS vs. ACTUAL OUTCOMES")
    predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]

    print(f"  Predictions made (2004): {len(predictions)}")
    for p in predictions:
        tech = p["tech_id"]
        print(f"    [{p['obs_id']}] {tech}: {p['metric_name']} = {p['metric_value']}")

    print(f"\n  Actual outcomes (verified): {len(outcomes)}")
    for o in outcomes:
        tech = o["tech_id"]
        print(f"    [{o['obs_id']}] {tech}: {o['metric_name']} = {o['metric_value']}")


def analyze_survey_data():
    """Extract and display key survey findings."""
    print_separator("KEY SURVEY FINDINGS (98 Respondents)")
    observations = load_csv("observations.csv")

    survey_obs = [
        o for o in observations
        if o["methodology_code"] == "statistical-analysis"
        and o["observation_type"] == "benchmark-result"
    ]

    for o in survey_obs:
        print(f"    {o['metric_name']:<35} {o['metric_value']:>20}")


def analyze_referential_integrity():
    """Verify referential integrity across CSV files."""
    print_separator("REFERENTIAL INTEGRITY CHECK")
    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")
    codes = load_csv("codes.csv")

    study_ids = {s["study_id"] for s in studies}
    entity_ids = {e["entity_id"] for e in entities}
    tech_ids = {t["tech_id"] for t in technologies}
    code_ids = {c["code_id"] for c in codes}

    errors = []

    # Check entity study_id references
    for e in entities:
        if e["study_id"] not in study_ids:
            errors.append(f"Entity {e['entity_id']}: invalid study_id '{e['study_id']}'")

    # Check technology study_id references
    for t in technologies:
        if t["study_id"] not in study_ids:
            errors.append(f"Technology {t['tech_id']}: invalid study_id '{t['study_id']}'")

    # Check observation references
    for o in observations:
        if o["study_id"] not in study_ids:
            errors.append(f"Observation {o['obs_id']}: invalid study_id '{o['study_id']}'")
        if o["entity_id"] and o["entity_id"] not in entity_ids:
            errors.append(f"Observation {o['obs_id']}: invalid entity_id '{o['entity_id']}'")
        if o["tech_id"] and o["tech_id"] not in tech_ids:
            errors.append(f"Observation {o['obs_id']}: invalid tech_id '{o['tech_id']}'")

    # Check observation types and methodologies against codes
    obs_type_codes = {c["code_id"] for c in codes if c["code_type"] == "observation_type"}
    method_codes = {c["code_id"] for c in codes if c["code_type"] == "methodology_code"}
    conf_codes = {c["code_id"] for c in codes if c["code_type"] == "confidence"}

    for o in observations:
        if o["observation_type"] not in obs_type_codes:
            errors.append(f"Observation {o['obs_id']}: invalid observation_type '{o['observation_type']}'")
        if o["methodology_code"] not in method_codes:
            errors.append(f"Observation {o['obs_id']}: invalid methodology_code '{o['methodology_code']}'")
        if o["confidence"] not in conf_codes:
            errors.append(f"Observation {o['obs_id']}: invalid confidence '{o['confidence']}'")

    if errors:
        print(f"  ERRORS FOUND: {len(errors)}")
        for err in errors:
            print(f"    - {err}")
    else:
        print("  All referential integrity checks passed.")
        print(f"    - {len(entities)} entities reference valid study_ids")
        print(f"    - {len(technologies)} technologies reference valid study_ids")
        print(f"    - {len(observations)} observations reference valid study_ids, entity_ids, tech_ids")
        print(f"    - All observation_type values match codes.csv definitions")
        print(f"    - All methodology_code values match codes.csv definitions")
        print(f"    - All confidence values match codes.csv definitions")


def main():
    """Run all analyses."""
    print("=" * 70)
    print("  FRICTIONLESS DATA PACKAGE ANALYSIS")
    print("  Intel's Itanium: Ready and Desirable for Mainframe-Class Workloads")
    print("  Aberdeen Group, March 2004")
    print("=" * 70)

    pkg = load_datapackage()
    print(f"\n  Package: {pkg['name']}")
    print(f"  Version: {pkg['version']}")
    print(f"  Resources: {len(pkg['resources'])}")

    analyze_study_metadata()
    analyze_entities()
    analyze_technologies()
    analyze_observations()
    analyze_survey_data()
    analyze_referential_integrity()

    print(f"\n{'=' * 70}")
    print("  Analysis complete.")
    print(f"{'=' * 70}\n")


if __name__ == "__main__":
    main()
