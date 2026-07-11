#!/usr/bin/env python3
'''write_study_verdict_rule_a_v1.py — compute a study's prescience verdict from
its scored observations (Rule A) and write it into _master_studies.csv.

Rule A:  used = scores where prescience_score != '' and != -1 (prefiltered)
  len(used)==0                    -> not-applicable
  mean(used) >= 3.5               -> high
  mean(used) >= 2.0               -> medium
  else                            -> low

Writes 'prescience' and 'prescience_rationale' on the study row. Dry-run default;
--commit to write. Backup + QUOTE_ALL + row-parity.
Usage:
  python3 scripts/write_study_verdict_rule_a_v1.py --study <study_id>            # dry-run
  python3 scripts/write_study_verdict_rule_a_v1.py --study <study_id> --commit
'''
import csv, shutil, sys, argparse, datetime, statistics
from pathlib import Path

A = Path.home()/'Desktop/Archive/aberdeen-group-archive'
STUD = A/'_master_studies.csv'; SCORES = A/'_master_prescience_scores.csv'
TS = datetime.datetime.now(datetime.UTC).strftime('%Y%m%dT%H%M%SZ')

ap = argparse.ArgumentParser()
ap.add_argument('--study', required=True)
ap.add_argument('--commit', action='store_true')
a = ap.parse_args()

# gather scores for the study
used = []
for r in csv.DictReader(open(SCORES)):
    if r['study_id'] != a.study: continue
    s = (r.get('prescience_score') or '').strip()
    if s == '' or s == '-1': continue
    try: used.append(float(s))
    except ValueError: pass

if not used:
    verdict, mean = 'not-applicable', None
elif statistics.mean(used) >= 3.5:
    verdict, mean = 'high', statistics.mean(used)
elif statistics.mean(used) >= 2.0:
    verdict, mean = 'medium', statistics.mean(used)
else:
    verdict, mean = 'low', statistics.mean(used)

meanstr = f'{mean:.2f}' if mean is not None else 'n/a'
rationale = (f'Rule A over {len(used)} scored obs (Pass C v7): mean={meanstr} -> {verdict} '
             f'[high>=3.5, medium>=2.0]. Hybrid memoir: curated observations only.')
print(f'study: {a.study}')
print(f'used scores: {used}  mean={meanstr}  -> verdict={verdict}')

with open(STUD, newline='') as f:
    rd = csv.reader(f); H = next(rd); rows = list(rd)
ix = {c:i for i,c in enumerate(H)}
hit = [r for r in rows if r[ix['study_id']]==a.study]
if not hit: sys.exit(f'ABORT: study {a.study} not found')
r = hit[0]
print(f'  before: prescience={r[ix["prescience"]]!r}')
r[ix['prescience']] = verdict
r[ix['prescience_rationale']] = rationale
print(f'  after : prescience={verdict!r}')
print(f'[studies] rows={len(rows)} (parity preserved) cols={len(H)}')

if a.commit:
    b = STUD.with_suffix(STUD.suffix+f'.bak_verdict_{TS}'); shutil.copy2(STUD,b); print('  backup:',b.name)
    with open(STUD,'w',newline='') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL); w.writerow(H); w.writerows(rows)
    print('WROTE study verdict.')
else:
    print('DRY-RUN only. Pass --commit to write.')
