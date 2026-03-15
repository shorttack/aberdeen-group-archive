#!/usr/bin/env python3
"""
Demo analysis for: IBM's Solution-Centric Global Healthcare Industry Practice - Just What the Doctor Ordered
Study ID: 1997-ibm-s-solution-centric-global-healt-7a073f
"""

import pandas as pd
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_data():
    studies = pd.read_csv(os.path.join(BASE, "data/studies.csv"))
    entities = pd.read_csv(os.path.join(BASE, "data/entities.csv"))
    technologies = pd.read_csv(os.path.join(BASE, "data/technologies.csv"))
    observations = pd.read_csv(os.path.join(BASE, "data/observations.csv"))
    codes = pd.read_csv(os.path.join(BASE, "data/codes.csv"))
    return studies, entities, technologies, observations, codes

def main():
    studies, entities, technologies, observations, codes = load_data()

    print("=== Study Overview ===")
    s = studies.iloc[0]
    print(f"Title: {s.title}")
    print(f"Date: {s.date}")
    print(f"Domain: {s.subject_domain}")
    print(f"Importance: {s.importance}/5 | Relevance: {s.relevance}/5 | Prescience: {s.prescience}/5")
    print()

    print("=== Entity Types ===")
    print(entities.groupby("entity_type")["entity_name"].count().sort_values(ascending=False).to_string())
    print()

    print("=== Technology Lifecycle (Current) ===")
    print(technologies.groupby("lifecycle_current")["tech_name"].count().sort_values(ascending=False).to_string())
    print()

    print("=== Observation Types ===")
    print(observations.groupby("observation_type")["obs_id"].count().sort_values(ascending=False).to_string())
    print()

    print("=== Viability Predictions ===")
    preds = observations[observations["observation_type"] == "viability-prediction"]
    for _, row in preds.iterrows():
        print(f"  {row.obs_id}: {row.metric_name}")
        print(f"    Value: {row.metric_value[:80]}...")
    print()

    print("=== Actual Outcomes ===")
    outcomes = observations[observations["observation_type"] == "actual-outcome"]
    for _, row in outcomes.iterrows():
        print(f"  {row.obs_id} ({row.year_observed}): {row.metric_name}")
        print(f"    Value: {row.metric_value[:80]}...")
    print()

    print("=== Entity Status Summary ===")
    print(entities.groupby("status")["entity_name"].count().sort_values(ascending=False).to_string())
    print()

if __name__ == "__main__":
    main()
