#!/usr/bin/env python3
"""
Demo analysis script for:
  DynaSoft's BoKS Family: A Pragmatic Choice for Single Sign-On
  Aberdeen Group Vendor Profile, June 1997
  Study ID: 1997-dynasoft's-boks-family--a-pragmatic-e6df7d
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
    print("=" * 70)
    print("Aberdeen Group: DynaSoft's BoKS Family — A Pragmatic Choice for SSO")
    print("Vendor Profile, June 1997")
    print("=" * 70)

    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")

    study = studies[0]
    print(f"\nTitle:  {study['title']}")
    print(f"Date:   {study['date']} | Type: {study['type']}")
    print(f"Scores: Importance={study['importance']}/5  Relevance={study['relevance']}/5  Prescience={study['prescience']}/5")

    # Observation type distribution
    print(f"\nObservations ({len(observations)} total):")
    obs_types = Counter(o["observation_type"] for o in observations)
    for otype, count in obs_types.most_common():
        print(f"  {otype:<30} {count:>3}")

    # Key enterprise customers
    print("\nNamed Enterprise BoKS Customers (1997):")
    for obs in observations:
        if obs["obs_id"] == "OBS-DYS-016":
            customers = obs["metric_value"].split(", ")
            for c in customers:
                print(f"  - {c}")

    # Entity acquisition chain
    print("\nDynaSoft Acquisition Chain:")
    acquisition_chain = [
        ("DynaSoft AB", "1984-1997", "Acquired by Security Dynamics $115M July 1997"),
        ("Security Dynamics", "1984-1999", "Renamed RSA Security in 1999"),
        ("RSA Security", "1999-2006", "Acquired by EMC Corporation for $2.1B in 2006"),
        ("RSA (EMC division)", "2006-2016", "Became part of Dell Technologies via EMC acquisition"),
        ("RSA (Dell)", "2016-2020", "Sold to Symphony Technology Group for $2.075B in 2020"),
        ("RSA Security (independent)", "2020-present", "Independent company under STG"),
    ]
    for company, years, note in acquisition_chain:
        print(f"  {company:<35} {years:<15} {note}")

    # Technology lifecycle
    print("\nTechnology Lifecycle Changes:")
    for tech in technologies:
        print(f"  {tech['tech_name']:<40} {tech['lifecycle_at_study']:<20} → {tech['lifecycle_current']}")

    print("\n" + "=" * 70)
    print("Source: https://web.archive.org/web/19971007160356/")
    print("  http://www.aberdeen.com:80/secure/profiles/1997/dyna/body.htm")
    print("License: CC-BY-4.0")


if __name__ == "__main__":
    main()
