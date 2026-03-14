"""
Demo Analysis Script
Study: aberdeen-1996-3com-reconciling-clientserver-development-internet
Reconciling Client/Server Development and the Internet
Aberdeen Group (Tim Sloane), November 1996
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
    print("Study: aberdeen-1996-3com-reconciling-clientserver-development-internet")
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
    print("  1. EDI over Internet within 5 years → CONFIRMED (AS2 standard 2002)")
    print("  2. Java not suited for complex OLTP in 1996 → CONFIRMED (J2EE addressed by 1999-2001)")
    print("  3. App-server replacing CGI → CONFIRMED (WebSphere, Tomcat, JBoss dominated by 2000)")
    print("  4. Browser as 'client for the masses' / server-centric → CONFIRMED (modern SaaS model)")

    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()
