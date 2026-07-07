#!/usr/bin/env python3
"""
07_audit_masters_v1.py — Phase 0 regression harness for the Kastner master CSVs.

Runs at the end of Phase 2 (or manually) to catch three regression classes that
have historically shipped silently:

  1. Alias-collision ratio — distinct_norm_names / total_rows for v_entities and
     v_technologies. Baseline captured 2026-07-07 (pre-cleanse worst case). The
     ratio must NOT drop by more than the alert threshold vs baseline.

  2. ID-vs-name congruence (tech only) — tech_id whose normalized slug bears no
     resemblance to normalized tech_name. Baseline grandfathers the 1,577
     current violators (Pass-B TECH-XXX-NNN codes and study-scoped tNN-NN). The
     harness alerts only on NEW violators past the grandfather set.

  3. Successor-bleed detector — entity rows whose `successor` string contains
     both "Compaq" AND "HP" but whose entity_name is not itself DEC/Compaq/
     Tandem/HP/Hewlett/EDS/3Com/Palm/Cray. Baseline grandfathers the 4 current
     bleeders (Phase B fixes them). Alerts only on NEW ones.

Reads baseline from Perplexity_Only/audit_masters_baseline.json.
Uses read-only DuckDB connection to ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb.

Exit codes:
  0 — pass (no alerts, no failures)
  1 — alert (at least one probe reports NEW violations under fail threshold)
  2 — fail (hard failure — collision ratio dropped past fail threshold, or new
       violations past fail threshold)

Usage:
  python3 07_audit_masters_v1.py                       # standard run
  python3 07_audit_masters_v1.py --db PATH             # override DuckDB path
  python3 07_audit_masters_v1.py --baseline PATH       # override baseline JSON
  python3 07_audit_masters_v1.py --write-report PATH   # emit report Markdown
  python3 07_audit_masters_v1.py --update-baseline     # OVERWRITE baseline
                                                        # (only use after a
                                                        # legitimate cleanse
                                                        # to reset the floor)
"""
import argparse
import datetime as _dt
import json
import re
import sys
from pathlib import Path

DEFAULT_DB = Path.home() / "Repos/kastner-aberdeen-wiki/db/kastner.duckdb"
DEFAULT_BASELINE = Path.home() / "Desktop/Archive/Perplexity_Only/audit_masters_baseline.json"


def _norm(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9]", "", (s or "").lower())


def _open_ro(db_path: Path):
    try:
        import duckdb  # type: ignore
    except ImportError:
        print("ERROR: duckdb Python package not installed. `pip install duckdb`", file=sys.stderr)
        sys.exit(3)
    return duckdb.connect(str(db_path), read_only=True)


def probe_1_collision_ratio(conn, baseline: dict) -> dict:
    """Probe 1: alias-collision ratio floor."""
    ent = conn.execute("""
        SELECT COUNT(*) AS total,
               COUNT(DISTINCT lower(regexp_replace(entity_name, '[^A-Za-z0-9]', '', 'g'))) AS distinct_norm
        FROM v_entities
    """).fetchone()
    tech = conn.execute("""
        SELECT COUNT(*) AS total,
               COUNT(DISTINCT lower(regexp_replace(tech_name, '[^A-Za-z0-9]', '', 'g'))) AS distinct_norm
        FROM v_technologies
    """).fetchone()
    ent_ratio = ent[1] / ent[0] if ent[0] else 1.0
    tech_ratio = tech[1] / tech[0] if tech[0] else 1.0

    base = baseline["collision_ratio"]
    gates = baseline["phase_0_gates"]
    alert_drop = gates["collision_ratio_drop_alert_pp"]
    fail_drop = gates["collision_ratio_drop_fail_pp"]

    ent_delta = ent_ratio - base["entities_ratio"]
    tech_delta = tech_ratio - base["technologies_ratio"]

    result = {
        "entities": {"total": ent[0], "distinct_norm": ent[1], "ratio": round(ent_ratio, 4),
                     "baseline_ratio": base["entities_ratio"], "delta": round(ent_delta, 4)},
        "technologies": {"total": tech[0], "distinct_norm": tech[1], "ratio": round(tech_ratio, 4),
                         "baseline_ratio": base["technologies_ratio"], "delta": round(tech_delta, 4)},
        "alerts": [],
        "failures": [],
    }
    if ent_delta < -fail_drop:
        result["failures"].append(f"entities collision ratio dropped {-ent_delta:.4f} > fail threshold {fail_drop}")
    elif ent_delta < -alert_drop:
        result["alerts"].append(f"entities collision ratio dropped {-ent_delta:.4f} > alert threshold {alert_drop}")
    if tech_delta < -fail_drop:
        result["failures"].append(f"technologies collision ratio dropped {-tech_delta:.4f} > fail threshold {fail_drop}")
    elif tech_delta < -alert_drop:
        result["alerts"].append(f"technologies collision ratio dropped {-tech_delta:.4f} > alert threshold {alert_drop}")
    return result


def probe_2_tech_congruence(conn, baseline: dict) -> dict:
    """Probe 2: tech_id vs tech_name substring congruence."""
    rows = conn.execute("""
        SELECT tech_id FROM v_technologies
        WHERE lower(regexp_replace(tech_name, '[^A-Za-z0-9]', '', 'g'))
          NOT LIKE ('%' || lower(regexp_replace(tech_id, '[^A-Za-z0-9]', '', 'g')) || '%')
          AND lower(regexp_replace(tech_id, '[^A-Za-z0-9]', '', 'g'))
          NOT LIKE ('%' || lower(regexp_replace(tech_name, '[^A-Za-z0-9]', '', 'g')) || '%')
        ORDER BY tech_id
    """).fetchall()
    current_ids = {r[0] for r in rows}

    grandfathered = set(baseline.get("tech_congruence_grandfathered_list", []))
    new_violators = sorted(current_ids - grandfathered)
    cleared = sorted(grandfathered - current_ids)  # informational — Phase A wins

    gates = baseline["phase_0_gates"]
    alert_n = gates["new_tech_congruence_violation_alert"]
    fail_n = gates["new_tech_congruence_violation_fail"]

    result = {
        "current_count": len(current_ids),
        "grandfathered_count": len(grandfathered),
        "new_violators": new_violators,
        "cleared_from_grandfather": cleared,
        "alerts": [],
        "failures": [],
    }
    if len(new_violators) >= fail_n:
        result["failures"].append(f"{len(new_violators)} NEW tech-congruence violators >= fail threshold {fail_n}")
    elif len(new_violators) >= alert_n:
        result["alerts"].append(f"{len(new_violators)} NEW tech-congruence violators >= alert threshold {alert_n}")
    return result


def probe_3_successor_bleed(conn, baseline: dict) -> dict:
    """Probe 3: DEC/Compaq/HP fanout bleed onto unrelated entities."""
    rows = conn.execute("""
        SELECT entity_id, entity_name, successor FROM v_entities
        WHERE successor ILIKE '%Compaq%' AND successor ILIKE '%HP%'
          AND entity_name NOT ILIKE '%DEC%' AND entity_name NOT ILIKE '%Digital Equipment%'
          AND entity_name NOT ILIKE '%Compaq%' AND entity_name NOT ILIKE '%Tandem%'
          AND entity_name NOT ILIKE '%HP %' AND entity_name NOT ILIKE '%Hewlett%'
          AND entity_name NOT ILIKE '%EDS%' AND entity_name NOT ILIKE '%3Com%'
          AND entity_name NOT ILIKE '%Palm%' AND entity_name NOT ILIKE '%Cray%'
          AND entity_name NOT ILIKE '%Alpha%' AND entity_name NOT ILIKE '%Digital%'
          AND entity_name NOT ILIKE 'HP'
        ORDER BY entity_id
    """).fetchall()
    current_bleeders = {r[0] for r in rows}
    current_detail = {r[0]: {"entity_name": r[1], "successor": r[2]} for r in rows}

    grandfathered = set(baseline.get("entity_successor_bleed_grandfathered", []))
    new_bleeders = sorted(current_bleeders - grandfathered)
    cleared = sorted(grandfathered - current_bleeders)

    gates = baseline["phase_0_gates"]
    alert_n = gates["new_successor_bleed_alert"]
    fail_n = gates["new_successor_bleed_fail"]

    result = {
        "current_count": len(current_bleeders),
        "grandfathered_count": len(grandfathered),
        "new_bleeders": [{"entity_id": eid, **current_detail[eid]} for eid in new_bleeders],
        "cleared_from_grandfather": cleared,
        "alerts": [],
        "failures": [],
    }
    if len(new_bleeders) >= fail_n:
        result["failures"].append(f"{len(new_bleeders)} NEW successor-bleeders >= fail threshold {fail_n}")
    elif len(new_bleeders) >= alert_n:
        result["alerts"].append(f"{len(new_bleeders)} NEW successor-bleeders >= alert threshold {alert_n}")
    return result


def build_report(probe1: dict, probe2: dict, probe3: dict) -> str:
    lines = ["# Phase 0 audit report", ""]
    lines.append(f"Generated: {_dt.datetime.now(_dt.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')}")
    lines.append("")

    lines.append("## Probe 1 — Alias-collision ratio")
    e = probe1["entities"]
    t = probe1["technologies"]
    lines.append(f"- **Entities**: {e['distinct_norm']}/{e['total']} = {e['ratio']:.4f} (baseline {e['baseline_ratio']:.4f}, delta {e['delta']:+.4f})")
    lines.append(f"- **Technologies**: {t['distinct_norm']}/{t['total']} = {t['ratio']:.4f} (baseline {t['baseline_ratio']:.4f}, delta {t['delta']:+.4f})")
    for a in probe1["alerts"]: lines.append(f"- ⚠️  ALERT: {a}")
    for f in probe1["failures"]: lines.append(f"- 🔴 FAIL: {f}")
    lines.append("")

    lines.append("## Probe 2 — Tech ID-vs-name congruence")
    lines.append(f"- Current violators: {probe2['current_count']} (grandfathered: {probe2['grandfathered_count']})")
    lines.append(f"- NEW violators: {len(probe2['new_violators'])}")
    if probe2["new_violators"]:
        for v in probe2["new_violators"][:20]:
            lines.append(f"  - `{v}`")
        if len(probe2["new_violators"]) > 20:
            lines.append(f"  - … and {len(probe2['new_violators']) - 20} more")
    if probe2["cleared_from_grandfather"]:
        lines.append(f"- ✅ Cleared from grandfather set: {len(probe2['cleared_from_grandfather'])} (e.g., {', '.join(probe2['cleared_from_grandfather'][:5])})")
    for a in probe2["alerts"]: lines.append(f"- ⚠️  ALERT: {a}")
    for f in probe2["failures"]: lines.append(f"- 🔴 FAIL: {f}")
    lines.append("")

    lines.append("## Probe 3 — Successor-bleed (DEC/Compaq/HP fanout)")
    lines.append(f"- Current bleeders: {probe3['current_count']} (grandfathered: {probe3['grandfathered_count']})")
    lines.append(f"- NEW bleeders: {len(probe3['new_bleeders'])}")
    for b in probe3["new_bleeders"]:
        lines.append(f"  - `{b['entity_id']}` ({b['entity_name']}) — successor: {b['successor']!r}")
    if probe3["cleared_from_grandfather"]:
        lines.append(f"- ✅ Cleared from grandfather set: {probe3['cleared_from_grandfather']}")
    for a in probe3["alerts"]: lines.append(f"- ⚠️  ALERT: {a}")
    for f in probe3["failures"]: lines.append(f"- 🔴 FAIL: {f}")
    lines.append("")

    return "\n".join(lines)


def main(argv: list) -> int:
    p = argparse.ArgumentParser(description="Phase 0 — Kastner masters audit harness")
    p.add_argument("--db", default=str(DEFAULT_DB))
    p.add_argument("--baseline", default=str(DEFAULT_BASELINE))
    p.add_argument("--write-report", default=None, help="Write Markdown report to this path")
    p.add_argument("--update-baseline", action="store_true",
                   help="OVERWRITE the baseline with current state. Only use after a legitimate cleanse.")
    args = p.parse_args(argv[1:])

    db = Path(args.db).expanduser()
    baseline_path = Path(args.baseline).expanduser()

    if not db.exists():
        print(f"ERROR: DuckDB not found at {db}", file=sys.stderr)
        return 3
    if not baseline_path.exists():
        print(f"ERROR: Baseline not found at {baseline_path}. Run generate_baseline_v1.py first.", file=sys.stderr)
        return 3

    baseline = json.loads(baseline_path.read_text())
    conn = _open_ro(db)
    try:
        probe1 = probe_1_collision_ratio(conn, baseline)
        probe2 = probe_2_tech_congruence(conn, baseline)
        probe3 = probe_3_successor_bleed(conn, baseline)
    finally:
        conn.close()

    report = build_report(probe1, probe2, probe3)
    print(report)

    if args.write_report:
        Path(args.write_report).write_text(report)
        print(f"\nReport written: {args.write_report}")

    all_alerts = probe1["alerts"] + probe2["alerts"] + probe3["alerts"]
    all_failures = probe1["failures"] + probe2["failures"] + probe3["failures"]

    if args.update_baseline:
        # Overwrite baseline shape + collision + grandfather lists with current state
        conn2 = _open_ro(db)
        try:
            shape = conn2.execute("""
              SELECT (SELECT COUNT(*) FROM v_studies), (SELECT COUNT(*) FROM v_observations),
                     (SELECT COUNT(*) FROM v_entities), (SELECT COUNT(*) FROM v_technologies),
                     (SELECT COUNT(*) FROM v_studies_with_high_prescience)
            """).fetchone()
            tech_ids = conn2.execute("""
              SELECT tech_id FROM v_technologies
              WHERE lower(regexp_replace(tech_name, '[^A-Za-z0-9]', '', 'g'))
                NOT LIKE ('%' || lower(regexp_replace(tech_id, '[^A-Za-z0-9]', '', 'g')) || '%')
                AND lower(regexp_replace(tech_id, '[^A-Za-z0-9]', '', 'g'))
                NOT LIKE ('%' || lower(regexp_replace(tech_name, '[^A-Za-z0-9]', '', 'g')) || '%')
              ORDER BY tech_id
            """).fetchall()
            ent_bleeders = conn2.execute("""
              SELECT entity_id FROM v_entities
              WHERE successor ILIKE '%Compaq%' AND successor ILIKE '%HP%'
                AND entity_name NOT ILIKE '%DEC%' AND entity_name NOT ILIKE '%Digital Equipment%'
                AND entity_name NOT ILIKE '%Compaq%' AND entity_name NOT ILIKE '%Tandem%'
                AND entity_name NOT ILIKE '%HP %' AND entity_name NOT ILIKE '%Hewlett%'
                AND entity_name NOT ILIKE '%EDS%' AND entity_name NOT ILIKE '%3Com%'
                AND entity_name NOT ILIKE '%Palm%' AND entity_name NOT ILIKE '%Cray%'
                AND entity_name NOT ILIKE '%Alpha%' AND entity_name NOT ILIKE '%Digital%'
                AND entity_name NOT ILIKE 'HP'
              ORDER BY entity_id
            """).fetchall()
        finally:
            conn2.close()
        baseline["shape"] = {"studies": shape[0], "observations": shape[1], "entities": shape[2],
                             "technologies": shape[3], "high_prescience": shape[4]}
        baseline["collision_ratio"]["entities_total"] = probe1["entities"]["total"]
        baseline["collision_ratio"]["entities_distinct_norm"] = probe1["entities"]["distinct_norm"]
        baseline["collision_ratio"]["entities_ratio"] = probe1["entities"]["ratio"]
        baseline["collision_ratio"]["technologies_total"] = probe1["technologies"]["total"]
        baseline["collision_ratio"]["technologies_distinct_norm"] = probe1["technologies"]["distinct_norm"]
        baseline["collision_ratio"]["technologies_ratio"] = probe1["technologies"]["ratio"]
        baseline["tech_congruence_grandfathered_list"] = [r[0] for r in tech_ids]
        baseline["tech_congruence_grandfathered_count"] = len(tech_ids)
        baseline["entity_successor_bleed_grandfathered"] = [r[0] for r in ent_bleeders]
        baseline["captured_at_utc"] = _dt.datetime.now(_dt.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
        baseline["source"] = f"live DuckDB at {db} (post-update-baseline)"
        baseline_path.write_text(json.dumps(baseline, indent=2, sort_keys=True))
        print(f"\n✅ Baseline UPDATED at {baseline_path}")

    if all_failures:
        print(f"\n🔴 FAIL: {len(all_failures)} failure(s), {len(all_alerts)} alert(s)")
        return 2
    if all_alerts:
        print(f"\n⚠️  ALERT: {len(all_alerts)} alert(s), 0 failures")
        return 1
    print(f"\n✅ PASS: no alerts or failures")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
