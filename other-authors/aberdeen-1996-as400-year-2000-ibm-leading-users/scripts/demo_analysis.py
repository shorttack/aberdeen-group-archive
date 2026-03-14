"""
Demo Analysis Script
Study: aberdeen-1996-as400-year-2000-ibm-leading-users
AS/400 and the Year 2000: IBM Leading Users Across an Unknown Chasm
Aberdeen Group, September 27, 1996
"""

import csv
import os
from collections import Counter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")


def load_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    print("=" * 60)
    print("Aberdeen Group Archival Analysis")
    print("Study: aberdeen-1996-as400-year-2000-ibm-leading-users")
    print("=" * 60)

    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")

    s = studies[0]
    print(f"\nTitle: {s['title']}")
    print(f"Date: {s['date']} | Type: {s['type']}")
    print(f"Importance: {s['importance']} | Relevance: {s['relevance']} | Prescience: {s['prescience']}")

    print(f"\n--- Entities ({len(entities)}) ---")
    for e in entities:
        print(f"  {e['entity_name']} [{e['entity_type']}] — {e['status']}")

    print(f"\n--- Technologies ({len(technologies)}) ---")
    for t in technologies:
        print(f"  {t['tech_name']}: {t['lifecycle_at_study']} → {t['lifecycle_current']}")

    print(f"\n--- Observations ({len(observations)}) ---")
    type_counts = Counter(o["observation_type"] for o in observations)
    for ot, count in sorted(type_counts.items()):
        print(f"  {ot}: {count}")

    print("\n--- Key Prescience Findings ---")
    print("  1. IBM Y2K leadership → greater user loyalty: CONFIRMED (AS/400 survived, rebranded as IBM i)")
    print("  2. No single-supplier silver bullet: CONFIRMED (required massive industry effort)")
    print("  3. Continuous Y2K 'gotchas': CONFIRMED (embedded systems, leap year 2000 bugs)")
    print("  4. FASB expensing requirement makes costs hit bottom line: CONFIRMED")

    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()
