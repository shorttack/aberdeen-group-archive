#!/usr/bin/env python3
"""Demo analysis for: Managing the People Dimension of Major Technology Transitions (Aberdeen Group, 1997)"""
import csv, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_csv(name):
    path = os.path.join(BASE, "data", name)
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")
    codes = load_csv("codes.csv")

    print("=" * 60)
    print(f"Study: {studies[0]['title']}")
    print(f"Author: {studies[0]['author']} | Date: {studies[0]['date']}")
    print(f"Importance: {studies[0]['importance']} | Relevance: {studies[0]['relevance']} | Prescience: {studies[0]['prescience']}")
    print("=" * 60)
    print(f"Entities: {len(entities)} | Technologies: {len(technologies)} | Observations: {len(observations)}")

    from collections import Counter
    type_counts = Counter(o["observation_type"] for o in observations)
    print("\nObservation types:")
    for k, v in sorted(type_counts.items()):
        print(f"  {k}: {v}")

    entity_ids = {e["entity_id"] for e in entities} | {""}
    tech_ids = {t["tech_id"] for t in technologies} | {""}
    code_ids = {c["code_id"] for c in codes}
    errors = []
    for o in observations:
        if o["entity_id"] not in entity_ids:
            errors.append(f"Unknown entity_id: {o['entity_id']} in {o['obs_id']}")
        if o["tech_id"] not in tech_ids:
            errors.append(f"Unknown tech_id: {o['tech_id']} in {o['obs_id']}")
        if o["observation_type"] not in code_ids:
            errors.append(f"Unknown observation_type: {o['observation_type']} in {o['obs_id']}")
    if errors:
        print("\nINTEGRITY ERRORS:")
        for e in errors:
            print(f"  ERROR: {e}")
    else:
        print("\nReferential integrity: PASS")

if __name__ == "__main__":
    main()
