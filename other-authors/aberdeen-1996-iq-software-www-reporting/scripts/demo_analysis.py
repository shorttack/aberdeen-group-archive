#!/usr/bin/env python3
"""Demo analysis for aberdeen-1996-iq-software-www-reporting dataset."""
import os, csv
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "..", "data")

def load_csv(name):
    with open(os.path.join(DATA, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")
    codes = load_csv("codes.csv")

    print("=" * 60)
    print("DATASET: aberdeen-1996-iq-software-www-reporting")
    print("=" * 60)
    s = studies[0]
    print(f"Title: {s['title']}")
    print(f"Date:  {s['date']}  |  Type: {s['type']}")
    print(f"Importance: {s['importance']}  Relevance: {s['relevance']}  Prescience: {s['prescience']}")
    print()
    print(f"Entities:     {len(entities)}")
    print(f"Technologies: {len(technologies)}")
    print(f"Observations: {len(observations)}")
    print()

    otype_counts = Counter(o["observation_type"] for o in observations)
    print("Observations by type:")
    for k, v in otype_counts.most_common():
        print(f"  {k:30s}: {v}")
    print()

    entity_ids = {e["entity_id"] for e in entities}
    tech_ids = {t["tech_id"] for t in technologies}
    code_ids = {c["code_id"] for c in codes}
    errors = []
    for o in observations:
        if o["entity_id"] and o["entity_id"] not in entity_ids:
            errors.append(f"Missing entity_id: {o['entity_id']} in {o['obs_id']}")
        if o["tech_id"] and o["tech_id"] not in tech_ids:
            errors.append(f"Missing tech_id: {o['tech_id']} in {o['obs_id']}")
        if o["observation_type"] not in code_ids:
            errors.append(f"Missing obs type: {o['observation_type']} in {o['obs_id']}")
        if o["methodology_code"] not in code_ids:
            errors.append(f"Missing method code: {o['methodology_code']} in {o['obs_id']}")
    if errors:
        print("INTEGRITY ERRORS:")
        for e in errors: print(f"  [FAIL] {e}")
    else:
        print("Referential integrity: PASS")
    print()

    predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    print(f"Viability predictions: {len(predictions)}")
    print(f"Actual outcomes:       {len(outcomes)}")
    print()
    print("Analysis complete.")

if __name__ == "__main__":
    main()
