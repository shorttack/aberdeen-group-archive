#!/usr/bin/env python3
"""Migrate all non-canonical codes.csv files to v18 canonical schema:
   code_id, code_type, label, definition

Mapping rules per variant:
- The 'code_id' column (or 'code' if no code_id) becomes code_id.
- Preserve the original label-as-code_id values where used (e.g. 'strategy-classification')
- If existing code_id is a surrogate like 'OT-001'/'METH-001' AND there's a
  separate 'code_value' or 'code' column, prefer the value column as code_id
  (matches obs.observation_type referential integrity).
- code_type ← 'code_type' / 'category' / 'scheme' / 'domain' / 'applies_to'
- label    ← 'label' / 'code_label' OR title-cased code_id
- definition ← 'description' / 'code_description' / 'definition'

Before writing, take a backup snapshot in _audits/codes_migration_backup/.
"""
import csv, os, shutil
from pathlib import Path
from collections import Counter

REPO = Path('/tmp/aberdeen-group-archive')
os.chdir(REPO)
BACKUP = REPO / '_audits' / 'codes_migration_backup'
BACKUP.mkdir(parents=True, exist_ok=True)

CANONICAL = ['code_id', 'code_type', 'label', 'definition']
STATS = Counter()
ACTIONS = []
def log(k, m):
    STATS[k] += 1
    ACTIONS.append(f"[{k}] {m}")

def write_qa(path, header, rows):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        for r in rows:
            w.writerow(r)

def migrate_one(study_path: Path) -> bool:
    """Migrate one study's codes.csv to canonical schema. Returns True if migrated."""
    codes_path = study_path / 'data' / 'codes.csv'
    if not codes_path.exists():
        return False
    with open(codes_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows: return False
    header = tuple(rows[0])
    if header == tuple(CANONICAL):
        return False  # already canonical

    # Parse each row as a dict against its header
    dict_rows = [dict(zip(header, r)) for r in rows[1:]]

    # Determine the code_id source column
    # Prefer the column whose value matches obs.observation_type references.
    # For schemas with both surrogate (OT-###) and value columns, use value column.
    id_col = None
    if 'code_value' in header:
        id_col = 'code_value'
    elif 'code' in header and 'code_id' not in header:
        id_col = 'code'
    elif 'code' in header and 'code_id' in header:
        # schema like (code_id, scheme, code, label, description) — use 'code'
        id_col = 'code'
    elif 'code_id' in header:
        id_col = 'code_id'
    elif 'code_label' in header:
        id_col = 'code_label'  # fallback for (code_id, code_label, ...)
    if id_col is None:
        log('SKIP_NO_ID_COL', f'{study_path}: header={header}')
        return False

    # Determine code_type source: category / code_type / scheme / domain / applies_to
    type_col = None
    for c in ('code_type', 'category', 'scheme', 'domain', 'applies_to'):
        if c in header:
            type_col = c; break

    # Determine label column
    label_col = None
    for c in ('label', 'code_label'):
        if c in header and c != id_col:
            label_col = c; break

    # Determine definition column
    def_col = None
    for c in ('definition', 'description', 'code_description'):
        if c in header:
            def_col = c; break

    # Build canonical rows
    new_rows = []
    seen = set()
    for r in dict_rows:
        code_id = r.get(id_col, '').strip()
        if not code_id: continue
        code_type = r.get(type_col, '').strip() if type_col else ''
        if not code_type:
            # Infer from context if obvious (e.g. nothing present -> 'observation_type')
            code_type = 'observation_type'
        label = r.get(label_col, '').strip() if label_col else ''
        if not label:
            label = code_id.replace('-', ' ').replace('_', ' ').title()
        definition = r.get(def_col, '').strip() if def_col else ''
        if not definition:
            definition = f"Code for {code_id}"
        key = (code_id, code_type)
        if key in seen:
            continue
        seen.add(key)
        new_rows.append([code_id, code_type, label, definition])

    # Backup original
    rel = study_path.relative_to(REPO)
    backup_path = BACKUP / rel / 'codes.csv'
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(codes_path, backup_path)

    # Write canonical
    write_qa(codes_path, CANONICAL, new_rows)
    log('MIGRATED', f'{rel}  (was {len(header)} cols, {len(dict_rows)} rows -> {len(new_rows)} canonical rows)')
    return True

def main():
    migrated = 0
    for base in ('kastner-author', 'other-authors'):
        for d in sorted(os.listdir(base)):
            sp = REPO / base / d
            if not (sp / 'data').is_dir(): continue
            if migrate_one(sp):
                migrated += 1
    print(f"\nMigrated {migrated} studies to canonical codes.csv schema")
    print(f"Backups saved to: {BACKUP}")
    print(f"\nStats:")
    for k, v in sorted(STATS.items()):
        print(f"  {k:25s} {v}")
    (REPO / '_audits' / 'codes_migration_actions.log').write_text('\n'.join(ACTIONS))

if __name__ == '__main__':
    main()
