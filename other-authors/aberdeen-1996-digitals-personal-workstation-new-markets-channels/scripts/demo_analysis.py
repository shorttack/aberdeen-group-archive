#!/usr/bin/env python3
"""Demo analysis for aberdeen-1996-digitals-personal-workstation-new-markets-channels."""
import csv, os

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

    print("=== Digital Personal Workstation - Dataset Summary ===")
    print(f"Study: {studies[0]['title'][:60]}... ({studies[0]['date']})")
    print(f"Entities: {len(entities)}, Technologies: {len(technologies)}, Observations: {len(observations)}")

    type_counts = {}
    for o in observations:
        t = o["observation_type"]
        type_counts[t] = type_counts.get(t, 0) + 1
    print("\nObservation types:")
    for t, c in sorted(type_counts.items()):
        print(f"  {t}: {c}")

    benchmarks = [o for o in observations if o["observation_type"] == "benchmark-result"]
    print("\nBenchmark Results:")
    for b in benchmarks:
        print(f"  {b['metric_name'][:70]}")
        print(f"    -> {b['metric_value'][:70]}")

    entity_ids = {e["entity_id"] for e in entities}
    tech_ids = {t["tech_id"] for t in technologies}
    code_ids = {c["code_id"] for c in codes}
    errors = []
    for o in observations:
        if o["entity_id"] and o["entity_id"] not in entity_ids:
            errors.append(f"Missing entity: {o['entity_id']}")
        if o["tech_id"] and o["tech_id"] not in tech_ids:
            errors.append(f"Missing tech: {o['tech_id']}")
        if o["observation_type"] not in code_ids:
            errors.append(f"Missing obs type: {o['observation_type']}")
    print("\n[OK] Referential integrity: PASS" if not errors else f"\n[REVIEW] {len(errors)} errors: {errors[:3]}")

if __name__ == "__main__":
    main()
