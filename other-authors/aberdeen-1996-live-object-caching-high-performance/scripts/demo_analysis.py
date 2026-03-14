#!/usr/bin/env python3
"""
Demo analysis script for: aberdeen-1996-live-object-caching-high-performance
Archival Ingest Skill v13
"""

import csv
import os
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_csv(filename):
    path = os.path.join(BASE, "data", filename)
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")
    codes = load_csv("codes.csv")

    print("=" * 60)
    print("STUDY SUMMARY")
    print("=" * 60)
    s = studies[0]
    print(f"Title      : {s['title']}")
    print(f"Author     : {s['author']}")
    print(f"Date       : {s['date']}")
    print(f"Domain     : {s['subject_domain']}")
    print(f"Importance : {s['importance']} — {s['importance_rationale']}")
    print(f"Relevance  : {s['relevance']} — {s['relevance_rationale']}")
    print(f"Prescience : {s['prescience']} — {s['prescience_rationale']}")
    print()
    print(f"Entities   : {len(entities)}")
    print(f"Technologies: {len(technologies)}")
    print(f"Observations: {len(observations)}")
    print()

    print("OBSERVATION TYPE BREAKDOWN")
    type_counts = defaultdict(int)
    for o in observations:
        type_counts[o["observation_type"]] += 1
    for t, c in sorted(type_counts.items()):
        print(f"  {t:30s} {c:3d}")
    print()

    print("REFERENTIAL INTEGRITY")
    entity_ids = {e["entity_id"] for e in entities}
    tech_ids = {t["tech_id"] for t in technologies}
    code_ids = {c["code_id"] for c in codes}
    errors = []
    for o in observations:
        if o["entity_id"] and o["entity_id"] not in entity_ids:
            errors.append(f"  [FAIL] obs {o['obs_id']}: entity_id '{o['entity_id']}' not in entities.csv")
        if o["tech_id"] and o["tech_id"] not in tech_ids:
            errors.append(f"  [FAIL] obs {o['obs_id']}: tech_id '{o['tech_id']}' not in technologies.csv")
        if o["observation_type"] not in code_ids:
            errors.append(f"  [FAIL] obs {o['obs_id']}: observation_type '{o['observation_type']}' not in codes.csv")
        if o["methodology_code"] and o["methodology_code"] not in code_ids:
            errors.append(f"  [FAIL] obs {o['obs_id']}: methodology_code '{o['methodology_code']}' not in codes.csv")
    if errors:
        for e in errors:
            print(e)
    else:
        print("  [PASS] All referential integrity checks passed.")
    print()

    predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    print(f"PREDICTION ACCURACY")
    print(f"  Predictions : {len(predictions)}")
    print(f"  Outcomes    : {len(outcomes)}")
    if predictions and outcomes:
        verified = [o for o in outcomes if o["confidence"] == "verified"]
        print(f"  Verified outcomes: {len(verified)}")
    print()
    print("=" * 60)
    print("Analysis complete.")

if __name__ == "__main__":
    main()
