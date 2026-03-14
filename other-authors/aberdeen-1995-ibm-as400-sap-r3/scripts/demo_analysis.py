#!/usr/bin/env python3
"""
demo_analysis.py
================
Demonstration analysis script for the Aberdeen Group (1995) data package:
  "IBM's AS/400 and SAP's R/3: Making the Complex and Slow Both Simple and Fast"

Study ID: aberdeen-1995-ibm-as400-sap-r3

This script loads all CSV tables from the data package, validates integrity,
and produces a series of summary analyses demonstrating how to work with the data.

Usage:
    python scripts/demo_analysis.py

Requirements:
    pip install pandas tabulate
"""

import os
import sys
import pandas as pd

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PKG_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PKG_DIR, "data")


def load_tables():
    """Load all CSV tables from the data package."""
    tables = {}
    for name in ["studies", "entities", "technologies", "observations", "codes"]:
        path = os.path.join(DATA_DIR, f"{name}.csv")
        tables[name] = pd.read_csv(path, dtype=str)
        print(f"  Loaded {name}.csv  ({len(tables[name])} rows, {len(tables[name].columns)} cols)")
    return tables


def print_section(title: str):
    print()
    print("=" * 70)
    print(f"  {title}")
    print("=" * 70)


# ---------------------------------------------------------------------------
# 1. Study metadata
# ---------------------------------------------------------------------------
def show_study_metadata(studies: pd.DataFrame):
    print_section("1. Study Metadata")
    row = studies.iloc[0]
    print(f"  Study ID    : {row['study_id']}")
    print(f"  Study #     : {row['study_num']}")
    print(f"  Title       : {row['title']}")
    print(f"  Author      : {row['author']}")
    print(f"  Date        : {row['date']}")
    print(f"  Type        : {row['study_type']}")
    print(f"  Domain      : {row['domain']}")
    print(f"  Methodology : {row['methodology']}")
    print(f"  Source URL  : {row['source_url']}")


# ---------------------------------------------------------------------------
# 2. Entity status summary
# ---------------------------------------------------------------------------
def show_entity_status(entities: pd.DataFrame):
    print_section("2. Entity Status Summary (as of 2026)")
    status_counts = entities["entity_status"].value_counts()
    print("  Current status distribution:")
    for status, count in status_counts.items():
        print(f"    {status:15s}  {count} entities")
    print()
    print("  Full entity list:")
    for _, row in entities.iterrows():
        successor = f" -> {row['successor_entity']}" if pd.notna(row.get("successor_entity")) and row["successor_entity"] else ""
        print(f"    [{row['entity_status']:10s}]  {row['entity_name']}{successor}")


# ---------------------------------------------------------------------------
# 3. Technology lifecycle summary
# ---------------------------------------------------------------------------
def show_tech_lifecycle(technologies: pd.DataFrame):
    print_section("3. Technology Lifecycle Summary (as of 2026)")
    status_counts = technologies["tech_status"].value_counts()
    print("  Tech lifecycle status distribution:")
    for status, count in status_counts.items():
        print(f"    {status:12s}  {count} technologies")
    print()
    print("  Full technology list:")
    for _, row in technologies.iterrows():
        successor = f" -> {row['successor_tech']}" if pd.notna(row.get("successor_tech")) and row["successor_tech"] else ""
        print(f"    [{row['tech_status']:10s}]  {row['tech_name']}{successor}")


# ---------------------------------------------------------------------------
# 4. Financial & market metrics
# ---------------------------------------------------------------------------
def show_financial_metrics(observations: pd.DataFrame):
    print_section("4. Key Financial & Market Metrics (from study)")
    fin_obs = observations[
        observations["obs_type"].isin(["financial-metric", "market-data", "market-share"])
    ].copy()
    print(f"  {len(fin_obs)} financial/market observations:\n")
    for _, row in fin_obs.iterrows():
        entity = row.get("subject_entity_id", "")
        metric = row.get("metric_name", "")
        value = row.get("metric_value", "")
        unit = row.get("metric_unit", "")
        period = row.get("period", "")
        print(f"  [{entity}]")
        print(f"    Metric : {metric}")
        print(f"    Value  : {value} {unit}  ({period})")
        if pd.notna(row.get("verbatim_quote")) and row["verbatim_quote"]:
            quote = row["verbatim_quote"]
            if len(quote) > 90:
                quote = quote[:87] + "..."
            print(f"    Quote  : \"{quote}\"")
        print()


# ---------------------------------------------------------------------------
# 5. AS/400 Advanced Series product line (Table 1 summary)
# ---------------------------------------------------------------------------
def show_as400_product_line(observations: pd.DataFrame):
    print_section("5. AS/400 Advanced Series Product Line (Table 1)")
    models = ["40S", "50S", "53S", "400", "500", "510", "530"]
    model_types = {
        "40S": "Advanced Server", "50S": "Advanced Server", "53S": "Advanced Server",
        "400": "Advanced System", "500": "Advanced System",
        "510": "Advanced System", "530": "Advanced System"
    }
    spec_obs = observations[
        (observations["obs_type"] == "product-spec") &
        (observations["subject_tech_id"] == "as400-advanced-series")
    ]

    def get_val(model, metric):
        rows = spec_obs[
            (spec_obs["metric_name"].str.contains(model, na=False)) &
            (spec_obs["metric_name"].str.contains(metric, na=False))
        ]
        if len(rows):
            return rows.iloc[0]["metric_value"]
        return "—"

    header = f"  {'Model':<8} {'Type':<17} {'Proc':>5} {'Mem Min':>8} {'Mem Max':>10} {'Disk Max':>10} {'TPm Min':>8} {'TPm Max':>8}"
    print(header)
    print("  " + "-" * 75)
    for m in models:
        proc_rows = spec_obs[spec_obs["metric_name"] == f"processors_model_{m}"]
        mem_min_rows = spec_obs[spec_obs["metric_name"] == f"memory_min_model_{m}"]
        mem_max_rows = spec_obs[spec_obs["metric_name"] == f"memory_max_model_{m}"]
        disk_max_rows = spec_obs[spec_obs["metric_name"] == f"disk_max_model_{m}"]
        tpm_min_rows = spec_obs[spec_obs["metric_name"] == f"tpm_min_model_{m}"]
        tpm_max_rows = spec_obs[spec_obs["metric_name"] == f"tpm_max_model_{m}"]
        # estimated_tpm for 40S is different field name
        if m == "40S":
            tpm_min_rows = spec_obs[spec_obs["metric_name"] == "estimated_tpm_model_40S"]
            tpm_max_rows = tpm_min_rows

        proc = proc_rows.iloc[0]["metric_value"] if len(proc_rows) else "—"
        mem_min = (mem_min_rows.iloc[0]["metric_value"] + "MB") if len(mem_min_rows) else "—"
        mem_max_v = mem_max_rows.iloc[0]["metric_value"] if len(mem_max_rows) else "—"
        if mem_max_v != "—":
            mem_max_i = int(mem_max_v)
            mem_max = f"{mem_max_i}MB" if mem_max_i < 1024 else f"{mem_max_i // 1024}GB"
        else:
            mem_max = "—"
        disk_max = (disk_max_rows.iloc[0]["metric_value"] + "GB") if len(disk_max_rows) else "—"
        tpm_min = tpm_min_rows.iloc[0]["metric_value"] if len(tpm_min_rows) else "—"
        tpm_max = tpm_max_rows.iloc[0]["metric_value"] if len(tpm_max_rows) else "—"
        mtype = model_types.get(m, "")
        print(f"  {m:<8} {mtype:<17} {proc:>5} {mem_min:>8} {mem_max:>10} {disk_max:>10} {tpm_min:>8} {tpm_max:>8}")
    print()
    print("  Source: Aberdeen Group, September 1995 (Table 1)")
    print("  Note: TPm = Transactions per minute (IBM RampC benchmark)")


# ---------------------------------------------------------------------------
# 6. SAP R/3 module inventory (Table 2)
# ---------------------------------------------------------------------------
def show_r3_modules(observations: pd.DataFrame):
    print_section("6. SAP R/3 CSS Module Inventory (Table 2)")
    module_obs = observations[
        (observations["obs_type"] == "product-module") &
        (observations["subject_tech_id"] == "sap-r3")
    ].copy()

    # Group by module area inferred from notes
    for area_keyword, area_label in [
        ("Accounting", "Accounting"), ("Logistics", "Logistics"),
        ("Human Resources", "Human Resources"), ("Industry Solution", "Industry Solutions")
    ]:
        area_modules = module_obs[
            module_obs["notes"].str.contains(area_keyword, na=False)
        ]["metric_value"].tolist()
        print(f"  {area_label} ({len(area_modules)} modules):")
        for m in area_modules:
            print(f"    • {m}")
        print()
    print("  Source: Aberdeen Group, September 1995 (Table 2)")


# ---------------------------------------------------------------------------
# 7. Observation type breakdown
# ---------------------------------------------------------------------------
def show_observation_breakdown(observations: pd.DataFrame):
    print_section("7. Observations by Type")
    breakdown = observations["obs_type"].value_counts()
    total = len(observations)
    print(f"  Total observations: {total}\n")
    for obs_type, count in breakdown.items():
        bar = "█" * count
        print(f"  {obs_type:<20s}  {count:3d}  {bar}")


# ---------------------------------------------------------------------------
# 8. FK integrity check
# ---------------------------------------------------------------------------
def check_integrity(tables: dict):
    print_section("8. Foreign Key Integrity Check")
    errors = []
    study_ids = set(tables["studies"]["study_id"])
    entity_ids = set(tables["entities"]["entity_id"])
    tech_ids = set(tables["technologies"]["tech_id"])

    # entities.study_id -> studies.study_id
    for val in tables["entities"]["study_id"].dropna():
        if val not in study_ids:
            errors.append(f"entities.study_id '{val}' not in studies")

    # technologies.study_id -> studies.study_id
    for val in tables["technologies"]["study_id"].dropna():
        if val not in study_ids:
            errors.append(f"technologies.study_id '{val}' not in studies")

    # technologies.vendor_entity_id -> entities.entity_id
    for val in tables["technologies"]["vendor_entity_id"].dropna():
        if val not in entity_ids:
            errors.append(f"technologies.vendor_entity_id '{val}' not in entities")

    # observations.study_id -> studies.study_id
    for val in tables["observations"]["study_id"].dropna():
        if val not in study_ids:
            errors.append(f"observations.study_id '{val}' not in studies")

    # observations.subject_entity_id -> entities.entity_id (allow empty)
    for val in tables["observations"]["subject_entity_id"].dropna():
        if val and val not in entity_ids:
            errors.append(f"observations.subject_entity_id '{val}' not in entities")

    # observations.subject_tech_id -> technologies.tech_id (allow empty)
    for val in tables["observations"]["subject_tech_id"].dropna():
        if val and val not in tech_ids:
            errors.append(f"observations.subject_tech_id '{val}' not in technologies")

    if errors:
        print(f"  FAIL: {len(errors)} integrity error(s):")
        for e in errors:
            print(f"    - {e}")
        return False
    else:
        print(f"  PASS: All FK references valid across {len(tables)} tables.")
        return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print()
    print("Aberdeen Group (1995) — AS/400 & SAP R/3 Data Package")
    print("Demo Analysis Script")
    print("Study: aberdeen-1995-ibm-as400-sap-r3")
    print()
    print("Loading tables...")
    tables = load_tables()

    show_study_metadata(tables["studies"])
    show_entity_status(tables["entities"])
    show_tech_lifecycle(tables["technologies"])
    show_financial_metrics(tables["observations"])
    show_as400_product_line(tables["observations"])
    show_r3_modules(tables["observations"])
    show_observation_breakdown(tables["observations"])
    ok = check_integrity(tables)

    print()
    print("=" * 70)
    print("  Analysis complete.")
    print("=" * 70)
    print()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
