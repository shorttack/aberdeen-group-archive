#!/usr/bin/env python3
"""
Demo Analysis Script — HP 3000: Continuously Increasing Customers' Successes
Archival Ingest Skill v13 | Validation and analysis script
"""
import csv
import os
import sys
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_csv(name):
    path = os.path.join(BASE, "data", f"{name}.csv")
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    print("=" * 60)
    print("DEMO ANALYSIS: HP 3000 Customers' Successes (1996)")
    print("=" * 60)

    studies = load_csv("studies")
    entities = load_csv("entities")
    technologies = load_csv("technologies")
    observations = load_csv("observations")
    codes = load_csv("codes")

    # ── Summary statistics ────────────────────────────────────────
    print(f"\n[STUDY SUMMARY]")
    s = studies[0]
    print(f"  Title:       {s['title']}")
    print(f"  Author:      {s['author']}")
    print(f"  Date:        {s['date']}")
    print(f"  Domain:      {s['subject_domain']}")
    print(f"  Importance:  {s['importance']} — {s['importance_rationale'][:80]}...")
    print(f"  Relevance:   {s['relevance']} — {s['relevance_rationale'][:80]}...")
    print(f"  Prescience:  {s['prescience']} — {s['prescience_rationale'][:80]}...")

    print(f"\n[TABLE COUNTS]")
    print(f"  Entities:      {len(entities)}")
    print(f"  Technologies:  {len(technologies)}")
    print(f"  Observations:  {len(observations)}")
    print(f"  Codes:         {len(codes)}")

    # ── Observation type breakdown ────────────────────────────────
    print(f"\n[OBSERVATIONS BY TYPE]")
    type_counts = defaultdict(int)
    for o in observations:
        type_counts[o["observation_type"]] += 1
    for otype, cnt in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {otype:<30} {cnt}")

    # ── Referential integrity checks ─────────────────────────────
    print(f"\n[REFERENTIAL INTEGRITY]")
    entity_ids = {e["entity_id"] for e in entities}
    tech_ids = {t["tech_id"] for t in technologies}
    code_ids = {c["code_id"] for c in codes}

    errors = []
    for o in observations:
        eid = o["entity_id"].strip()
        tid = o["tech_id"].strip()
        mc = o["methodology_code"].strip()
        ot = o["observation_type"].strip()
        if eid and eid not in entity_ids:
            errors.append(f"  [FAIL] obs {o['obs_id']}: entity_id '{eid}' not in entities.csv")
        if tid and tid not in tech_ids:
            errors.append(f"  [FAIL] obs {o['obs_id']}: tech_id '{tid}' not in technologies.csv")
        if mc and mc not in code_ids:
            errors.append(f"  [FAIL] obs {o['obs_id']}: methodology_code '{mc}' not in codes.csv")
        if ot not in code_ids:
            errors.append(f"  [FAIL] obs {o['obs_id']}: observation_type '{ot}' not in codes.csv")

    if errors:
        for e in errors:
            print(e)
    else:
        print("  PASS — All foreign keys valid")

    # ── Prediction accuracy ───────────────────────────────────────
    print(f"\n[PREDICTION ACCURACY]")
    predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    print(f"  Predictions:  {len(predictions)}")
    print(f"  Outcomes:     {len(outcomes)}")
    if predictions:
        for p in predictions:
            print(f"\n  PREDICTION: {p['metric_name']}")
            print(f"    Claimed: {p['metric_value'][:80]}")
        for o in outcomes:
            print(f"\n  OUTCOME: {o['metric_name']}")
            print(f"    Result: {o['metric_value'][:80]}")

    # ── Technologies lifecycle ────────────────────────────────────
    print(f"\n[TECHNOLOGY LIFECYCLE]")
    for t in technologies:
        print(f"  {t['tech_name']:<40} at_study={t['lifecycle_at_study']:<10} current={t['lifecycle_current']}")

    print("\n" + "=" * 60)
    print("Validation complete.")
    return 0 if not errors else 1

if __name__ == "__main__":
    sys.exit(main())
