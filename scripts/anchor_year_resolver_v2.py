#!/usr/bin/env python3
"""
anchor_year_resolver_v2.py — Short-horizon prescience anchor year + window resolution.

v2 changes (2026-06-15 PM, post-driver-v8-landing reconciliation):
  - Field names aligned to actual master schemas:
      obs row:    `year_observed` (NOT `obs_date`)
      study row:  `date`          (NOT `published_at`)
      study type: `type`          (unchanged)
  - `period_start_year` field is NOT present in current master_observations;
    memoir fallback now: obs.year_observed → study.date (no period_start_year hop).
  - Backward-compat: still accepts `obs_date` / `published_at` if caller sets them
    (e.g. enriched calibration CSVs); falls through to canonical names otherwise.

Anchor resolution order:
  1. obs.year_observed (or legacy obs.obs_date if set)
  2. study.date (or legacy study.published_at if set) — used for ALL non-empty
     study rows, including memoirs (memoir period_start_year column not in master)

Window math (inclusive of anchor year):
  3y window: [anchor_year, anchor_year + 3]   (4 calendar years)
  5y window: [anchor_year, anchor_year + 5]   (6 calendar years)

Elapsed rule (STRICT):
  elapsed iff today_year > anchor_year + horizon
  → 2026-06-15 cutoffs: 3y anchor ≤ 2022 ; 5y anchor ≤ 2020

Pending row shape (no API call, short-circuit in driver):
  score        = -2
  confidence   = NULL (empty string in CSV)
  rationale    = f"window_not_elapsed:{horizon}y:cutoff_{cutoff_year}"
"""
from __future__ import annotations
import re
from dataclasses import dataclass
from typing import Optional, Tuple

YEAR_RE = re.compile(r"(\d{4})")  # matches a 4-digit year anywhere in the field


class AnchorResolutionError(ValueError):
    """No anchor year resolvable. Driver should tag score=-1 reason=no_anchor."""


@dataclass
class AnchorResult:
    year: int
    source: str  # 'year_observed' | 'study_date'


def _parse_year(val) -> Optional[int]:
    """Extract the first 4-digit year in [1900, 2100] from `val`, else None."""
    if val is None:
        return None
    s = str(val).strip()
    if not s or s.lower() in ("nan", "none", "null"):
        return None
    m = YEAR_RE.search(s)
    if not m:
        return None
    y = int(m.group(1))
    return y if 1900 <= y <= 2100 else None


def _obs_year(obs_row: dict) -> Optional[int]:
    """Try canonical `year_observed`, then legacy `obs_date`."""
    y = _parse_year(obs_row.get("year_observed"))
    if y is None:
        y = _parse_year(obs_row.get("obs_date"))
    return y


def _study_year(study_row: dict) -> Optional[int]:
    """Try canonical `date`, then legacy `published_at`."""
    y = _parse_year(study_row.get("date"))
    if y is None:
        y = _parse_year(study_row.get("published_at"))
    return y


def resolve_anchor_year(obs_row: dict, study_row: dict) -> AnchorResult:
    """Resolve anchor year per locked precedence."""
    y = _obs_year(obs_row)
    if y is not None:
        return AnchorResult(year=y, source="year_observed")

    y = _study_year(study_row)
    if y is not None:
        return AnchorResult(year=y, source="study_date")

    raise AnchorResolutionError(
        f"no_anchor: year_observed={obs_row.get('year_observed')!r} "
        f"obs_date={obs_row.get('obs_date')!r} "
        f"study.type={(study_row.get('type') or '')!r} "
        f"study.date={study_row.get('date')!r} "
        f"study.published_at={study_row.get('published_at')!r}"
    )


def window_bounds(anchor_year: int, horizon: int) -> Tuple[int, int]:
    """Inclusive [start, end] for the horizon window."""
    if horizon not in (3, 5):
        raise ValueError(f"horizon must be 3 or 5, got {horizon}")
    return (anchor_year, anchor_year + horizon)


def is_window_elapsed(anchor_year: int, horizon: int, today_year: int) -> bool:
    """STRICT: today_year > anchor_year + horizon."""
    if horizon not in (3, 5):
        raise ValueError(f"horizon must be 3 or 5, got {horizon}")
    return today_year > anchor_year + horizon


def cutoff_year(horizon: int, today_year: int) -> int:
    """Max anchor_year that is currently 'elapsed' for this horizon."""
    return today_year - horizon - 1


def pending_rationale(horizon: int, today_year: int) -> str:
    """Locked rationale string for score=-2 rows."""
    return f"window_not_elapsed:{horizon}y:cutoff_{cutoff_year(horizon, today_year)}"


# ---- self-test ----
if __name__ == "__main__":
    TODAY = 2026

    # Cutoffs match spec doc exactly
    assert cutoff_year(3, TODAY) == 2022, cutoff_year(3, TODAY)
    assert cutoff_year(5, TODAY) == 2020, cutoff_year(5, TODAY)

    # Strict semantics
    assert is_window_elapsed(2022, 3, TODAY) is True
    assert is_window_elapsed(2023, 3, TODAY) is False
    assert is_window_elapsed(2020, 5, TODAY) is True
    assert is_window_elapsed(2021, 5, TODAY) is False

    # Anchor: year_observed wins (canonical field)
    r = resolve_anchor_year({"year_observed": "2003"}, {"type": "x", "date": "2020"})
    assert r.year == 2003 and r.source == "year_observed", r

    # Anchor: legacy obs_date still accepted
    r = resolve_anchor_year({"obs_date": "2024-03-15"}, {"type": "x", "date": "2020"})
    assert r.year == 2024 and r.source == "year_observed", r

    # Anchor: empty obs → study.date fallback
    r = resolve_anchor_year({"year_observed": ""}, {"type": "memoir", "date": "2024-01-01"})
    assert r.year == 2024 and r.source == "study_date", r

    # Anchor: legacy published_at still accepted on study side
    r = resolve_anchor_year({}, {"type": "research_brief", "published_at": "2019-06-01"})
    assert r.year == 2019 and r.source == "study_date", r

    # Anchor: memoir with year_observed wins over study.date (memoir narrates 1979)
    r = resolve_anchor_year({"year_observed": "1979"}, {"type": "memoir", "date": "2025"})
    assert r.year == 1979 and r.source == "year_observed", r

    # Hard fail: nothing resolvable
    try:
        resolve_anchor_year({}, {"type": "memoir", "date": None})
    except AnchorResolutionError:
        pass
    else:
        raise AssertionError("expected AnchorResolutionError")

    # Pending rationale shape
    assert pending_rationale(3, TODAY) == "window_not_elapsed:3y:cutoff_2022"
    assert pending_rationale(5, TODAY) == "window_not_elapsed:5y:cutoff_2020"

    # Year embedded in messy string ("Q3 2019")
    r = resolve_anchor_year({"year_observed": "Q3 2019"}, {})
    assert r.year == 2019 and r.source == "year_observed", r

    # Year-only ("2003")
    r = resolve_anchor_year({"year_observed": "2003"}, {})
    assert r.year == 2003, r

    print("self-test: PASS")
