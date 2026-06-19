"""
backfill_blank_horizon_3y_v2.py — fill `3` into blank forecast_horizon_years
for Pipeline-1-eligible rows of kastner_quotes_clean.csv.

Context (2026-06-19):
  After route_quotations_to_horizon_v2.py, 244 of 474 P1-eligible rows have
  blank forecast_horizon_years and route_v2 silently drops them as "empty
  horizon". Pete authorized a default backfill of 3 years (parses to SH-3y)
  to unblock the v1.8.0 calibration scorer pilot.

Eligibility (mirrors route_v2.py exactly):
  reject column blank AND (
    normalize_text(headline) is in corpus.articles[*] (recomputed)
    OR row_id is in _format_mismatch_admits_v1.json
  )

Backfill rule:
  IF eligible AND forecast_horizon_years.strip() == "":
    write "3" into forecast_horizon_years

Outputs (--commit only):
  1. kastner_quotes_clean.csv (updated in place, csv.QUOTE_ALL)
  2. kastner_quotes_clean.csv.bak_horizon_backfill_3y_<utc>  (full backup)
  3. _horizon_backfill_3y_v1_applied.txt   (audit sidecar)
     - timestamp UTC
     - 244 row_ids, headline, prior raw value, new value, eligibility reason
"""

from __future__ import annotations
import csv, json, re, shutil, sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ARCHIVE     = Path.home() / "Desktop/Archive/aberdeen-group-archive"
QUOTATIONS  = ARCHIVE / "kastner-author/quotations"
CSV_PATH    = QUOTATIONS / "kastner_quotes_clean.csv"
CORPUS_JSON = QUOTATIONS / "article_corpus_v1.json"
ADMITS_JSON = QUOTATIONS / "_format_mismatch_admits_v1.json"
AUDIT_TXT   = QUOTATIONS / "_horizon_backfill_3y_v1_applied.txt"

DEFAULT_HORIZON = "3"
BACKFILL_TAG    = "backfill_default_3y_v1"

def normalize_text(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()

def main() -> int:
    commit = "--commit" in sys.argv
    print(f"=== backfill_blank_horizon_3y_v1 — mode={'COMMIT' if commit else 'DRY-RUN'} ===\n")

    for p in (CSV_PATH, CORPUS_JSON):
        if not p.exists():
            print(f"FATAL: missing input {p}", file=sys.stderr); return 1

    # Build corpus headline_norm set (recomputed, matches route_v2)
    corpus = json.loads(CORPUS_JSON.read_text())
    corpus_norms = set()
    for a in corpus.get("articles", []):
        nh = normalize_text(a.get("headline", ""))
        if nh: corpus_norms.add(nh)
    print(f"corpus: {len(corpus_norms)} distinct recomputed headline_norms")

    # Admits
    admits: set[int] = set()
    if ADMITS_JSON.exists():
        admits = {int(r) for r in json.loads(ADMITS_JSON.read_text()).get("admit_row_ids", [])}
    print(f"admits: {len(admits)} row_ids")

    # Read master
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    print(f"master: {len(rows)} rows, {len(fieldnames)} cols")

    required = ["row_id", "headline", "forecast_horizon_years"]
    missing = [c for c in required if c not in fieldnames]
    if missing:
        print(f"FATAL: master missing required cols: {missing}", file=sys.stderr); return 1

    # Walk rows: identify P1-eligible + blank-horizon
    targets: list[tuple[int, str, str, str]] = []  # (rid, headline, prior_raw, eligibility_reason)
    p1_count = 0
    p1_blank = 0
    p1_nonblank = 0
    eligibility_reasons: Counter = Counter()

    for r in rows:
        rid_s = r.get("row_id", "").strip()
        if not rid_s.isdigit():
            continue
        rid = int(rid_s)
        nh = normalize_text(r.get("headline", ""))
        in_corpus = bool(nh) and nh in corpus_norms
        is_admit = rid in admits
        if not (in_corpus or is_admit):
            continue
        # Note: route_v2 partitions purely on (admit OR in_corpus); no `reject`
        # column exists in this master. Pete's blank=admit rule applies to the
        # format-mismatch review CSV, not kastner_quotes_clean.csv.
        p1_count += 1
        raw = r.get("forecast_horizon_years", "")
        if (raw or "").strip() != "":
            p1_nonblank += 1
            continue
        p1_blank += 1
        if in_corpus and is_admit: reason = "in_corpus+admit"
        elif in_corpus:            reason = "in_corpus"
        else:                      reason = "admit_only"
        eligibility_reasons[reason] += 1
        targets.append((rid, r.get("headline", ""), raw, reason))

    print(f"\nP1-eligible rows: {p1_count}")
    print(f"  with horizon already set: {p1_nonblank}")
    print(f"  blank horizon (backfill targets): {p1_blank}")
    print(f"\neligibility breakdown of targets: {dict(eligibility_reasons)}")
    assert p1_blank == len(targets)

    # Sanity: expect 244 (per diag)
    if p1_blank != 244:
        print(f"\nWARN: target count {p1_blank} != expected 244 (per diag 2026-06-19). "
              f"Continuing — count drift is informational, not fatal.")

    # Show first 5 + last 5
    print(f"\nfirst 5 targets:")
    for rid, h, raw, why in targets[:5]:
        print(f"  rid={rid:>5}  [{why}]  {h[:80]}")
    if len(targets) > 10:
        print(f"  ... ({len(targets) - 10} more) ...")
    print(f"last 5 targets:")
    for rid, h, raw, why in targets[-5:]:
        print(f"  rid={rid:>5}  [{why}]  {h[:80]}")

    if not commit:
        print(f"\nDRY-RUN: no writes. Pass --commit to apply.")
        print(f"\nWould write:")
        print(f"  {CSV_PATH.name} (in-place, {p1_blank} cells set to {DEFAULT_HORIZON!r})")
        print(f"  {CSV_PATH.name}.bak_horizon_backfill_3y_<utc> (backup)")
        print(f"  {AUDIT_TXT.name} (audit sidecar, {p1_blank} entries)")
        return 0

    # ------ commit ------
    target_rids = {rid for rid, _, _, _ in targets}

    # Backup
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    bak = CSV_PATH.with_suffix(f".csv.bak_horizon_backfill_3y_{ts}")
    shutil.copy2(CSV_PATH, bak)
    print(f"\nbackup: {bak.name}")

    # Mutate rows
    n_mutated = 0
    for r in rows:
        rid_s = r.get("row_id", "").strip()
        if not rid_s.isdigit(): continue
        rid = int(rid_s)
        if rid in target_rids and (r.get("forecast_horizon_years") or "").strip() == "":
            r["forecast_horizon_years"] = DEFAULT_HORIZON
            n_mutated += 1
    assert n_mutated == p1_blank, f"mutation count drift: {n_mutated} != {p1_blank}"

    # Write CSV with QUOTE_ALL
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)
    print(f"wrote: {CSV_PATH.name} ({CSV_PATH.stat().st_size:,} bytes, {n_mutated} cells set)")

    # Audit sidecar
    audit_lines = [
        f"# horizon backfill audit — v1",
        f"# generated_at: {datetime.now(timezone.utc).isoformat()}",
        f"# tag: {BACKFILL_TAG}",
        f"# value_applied: {DEFAULT_HORIZON}",
        f"# target_count: {n_mutated}",
        f"# eligibility_breakdown: {dict(eligibility_reasons)}",
        f"# source_csv: {CSV_PATH.name}",
        f"# source_backup: {bak.name}",
        f"# source_corpus: {CORPUS_JSON.name}",
        f"# source_admits: {ADMITS_JSON.name if ADMITS_JSON.exists() else '(absent)'}",
        f"# columns: row_id\theadline\tprior_raw\tnew_value\teligibility_reason",
        "",
    ]
    for rid, h, raw, why in targets:
        audit_lines.append(f"{rid}\t{h}\t{raw!r}\t{DEFAULT_HORIZON}\t{why}")
    AUDIT_TXT.write_text("\n".join(audit_lines) + "\n", encoding="utf-8")
    print(f"wrote: {AUDIT_TXT.name} ({AUDIT_TXT.stat().st_size:,} bytes)")

    print(f"\n=== GREEN — backfill complete ===")
    print(f"\nNEXT: re-run route_quotations_to_horizon_v2.py to see new P1 routed count")
    print(f"  expected: ~474 P1 eligible / ~470 routed (+ {n_mutated} new SH-3y tuples)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
