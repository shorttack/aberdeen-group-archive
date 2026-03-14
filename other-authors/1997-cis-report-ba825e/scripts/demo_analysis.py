#!/usr/bin/env python3
import csv, os
from collections import Counter

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
    s = studies[0]
    print("=" * 70)
    print("Study: " + s["title"])
    print("Author: " + s["author"] + " | Date: " + s["date"])
    print("Importance: " + s["importance"] + " | Relevance: " + s["relevance"] + " | Prescience: " + s["prescience"])
    print("=" * 70)
    print("Entities: " + str(len(entities)) + " | Techs: " + str(len(technologies)) + " | Observations: " + str(len(observations)))
    type_counts = Counter(o["observation_type"] for o in observations)
    print("")
    print("Observation types:")
    for k, v in sorted(type_counts.items()):
        print("  " + k + ": " + str(v))

    predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    print("")
    print("Viability predictions: " + str(len(predictions)))
    print("Actual outcomes: " + str(len(outcomes)))

    print("")
    print("CIS vendor fates:")
    for e in entities:
        if e["status"] == "acquired":
            print("  " + e["entity_name"] + " -> " + e["successor"])

    entity_ids = {e["entity_id"] for e in entities} | {""}
    tech_ids = {t["tech_id"] for t in technologies} | {""}
    code_ids = {c["code_id"] for c in codes}
    errors = []
    for o in observations:
        if o["entity_id"] not in entity_ids:
            errors.append("BAD entity_id: " + o["entity_id"] + " in " + o["obs_id"])
        if o["tech_id"] not in tech_ids:
            errors.append("BAD tech_id: " + o["tech_id"] + " in " + o["obs_id"])
        if o["observation_type"] not in code_ids:
            errors.append("BAD obs type: " + o["observation_type"] + " in " + o["obs_id"])
    if errors:
        print("")
        print("VALIDATION ERRORS:")
        for e in errors:
            print("  " + e)
    else:
        print("")
        print("All observations validated OK.")

if __name__ == "__main__":
    main()
