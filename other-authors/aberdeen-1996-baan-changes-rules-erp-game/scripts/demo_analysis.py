#!/usr/bin/env python3
"""Demo analysis script for aberdeen-1996-baan-changes-rules-erp-game dataset."""
import os, sys
import csv

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "..", "data")

def load_csv(name):
    with open(os.path.join(DATA, name), newline="") as f:
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
    print(f"Importance : {s['importance']} — {s['importance_rationale'][:80]}...")
    print(f"Relevance  : {s['relevance']} — {s['relevance_rationale'][:80]}...")
    print(f"Prescience : {s['prescience']} — {s['prescience_rationale'][:80]}...")

    print("\n" + "=" * 60)
    print(f"ENTITIES ({len(entities)})")
    print("=" * 60)
    for e in entities:
        print(f"  {e['entity_name']:40s} status={e['status']}")

    print("\n" + "=" * 60)
    print(f"TECHNOLOGIES ({len(technologies)})")
    print("=" * 60)
    for t in technologies:
        print(f"  {t['tech_name']:40s} lifecycle_now={t['lifecycle_current']}")

    print("\n" + "=" * 60)
    print(f"OBSERVATIONS ({len(observations)})")
    print("=" * 60)
    by_type = {}
    for o in observations:
        by_type[o['observation_type']] = by_type.get(o['observation_type'], 0) + 1
    for k, v in sorted(by_type.items()):
        print(f"  {k:30s}: {v}")

    # Referential integrity
    print("\n" + "=" * 60)
    print("REFERENTIAL INTEGRITY")
    print("=" * 60)
    entity_ids = {e['entity_id'] for e in entities}
    tech_ids = {t['tech_id'] for t in technologies}
    code_ids = {c['code_id'] for c in codes}
    errors = []
    for o in observations:
        if o['entity_id'] and o['entity_id'] not in entity_ids:
            errors.append(f"  MISSING entity_id: {o['entity_id']} in {o['obs_id']}")
        if o['tech_id'] and o['tech_id'] not in tech_ids:
            errors.append(f"  MISSING tech_id: {o['tech_id']} in {o['obs_id']}")
        if o['observation_type'] not in code_ids:
            errors.append(f"  MISSING obs type code: {o['observation_type']} in {o['obs_id']}")
    if errors:
        for e in errors:
            print(e)
    else:
        print("  All referential integrity checks PASSED")

    # Prediction accuracy
    print("\n" + "=" * 60)
    print("PREDICTION vs OUTCOME ANALYSIS")
    print("=" * 60)
    predictions = [o for o in observations if o['observation_type'] == 'viability-prediction']
    outcomes = [o for o in observations if o['observation_type'] == 'actual-outcome']
    print(f"  Predictions: {len(predictions)}")
    print(f"  Verified outcomes: {len(outcomes)}")
    for p in predictions:
        print(f"  PREDICTION: {p['metric_name']}")
        print(f"    Claimed: {p['metric_value'][:80]}")
        matching = [o for o in outcomes if o['entity_id'] == p['entity_id']]
        for m in matching:
            print(f"    OUTCOME ({m['year_observed']}): {m['metric_value'][:80]}")

if __name__ == "__main__":
    main()
