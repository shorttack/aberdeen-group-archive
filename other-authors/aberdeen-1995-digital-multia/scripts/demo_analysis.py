#!/usr/bin/env python3
"""
demo_analysis.py — Frictionless Data Package Validation & Analysis
Study: aberdeen-1995-digital-multia
       Digital's Multia Enterprise Client: Finally Someone Listened
       Aberdeen Group, December 1995

Validates referential integrity, code coverage, and data completeness.
Cross-references viability predictions against actual outcomes.
"""
import csv
import os
import sys
from pathlib import Path
from collections import defaultdict

# Portable path resolution
BASE = Path(os.path.dirname(os.path.abspath(__file__))).parent
DATA = BASE / "data"

REVIEW_ITEMS = []


def load_csv(name: str) -> list[dict]:
    path = DATA / f"{name}.csv"
    if not path.exists():
        print(f"  [ERROR] Missing file: {path}")
        sys.exit(1)
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def flag(msg: str):
    REVIEW_ITEMS.append(msg)
    print(f"  [REVIEW] {msg}")


# ── Load all tables ────────────────────────────────────────────────────────────
print("=" * 62)
print("Aberdeen Group Archival Data Package — Demo Analysis")
print("Study: aberdeen-1995-digital-multia")
print("=" * 62)

studies = load_csv("studies")
entities = load_csv("entities")
technologies = load_csv("technologies")
observations = load_csv("observations")
codes = load_csv("codes")

print(f"\n[1] TABLE ROW COUNTS")
print(f"    studies.csv       : {len(studies):>4} row(s)")
print(f"    entities.csv      : {len(entities):>4} row(s)")
print(f"    technologies.csv  : {len(technologies):>4} row(s)")
print(f"    observations.csv  : {len(observations):>4} row(s)")
print(f"    codes.csv         : {len(codes):>4} row(s)")

# ── Study completeness check ───────────────────────────────────────────────────
print(f"\n[2] STUDY COMPLETENESS")
REQUIRED_STUDY_FIELDS = ["study_id", "title", "author", "date", "type",
                          "subject_domain", "methodology", "source_file", "abstract", "license"]
for study in studies:
    for field in REQUIRED_STUDY_FIELDS:
        if not study.get(field, "").strip():
            flag(f"studies.csv: empty required field '{field}' in study '{study.get('study_id')}'")
    print(f"    study_id   : {study['study_id']}")
    print(f"    title      : {study['title']}")
    print(f"    author     : {study['author']}")
    print(f"    date       : {study['date']}")
    print(f"    type       : {study['type']}")
    print(f"    domain     : {study['subject_domain']}")
    print(f"    methods    : {study['methodology']}")
    print(f"    abstract   : {study['abstract'][:100]}...")

# ── Build lookup sets ──────────────────────────────────────────────────────────
study_ids = {s["study_id"] for s in studies}
entity_ids = {e["entity_id"] for e in entities}
tech_ids = {t["tech_id"] for t in technologies}
code_ids = {c["code_id"] for c in codes}

# ── Referential integrity: observations → entities ────────────────────────────
print(f"\n[3] REFERENTIAL INTEGRITY — observations → entities")
entity_ref_ok = 0
entity_ref_miss = 0
for obs in observations:
    eid = obs.get("entity_id", "").strip()
    if eid and eid not in entity_ids:
        flag(f"observations OBS {obs['obs_id']}: entity_id '{eid}' not found in entities.csv")
        entity_ref_miss += 1
    elif eid:
        entity_ref_ok += 1
print(f"    entity_id refs resolved : {entity_ref_ok}")
print(f"    entity_id refs missing  : {entity_ref_miss}")

# ── Referential integrity: observations → technologies ────────────────────────
print(f"\n[4] REFERENTIAL INTEGRITY — observations → technologies")
tech_ref_ok = 0
tech_ref_miss = 0
for obs in observations:
    tid = obs.get("tech_id", "").strip()
    if tid and tid not in tech_ids:
        flag(f"observations OBS {obs['obs_id']}: tech_id '{tid}' not found in technologies.csv")
        tech_ref_miss += 1
    elif tid:
        tech_ref_ok += 1
print(f"    tech_id refs resolved   : {tech_ref_ok}")
print(f"    tech_id refs missing    : {tech_ref_miss}")

# ── Code coverage: observation_type ───────────────────────────────────────────
print(f"\n[5] CODE COVERAGE — observation_type")
obs_types_used = {obs["observation_type"] for obs in observations if obs.get("observation_type")}
obs_types_missing = obs_types_used - code_ids
obs_types_ok = obs_types_used - obs_types_missing
print(f"    observation_type codes used     : {len(obs_types_used)}")
print(f"    observation_type codes verified : {len(obs_types_ok)}")
for code in sorted(obs_types_missing):
    flag(f"observation_type '{code}' used in observations.csv but not defined in codes.csv")

# ── Code coverage: methodology_code ───────────────────────────────────────────
print(f"\n[6] CODE COVERAGE — methodology_code")
method_codes_used = {obs["methodology_code"] for obs in observations if obs.get("methodology_code")}
method_codes_missing = method_codes_used - code_ids
method_codes_ok = method_codes_used - method_codes_missing
print(f"    methodology_code codes used     : {len(method_codes_used)}")
print(f"    methodology_code codes verified : {len(method_codes_ok)}")
for code in sorted(method_codes_missing):
    flag(f"methodology_code '{code}' used in observations.csv but not defined in codes.csv")

# ── Code coverage: confidence ─────────────────────────────────────────────────
print(f"\n[7] CODE COVERAGE — confidence")
confidence_used = {obs["confidence"] for obs in observations if obs.get("confidence")}
confidence_missing = confidence_used - code_ids
print(f"    confidence codes used    : {len(confidence_used)}")
for code in sorted(confidence_missing):
    flag(f"confidence '{code}' used in observations.csv but not defined in codes.csv")

# ── ISO 8601 date format check ────────────────────────────────────────────────
print(f"\n[8] DATE FORMAT CHECK (ISO 8601)")
import re
iso_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
date_ok = 0
for study in studies:
    d = study.get("date", "")
    if iso_pattern.match(d):
        date_ok += 1
        print(f"    study date '{d}' — OK")
    else:
        flag(f"studies.csv: date '{d}' does not match ISO 8601 YYYY-MM-DD format")

# ── Lowercase-hyphenated ID check ─────────────────────────────────────────────
print(f"\n[9] ID FORMAT CHECK (lowercase-hyphenated)")
id_pattern = re.compile(r"^[a-z0-9][a-z0-9\-]*$")
id_errors = 0
for study in studies:
    if not id_pattern.match(study["study_id"]):
        flag(f"studies.csv: study_id '{study['study_id']}' not lowercase-hyphenated")
        id_errors += 1
for entity in entities:
    if not id_pattern.match(entity["entity_id"]):
        flag(f"entities.csv: entity_id '{entity['entity_id']}' not lowercase-hyphenated")
        id_errors += 1
for tech in technologies:
    if not id_pattern.match(tech["tech_id"]):
        flag(f"technologies.csv: tech_id '{tech['tech_id']}' not lowercase-hyphenated")
        id_errors += 1
if id_errors == 0:
    print(f"    All IDs pass lowercase-hyphenated check")

# ── Viability predictions vs. actual outcomes ──────────────────────────────────
print(f"\n[10] VIABILITY PREDICTIONS vs. ACTUAL OUTCOMES")
predictions = [obs for obs in observations if obs["observation_type"] == "viability-prediction"]
actuals = [obs for obs in observations if obs["observation_type"] == "actual-outcome"]
print(f"    Viability predictions : {len(predictions)}")
print(f"    Actual outcomes       : {len(actuals)}")

# Check coverage
pred_techs = {obs.get("tech_id") for obs in predictions} | {obs.get("entity_id") for obs in predictions}
actual_techs = {obs.get("tech_id") for obs in actuals} | {obs.get("entity_id") for obs in actuals}
covered = pred_techs & actual_techs
print(f"\n    Prediction subjects with actual outcome coverage:")
for subj in sorted(covered):
    if subj:
        print(f"      - {subj}: COVERED")

# Accuracy summary
print(f"\n    Summary:")
print(f"      Aberdeen predicted IS cost reduction from central mgmt — PARTIALLY VERIFIED")
print(f"      (Multia discontinued ~1997; DEC acquired by Compaq 1998 for ~$9.6B)")
print(f"      Aberdeen predicted 'market-oriented Digital has finally arrived' — NOT BORNE OUT")
print(f"      (DEC did not survive as independent company; acquired within 3 years)")

# ── Entity status summary ─────────────────────────────────────────────────────
print(f"\n[11] ENTITY STATUS SUMMARY")
status_counts = defaultdict(int)
for entity in entities:
    status_counts[entity["status"]] += 1
for status, count in sorted(status_counts.items()):
    print(f"    {status:<20}: {count}")

# ── Technology lifecycle summary ──────────────────────────────────────────────
print(f"\n[12] TECHNOLOGY LIFECYCLE SUMMARY (current)")
lifecycle_counts = defaultdict(int)
for tech in technologies:
    lifecycle_counts[tech["lifecycle_current"]] += 1
for lc, count in sorted(lifecycle_counts.items()):
    print(f"    {lc:<20}: {count}")

# ── Final summary ──────────────────────────────────────────────────────────────
print(f"\n{'=' * 62}")
print(f"VALIDATION COMPLETE")
print(f"  Total observations     : {len(observations)}")
print(f"  Total entities         : {len(entities)}")
print(f"  Total technologies     : {len(technologies)}")
print(f"  Items flagged [REVIEW] : {len(REVIEW_ITEMS)}")

if REVIEW_ITEMS:
    print(f"\n  REVIEW ITEMS:")
    for item in REVIEW_ITEMS:
        print(f"    - {item}")
    print(f"\nResult: NEEDS REVIEW ({len(REVIEW_ITEMS)} item(s))")
else:
    print(f"\nResult: ALL CHECKS PASSED — Package integrity verified.")
print("=" * 62)
