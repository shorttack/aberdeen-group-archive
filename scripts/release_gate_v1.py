#!/usr/bin/env python3
"""
release_gate_v1.py — Pre-flight gate for Kastner Aberdeen Archive releases.

Runs a series of automated checks against the master CSVs (and, when present,
the rebuilt wiki) and reports a per-gate PASS/FAIL summary. Operator decides
whether findings are blocking — this is advisory mode, not strict mode.

Designed to be run on the Mac before `git tag` + `git push origin vX.Y.Z` +
`gh release create`. Exit code is non-zero on any FAIL so it can also be wired
into a Makefile or pre-commit hook later, but the operator can override.

USAGE
-----
    python3 scripts/release_gate_v1.py \
        --archive ~/Desktop/Archive/aberdeen-group-archive \
        --wiki ~/Repos/kastner-aberdeen-wiki

OPTIONAL
--------
    --gate N        Run only gate N (default: all)
    --json          Emit machine-readable JSON instead of the pretty table
    --target TAG    Tag this gate report is being run for (e.g., v1.6.2)

GATES (planned full set)
------------------------
    1. Enum validity              — prescience/importance/relevance/license/methodology
    2. Canonical-ID hygiene       — no tech-NNN / ent-NNN / study-* fallback slugs
    3. Master/wiki parity         — every master row has a wiki page (and vice versa)
    4. Script drift               — sandbox/Mac/repo scripts in sync
    5. Shape audit                — row counts match expected
    6. Tag-readiness              — clean tree, synced branch, unique tag

This v1 implements GATE 1 only. Subsequent gates land in v1.1, v1.2, ... as
each is built, validated against a known-failure dataset, then promoted from
the SKIP state to active.

NOTATION
--------
Findings are tagged:
    INTRODUCED  — this release's diff caused the issue (block-worthy)
    LEGACY      — pre-existed; surfaced by gate but not caused by this release
    UNKNOWN     — gate can't determine origin (treat as INTRODUCED by default)

The operator override model means even an "INTRODUCED FAIL" can be shipped if
the operator explicitly accepts it — the gate's job is to surface, not enforce.

Author: Perplexity Computer + Pete Kastner, 2026-06-13.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

# ─────────────────────────────────────────────────────────────────────────────
# COLOR / FORMATTING HELPERS
# ─────────────────────────────────────────────────────────────────────────────

class C:
    GREEN  = "\033[32m"
    RED    = "\033[31m"
    YELLOW = "\033[33m"
    GRAY   = "\033[90m"
    BOLD   = "\033[1m"
    RESET  = "\033[0m"

def green(s):  return f"{C.GREEN}{s}{C.RESET}"
def red(s):    return f"{C.RED}{s}{C.RESET}"
def yellow(s): return f"{C.YELLOW}{s}{C.RESET}"
def gray(s):   return f"{C.GRAY}{s}{C.RESET}"
def bold(s):   return f"{C.BOLD}{s}{C.RESET}"

# ─────────────────────────────────────────────────────────────────────────────
# DATA MODEL
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class Finding:
    """A single issue discovered by a gate."""
    gate_id: int
    rule_id: str          # short stable identifier, e.g. "prescience-enum"
    severity: str          # "FAIL" or "WARN"
    origin: str            # "INTRODUCED" | "LEGACY" | "UNKNOWN"
    where: str             # file path or table name
    row_key: str           # e.g. study_id, tech_id, or "" for table-level
    detail: str            # human-readable

    def as_dict(self):
        return {
            "gate_id":  self.gate_id,
            "rule_id":  self.rule_id,
            "severity": self.severity,
            "origin":   self.origin,
            "where":    self.where,
            "row_key":  self.row_key,
            "detail":   self.detail,
        }

@dataclass
class GateResult:
    gate_id: int
    name: str
    status: str = "PASS"   # "PASS" | "FAIL" | "SKIP" | "WARN"
    findings: list[Finding] = field(default_factory=list)
    note: str = ""

    @property
    def color_status(self):
        if self.status == "PASS": return green("🟢 PASS")
        if self.status == "FAIL": return red("🔴 FAIL")
        if self.status == "WARN": return yellow("🟡 WARN")
        return gray("⚪ SKIP")

# ─────────────────────────────────────────────────────────────────────────────
# CONFIG: ENUM VOCABULARIES
# ─────────────────────────────────────────────────────────────────────────────
#
# These are the §13.1 v20 schema-canonical values. Anything outside these sets
# is flagged. Update here when the schema vocabulary expands (e.g., adding a
# new license type means amending LICENSE_ENUM).
#
# The methodology vocabulary is open-ended by design (operators add new ones
# as new study types emerge), so we use a "warn on unknown" model: if the gate
# sees a methodology token it doesn't recognize, it warns and asks the operator
# to confirm. Add accepted tokens to METHODOLOGY_KNOWN as they're validated.

PRESCIENCE_ENUM = {"low", "medium", "high"}
IMPORTANCE_ENUM = {"low", "medium", "high"}
RELEVANCE_ENUM  = {"low", "medium", "high"}

LICENSE_ENUM = {
    "CC-BY-4.0",
    "CC-BY-SA-4.0",
    "CC-BY-NC-4.0",
    "CC-BY-NC-SA-4.0",
    "CC0-1.0",
}

# Methodology vocabulary as known so far. Anything outside this set triggers a
# WARN (not a FAIL) so new methodologies can be introduced without breaking the
# gate, but the operator is forced to acknowledge them.
METHODOLOGY_KNOWN = {
    # field-method extraction styles
    "expert-quote", "expert-interview", "oral-history", "panel-discussion",
    "ai-generated-summary", "literature-review",
    # archive types
    "internal-sales-training-archive", "vendor-event-archive", "broadcast-archive",
    "memoir-archive", "industry-research", "competitor-analysis",
    # technical methodologies
    "benchmark-analysis", "survey-research", "case-study", "market-sizing",
    "prescience-scoring",
}

# ─────────────────────────────────────────────────────────────────────────────
# GATE 1 — ENUM VALIDITY
# ─────────────────────────────────────────────────────────────────────────────

def gate_1_enum_validity(archive_dir: Path, target_tag: str | None) -> GateResult:
    """
    Validates that every enum column in _master_studies.csv contains only values
    from its canonical vocabulary.

    Columns checked:
        importance      strict      {low|medium|high}
        relevance       strict      {low|medium|high}
        prescience      strict      {low|medium|high}
        license         strict      LICENSE_ENUM set
        methodology     warn        METHODOLOGY_KNOWN (semicolon- or comma-sep)

    Origin classification:
        INTRODUCED — row's study_id matches a pattern we recognize as new in
                     this cycle (best-effort; falls back to UNKNOWN).
        LEGACY     — row existed prior to this release cycle.

    For v1, we don't have a reliable "added in this release" marker baked into
    the CSV (no created_at column), so origin defaults to UNKNOWN. v1.1 will
    add a sidecar "release marker" file the apply scripts write.
    """
    result = GateResult(gate_id=1, name="Enum validity")
    studies_path = archive_dir / "_master_studies.csv"

    if not studies_path.exists():
        result.status = "FAIL"
        result.note = f"_master_studies.csv not found at {studies_path}"
        return result

    with open(studies_path, newline="") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        result.status = "FAIL"
        result.note = f"_master_studies.csv is empty"
        return result

    # Verify required columns exist
    required = {"study_id", "importance", "relevance", "prescience", "license", "methodology"}
    missing = required - set(rows[0].keys())
    if missing:
        result.status = "FAIL"
        result.note = f"missing required columns: {sorted(missing)}"
        return result

    # ── 1a. Strict enums ────────────────────────────────────────────────────
    enum_checks = [
        ("importance", IMPORTANCE_ENUM, "imp-enum"),
        ("relevance",  RELEVANCE_ENUM,  "rel-enum"),
        ("prescience", PRESCIENCE_ENUM, "pres-enum"),
        ("license",    LICENSE_ENUM,    "lic-enum"),
    ]
    for col, allowed, rule_id in enum_checks:
        for row in rows:
            val = (row.get(col) or "").strip()
            if not val:
                result.findings.append(Finding(
                    gate_id=1, rule_id=rule_id, severity="FAIL", origin="UNKNOWN",
                    where=str(studies_path.name), row_key=row["study_id"],
                    detail=f"{col} is empty",
                ))
            elif val not in allowed:
                result.findings.append(Finding(
                    gate_id=1, rule_id=rule_id, severity="FAIL", origin="UNKNOWN",
                    where=str(studies_path.name), row_key=row["study_id"],
                    detail=f"{col}={val!r} not in enum {sorted(allowed)}",
                ))

    # ── 1b. Methodology warn-on-unknown ─────────────────────────────────────
    # Methodology is multi-valued, separated by either ';' or ','. Split on both.
    import re
    for row in rows:
        raw = (row.get("methodology") or "").strip()
        if not raw:
            result.findings.append(Finding(
                gate_id=1, rule_id="meth-empty", severity="FAIL", origin="UNKNOWN",
                where=str(studies_path.name), row_key=row["study_id"],
                detail="methodology is empty",
            ))
            continue
        tokens = [t.strip() for t in re.split(r"[;,]", raw) if t.strip()]
        for tok in tokens:
            if tok not in METHODOLOGY_KNOWN:
                result.findings.append(Finding(
                    gate_id=1, rule_id="meth-unknown", severity="WARN", origin="UNKNOWN",
                    where=str(studies_path.name), row_key=row["study_id"],
                    detail=f"methodology token {tok!r} not in known vocabulary; "
                           f"add to METHODOLOGY_KNOWN if accepted",
                ))

    # ── Aggregate status ────────────────────────────────────────────────────
    has_fail = any(f.severity == "FAIL" for f in result.findings)
    has_warn = any(f.severity == "WARN" for f in result.findings)
    if has_fail:
        result.status = "FAIL"
    elif has_warn:
        result.status = "WARN"
    else:
        result.status = "PASS"
    result.note = f"{len(rows)} studies checked"
    return result

# ─────────────────────────────────────────────────────────────────────────────
# GATE 2-6 — PLACEHOLDERS
# ─────────────────────────────────────────────────────────────────────────────

def gate_2_skip(*a, **kw) -> GateResult:
    r = GateResult(gate_id=2, name="Canonical-ID hygiene", status="SKIP")
    r.note = "not yet implemented (planned for v1.1)"
    return r

def gate_3_skip(*a, **kw) -> GateResult:
    r = GateResult(gate_id=3, name="Master/wiki parity", status="SKIP")
    r.note = "not yet implemented (planned for v1.2)"
    return r

def gate_4_skip(*a, **kw) -> GateResult:
    r = GateResult(gate_id=4, name="Script drift", status="SKIP")
    r.note = "not yet implemented (planned for v1.3)"
    return r

def gate_5_skip(*a, **kw) -> GateResult:
    r = GateResult(gate_id=5, name="Shape audit", status="SKIP")
    r.note = "not yet implemented (planned for v1.4)"
    return r

def gate_6_skip(*a, **kw) -> GateResult:
    r = GateResult(gate_id=6, name="Tag-readiness", status="SKIP")
    r.note = "not yet implemented (planned for v1.5)"
    return r

GATE_REGISTRY: list[tuple[int, str, Callable]] = [
    (1, "Enum validity",          gate_1_enum_validity),
    (2, "Canonical-ID hygiene",   gate_2_skip),
    (3, "Master/wiki parity",     gate_3_skip),
    (4, "Script drift",           gate_4_skip),
    (5, "Shape audit",            gate_5_skip),
    (6, "Tag-readiness",          gate_6_skip),
]

# ─────────────────────────────────────────────────────────────────────────────
# RUNNER
# ─────────────────────────────────────────────────────────────────────────────

def print_report(results: list[GateResult], target_tag: str | None) -> None:
    print()
    print("═" * 60)
    print(f"  {bold('KASTNER ARCHIVE RELEASE GATE v1')}")
    if target_tag:
        print(f"  target: {bold(target_tag)}")
    print("═" * 60)
    print()

    for r in results:
        n_fail = sum(1 for f in r.findings if f.severity == "FAIL")
        n_warn = sum(1 for f in r.findings if f.severity == "WARN")
        meta = []
        if n_fail: meta.append(red(f"{n_fail} FAIL"))
        if n_warn: meta.append(yellow(f"{n_warn} WARN"))
        if r.note: meta.append(gray(r.note))
        meta_str = "  " + " · ".join(meta) if meta else ""
        print(f"  GATE {r.gate_id} — {r.name:<28} {r.color_status}{meta_str}")

    print()

    # Detail block for any gate with findings
    any_findings = False
    for r in results:
        if not r.findings:
            continue
        any_findings = True
        print("─" * 60)
        print(f"  GATE {r.gate_id} findings ({len(r.findings)})")
        print("─" * 60)
        # Group by rule_id for readability
        from collections import defaultdict
        by_rule = defaultdict(list)
        for f in r.findings:
            by_rule[f.rule_id].append(f)
        for rule_id, items in sorted(by_rule.items()):
            sev = items[0].severity
            tag = red(f"[{sev}]") if sev == "FAIL" else yellow(f"[{sev}]")
            print(f"\n  {tag} rule={rule_id}  ({len(items)} item(s))")
            for f in items[:10]:  # cap to 10 per rule to keep output sane
                origin_color = gray(f"({f.origin})")
                print(f"      · {f.row_key:<60} {f.detail}  {origin_color}")
            if len(items) > 10:
                print(f"      · ... and {len(items) - 10} more")
        print()

    # Summary verdict
    print("═" * 60)
    n_fail_total = sum(1 for r in results for f in r.findings if f.severity == "FAIL")
    n_warn_total = sum(1 for r in results for f in r.findings if f.severity == "WARN")
    n_skip = sum(1 for r in results if r.status == "SKIP")
    any_fail = any(r.status == "FAIL" for r in results)
    if not any_fail and n_warn_total == 0:
        if n_skip == len(results):
            print(f"  {yellow('⚠️  All gates SKIPPED — gate not yet implemented')}")
        else:
            print(f"  {green('✅ READY TO TAG')} — all active gates GREEN.")
    else:
        bits = []
        if n_fail_total: bits.append(red(f"{n_fail_total} FAIL"))
        if n_warn_total: bits.append(yellow(f"{n_warn_total} WARN"))
        print(f"  {red('❌ NOT READY')} — {' · '.join(bits)}.")
        print(f"  Operator may override if findings are intentional or out-of-scope.")
    if n_skip:
        print(f"  {gray(f'  ({n_skip} gate(s) skipped — not yet implemented)')}")
    print("═" * 60)
    print()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--archive", required=True, type=Path,
                    help="path to archive_masters directory (contains _master_*.csv)")
    ap.add_argument("--wiki", type=Path, default=None,
                    help="path to kastner-aberdeen-wiki repo (for gates 3+)")
    ap.add_argument("--gate", type=int, default=None,
                    help="run only gate N")
    ap.add_argument("--json", action="store_true",
                    help="emit JSON instead of pretty table")
    ap.add_argument("--target", default=None,
                    help="target tag for this gate report, e.g. v1.6.2")
    ap.add_argument("--dry-run-audit", type=Path, default=None, metavar="DIR",
                    help="read-only audit mode; write timestamped JSON report to DIR")
    ap.add_argument("--expected", type=Path, default=None, metavar="FILE",
                    help="JSON file of known-expected findings to classify in report")
    args = ap.parse_args()

    if not args.archive.is_dir():
        print(red(f"ERROR: archive dir not found: {args.archive}"), file=sys.stderr)
        sys.exit(2)

    results = []
    for gate_id, name, fn in GATE_REGISTRY:
        if args.gate is not None and gate_id != args.gate:
            continue
        try:
            r = fn(args.archive, args.target) if gate_id == 1 else fn()
        except Exception as e:
            r = GateResult(gate_id=gate_id, name=name, status="FAIL",
                           note=f"gate raised exception: {e!r}")
        results.append(r)

    # ── DRY-RUN AUDIT MODE ──────────────────────────────────────────────────
    # Read-only discovery: write timestamped JSON report, classify findings as
    # EXPECTED vs UNKNOWN, never block. Exit code is always 0 in this mode.
    if args.dry_run_audit is not None:
        from datetime import datetime, timezone
        audit_dir = args.dry_run_audit
        audit_dir.mkdir(parents=True, exist_ok=True)

        expected_set = set()
        if args.expected and args.expected.exists():
            try:
                exp_data = json.loads(args.expected.read_text())
                for e in exp_data:
                    expected_set.add((e["gate_id"], e["rule_id"], e["row_key"]))
            except Exception as e:
                print(red(f"WARNING: could not parse --expected: {e!r}"), file=sys.stderr)

        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        audit_record = {
            "audit_id": f"release_gate_audit_{ts}",
            "timestamp_utc": ts,
            "target_tag": args.target,
            "archive_dir": str(args.archive),
            "wiki_dir": str(args.wiki) if args.wiki else None,
            "gates_run": [r.gate_id for r in results],
            "summary": {
                "total_findings": sum(len(r.findings) for r in results),
                "by_severity": {
                    "FAIL": sum(1 for r in results for f in r.findings if f.severity == "FAIL"),
                    "WARN": sum(1 for r in results for f in r.findings if f.severity == "WARN"),
                },
                "by_classification": {"EXPECTED": 0, "UNKNOWN": 0},
                "by_gate": {r.gate_id: {"name": r.name, "status": r.status, "n_findings": len(r.findings)} for r in results},
            },
            "findings": [],
        }

        for r in results:
            for f in r.findings:
                key = (f.gate_id, f.rule_id, f.row_key)
                classification = "EXPECTED" if key in expected_set else "UNKNOWN"
                audit_record["summary"]["by_classification"][classification] += 1
                rec = f.as_dict()
                rec["classification"] = classification
                audit_record["findings"].append(rec)

        out_path = audit_dir / f"release_gate_audit_{ts}.json"
        out_path.write_text(json.dumps(audit_record, indent=2))

        s = audit_record["summary"]
        print()
        print("═" * 60)
        print(f"  {bold('DRY-RUN AUDIT REPORT')}")
        print(f"  written to: {out_path}")
        print("═" * 60)
        print()
        for r in results:
            n_expected = sum(1 for f in r.findings
                             if (f.gate_id, f.rule_id, f.row_key) in expected_set)
            n_unknown = len(r.findings) - n_expected
            extras = []
            if n_expected: extras.append(gray(f"{n_expected} EXPECTED"))
            if n_unknown:  extras.append(red(f"{n_unknown} UNKNOWN"))
            extras_str = "  " + " · ".join(extras) if extras else ""
            print(f"  GATE {r.gate_id} — {r.name:<28} {r.color_status}{extras_str}")
        print()
        print("  Totals:")
        print(f"    FAIL severity:        {s['by_severity']['FAIL']}")
        print(f"    WARN severity:        {s['by_severity']['WARN']}")
        print(f"    Classified EXPECTED:  {s['by_classification']['EXPECTED']}")
        latent_msg = red('← LATENT DEBT') if s['by_classification']['UNKNOWN'] else green('← no latent debt')
        print(f"    Classified UNKNOWN:   {s['by_classification']['UNKNOWN']}  {latent_msg}")
        print()
        print("═" * 60)
        sys.exit(0)

    # ── NORMAL MODE ─────────────────────────────────────────────────────────────
    if args.json:
        out = [
            {
                "gate_id": r.gate_id,
                "name": r.name,
                "status": r.status,
                "note": r.note,
                "findings": [f.as_dict() for f in r.findings],
            }
            for r in results
        ]
        print(json.dumps(out, indent=2))
    else:
        print_report(results, args.target)

    # Exit code: 0 if all PASS or SKIP, 1 if any FAIL, 2 if any unexpected error
    if any(r.status == "FAIL" for r in results):
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
