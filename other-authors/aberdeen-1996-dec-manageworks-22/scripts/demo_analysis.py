#!/usr/bin/env python3
"""Demo analysis script for aberdeen-1996-dec-manageworks-22 dataset."""
import csv
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_csv(name):
    with open(os.path.join(BASE, "data", name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")
    codes = load_csv("codes.csv")

    print("=== ManageWORKS 2.2 Market Profile - Dataset Summary ===")
    print(f"Study: {studies[0]['title']} ({studies[0]['date']})")
    print(f"Entities: {len(entities)}")
    print(f"Technologies: {len(technologies)}")
    print(f"Observations: {len(observations)}")

    # Observation type breakdown
    type_counts = {}
    for o in observations:
        t = o["observation_type"]
        type_counts[t] = type_counts.get(t, 0) + 1
    print("\nObservation types:")
    for t, c in sorted(type_counts.items()):
        print(f"  {t}: {c}")

    # Referential integrity
    entity_ids = {e["entity_id"] for e in entities}
    tech_ids = {t["tech_id"] for t in technologies}
    code_ids = {c["code_id"] for c in codes}
    errors = []
    for o in observations:
        if o["entity_id"] and o["entity_id"] not in entity_ids:
            errors.append(f"Missing entity: {o['entity_id']} in {o['obs_id']}")
        if o["tech_id"] and o["tech_id"] not in tech_ids:
            errors.append(f"Missing tech: {o['tech_id']} in {o['obs_id']}")
        if o["observation_type"] not in code_ids:
            errors.append(f"Missing code: {o['observation_type']} in {o['obs_id']}")
        if o["methodology_code"] not in code_ids:
            errors.append(f"Missing method code: {o['methodology_code']} in {o['obs_id']}")

    if errors:
        print("\n[REVIEW] Integrity errors:")
        for e in errors:
            print(f"  {e}")
    else:
        print("\n[OK] Referential integrity: PASS")

    # Prediction accuracy
    preds = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    print(f"\nPredictions: {len(preds)}, Outcomes: {len(outcomes)}")
    for p in preds:
        print(f"  Prediction: {p['metric_name']} -> {p['metric_value'][:80]}")
    for o in outcomes:
        print(f"  Outcome:    {o['metric_name']} -> {o['metric_value'][:80]}")

if __name__ == "__main__":
    main()
