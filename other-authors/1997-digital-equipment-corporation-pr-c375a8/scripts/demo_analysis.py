#!/usr/bin/env python3
"""Demo Analysis: Digital Equipment Corporation Telecom Study (1997)"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_csv(name):
    with open(os.path.join(BASE, "data", f"{name}.csv")) as f:
        return list(csv.DictReader(f))

def main():
    observations = load_csv("observations")
    entities = load_csv("entities")

    print("=== Digital Equipment Corp Telecom Study — Demo Analysis ===\n")
    
    obs_types = {}
    for o in observations:
        t = o["observation_type"]
        obs_types[t] = obs_types.get(t, 0) + 1
    print("Observation types:")
    for k, v in sorted(obs_types.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")
    
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    print(f"\nActual outcomes documented: {len(outcomes)}")
    for o in outcomes:
        print(f"  {o['metric_name']}: {o['metric_value']}")

    print("\nEntity Status Summary:")
    for e in entities:
        print(f"  {e['entity_name']}: {e['status']} -> {e['successor']}")

if __name__ == "__main__":
    main()
