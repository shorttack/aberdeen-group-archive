#!/usr/bin/env python3
"""Demo Analysis: Digital HPTC Leadership Study (1997)"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_csv(name):
    with open(os.path.join(BASE, "data", f"{name}.csv")) as f:
        return list(csv.DictReader(f))

def main():
    observations = load_csv("observations")
    entities = load_csv("entities")
    technologies = load_csv("technologies")

    print("=== Digital HPTC Leadership Study — Demo Analysis ===\n")
    
    obs_types = {}
    for o in observations:
        t = o["observation_type"]
        obs_types[t] = obs_types.get(t, 0) + 1
    print("Observation types:")
    for k, v in sorted(obs_types.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")
    
    preds = [o for o in observations if o["observation_type"] == "viability-prediction"]
    print(f"\nViability predictions ({len(preds)}):")
    for p in preds:
        print(f"  {p['metric_name']}: {p['metric_value']}")
    
    print("\nEntity outcomes:")
    for e in entities:
        print(f"  {e['entity_name']}: {e['status']}")

if __name__ == "__main__":
    main()
