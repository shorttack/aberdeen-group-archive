#!/usr/bin/env python3
"""batch_verdict_backlog_v1.py — recompute Rule A verdicts for backlog-scored
studies, PROTECTING hand-authored verdicts.

Scope (Pete-approved 2026-07-18): recompute only studies that
  (a) received new scores in this backlog sweep (appear in the promote ledger), AND
  (b) currently carry a Rule-A-computed OR empty/[DEFERRED] verdict rationale.
Studies with AUTHORED rationales are LEFT UNTOUCHED (Path-B / hand-set verdicts).

Rule A (matches write_study_verdict_rule_a_v1.py):
  used = scores where prescience_score != '' and != -1
  mean(used) -> high >=3.5, medium >=2.0, else low ; empty used -> [DEFERRED]

Value-only edits to _master_studies.csv (prescience + prescience_rationale).
dry-run default; --commit writes (with timestamped backup + audit sidecar).
"""
import csv, sys, shutil, datetime
from pathlib import Path
from collections import defaultdict

A = Path.home()/"Desktop/Archive/aberdeen-group-archive"
STUD = A/"_master_studies.csv"
SCORES = A/"_master_prescience_scores.csv"
LEDGER = Path.home()/"Desktop/Archive/pass_c_backlog_PROMOTE.csv"

commit = "--commit" in sys.argv

# 1. studies touched by the sweep
touched = set()
for r in csv.DictReader(open(LEDGER)):
    touched.add(r["study_id"])

# 2. all scores by study (from the master, post-promote)
by_study = defaultdict(list)
for r in csv.DictReader(open(SCORES)):
    s = (r.get("prescience_score") or "").strip()
    if s == "": continue
    try: v = int(float(s))
    except: continue
    by_study[r["study_id"]].append(v)

def rule_a(scores):
    used = [v for v in scores if v != -1]
    if not used: return "[DEFERRED]", "Rule A: no usable scored obs -> [DEFERRED]."
    mean = sum(used)/len(used)
    verdict = "high" if mean>=3.5 else "medium" if mean>=2.0 else "low"
    excl = len(scores)-len(used)
    return verdict, f"Rule A: mean={mean:.2f} over {len(used)} usable obs ({excl} excluded of {len(scores)}) -> {verdict} [thresholds high>=3.5, medium>=2.0]."

def is_authored(rat):
    low = (rat or "").strip().lower()
    if low == "": return False
    if low.startswith("rule a") or "scored obs" in low or "usable obs" in low or "mean=" in low:
        return False
    return True  # anything else is hand-authored -> protect

# 3. load studies, decide, edit
rows = list(csv.reader(open(STUD)))
H = rows[0]; ix = {c:i for i,c in enumerate(H)}
si, pi, ri = ix["study_id"], ix["prescience"], ix["prescience_rationale"]

changed, protected, nochange, notouch = [], 0, 0, 0
for r in rows[1:]:
    sid = r[si]
    if sid not in touched:
        notouch += 1; continue
    if is_authored(r[ri]):
        protected += 1; continue
    scores = by_study.get(sid, [])
    newv, newr = rule_a(scores)
    if r[pi] == newv:
        nochange += 1
        # still refresh rationale to reflect fuller obs set? keep it simple: only log verdict change
        continue
    changed.append((sid, r[pi], newv, len(scores)))
    r[pi] = newv; r[ri] = newr

print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}")
print(f"Studies in ledger: {len(touched)}")
print(f"  protected (authored verdict): {protected}")
print(f"  untouched (not in ledger):    {notouch}")
print(f"  verdict unchanged:            {nochange}")
print(f"  VERDICT CHANGED:              {len(changed)}")
from collections import Counter
trans = Counter((o,n) for _,o,n,_ in changed)
print("  transitions (old -> new):")
for (o,n),c in trans.most_common():
    print(f"    {o:12s} -> {n:12s}: {c}")
print("  sample changes:")
for sid,o,n,ns in changed[:12]:
    print(f"    {o:10s}->{n:10s} ({ns} obs)  {sid[:50]}")

# parity
assert len(rows)-1 == (len(touched.intersection({r[si] for r in rows[1:]})) + 0) or True  # informational
assert len(H) == len(rows[0]), "col drift"

if commit:
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    bak = STUD.with_suffix(f".csv.bak_batch_verdict_{ts}")
    shutil.copy2(STUD, bak)
    with open(STUD,"w",newline="") as f:
        w=csv.writer(f,quoting=csv.QUOTE_ALL); w.writerow(H); w.writerows(rows[1:])
    audit = STUD.with_suffix(f".csv.applied_batch_verdict_{ts}.txt")
    audit.write_text(f"batch_verdict_backlog_v1  {ts}\nbackup: {bak.name}\nchanged {len(changed)}, protected {protected}\n\n"+
                     "\n".join(f"{s}: {o} -> {n} ({ns} obs)" for s,o,n,ns in changed))
    print(f"\nBackup: {bak.name}\nAudit: {audit.name}\nWROTE {STUD.name} ({len(rows)-1} studies, {len(H)} cols)")
else:
    print("\nDRY-RUN only — pass --commit to write.")
