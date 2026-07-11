#!/usr/bin/env python3
'''promote_pass_c_v7_to_master_v1.py — append a v7 Pass C batch (--output CSV
from run_prescience_pass_c_v7.py) into the canonical score master.

Why this exists: the older promote_pass_c_to_master_v1.py is v5-era — it reads a
hardcoded File-1 path, takes no --input, and does not emit the score master's
'row_class' column. This v7-aware appender takes --input, maps the 11-col v7
batch schema onto the 12-col master schema (adding row_class='scored', or
'prefiltered' for rule-based skips), dedupes on obs_id against the master, and
follows the standard invariants (dry-run default, backup, QUOTE_ALL, parity).

Usage:
  python3 scripts/promote_pass_c_v7_to_master_v1.py --input /tmp/.../pass_c_batch.csv          # dry-run
  python3 scripts/promote_pass_c_v7_to_master_v1.py --input /tmp/.../pass_c_batch.csv --commit
'''
import csv, shutil, sys, argparse, datetime
from pathlib import Path

MASTER = Path.home()/'Desktop/Archive/aberdeen-group-archive/_master_prescience_scores.csv'
TS = datetime.datetime.now(datetime.UTC).strftime('%Y%m%dT%H%M%SZ')

ap = argparse.ArgumentParser()
ap.add_argument('--input', required=True, help='v7 batch --output CSV to promote')
ap.add_argument('--commit', action='store_true')
a = ap.parse_args()

# read master schema (authoritative column order)
with open(MASTER, newline='') as f:
    rd = csv.reader(f); MH = next(rd); mrows = list(rd)
mcols = MH
existing = {r[0] for r in mrows}  # obs_id is col 0
print(f'Mode: {"COMMIT" if a.commit else "DRY-RUN"}  utc={TS}')
print(f'master cols ({len(mcols)}): {mcols}')

# read batch
with open(a.input, newline='') as f:
    batch = list(csv.DictReader(f))
print(f'batch rows: {len(batch)} from {a.input}')

def row_class_for(r):
    sp = (r.get('source_pass') or '').lower()
    if 'prefilter' in sp: return 'prefiltered'
    return 'scored'

new, skipped_dup, mapped = [], 0, []
for r in batch:
    oid = r.get('obs_id','')
    if not oid:
        continue
    if oid in existing:
        skipped_dup += 1; continue
    out = {c: (r.get(c) or '') for c in mcols}   # map by name; missing -> ''
    if 'row_class' in mcols and not out['row_class']:
        out['row_class'] = row_class_for(r)
    new.append([out[c] for c in mcols])
    mapped.append((oid, r.get('prescience_score'), out.get('row_class'), r.get('scorer_version'), r.get('source_pass')))

print(f'to append: {len(new)}   (dupes skipped: {skipped_dup})')
for oid, sc, rc, ver, sp in mapped:
    print(f'   + {oid}  score={sc}  class={rc}  ver={ver}  pass={sp}')
print(f'[master] rows {len(mrows)} -> {len(mrows)+len(new)}')

# schema sanity: batch must contain all master cols except row_class (which we synthesize)
missing_src = [c for c in mcols if c!='row_class' and c not in (batch[0].keys() if batch else [])]
if missing_src:
    print(f'WARNING: batch missing master cols (filled empty): {missing_src}')

if a.commit and new:
    b = MASTER.with_suffix(MASTER.suffix+f'.bak_promote_v7_{TS}'); shutil.copy2(MASTER,b); print('  backup:',b.name)
    with open(MASTER,'a',newline='') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerows(new)
    print('APPENDED to score master.')
elif a.commit:
    print('Nothing to append.')
else:
    print('DRY-RUN only. Pass --commit to write.')
