#!/usr/bin/env python3
"""
compute_qwen_master_kappa_v2.py
================================
v2 calibration diagnostic. v1 produced raw kappa Qwen-vs-Sonar = 0.24 and
revealed two distinct patterns:

  Pattern 1: Abstention asymmetry. Sonar (web-grounded) abstains far more
             than Qwen (frozen LLM). 1,324 of 2,374 overlap rows had Sonar=0
             but Qwen committed to a score.
  Pattern 2: Where both committed (n=1,041), Qwen is systematically +1 high
             vs Sonar (Qwen lives in {4,5}, Sonar lives in {3,4}).

v2 adds three calibrated kappa variants to test those hypotheses:

  A. Raw kappa (5-class, 1..5)                          -- baseline from v1
  B. Qwen-minus-1 calibrated kappa                      -- tests "+1 offset" hypothesis
  C. Tier-bucket kappa (low={1,2}, mid={3}, high={4,5}) -- tests "tier-level reliable"
  D. Best-linear-shift kappa (search shifts in {-2..+2})-- finds the empirically optimal shift

Plus diagnostic stats per variant:
  - n, accuracy (exact-match rate), |off-by-one| rate, |off-by>=2| rate

Inputs (read-only):
  scripts/audit_abandoned_qwen_rows_v1.csv      (Qwen)
  _master_prescience_scores.csv                 (Sonar + Claude)

Outputs (next to this script):
  qwen_master_kappa_v2_report.md
  qwen_master_kappa_v2_paired.csv               (per-pair shifted + tier scores)

Run on Mac:
  cd ~/Desktop/Archive/aberdeen-group-archive
  python3 scripts/compute_qwen_master_kappa_v2.py
"""
from __future__ import annotations
import csv
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE       = Path(__file__).resolve().parent
REPO       = HERE.parent
QWEN_CSV   = HERE / "audit_abandoned_qwen_rows_v1.csv"
MASTER_CSV = REPO / "_master_prescience_scores.csv"

OUT_REPORT = HERE / "qwen_master_kappa_v2_report.md"
OUT_PAIRED = HERE / "qwen_master_kappa_v2_paired.csv"

KAPPA_LABELS_5  = [1, 2, 3, 4, 5]
TIER_LABELS_3   = ["low", "mid", "high"]
GO_THRESHOLD    = 0.70
SUBSTANTIAL     = 0.60  # secondary threshold worth flagging


def short(p: Path) -> str:
    try:
        return str(p.relative_to(Path.home()))
    except ValueError:
        return str(p)


def read_csv_rows(path: Path) -> list[dict]:
    if not path.exists():
        print(f"ERROR: missing {path}", file=sys.stderr)
        sys.exit(1)
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def parse_score(v: str) -> int | None:
    if v is None:
        return None
    s = v.strip()
    if not s:
        return None
    try:
        return int(s)
    except ValueError:
        return None


def quadratic_weighted_kappa(pairs: list[tuple[int, int]], labels: list) -> tuple[float, int, list[list[int]]]:
    """Cohen's quadratic-weighted kappa on ordinal labels (numeric OR string)."""
    K = len(labels)
    idx = {lbl: i for i, lbl in enumerate(labels)}
    O = [[0] * K for _ in range(K)]
    for a, b in pairs:
        if a not in idx or b not in idx:
            continue
        O[idx[a]][idx[b]] += 1

    n = sum(sum(r) for r in O)
    if n == 0:
        return float("nan"), 0, O

    W = [[((i - j) ** 2) / ((K - 1) ** 2) for j in range(K)] for i in range(K)]
    row_marg = [sum(O[i]) for i in range(K)]
    col_marg = [sum(O[i][j] for i in range(K)) for j in range(K)]
    E = [[(row_marg[i] * col_marg[j]) / n for j in range(K)] for i in range(K)]

    num = sum(W[i][j] * O[i][j] for i in range(K) for j in range(K))
    den = sum(W[i][j] * E[i][j] for i in range(K) for j in range(K))
    if den == 0:
        return float("nan"), n, O
    return 1.0 - (num / den), n, O


def to_tier(score: int) -> str:
    if score <= 2:
        return "low"
    if score == 3:
        return "mid"
    return "high"  # 4, 5


def diag_stats(pairs: list[tuple[int, int]]) -> dict:
    """Exact / off-by-1 / off-by>=2 rates for integer pairs."""
    n = len(pairs)
    if n == 0:
        return {"n": 0, "exact_pct": 0.0, "off1_pct": 0.0, "off2plus_pct": 0.0}
    exact = sum(1 for a, b in pairs if a == b)
    off1  = sum(1 for a, b in pairs if abs(a - b) == 1)
    off2  = sum(1 for a, b in pairs if abs(a - b) >= 2)
    return {
        "n": n,
        "exact_pct":    100.0 * exact / n,
        "off1_pct":     100.0 * off1  / n,
        "off2plus_pct": 100.0 * off2  / n,
    }


def render_matrix_md(matrix: list[list[int]], row_labels: list, col_labels: list,
                     row_name: str, col_name: str) -> str:
    head = "| " + f"{row_name} \\ {col_name}" + " | " + " | ".join(str(c) for c in col_labels) + " | total |"
    sep  = "|" + "|".join(["---"] * (len(col_labels) + 2)) + "|"
    lines = [head, sep]
    col_totals = [0] * len(col_labels)
    grand = 0
    for i, r in enumerate(row_labels):
        row_total = sum(matrix[i])
        grand += row_total
        for j in range(len(col_labels)):
            col_totals[j] += matrix[i][j]
        lines.append("| " + str(r) + " | " + " | ".join(str(matrix[i][j]) for j in range(len(col_labels))) + f" | **{row_total}** |")
    lines.append("| **total** | " + " | ".join(f"**{t}**" for t in col_totals) + f" | **{grand}** |")
    return "\n".join(lines)


def main() -> int:
    qwen_rows   = read_csv_rows(QWEN_CSV)
    master_rows = read_csv_rows(MASTER_CSV)
    print(f"[v2] qwen rows:   {len(qwen_rows)}")
    print(f"[v2] master rows: {len(master_rows)}")

    qwen_by_obs: dict[str, dict] = {}
    for r in qwen_rows:
        oid = (r.get("obs_id") or "").strip()
        if oid:
            qwen_by_obs[oid] = r

    # Filter master to Sonar only (Claude n=36 is statistically useless per v1 finding)
    sonar_rows = [r for r in master_rows if (r.get("model") or "").strip() == "sonar-reasoning-pro"]
    print(f"[v2] sonar master rows: {len(sonar_rows)}")

    # Build pairs (Qwen committed AND Sonar committed -> both in 1..5)
    base_pairs: list[tuple[int, int]] = []          # (qwen, sonar), both 1..5
    paired_out: list[dict] = []

    abstain_qwen_only = 0
    abstain_sonar_only = 0
    abstain_both       = 0
    out_of_range       = 0

    for sr in sonar_rows:
        oid = (sr.get("obs_id") or "").strip()
        if not oid or oid not in qwen_by_obs:
            continue
        qr = qwen_by_obs[oid]
        q = parse_score(qr.get("prescience_score"))
        s = parse_score(sr.get("prescience_score"))
        if q is None or s is None:
            continue

        # Track abstention pattern
        q_abs = (q == 0 or q == -1)
        s_abs = (s == 0 or s == -1)
        if q_abs and s_abs:
            abstain_both += 1
        elif q_abs:
            abstain_qwen_only += 1
        elif s_abs:
            abstain_sonar_only += 1

        if q in KAPPA_LABELS_5 and s in KAPPA_LABELS_5:
            base_pairs.append((q, s))
            paired_out.append({
                "obs_id":         oid,
                "qwen_score":     q,
                "sonar_score":    s,
                "diff_qwen_minus_sonar": q - s,
                "qwen_shifted_-1": q - 1,
                "qwen_tier":      to_tier(q),
                "sonar_tier":     to_tier(s),
            })
        elif q in {-1, 0, 1, 2, 3, 4, 5} and s in {-1, 0, 1, 2, 3, 4, 5}:
            pass  # excluded but valid
        else:
            out_of_range += 1

    if paired_out:
        with OUT_PAIRED.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(paired_out[0].keys()))
            w.writeheader()
            for r in paired_out:
                w.writerow(r)
        print(f"[v2] wrote {short(OUT_PAIRED)} ({len(paired_out)} pairs)")

    # ---------- Variant A: raw kappa ----------
    kA, nA, cmA = quadratic_weighted_kappa(base_pairs, KAPPA_LABELS_5)
    dA = diag_stats(base_pairs)

    # ---------- Variant B: Qwen -1 shift ----------
    # Shift Qwen scores down by 1 and clamp to [1..5]
    def clamp(x: int) -> int:
        return max(1, min(5, x))
    shifted_pairs = [(clamp(q - 1), s) for (q, s) in base_pairs]
    kB, nB, cmB = quadratic_weighted_kappa(shifted_pairs, KAPPA_LABELS_5)
    dB = diag_stats(shifted_pairs)

    # ---------- Variant C: tier-bucket kappa (3 classes) ----------
    tier_pairs = [(to_tier(q), to_tier(s)) for (q, s) in base_pairs]
    kC, nC, cmC = quadratic_weighted_kappa(tier_pairs, TIER_LABELS_3)
    # tier exact-match rate
    exact_tier = sum(1 for a, b in tier_pairs if a == b) / max(1, len(tier_pairs))

    # ---------- Variant D: best linear shift in {-2..+2} ----------
    shift_results: list[tuple[int, float, int]] = []
    for shift in (-2, -1, 0, 1, 2):
        sp = [(clamp(q + shift), s) for (q, s) in base_pairs]
        k, n, _ = quadratic_weighted_kappa(sp, KAPPA_LABELS_5)
        shift_results.append((shift, k, n))
    best_shift, kD, nD = max(shift_results, key=lambda x: (x[1] if x[1] == x[1] else -2.0))

    # ---------- Build "Qwen calibration map" from sonar marginals ----------
    # For each Qwen score, what's the median (or mean) Sonar score?
    qwen_to_sonar_mean: dict[int, float] = {}
    qwen_to_sonar_count: dict[int, int] = {}
    for q in KAPPA_LABELS_5:
        sonars = [s for (qq, s) in base_pairs if qq == q]
        qwen_to_sonar_count[q] = len(sonars)
        qwen_to_sonar_mean[q] = (sum(sonars) / len(sonars)) if sonars else float("nan")

    # ---------- Verdict logic ----------
    verdicts: list[str] = []
    if kA >= GO_THRESHOLD:
        verdicts.append(f"GO (raw): κ={kA:.3f}")
    if kB >= GO_THRESHOLD:
        verdicts.append(f"GO (after Qwen−1 shift): κ={kB:.3f}")
    if kC >= GO_THRESHOLD:
        verdicts.append(f"GO (tier-bucket): κ={kC:.3f}")
    if kD >= GO_THRESHOLD and best_shift != 0:
        verdicts.append(f"GO (with shift {best_shift:+d}): κ={kD:.3f}")

    if verdicts:
        verdict = "GO — " + " | ".join(verdicts)
    elif kB >= SUBSTANTIAL or kC >= SUBSTANTIAL:
        verdict = f"BORDERLINE — needs prompt calibration (best κ achievable = {max(kA, kB, kC, kD):.3f})"
    else:
        verdict = f"NO-GO — fundamental disagreement (max κ across all variants = {max(kA, kB, kC, kD):.3f})"

    # ---------- Markdown report ----------
    def fmt(k: float) -> str:
        return f"{k:.4f}" if k == k else "NaN"

    report = f"""# Qwen-vs-Sonar Calibration Diagnostic v2

**Computed**: {datetime.now(timezone.utc).isoformat()}
**Inputs**:
- Qwen: `{short(QWEN_CSV)}` ({len(qwen_rows)} rows)
- Sonar: `{short(MASTER_CSV)}` filtered to `sonar-reasoning-pro` ({len(sonar_rows)} rows)
- Claude excluded (n=36 in v1 is statistically too small)

## Verdict

**{verdict}**

## Variant comparison

| Variant | n | κ (quadratic) | Exact-match | Off-by-1 | Off-by ≥2 | Gate (≥ {GO_THRESHOLD}) |
|---|---|---|---|---|---|---|
| A. Raw (5-class)              | {dA['n']} | **{fmt(kA)}** | {dA['exact_pct']:.1f}% | {dA['off1_pct']:.1f}% | {dA['off2plus_pct']:.1f}% | {'PASS' if kA >= GO_THRESHOLD else 'FAIL'} |
| B. Qwen−1 shifted (5-class)   | {dB['n']} | **{fmt(kB)}** | {dB['exact_pct']:.1f}% | {dB['off1_pct']:.1f}% | {dB['off2plus_pct']:.1f}% | {'PASS' if kB >= GO_THRESHOLD else 'FAIL'} |
| C. Tier-bucket (3-class)      | {nC} | **{fmt(kC)}** | {100*exact_tier:.1f}% | — | — | {'PASS' if kC >= GO_THRESHOLD else 'FAIL'} |
| D. Best linear shift ({best_shift:+d})  | {nD} | **{fmt(kD)}** | — | — | — | {'PASS' if kD >= GO_THRESHOLD else 'FAIL'} |

### Linear-shift search (Variant D detail)

| Shift applied to Qwen | n | κ |
|---|---|---|
""" + "\n".join(f"| {s:+d} | {n} | {fmt(k)} |" for (s, k, n) in shift_results) + f"""

## Abstention pattern (informational only — excluded from κ above)

| Pattern | Count |
|---|---|
| Both abstained (Qwen=0 AND Sonar=0)     | {abstain_both} |
| Only Qwen abstained (Sonar committed)   | {abstain_qwen_only} |
| Only Sonar abstained (Qwen committed)   | {abstain_sonar_only} |

The dominant noise in v1's raw κ was "only Sonar abstained" — Qwen committed where Sonar refused. That's prior-knowledge asymmetry, not disagreement.

## Qwen → Sonar calibration curve (Variant B rationale)

Per Qwen score, the mean Sonar score on the same obs:

| Qwen says... | Sonar says (mean) | n |
|---|---|---|
""" + "\n".join(f"| {q} | {qwen_to_sonar_mean[q]:.2f} | {qwen_to_sonar_count[q]} |" if qwen_to_sonar_count[q] else f"| {q} | (no data) | 0 |" for q in KAPPA_LABELS_5) + f"""

If this column shows a near-monotonic shift (Qwen 5 → ~Sonar 4, Qwen 4 → ~Sonar 3, etc.), Variant B (−1 shift) is the right correction.

## Confusion matrices

### A. Raw (rows = Qwen, cols = Sonar)

{render_matrix_md(cmA, KAPPA_LABELS_5, KAPPA_LABELS_5, "qwen", "sonar")}

### B. Qwen−1 shifted (rows = Qwen−1, cols = Sonar)

{render_matrix_md(cmB, KAPPA_LABELS_5, KAPPA_LABELS_5, "qwen-1", "sonar")}

### C. Tier-bucket (rows = Qwen tier, cols = Sonar tier)

{render_matrix_md(cmC, TIER_LABELS_3, TIER_LABELS_3, "qwen", "sonar")}

## Next moves by verdict shape

- **GO (any variant)**: If Variant B (Qwen−1) hits the gate, the production rescore can apply that calibration post-hoc to Qwen output — no prompt change needed. If Variant C (tier-bucket) is the one that hits, report tiers to consumers rather than integer scores. If Variant D's best shift is non-zero, document the offset and apply at promote time.
- **BORDERLINE**: prompt-anchor revision. Add 3 worked examples to `prescience_score_prompt_v2.md` matching the canonical Sonar anchoring (e.g., explicit "this obs is a 4, not a 5"). Rerun v8 calibration on a fresh 30-obs sample.
- **NO-GO**: Qwen 27B fundamentally over-scores. Options: (1) keep Sonar as primary scorer for new Pass C runs, (2) try a different local model (Llama 3.3 70B, Mistral Large), (3) treat Qwen as cheap pre-filter and Sonar as scorer.

## Files

- `{short(OUT_REPORT)}` — this report
- `{short(OUT_PAIRED)}` — per-pair Qwen/Sonar with shift + tier columns
"""

    OUT_REPORT.write_text(report, encoding="utf-8")
    print(f"[v2] wrote {short(OUT_REPORT)}")

    # ---------- stdout summary ----------
    print()
    print("=" * 64)
    print(f"VERDICT: {verdict}")
    print("=" * 64)
    print(f"A. raw            n={dA['n']:<5} κ={fmt(kA)}   exact={dA['exact_pct']:.1f}%")
    print(f"B. Qwen-1 shifted n={dB['n']:<5} κ={fmt(kB)}   exact={dB['exact_pct']:.1f}%")
    print(f"C. tier-bucket    n={nC:<5} κ={fmt(kC)}   exact={100*exact_tier:.1f}%")
    print(f"D. best shift     n={nD:<5} κ={fmt(kD)}   shift={best_shift:+d}")
    print()
    print(f"Abstention: both={abstain_both} qwen-only={abstain_qwen_only} sonar-only={abstain_sonar_only}")
    print()
    print(f"See: {short(OUT_REPORT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
