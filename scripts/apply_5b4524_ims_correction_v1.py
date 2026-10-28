#!/usr/bin/env python3
"""apply_5b4524_ims_correction_v1.py — PENDING-CHANGES row 49 (Kastner, 2026-09-07), masters side.

The FLORIDA System's database was IMS, not DB2 (AG Report 13287 pp. 15-16; FLORIDA README § 5).
The 5b4524 study package was corrected on 2026-10-28 (commit 86e0135). This script applies the
same correction to the masters at repo root, which are the pipeline's source of truth.

Touches, for study_id = unisys-florida-hrs-expert-witness-tallah-5b4524 only:
  _master_studies.csv       text cells: "IBM DB2" -> "IBM IMS", "DB2" -> "IMS"
  _master_observations.csv  tech_id ibm-db2 -> ibm-ims; text cells as above
  _master_tech_studies.csv  (ibm-db2, sid) -> (ibm-ims, sid); dropped instead if (ibm-ims, sid) already exists

Deliberately NOT touched (scorer provenance; the rationale text records what was scored):
  _master_prescience_scores.csv, _master_prescience_short_horizon.csv — counts reported only.

Invariants: dry-run default (--commit to write); UTC-stamped backup before every write;
csv.QUOTE_ALL; row and column parity asserted and printed.
Usage: python3 apply_5b4524_ims_correction_v1.py [--commit] [--archive DIR]
"""
import csv, shutil, datetime, sys
from pathlib import Path

SID = "unisys-florida-hrs-expert-witness-tallah-5b4524"
OLD_TECH, NEW_TECH = "ibm-db2", "ibm-ims"
commit = "--commit" in sys.argv
archive = Path.home() / "Desktop/Archive/aberdeen-group-archive"
if "--archive" in sys.argv:
    archive = Path(sys.argv[sys.argv.index("--archive") + 1]).expanduser()
ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}   archive: {archive}")

def subst(text):
    return text.replace("ibm-db2", "ibm-ims").replace("IBM DB2", "IBM IMS").replace("DB2", "IMS")

def load(name):
    p = archive / name
    with open(p, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    return p, rows[0], rows[1:]

def save(p, header, rows, n_rows_before, n_cols_before):
    assert len(rows) == n_rows_before, f"row parity broken in {p.name}: {n_rows_before} -> {len(rows)}"
    assert len(header) == n_cols_before, f"column parity broken in {p.name}"
    if not commit:
        print(f"  DRY-RUN: would write {p.name} ({len(rows)} rows, {len(header)} cols)"); return
    bak = p.with_suffix(f".csv.bak_5b4524_ims_{ts}")
    shutil.copy2(p, bak); print(f"  backup: {bak.name}")
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL); w.writerow(header); w.writerows(rows)
    print(f"  wrote {p.name} ({len(rows)} rows, {len(header)} cols)")

# ---- _master_studies.csv
p, h, rows = load("_master_studies.csv"); n0, c0 = len(rows), len(h)
i_sid = h.index("study_id"); changed = cells = 0
for r in rows:
    if r[i_sid] == SID:
        new = [subst(c) for c in r]; cells += sum(a != b for a, b in zip(r, new))
        if new != r: r[:] = new; changed += 1
print(f"_master_studies.csv: {n0} rows; study rows changed={changed}, cells={cells}")
assert changed <= 1
save(p, h, rows, n0, c0)

# ---- _master_observations.csv
p, h, rows = load("_master_observations.csv"); n0, c0 = len(rows), len(h)
i_sid, i_tech = h.index("study_id"), h.index("tech_id"); changed = cells = tech = 0
for r in rows:
    if r[i_sid] == SID:
        new = [subst(c) for c in r]
        if r[i_tech] == OLD_TECH: new[i_tech] = NEW_TECH; tech += 1
        cells += sum(a != b for a, b in zip(r, new))
        if new != r: r[:] = new; changed += 1
print(f"_master_observations.csv: {n0} rows; study rows changed={changed}, cells={cells}, tech_id remapped={tech}")
save(p, h, rows, n0, c0)

# ---- _master_tech_studies.csv
p, h, rows = load("_master_tech_studies.csv"); n0, c0 = len(rows), len(h)
has_new = any(r == [NEW_TECH, SID] for r in rows)
idx = [i for i, r in enumerate(rows) if r == [OLD_TECH, SID]]
if idx and has_new:
    for i in reversed(idx): rows.pop(i)
    print(f"_master_tech_studies.csv: (ibm-ims, sid) already present; dropped {len(idx)} (ibm-db2, sid) row(s): {n0} -> {len(rows)}")
    n0 = len(rows)
elif idx:
    for i in idx: rows[i] = [NEW_TECH, SID]
    print(f"_master_tech_studies.csv: remapped {len(idx)} row(s) ibm-db2 -> ibm-ims")
else:
    print("_master_tech_studies.csv: no (ibm-db2, sid) row found; nothing to do")
save(p, h, rows, n0, c0)

# ---- report-only
for name in ("_master_prescience_scores.csv", "_master_prescience_short_horizon.csv"):
    p, h, rows = load(name); i_sid = h.index("study_id")
    n = sum(1 for r in rows if r[i_sid] == SID and any("DB2" in c for c in r))
    print(f"{name}: {n} scorer-rationale rows for this study mention DB2 — left unchanged (provenance)")

# ---- verify ibm-ims exists in technologies
_, h, rows = load("_master_technologies.csv"); i = h.index("tech_id")
print("ibm-ims present in _master_technologies.csv:", any(r[i] == NEW_TECH for r in rows))
print("DONE" if commit else "DRY-RUN complete — re-run with --commit to write.")
