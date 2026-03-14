#!/usr/bin/env python3
"""
demo_analysis.py — Validation and analysis script for the Aberdeen 1995
Commercial Messaging Frictionless Data Package.

Usage:
    python scripts/demo_analysis.py

Performs:
    1. Loads all five CSV tables
    2. Prints study summary statistics
    3. Validates referential integrity (entity_id and tech_id in observations)
    4. Checks all observation_type and methodology_code values exist in codes.csv
    5. Cross-references viability predictions against actual outcomes
    6. Computes prediction accuracy
    7. Reports results to stdout
"""

import csv
import os
import sys
from collections import defaultdict

# ── Path resolution ────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PACKAGE_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PACKAGE_DIR, "data")

def load_csv(filename):
    """Load a CSV file and return list of dicts."""
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        print(f"ERROR: File not found: {path}")
        sys.exit(1)
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

# ── Load all tables ────────────────────────────────────────────────────────────
print("=" * 60)
print("Aberdeen 1995 Commercial Messaging — Data Package Validation")
print("=" * 60)

studies       = load_csv("studies.csv")
entities      = load_csv("entities.csv")
technologies  = load_csv("technologies.csv")
observations  = load_csv("observations.csv")
codes         = load_csv("codes.csv")

print(f"\n[1] TABLE SUMMARY")
print(f"    studies.csv       : {len(studies):>4} row(s)")
print(f"    entities.csv      : {len(entities):>4} row(s)")
print(f"    technologies.csv  : {len(technologies):>4} row(s)")
print(f"    observations.csv  : {len(observations):>4} row(s)")
print(f"    codes.csv         : {len(codes):>4} row(s)")

# ── Study metadata ─────────────────────────────────────────────────────────────
print(f"\n[2] STUDY METADATA")
study = studies[0]
print(f"    Study ID    : {study['study_id']}")
print(f"    Title       : {study['title']}")
print(f"    Author      : {study['author']}")
print(f"    Date        : {study['date']}")
print(f"    Type        : {study['type']}")
print(f"    Domain      : {study['subject_domain']}")
print(f"    Methodology : {study['methodology']}")
print(f"    License     : {study['license']}")

# ── Observation type breakdown ─────────────────────────────────────────────────
print(f"\n[3] OBSERVATION TYPE BREAKDOWN")
obs_type_counts = defaultdict(int)
for obs in observations:
    obs_type_counts[obs["observation_type"]] += 1
for otype, count in sorted(obs_type_counts.items()):
    print(f"    {otype:<30} : {count:>3}")

# ── Entity status breakdown ────────────────────────────────────────────────────
print(f"\n[4] ENTITY STATUS BREAKDOWN")
status_counts = defaultdict(int)
for ent in entities:
    status_counts[ent["status"]] += 1
for status, count in sorted(status_counts.items()):
    print(f"    {status:<20} : {count:>3}")

# ── Technology lifecycle breakdown ────────────────────────────────────────────
print(f"\n[5] TECHNOLOGY LIFECYCLE (AT STUDY vs. CURRENT)")
lc_at_study = defaultdict(int)
lc_current  = defaultdict(int)
for tech in technologies:
    lc_at_study[tech["lifecycle_at_study"]] += 1
    lc_current[tech["lifecycle_current"]] += 1
print("    At study time:")
for lc, count in sorted(lc_at_study.items()):
    print(f"      {lc:<20} : {count:>3}")
print("    Current (2025):")
for lc, count in sorted(lc_current.items()):
    print(f"      {lc:<20} : {count:>3}")

# ── Referential integrity checks ──────────────────────────────────────────────
print(f"\n[6] REFERENTIAL INTEGRITY CHECK")

errors = []

# Valid entity_ids and tech_ids
valid_entity_ids  = {e["entity_id"] for e in entities}
valid_tech_ids    = {t["tech_id"] for t in technologies}
valid_study_ids   = {s["study_id"] for s in studies}

# Observations: check entity_id, tech_id, study_id
for obs in observations:
    if obs["entity_id"] and obs["entity_id"] not in valid_entity_ids:
        errors.append(f"    BROKEN entity_id '{obs['entity_id']}' in obs {obs['obs_id']}")
    if obs["tech_id"] and obs["tech_id"] not in valid_tech_ids:
        errors.append(f"    BROKEN tech_id '{obs['tech_id']}' in obs {obs['obs_id']}")
    if obs["study_id"] not in valid_study_ids:
        errors.append(f"    BROKEN study_id '{obs['study_id']}' in obs {obs['obs_id']}")

# Entities: check study_id
for ent in entities:
    if ent["study_id"] not in valid_study_ids:
        errors.append(f"    BROKEN study_id '{ent['study_id']}' in entity {ent['entity_id']}")

# Technologies: check study_id
for tech in technologies:
    if tech["study_id"] not in valid_study_ids:
        errors.append(f"    BROKEN study_id '{tech['study_id']}' in tech {tech['tech_id']}")

if errors:
    print(f"    FAILURES ({len(errors)}):")
    for e in errors:
        print(e)
else:
    print("    PASS — all foreign keys resolve correctly")

# ── Code coverage checks ───────────────────────────────────────────────────────
print(f"\n[7] CODE COVERAGE CHECK")

code_ids = {c["code_id"] for c in codes}
code_errors = []

# observation_type values
for obs in observations:
    ot = obs["observation_type"]
    if ot not in code_ids:
        code_errors.append(f"    observation_type '{ot}' not in codes.csv (obs {obs['obs_id']})")

# methodology_code values
for obs in observations:
    mc = obs["methodology_code"]
    if mc and mc not in code_ids:
        code_errors.append(f"    methodology_code '{mc}' not in codes.csv (obs {obs['obs_id']})")

if code_errors:
    print(f"    FAILURES ({len(code_errors)}):")
    for e in code_errors:
        print(e)
else:
    print("    PASS — all observation_type and methodology_code values exist in codes.csv")

# ── Completeness check ─────────────────────────────────────────────────────────
print(f"\n[8] STUDIES COMPLETENESS CHECK")
required_fields = ["study_id", "title", "author", "date", "type",
                   "subject_domain", "methodology", "source_file", "abstract", "license"]
completeness_errors = []
for study in studies:
    for field in required_fields:
        if not study.get(field, "").strip():
            completeness_errors.append(f"    Missing required field '{field}' in study {study.get('study_id', 'UNKNOWN')}")
if completeness_errors:
    print(f"    FAILURES ({len(completeness_errors)}):")
    for e in completeness_errors:
        print(e)
else:
    print("    PASS — all required fields populated in studies.csv")

# ── ID format check ────────────────────────────────────────────────────────────
print(f"\n[9] ID FORMAT CHECK (lowercase-hyphenated)")
import re
id_pattern = re.compile(r'^[a-z0-9][a-z0-9\-\.]*$')
id_errors = []

for s in studies:
    if not id_pattern.match(s["study_id"]):
        id_errors.append(f"    Non-conforming study_id: '{s['study_id']}'")
for e in entities:
    if not id_pattern.match(e["entity_id"]):
        id_errors.append(f"    Non-conforming entity_id: '{e['entity_id']}'")
for t in technologies:
    if not id_pattern.match(t["tech_id"]):
        id_errors.append(f"    Non-conforming tech_id: '{t['tech_id']}'")

if id_errors:
    print(f"    FAILURES ({len(id_errors)}):")
    for e in id_errors:
        print(e)
else:
    print("    PASS — all IDs are lowercase-hyphenated")

# ── Prediction accuracy analysis ───────────────────────────────────────────────
print(f"\n[10] VIABILITY PREDICTION ACCURACY")

predictions = [obs for obs in observations if obs["observation_type"] == "viability-prediction"]
outcomes    = [obs for obs in observations if obs["observation_type"] == "actual-outcome"]

print(f"    Viability predictions found : {len(predictions)}")
print(f"    Actual outcome rows found   : {len(outcomes)}")

# Match predictions to outcomes by tech_id or entity_id
prediction_summary = []
for pred in predictions:
    matching_outcomes = []
    for out in outcomes:
        if (pred["tech_id"] and pred["tech_id"] == out["tech_id"]) or \
           (pred["entity_id"] and pred["entity_id"] == out["entity_id"]):
            matching_outcomes.append(out)
    prediction_summary.append({
        "prediction": pred["metric_name"],
        "predicted_value": pred["metric_value"],
        "tech_id": pred["tech_id"],
        "entity_id": pred["entity_id"],
        "matched_outcomes": len(matching_outcomes),
    })

verified = sum(1 for p in prediction_summary if p["matched_outcomes"] > 0)
accuracy = (verified / len(predictions) * 100) if predictions else 0

print(f"\n    Predictions with matched outcome rows: {verified}/{len(predictions)}")
print(f"    Coverage rate: {accuracy:.0f}%")
print(f"\n    Prediction details:")
for p in prediction_summary:
    ref = p["tech_id"] or p["entity_id"] or "—"
    matched = "MATCHED" if p["matched_outcomes"] > 0 else "no match"
    print(f"      [{matched}] ({ref}) {p['prediction'][:70]}")

# ── Confidence distribution ────────────────────────────────────────────────────
print(f"\n[11] CONFIDENCE LEVEL DISTRIBUTION")
conf_counts = defaultdict(int)
for obs in observations:
    conf_counts[obs["confidence"]] += 1
for conf, count in [("high", conf_counts["high"]), ("medium", conf_counts["medium"]),
                    ("low", conf_counts["low"]), ("verified", conf_counts["verified"])]:
    bar = "█" * count
    print(f"    {conf:<12} : {count:>3}  {bar}")

# ── Key market data summary ────────────────────────────────────────────────────
print(f"\n[12] KEY MARKET DATA (1995)")
market_obs = [obs for obs in observations if obs["observation_type"] == "market-data"]
for obs in market_obs:
    print(f"    {obs['metric_name'][:45]:<45} : {obs['metric_value']}")

# ── Final summary ──────────────────────────────────────────────────────────────
total_errors = len(errors) + len(code_errors) + len(completeness_errors) + len(id_errors)
print(f"\n{'=' * 60}")
print(f"VALIDATION SUMMARY")
print(f"{'=' * 60}")
print(f"    Total checks run     : referential integrity, code coverage,")
print(f"                           completeness, ID format")
print(f"    Total errors found   : {total_errors}")
if total_errors == 0:
    print(f"    STATUS               : PASS — package is valid")
else:
    print(f"    STATUS               : FAIL — {total_errors} error(s) require review")
print(f"{'=' * 60}")
print(f"\nStudy: aberdeen-1995-commercial-messaging")
print(f"  {len(entities)} entities | {len(technologies)} technologies | {len(observations)} observations")
print(f"  Prediction coverage: {accuracy:.0f}%")
print(f"  Technology obsolescence rate: {lc_current.get('obsolete', 0)}/{len(technologies)} technologies now obsolete")
print(f"  Entity dissolution/acquisition rate: {status_counts.get('dissolved', 0) + status_counts.get('acquired', 0)}/{len(entities)} entities no longer independent")
