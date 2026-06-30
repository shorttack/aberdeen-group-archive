#!/usr/bin/env python3
"""Phase 2 remediation — targeted handling of alt-schema codes.csv gaps
and cache additions for Intel-acquired tech IDs."""
import csv, os
from pathlib import Path
from collections import Counter

REPO = Path('/tmp/aberdeen-group-archive')
os.chdir(REPO)

STATS = Counter()
ACTIONS = []
def log(kind, msg):
    STATS[kind] += 1
    ACTIONS.append(f"[{kind}] {msg}")

def write_rows_quote_all(path, all_rows):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        for r in all_rows:
            w.writerow(r)

# ============================================================
# Part A: Add newly-introduced technology/entity IDs to the repo cache
# so Layer C is clean
# ============================================================
CACHE_ADDITIONS_TECH = [
    # (tech_id, tech_name, category, vendor, era, lifecycle_at_study, lifecycle_current, notes)
    ('wind-river', 'Wind River (VxWorks RTOS)', 'platform', 'Intel', '2009-2018', 'mature',
     'divested (Intel spun out 2018; Aptiv acquired 2022)',
     'Real-time OS; Intel acquired 2009 ($884M) then divested 2018'),
    ('mcafee', 'McAfee Security Platform', 'platform', 'Intel', '2011-2017', 'mature',
     'divested (majority sold to TPG 2017)',
     'Security software; Intel acquisition (2011, $7.68B) later unwound'),
    ('infineon', 'Infineon Wireless Solutions (WLS)', 'component', 'Intel', '2011-2019', 'growth',
     'divested (smartphone modem unit sold to Apple 2019, $1B)',
     'Baseband modem silicon acquired from Infineon (2011, $1.4B) for Intel mobile push'),
]

def part_a_cache():
    techs_path = REPO / '_known_technologies.csv'
    with open(techs_path, newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f))
    header = rows[0]
    data = rows[1:]
    existing = {r[0] for r in data if r}
    for row in CACHE_ADDITIONS_TECH:
        if row[0] in existing:
            log('TECH_CACHE_SKIP', f'{row[0]} already in cache')
            continue
        data.append(list(row))
        log('TECH_CACHE_ADD', f'{row[0]} -> _known_technologies.csv')
    data.sort(key=lambda r: r[0])
    write_rows_quote_all(techs_path, [header] + data)

# ============================================================
# Part B: codes.csv completion for alt-schema studies
# ============================================================
OBS_TYPE_DEFS = {
    'strategy-classification': 'Characterizes strategic positioning or market stance of a vendor or technology',
    'viability-prediction': 'Forward-looking claim about viability of a product, company, or market',
    'actual-outcome': 'Post-study documented result that validates or refutes an earlier claim',
    'technology-assessment': 'Evaluation of a technology\'s maturity, capabilities, or fitness',
    'benchmark-result': 'Quantitative performance measurement from a formal or informal benchmark',
    'framework-factor': 'A criterion or dimension in an analyst\'s evaluative framework',
    'market-data': 'Quantitative or qualitative market size, growth, or segment statistic',
    'expert-opinion': 'Qualitative professional judgment from a domain practitioner',
    'prescience-vindication': 'Retrospective evidence that a prior prediction was borne out',
    'personal-recollection': 'First-person memory or anecdote',
    'ai-exchange': 'Structured Q&A exchange with an AI system',
    'topic-insight': 'An analytical claim within a topic deep-dive',
    'metric-value': 'Study-specific quantitative measurement',
}

def collect_missing_obs_types(codes_path, obs_path):
    with open(codes_path, newline='', encoding='utf-8') as f:
        code_rows = list(csv.reader(f))
    with open(obs_path, newline='', encoding='utf-8') as f:
        obs_rows = list(csv.reader(f))
    if not code_rows or not obs_rows:
        return None, None, None
    code_header = code_rows[0]
    obs_header = obs_rows[0]
    # Find the ID column in codes.csv (first of 'code_id','code')
    if 'code_id' in code_header:
        id_idx = code_header.index('code_id')
    elif 'code' in code_header:
        id_idx = code_header.index('code')
    else:
        return None, None, None
    # But some schemas have both code_id and code; code_id is a surrogate PK (OT-001)
    # and code is the label. The obs.observation_type value matches the LABEL, not the surrogate.
    # Find label column if present — that's what obs_type actually matches against.
    if 'code' in code_header and 'code_id' in code_header:
        # Use 'code' column (the label/value) as the match column
        id_idx = code_header.index('code')
    elif 'code_value' in code_header:
        # alt schema: 'code_id, code_type, code_value, ...' — obs_type matches code_value
        id_idx = code_header.index('code_value')
    elif 'label' in code_header and 'code_id' in code_header:
        # Schema where code_id is surrogate and label is the match value
        # (Actually for v18 canonical schema code_id IS the label, so this branch only
        # triggers for alt schemas like 'code_id, code_label, code_description, applies_to'
        # where code_label is the match value.)
        pass
    elif 'code_label' in code_header:
        id_idx = code_header.index('code_label')
    existing_codes = {r[id_idx] for r in code_rows[1:] if len(r) > id_idx}

    if 'observation_type' not in obs_header:
        return None, None, None
    ot_idx = obs_header.index('observation_type')
    used = {r[ot_idx] for r in obs_rows[1:] if len(r) > ot_idx and r[ot_idx]}
    missing = used - existing_codes
    return code_rows, code_header, (missing, id_idx)

def part_b_codes_alt_schemas():
    # We target each known alt-schema variant with a builder that appends
    # rows matching the existing column structure.
    for base in ('kastner-author','other-authors'):
        for d in sorted(os.listdir(base)):
            codes_path = REPO / base / d / 'data' / 'codes.csv'
            obs_path = REPO / base / d / 'data' / 'observations.csv'
            if not (codes_path.exists() and obs_path.exists()): continue
            try:
                with open(codes_path, newline='', encoding='utf-8') as f:
                    code_rows = list(csv.reader(f))
                with open(obs_path, newline='', encoding='utf-8') as f:
                    obs_rows = list(csv.reader(f))
            except Exception as e:
                log('ERROR', f'{base}/{d}: read failed: {e}')
                continue
            if not code_rows or not obs_rows: continue
            code_header = tuple(code_rows[0])
            obs_header = obs_rows[0]
            if 'observation_type' not in obs_header: continue
            ot_idx = obs_header.index('observation_type')
            used = {r[ot_idx] for r in obs_rows[1:] if len(r) > ot_idx and r[ot_idx]}

            # Determine existing code set + row builder per schema
            new_rows_to_add = []
            existing_codes = set()
            def label_of(c):
                return c.replace('-',' ').title()
            def desc_of(c):
                return OBS_TYPE_DEFS.get(c, f'Observation of type {c}')

            if code_header == ('code_id','code_type','label','definition'):
                # v18 canonical — already handled in Phase 1
                continue
            elif code_header == ('code','description'):
                existing_codes = {r[0] for r in code_rows[1:] if r}
                missing = used - existing_codes
                for t in sorted(missing):
                    if t in OBS_TYPE_DEFS:
                        new_rows_to_add.append([t, desc_of(t)])
            elif code_header == ('code','category','description'):
                existing_codes = {r[0] for r in code_rows[1:] if r}
                missing = used - existing_codes
                for t in sorted(missing):
                    if t in OBS_TYPE_DEFS:
                        new_rows_to_add.append([t, 'observation_type', desc_of(t)])
            elif code_header == ('code','label','description'):
                existing_codes = {r[0] for r in code_rows[1:] if r}
                missing = used - existing_codes
                for t in sorted(missing):
                    if t in OBS_TYPE_DEFS:
                        new_rows_to_add.append([t, label_of(t), desc_of(t)])
            elif code_header == ('code','label','category','description'):
                existing_codes = {r[0] for r in code_rows[1:] if r}
                missing = used - existing_codes
                for t in sorted(missing):
                    if t in OBS_TYPE_DEFS:
                        new_rows_to_add.append([t, label_of(t), 'observation_type', desc_of(t)])
            elif code_header == ('code','label','description','category'):
                existing_codes = {r[0] for r in code_rows[1:] if r}
                missing = used - existing_codes
                for t in sorted(missing):
                    if t in OBS_TYPE_DEFS:
                        new_rows_to_add.append([t, label_of(t), desc_of(t), 'observation_type'])
            elif code_header == ('code','label','domain','description'):
                existing_codes = {r[0] for r in code_rows[1:] if r}
                missing = used - existing_codes
                for t in sorted(missing):
                    if t in OBS_TYPE_DEFS:
                        new_rows_to_add.append([t, label_of(t), 'observation_type', desc_of(t)])
            elif code_header == ('code_id','code_type','description'):
                existing_codes = {r[0] for r in code_rows[1:] if r}
                missing = used - existing_codes
                for t in sorted(missing):
                    if t in OBS_TYPE_DEFS:
                        new_rows_to_add.append([t, 'observation_type', desc_of(t)])
            elif code_header == ('code_id','code_type','code_value','label','description'):
                # code_value is the match column
                existing_codes = {r[2] for r in code_rows[1:] if len(r) > 2}
                missing = used - existing_codes
                # Use surrogate code_id like OT-### continuing from existing
                existing_surrogates = {r[0] for r in code_rows[1:] if r}
                next_n = 1
                while f'OT-{next_n:03d}' in existing_surrogates:
                    next_n += 1
                for t in sorted(missing):
                    if t in OBS_TYPE_DEFS:
                        new_rows_to_add.append([f'OT-{next_n:03d}', 'observation_type', t, label_of(t), desc_of(t)])
                        next_n += 1
            elif code_header == ('code_id','code_type','code_value','description','study_id'):
                existing_codes = {r[2] for r in code_rows[1:] if len(r) > 2}
                missing = used - existing_codes
                existing_surrogates = {r[0] for r in code_rows[1:] if r}
                next_n = 1
                while f'OT-{next_n:03d}' in existing_surrogates:
                    next_n += 1
                for t in sorted(missing):
                    if t in OBS_TYPE_DEFS:
                        new_rows_to_add.append([f'OT-{next_n:03d}', 'observation_type', t, desc_of(t), d])
                        next_n += 1
            elif code_header == ('code_id','code_label','code_description','applies_to'):
                existing_codes = {r[1] for r in code_rows[1:] if len(r) > 1} | {r[0] for r in code_rows[1:] if r}
                missing = used - existing_codes
                existing_surrogates = {r[0] for r in code_rows[1:] if r}
                next_n = 1
                while f'OT-{next_n:03d}' in existing_surrogates:
                    next_n += 1
                for t in sorted(missing):
                    if t in OBS_TYPE_DEFS:
                        new_rows_to_add.append([f'OT-{next_n:03d}', t, desc_of(t), 'observation'])
                        next_n += 1
            elif code_header == ('code_id','scheme','code','label','description'):
                existing_codes = {r[2] for r in code_rows[1:] if len(r) > 2}
                missing = used - existing_codes
                existing_surrogates = {r[0] for r in code_rows[1:] if r}
                next_n = 1
                while f'OT-{next_n:03d}' in existing_surrogates:
                    next_n += 1
                for t in sorted(missing):
                    if t in OBS_TYPE_DEFS:
                        new_rows_to_add.append([f'OT-{next_n:03d}', 'observation_type', t, label_of(t), desc_of(t)])
                        next_n += 1
            else:
                log('CODES_SKIP_UNKNOWN_SCHEMA', f'{base}/{d}: schema {code_header}')
                continue

            if new_rows_to_add:
                write_rows_quote_all(codes_path, code_rows + new_rows_to_add)
                for nr in new_rows_to_add:
                    log('CODE_ADD_ALT', f'{base}/{d}/data/codes.csv: added obs_type row (schema cols={len(code_header)})')

# ============================================================
# Part C: fix 'prescience-vindication' which is valid but not in any codes.csv
# by adding it where used in v18-canonical schemas (first phase missed some)
# — actually Phase 1 already covers v18 schemas; re-run is safe
# ============================================================

if __name__ == '__main__':
    print("=== PART A: Add tech IDs to repo cache ===")
    part_a_cache()
    print("=== PART B: codes.csv completion for alt schemas ===")
    part_b_codes_alt_schemas()
    print()
    print("SUMMARY")
    for k, v in sorted(STATS.items()):
        print(f"  {k:30s} {v}")
    with open('/tmp/remediation_phase2_actions.log','w') as f:
        f.write('\n'.join(ACTIONS))
    print(f"\nActions log: /tmp/remediation_phase2_actions.log ({len(ACTIONS)} lines)")
