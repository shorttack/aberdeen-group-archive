#!/usr/bin/env python3
"""
demo_analysis.py
================
Demonstration analysis script for the Frictionless Data Package:
  Aberdeen Group (1995) — Data Warehouse Query Tools: Evolving to Relational OLAP
  Study ID: aberdeen-1995-data-warehouse-olap

Source: https://web.archive.org/web/19970112010847/http://www.aberdeen.com:80/secure/viewpnts/v8n8/v8n8.htm

Run from the package root directory:
    python scripts/demo_analysis.py
"""

import os
import sys
import pandas as pd

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")


def load_package():
    """Load all CSV tables from data/ into a dict of DataFrames."""
    tables = {}
    for name in ["studies", "entities", "technologies", "observations", "codes"]:
        path = os.path.join(DATA_DIR, f"{name}.csv")
        tables[name] = pd.read_csv(path)
    return tables


# ---------------------------------------------------------------------------
# Analysis functions
# ---------------------------------------------------------------------------

def print_section(title: str):
    width = 70
    print("\n" + "=" * width)
    print(f"  {title}")
    print("=" * width)


def study_overview(tables):
    print_section("1. STUDY OVERVIEW")
    s = tables["studies"].iloc[0]
    print(f"  Title     : {s['title']}")
    print(f"  Author    : {s['author']}")
    print(f"  Date      : {s['date']}")
    print(f"  Domain    : {s['domain']}")
    print(f"  Methods   : {s['methodology']}")
    print(f"  Pages     : {s['pages']}")
    print(f"  Source    : {s['source_url']}")


def entity_status_summary(tables):
    print_section("2. ENTITY STATUS SUMMARY (as of 2026)")
    ents = tables["entities"]
    status_counts = ents["status"].value_counts()
    print("\n  Status breakdown:")
    for status, count in status_counts.items():
        print(f"    {status:<15} {count:>3} entities")

    print("\n  Still active entities:")
    active = ents[ents["status"] == "active"][["entity_name", "sector", "years_active"]]
    for _, row in active.iterrows():
        print(f"    - {row['entity_name']} ({row['sector']}, {row['years_active']})")

    print("\n  Acquired entities with known successors:")
    acquired = ents[ents["status"] == "acquired"][["entity_name", "successor"]].dropna()
    for _, row in acquired.iterrows():
        print(f"    - {row['entity_name']} → {row['successor']}")


def technology_lifecycle_shift(tables):
    print_section("3. TECHNOLOGY LIFECYCLE SHIFT (1995 → 2026)")
    techs = tables["technologies"]

    print("\n  Technologies that were EMERGING in 1995 and are still ACTIVE in 2026:")
    still_emerging = techs[
        (techs["lifecycle_at_study"] == "emerging") &
        (techs["lifecycle_current"] == "active")
    ][["tech_name", "category", "vendor"]]
    for _, row in still_emerging.iterrows():
        print(f"    - {row['tech_name']} [{row['category']}]")

    print("\n  Technologies that were MAINSTREAM in 1995 but are now OBSOLETE/DISCONTINUED/LEGACY:")
    declined = techs[
        (techs["lifecycle_at_study"] == "mainstream") &
        (techs["lifecycle_current"].isin(["obsolete", "discontinued", "legacy", "legacy-niche"]))
    ][["tech_name", "lifecycle_current"]]
    for _, row in declined.iterrows():
        print(f"    - {row['tech_name']} → {row['lifecycle_current']}")

    print("\n  Technology category breakdown:")
    cat_counts = techs["category"].value_counts()
    for cat, count in cat_counts.head(10).items():
        print(f"    {cat:<35} {count:>2}")


def observation_type_breakdown(tables):
    print_section("4. OBSERVATION TYPE BREAKDOWN")
    obs = tables["observations"]
    type_counts = obs["observation_type"].value_counts()
    print(f"\n  Total observations: {len(obs)}")
    print("\n  By type:")
    for otype, count in type_counts.items():
        print(f"    {otype:<30} {count:>3}")

    print("\n  By confidence level:")
    conf_counts = obs["confidence"].value_counts()
    for conf, count in conf_counts.items():
        print(f"    {conf:<10} {count:>3}")

    print("\n  By source page:")
    page_counts = obs["source_page"].value_counts().sort_index()
    for page, count in page_counts.items():
        print(f"    Page {int(page)}: {count:>3} observations")


def key_market_data(tables):
    print_section("5. KEY MARKET DATA POINTS")
    obs = tables["observations"]
    market_data = obs[obs["observation_type"].isin(["market-data", "market-assessment"])]
    print()
    for _, row in market_data.iterrows():
        print(f"  [{row['obs_id']}] {row['metric_name']}")
        print(f"         Value : {row['metric_value']}")
        print(f"         Conf  : {row['confidence']} | Method: {row['methodology_code']} | Page: {row['source_page']}")
        print()


def forecasts_and_predictions(tables):
    print_section("6. FORECASTS & PREDICTIONS (1995 vantage)")
    obs = tables["observations"]
    forecasts = obs[obs["observation_type"] == "market-forecast"]
    print()
    for _, row in forecasts.iterrows():
        print(f"  [{row['obs_id']}] {row['metric_name']}")
        print(f"         Prediction : {row['metric_value']}")
        print(f"         Confidence : {row['confidence']}")
        print(f"         Notes      : {row['notes'][:100]}...")
        print()


def entity_observation_matrix(tables):
    print_section("7. ENTITY OBSERVATION COUNT")
    obs = tables["observations"]
    ents = tables["entities"]
    entity_obs = obs[obs["entity_id"].notna()].groupby("entity_id").size().reset_index(name="obs_count")
    entity_obs = entity_obs.merge(ents[["entity_id", "entity_name"]], on="entity_id")
    entity_obs = entity_obs.sort_values("obs_count", ascending=False)
    print()
    for _, row in entity_obs.iterrows():
        print(f"  {row['entity_name']:<35} {row['obs_count']:>3} observations")


def technology_observation_count(tables):
    print_section("8. TECHNOLOGY OBSERVATION COUNT")
    obs = tables["observations"]
    techs = tables["technologies"]
    tech_obs = obs[obs["tech_id"].notna()].groupby("tech_id").size().reset_index(name="obs_count")
    tech_obs = tech_obs.merge(techs[["tech_id", "tech_name"]], on="tech_id")
    tech_obs = tech_obs.sort_values("obs_count", ascending=False)
    print()
    for _, row in tech_obs.head(15).iterrows():
        print(f"  {row['tech_name']:<45} {row['obs_count']:>3} observations")


def rolap_vs_molap_comparison(tables):
    print_section("9. ROLAP vs MOLAP — KEY DIFFERENTIATORS FROM STUDY")
    obs = tables["observations"]
    techs = tables["technologies"]

    rolap_id = techs[techs["tech_name"].str.contains("Relational OLAP", na=False)]["tech_id"].iloc[0]
    molap_id = techs[techs["tech_name"].str.contains("Multidimensional OLAP", na=False)]["tech_id"].iloc[0]

    print("\n  ROLAP observations:")
    for _, row in obs[obs["tech_id"] == rolap_id].iterrows():
        print(f"    [{row['observation_type']}] {row['metric_name']}: {row['metric_value'][:80]}")

    print("\n  MOLAP / MDB limitations:")
    mdb_id = techs[techs["tech_name"].str.contains("Multidimensional Database", na=False)]["tech_id"].iloc[0]
    for _, row in obs[obs["tech_id"].isin([molap_id, mdb_id])].iterrows():
        print(f"    [{row['observation_type']}] {row['metric_name']}: {row['metric_value'][:80]}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("\nAberdeen Group (1995) — Data Warehouse Query Tools: Evolving to Relational OLAP")
    print("Frictionless Data Package Demo Analysis")
    print("Source: https://web.archive.org/web/19970112010847/http://www.aberdeen.com:80/secure/viewpnts/v8n8/v8n8.htm")

    try:
        tables = load_package()
    except FileNotFoundError as e:
        print(f"\nERROR: Could not load data files. Run from the package root directory.\n  {e}")
        sys.exit(1)

    study_overview(tables)
    entity_status_summary(tables)
    technology_lifecycle_shift(tables)
    observation_type_breakdown(tables)
    key_market_data(tables)
    forecasts_and_predictions(tables)
    entity_observation_matrix(tables)
    technology_observation_count(tables)
    rolap_vs_molap_comparison(tables)

    print("\n" + "=" * 70)
    print("  Analysis complete.")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
