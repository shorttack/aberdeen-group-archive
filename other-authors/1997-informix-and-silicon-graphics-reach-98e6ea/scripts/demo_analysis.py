"""
Demo Analysis Script — 1997-informix-and-silicon-graphics-reach-98e6ea
Informix and Silicon Graphics Reach New TPC-C SMP High-Water Mark
Aberdeen Group, 1997
"""

import csv
import json
from pathlib import Path
from collections import Counter

BASE = Path(__file__).parent.parent


def load_csv(name):
    with open(BASE / "data" / f"{name}.csv", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    print("=" * 60)
    print("Aberdeen Group — Informix/SGI TPC-C Benchmark (1997)")
    print("Frictionless Data Package Demo Analysis")
    print("=" * 60)

    studies = load_csv("studies")
    s = studies[0]
    print(f"\nStudy: {s['title']}")
    print(f"Date:  {s['date']}")
    print(f"\nScores:")
    print(f"  Importance: {s['importance']}/10")
    print(f"  Relevance:  {s['relevance']}/10")
    print(f"  Prescience: {s['prescience']}/10")

    obs = load_csv("observations")
    print(f"\nObservations: {len(obs)}")
    obs_types = Counter(o["observation_type"] for o in obs)
    for otype, count in obs_types.most_common():
        print(f"  {otype:<35} {count}")

    # Show benchmark results
    benchmarks = [o for o in obs if o["observation_type"] == "benchmark-result"]
    print(f"\nBenchmark Results ({len(benchmarks)}):")
    for b in benchmarks:
        print(f"  {b['metric_name']:<35} {b['metric_value']}")

    # Predictions vs outcomes
    preds = [o for o in obs if o["observation_type"] == "viability-prediction"]
    outs = [o for o in obs if o["observation_type"] == "actual-outcome"]
    print(f"\nPredictions: {len(preds)}  Outcomes documented: {len(outs)}")

    entities = load_csv("entities")
    print(f"\nEntities: {len(entities)}")
    for e in entities:
        print(f"  {e['entity_name']:<40} Status: {e['status'][:40]}")

    print("\n--- End of Demo Analysis ---")


if __name__ == "__main__":
    main()
