#!/bin/bash
# inspect_sh_cols_v1.sh
# Read-only inspection of the 14 SH cols sitting in the working tree's
# _master_observations.csv. Does NOT modify anything.

CSV="$HOME/Desktop/Archive/archive_masters/_master_observations.csv"

echo "=================================================================="
echo "  SH-cols inspection: $CSV"
echo "  $(stat -f "mtime=%Sm  size=%z" -t "%Y-%m-%d %H:%M" "$CSV")"
echo "=================================================================="

# Column count + header
TOTAL_COLS=$(head -1 "$CSV" | tr ',' '\n' | wc -l | tr -d ' ')
TOTAL_ROWS=$(($(wc -l < "$CSV") - 1))
echo
echo "Total cols: $TOTAL_COLS  (HEAD has 17)"
echo "Total rows: $TOTAL_ROWS"
echo

# The 14 SH cols (positions 18-31, 1-indexed)
SH_COLS=("prescience_3y" "confidence_3y" "rationale_3y" "prescience_5y" "confidence_5y" "rationale_5y" "windows_diverge" "divergence_note" "anchor_year" "anchor_source" "scored_at_sh" "scorer_version_sh" "source_pass_sh" "raw_response_sh")

echo "Per-column non-blank counts (out of $TOTAL_ROWS rows):"
echo

# Use python for robust CSV parsing (commas in quoted rationale fields would break awk)
python3 <<PY
import csv

CSV = "$CSV"
SH = "prescience_3y confidence_3y rationale_3y prescience_5y confidence_5y rationale_5y windows_diverge divergence_note anchor_year anchor_source scored_at_sh scorer_version_sh source_pass_sh raw_response_sh".split()

with open(CSV, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames
    extras = [c for c in header if c not in {"obs_id","study_id","entity_id","tech_id","observation_type","year_observed","metric_name","metric_value","confidence","verification_method","methodology_code","source_page","notes","collection","thread_tag","section","legacy_obs_id"}]
    print(f"  Schema has {len(header)} cols, {len(extras)} extras beyond HEAD-17")
    print(f"  Extras detected: {extras}")
    print()

    counts = {c: {"nonblank": 0, "unique_vals": set(), "examples": []} for c in SH}
    total = 0
    rows_with_any_sh = 0
    sh_set_present = []

    for row in reader:
        total += 1
        any_sh = False
        for c in SH:
            v = (row.get(c) or "").strip()
            if v:
                counts[c]["nonblank"] += 1
                any_sh = True
                if len(counts[c]["unique_vals"]) < 20:
                    counts[c]["unique_vals"].add(v[:60])
                if len(counts[c]["examples"]) < 2:
                    counts[c]["examples"].append((row.get("obs_id",""), v[:80]))
        if any_sh:
            rows_with_any_sh += 1

    print(f"  Rows with ANY SH col non-blank: {rows_with_any_sh} / {total}")
    print()
    print("  Per-col fill rate:")
    for c in SH:
        n = counts[c]["nonblank"]
        pct = (100.0 * n / total) if total else 0.0
        print(f"    {c:<22} {n:>6} ({pct:5.1f}%)  uniq_seen={len(counts[c]['unique_vals'])}")

    print()
    print("  Sample values (first 2 non-blank rows per col):")
    for c in SH:
        if counts[c]["examples"]:
            print(f"    [{c}]")
            for obs_id, ex in counts[c]["examples"]:
                print(f"      {obs_id}: {ex}")

    # Check the SH provenance cols specifically — these tell us about runs
    print()
    print("  Distinct scorer_version_sh:")
    versions = {}
    f.seek(0); reader = csv.DictReader(open(CSV, newline="", encoding="utf-8"))
    for row in reader:
        v = (row.get("scorer_version_sh") or "").strip()
        if v:
            versions[v] = versions.get(v,0) + 1
    for v, n in sorted(versions.items()):
        print(f"    {v}: {n}")

    print()
    print("  Distinct source_pass_sh:")
    passes = {}
    reader = csv.DictReader(open(CSV, newline="", encoding="utf-8"))
    for row in reader:
        v = (row.get("source_pass_sh") or "").strip()
        if v:
            passes[v] = passes.get(v,0) + 1
    for v, n in sorted(passes.items()):
        print(f"    {v}: {n}")

PY

echo
echo "=================================================================="
echo "  Done."
echo "=================================================================="
