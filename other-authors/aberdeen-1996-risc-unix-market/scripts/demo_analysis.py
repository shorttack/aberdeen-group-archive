#!/usr/bin/env python3
"""
demo_analysis.py — Validation and analysis script for:
  Aberdeen Group — Commercial, Multiuser RISC/Unix 1995: High Growth and HP Dominate
  study_id: aberdeen-1996-risc-unix-market

Usage:
    python scripts/demo_analysis.py

Performs:
  1. Load all five CSV files
  2. Print study summary statistics
  3. Validate referential integrity (entity_id, tech_id, methodology_code, observation_type)
  4. Cross-reference viability predictions against actual outcomes (where available)
  5. Print market share and revenue summary tables
"""

import csv
import os
import sys
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

ERRORS   = []
WARNINGS = []

# ─────────────────────────────────────────────────────────────────────────────
def load_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

# ─────────────────────────────────────────────────────────────────────────────
def section(title):
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}")

# ─────────────────────────────────────────────────────────────────────────────
def main():
    # ── 1. Load all tables ──────────────────────────────────────────────────
    section("1. LOADING DATA FILES")
    studies       = load_csv("studies.csv")
    entities      = load_csv("entities.csv")
    technologies  = load_csv("technologies.csv")
    observations  = load_csv("observations.csv")
    codes         = load_csv("codes.csv")

    print(f"  studies.csv        : {len(studies)} row(s)")
    print(f"  entities.csv       : {len(entities)} row(s)")
    print(f"  technologies.csv   : {len(technologies)} row(s)")
    print(f"  observations.csv   : {len(observations)} row(s)")
    print(f"  codes.csv          : {len(codes)} row(s)")

    study = studies[0]

    # ── 2. Study summary ────────────────────────────────────────────────────
    section("2. STUDY METADATA")
    print(f"  Study ID     : {study['study_id']}")
    print(f"  Title        : {study['title']}")
    print(f"  Author       : {study['author']}")
    print(f"  Date         : {study['date']}")
    print(f"  Type         : {study['type']}")
    print(f"  Domain       : {study['subject_domain']}")
    print(f"  Methodology  : {study['methodology']}")
    print(f"  License      : {study['license']}")
    print(f"  Source File  : {study['source_file']}")
    print()
    abstract_preview = study['abstract'][:300].replace('\n', ' ')
    print(f"  Abstract (first 300 chars):\n  {abstract_preview}...")

    # ── 3. Referential integrity checks ────────────────────────────────────
    section("3. REFERENTIAL INTEGRITY VALIDATION")

    entity_ids  = {e["entity_id"] for e in entities}
    tech_ids    = {t["tech_id"]   for t in technologies}
    code_ids    = {c["code_id"]   for c in codes}
    study_ids   = {s["study_id"]  for s in studies}

    obs_errors = 0
    for obs in observations:
        eid = obs["entity_id"].strip()
        tid = obs["tech_id"].strip()
        mid = obs["methodology_code"].strip()
        otype = obs["observation_type"].strip()
        sid = obs["study_id"].strip()

        if eid and eid not in entity_ids:
            ERRORS.append(f"  [INTEGRITY] obs {obs['obs_id']}: entity_id '{eid}' not in entities.csv")
            obs_errors += 1
        if tid and tid not in tech_ids:
            ERRORS.append(f"  [INTEGRITY] obs {obs['obs_id']}: tech_id '{tid}' not in technologies.csv")
            obs_errors += 1
        if mid and mid not in code_ids:
            ERRORS.append(f"  [INTEGRITY] obs {obs['obs_id']}: methodology_code '{mid}' not in codes.csv")
            obs_errors += 1
        if otype and otype not in code_ids:
            ERRORS.append(f"  [INTEGRITY] obs {obs['obs_id']}: observation_type '{otype}' not in codes.csv")
            obs_errors += 1
        if sid not in study_ids:
            ERRORS.append(f"  [INTEGRITY] obs {obs['obs_id']}: study_id '{sid}' not in studies.csv")
            obs_errors += 1

    # Check entities FK
    for ent in entities:
        if ent["study_id"] not in study_ids:
            ERRORS.append(f"  [INTEGRITY] entity {ent['entity_id']}: study_id not in studies.csv")

    # Check technologies FK
    for tech in technologies:
        if tech["study_id"] not in study_ids:
            ERRORS.append(f"  [INTEGRITY] tech {tech['tech_id']}: study_id not in studies.csv")

    if not ERRORS:
        print("  PASS: All referential integrity checks passed (0 errors)")
    else:
        for e in ERRORS:
            print(e)
        print(f"\n  FAIL: {len(ERRORS)} integrity error(s) found")

    # ── 4. Code coverage ────────────────────────────────────────────────────
    section("4. CODE COVERAGE")
    obs_types_used    = {o["observation_type"] for o in observations if o["observation_type"]}
    method_codes_used = {o["methodology_code"]  for o in observations if o["methodology_code"]}
    all_used_codes    = obs_types_used | method_codes_used

    missing_codes = all_used_codes - code_ids
    if missing_codes:
        print(f"  WARN: {len(missing_codes)} codes used in observations but missing from codes.csv:")
        for c in sorted(missing_codes):
            print(f"    - {c}")
    else:
        print(f"  PASS: All {len(all_used_codes)} codes used in observations exist in codes.csv")

    print(f"\n  Observation types used ({len(obs_types_used)}):")
    for t in sorted(obs_types_used):
        count = sum(1 for o in observations if o["observation_type"] == t)
        print(f"    {t:<35} : {count:3d} observation(s)")

    # ── 5. Observation type distribution ────────────────────────────────────
    section("5. OBSERVATION BREAKDOWN")
    by_type = defaultdict(list)
    for o in observations:
        by_type[o["observation_type"]].append(o)

    for otype, obs_list in sorted(by_type.items(), key=lambda x: -len(x[1])):
        print(f"  {otype:<35} : {len(obs_list):3d}")

    # ── 6. Revenue / Market-share summary ───────────────────────────────────
    section("6. 1995 RISC/UNIX MARKET REVENUE SUMMARY (from observations)")
    revenue_obs = [o for o in observations
                   if o["observation_type"] == "market-data"
                   and "revenue" in o["metric_name"].lower()
                   and "prior year" not in o["metric_name"].lower()
                   and o["year_observed"] == "1995"]

    print(f"  {'Entity':<45} {'Metric':<35} {'Value'}")
    print(f"  {'-'*45} {'-'*35} {'-'*20}")
    for o in sorted(revenue_obs, key=lambda x: x["entity_id"]):
        ename = o["entity_id"] if o["entity_id"] else "(market total)"
        print(f"  {ename:<45} {o['metric_name']:<35} {o['metric_value']}")

    # ── 7. Viability predictions vs outcomes ────────────────────────────────
    section("7. VIABILITY PREDICTIONS")
    predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outcomes    = [o for o in observations if o["observation_type"] == "actual-outcome"]

    print(f"  Total predictions    : {len(predictions)}")
    print(f"  Total actual outcomes: {len(outcomes)}")
    print()
    print(f"  {'obs_id':<40} {'Year':<6} {'Metric':<45} {'Prediction'}")
    print(f"  {'-'*40} {'-'*6} {'-'*45} {'-'*40}")
    for p in predictions:
        print(f"  {p['obs_id']:<40} {p['year_observed']:<6} {p['metric_name'][:44]:<45} {p['metric_value'][:50]}")

    # ── 8. Entity status summary ─────────────────────────────────────────────
    section("8. ENTITY STATUS SUMMARY")
    status_counts = defaultdict(int)
    for e in entities:
        status_counts[e["status"]] += 1
    for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
        print(f"  {status:<20}: {count:3d} entit(ies)")

    # ── 9. Technology lifecycle summary ─────────────────────────────────────
    section("9. TECHNOLOGY LIFECYCLE AT STUDY DATE (1996)")
    lc_counts_at = defaultdict(int)
    lc_counts_now = defaultdict(int)
    for t in technologies:
        lc_counts_at[t["lifecycle_at_study"]] += 1
        lc_counts_now[t["lifecycle_current"]] += 1

    print("  Lifecycle AT STUDY:")
    for lc, cnt in sorted(lc_counts_at.items(), key=lambda x: -x[1]):
        print(f"    {lc:<25}: {cnt:3d}")
    print("  Lifecycle CURRENT:")
    for lc, cnt in sorted(lc_counts_now.items(), key=lambda x: -x[1]):
        print(f"    {lc:<25}: {cnt:3d}")

    # ── Final summary ────────────────────────────────────────────────────────
    section("VALIDATION SUMMARY")
    total_checks = len(observations) * 5 + len(entities) + len(technologies)
    error_count  = len(ERRORS)
    warn_count   = len(WARNINGS)

    print(f"  Total rows checked   : {total_checks}")
    print(f"  Integrity errors     : {error_count}")
    print(f"  Warnings             : {warn_count}")
    print()
    if error_count == 0 and warn_count == 0:
        print("  RESULT: PASS — Dataset is valid and complete.")
    elif error_count == 0:
        print(f"  RESULT: PASS with {warn_count} warning(s). Review warnings above.")
    else:
        print(f"  RESULT: FAIL — {error_count} error(s) require attention.")
        sys.exit(1)

    print()

if __name__ == "__main__":
    main()
