#!/usr/bin/env python3
"""
Demo Analysis: Dialogic CT Media Study (1997)
Study ID: 1997-dialogic-ct-media-sets-the-pace-for-440d5e
"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_csv(name):
    with open(os.path.join(BASE, "data", f"{name}.csv")) as f:
        reader = csv.DictReader(f)
        return list(reader)

def main():
    observations = load_csv("observations")
    entities = load_csv("entities")
    technologies = load_csv("technologies")

    print("=== Dialogic CT Media Study — Demo Analysis ===\n")
    
    # Count observation types
    obs_types = {}
    for o in observations:
        t = o["observation_type"]
        obs_types[t] = obs_types.get(t, 0) + 1
    print("Observation types:")
    for k, v in sorted(obs_types.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")
    
    # Predictions vs Outcomes
    preds = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    print(f"\nViability predictions: {len(preds)}")
    print(f"Actual outcomes documented: {len(outcomes)}")
    
    # Entity status summary
    print("\nEntity Status Summary:")
    for e in entities:
        print(f"  {e['entity_name']}: {e['status']} -> {e['successor']}")
    
    # Technology lifecycle
    print("\nTechnology Lifecycle (current):")
    for t in technologies:
        print(f"  {t['tech_name']}: {t['lifecycle_current']}")

if __name__ == "__main__":
    main()
