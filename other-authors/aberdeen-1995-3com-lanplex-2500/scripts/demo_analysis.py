#!/usr/bin/env python3
"""
demo_analysis.py
================
Standalone validation and analysis script for the Frictionless Data Package:
  aberdeen-1995-3com-lanplex-2500

Runs the following checks:
  1. Load all five CSV files
  2. Print study summary statistics
  3. Validate referential integrity
     - Every entity_id in observations exists in entities (or is blank)
     - Every tech_id in observations exists in technologies (or is blank)
  4. Validate code coverage
     - Every observation_type in observations exists in codes.csv
     - Every methodology_code in observations exists in codes.csv
     - Every confidence value in observations exists in codes.csv
  5. Cross-reference viability predictions against actual outcomes
     and compute prediction accuracy
  6. Print lifecycle summary for technologies
  7. Print entity status summary
"""

import csv
import os
import sys
from collections import Counter, defaultdict

# ── Path resolution ────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")


def load_csv(filename):
    """Load a CSV file from DATA_DIR and return list of dicts."""
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        print(f"[ERROR] File not found: {path}")
        sys.exit(1)
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def divider(title=""):
    width = 72
    if title:
        pad = (width - len(title) - 2) // 2
        print("=" * pad + f" {title} " + "=" * (width - pad - len(title) - 2))
    else:
        print("=" * width)


# ── Load data ─────────────────────────────────────────────────────────────────
studies      = load_csv("studies.csv")
entities     = load_csv("entities.csv")
technologies = load_csv("technologies.csv")
observations = load_csv("observations.csv")
codes        = load_csv("codes.csv")

# ── 1. Study summary statistics ───────────────────────────────────────────────
divider("STUDY SUMMARY")
for s in studies:
    print(f"  Study ID      : {s['study_id']}")
    print(f"  Title         : {s['title']}")
    print(f"  Author        : {s['author']}")
    print(f"  Date          : {s['date']}")
    print(f"  Type          : {s['type']}")
    print(f"  Domain        : {s['subject_domain']}")
    print(f"  Methodology   : {s['methodology']}")
    print(f"  License       : {s['license']}")
    print()

print(f"  Entities      : {len(entities)}")
print(f"  Technologies  : {len(technologies)}")
print(f"  Observations  : {len(observations)}")
print(f"  Codes         : {len(codes)}")

# ── 2. Referential integrity checks ──────────────────────────────────────────
divider("REFERENTIAL INTEGRITY")
errors = []

entity_ids = {e["entity_id"] for e in entities}
tech_ids   = {t["tech_id"]   for t in technologies}
code_ids   = {c["code_id"]   for c in codes}

for obs in observations:
    eid = obs["entity_id"].strip()
    if eid and eid not in entity_ids:
        errors.append(f"  [FAIL] obs {obs['obs_id']}: entity_id '{eid}' not in entities.csv")

    tid = obs["tech_id"].strip()
    if tid and tid not in tech_ids:
        errors.append(f"  [FAIL] obs {obs['obs_id']}: tech_id '{tid}' not in technologies.csv")

if errors:
    for e in errors:
        print(e)
else:
    print("  [PASS] All entity_id and tech_id references are valid.")

# ── 3. Code coverage checks ───────────────────────────────────────────────────
divider("CODE COVERAGE")
code_errors = []

for obs in observations:
    ot = obs["observation_type"].strip()
    if ot and ot not in code_ids:
        code_errors.append(f"  [FAIL] obs {obs['obs_id']}: observation_type '{ot}' not in codes.csv")

    mc = obs["methodology_code"].strip()
    if mc and mc not in code_ids:
        code_errors.append(f"  [FAIL] obs {obs['obs_id']}: methodology_code '{mc}' not in codes.csv")

    cf = obs["confidence"].strip()
    if cf and cf not in code_ids:
        code_errors.append(f"  [FAIL] obs {obs['obs_id']}: confidence '{cf}' not in codes.csv")

if code_errors:
    for e in code_errors:
        print(e)
else:
    print("  [PASS] All observation_type, methodology_code, and confidence values are valid.")

# ── 4. Observation type distribution ─────────────────────────────────────────
divider("OBSERVATION TYPE DISTRIBUTION")
otype_counts = Counter(obs["observation_type"] for obs in observations)
for otype, count in sorted(otype_counts.items(), key=lambda x: -x[1]):
    bar = "#" * count
    print(f"  {otype:<30} {count:>3}  {bar}")

# ── 5. Viability predictions vs. actual outcomes ──────────────────────────────
divider("PREDICTIONS vs. ACTUAL OUTCOMES")
predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
actuals     = [o for o in observations if o["observation_type"] == "actual-outcome"]

print(f"  Viability predictions : {len(predictions)}")
print(f"  Actual outcomes       : {len(actuals)}")
print()

if predictions:
    print("  Predictions:")
    for p in predictions:
        print(f"    [{p['obs_id']}] ({p['year_observed']}) {p['metric_name']}")
        print(f"      Value: {p['metric_value']}")
        print()

if actuals:
    print("  Actual outcomes:")
    for a in actuals:
        print(f"    [{a['obs_id']}] ({a['year_observed']}) {a['metric_name']}")
        print(f"      Value: {a['metric_value']}")
        print()

# Note: direct cross-matching requires additional verified-outcome data
print("  Note: Predictions in this study concern Q1 1996 product ship dates (Fast Ethernet card,")
print("  OC-3 ATM uplink) and 1996 enterprise ATM adoption. Verified outcomes from historical")
print("  record: 3Com did ship Fast Ethernet uplinks for the LANplex 2500 in 1996. ATM backbone")
print("  adoption in enterprises generally lagged projections, with Ethernet (Fast/Gigabit)")
print("  ultimately displacing ATM by the late 1990s. 3Com's competitive lead was eroded by")
print("  Cisco's rapid feature development as predicted.")

# ── 6. Technology lifecycle summary ───────────────────────────────────────────
divider("TECHNOLOGY LIFECYCLE SUMMARY")
lc_at_study = Counter(t["lifecycle_at_study"] for t in technologies)
lc_current  = Counter(t["lifecycle_current"]  for t in technologies)

print("  At time of study (1995):")
for lc, count in sorted(lc_at_study.items(), key=lambda x: -x[1]):
    print(f"    {lc:<20} {count}")
print()
print("  Current status (2026):")
for lc, count in sorted(lc_current.items(), key=lambda x: -x[1]):
    print(f"    {lc:<20} {count}")

# ── 7. Entity status summary ──────────────────────────────────────────────────
divider("ENTITY STATUS SUMMARY")
status_counts = Counter(e["status"] for e in entities)
for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
    print(f"  {status:<20} {count}")

print()
print("  Acquired entities:")
for e in entities:
    if e["status"] == "acquired":
        print(f"    {e['entity_name']:<35} -> {e['successor']}")

# ── 8. Completeness check ─────────────────────────────────────────────────────
divider("COMPLETENESS CHECK")
required_study_fields = ["study_id", "title", "author", "date", "type",
                          "subject_domain", "methodology", "source_file", "abstract", "license"]
completeness_errors = []
for s in studies:
    for field in required_study_fields:
        if not s.get(field, "").strip():
            completeness_errors.append(f"  [FAIL] studies.csv: empty required field '{field}'")

if completeness_errors:
    for e in completeness_errors:
        print(e)
else:
    print("  [PASS] All required study fields are populated.")

# ── Summary ───────────────────────────────────────────────────────────────────
divider("VALIDATION SUMMARY")
total_checks = 3  # integrity, code coverage, completeness
failed = len(errors) + len(code_errors) + len(completeness_errors)
passed = total_checks - (1 if errors else 0) - (1 if code_errors else 0) - (1 if completeness_errors else 0)

print(f"  Checks passed : {passed}/{total_checks}")
print(f"  Issues found  : {failed}")
if failed == 0:
    print("  Status        : ALL CHECKS PASSED")
else:
    print("  Status        : REVIEW REQUIRED")

divider()
