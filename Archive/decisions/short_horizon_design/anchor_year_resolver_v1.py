#!/usr/bin/env python3
"""
anchor_year_resolver_v1.py — Short-horizon prescience anchor year + window resolution.

Spec (locked 2026-06-15, decisions_log_entry_2026_06_15_short_horizon_prescience_v2.md
+ ask_user follow-up):

Anchor resolution order:
  1. obs_date year (parse YYYY-MM-DD or YYYY)
  2. memoir period_start_year (ONLY when study.type == 'memoir')
  3. study.published_at year
  4. hard fail → AnchorResolutionError (driver tags row score=-1 reason=no_anchor)

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

YEAR_RE = re.compile(r"^\s*(\d{4})")


class AnchorResolutionError(ValueError):
    """No anchor year resolvable. Driver should tag score=-1 reason=no_anchor."""


@dataclass
class AnchorResult:
    year: int
    source: str  # 'obs_date' | 'memoir_period_start' | 'study_published_at'


def _parse_year(val) -> Optional[int]:
    if val is None:
        return None
    s = str(val).strip()
    if not s or s.lower() in ("nan", "none", "null"):
        return None
    m = YEAR_RE.match(s)
    if not m:
        return None
    y = int(m.group(1))
    return y if 1900 <= y <= 2100 else None


def resolve_anchor_year(obs_row: dict, study_row: dict) -> AnchorResult:
    """Resolve anchor year per locked precedence."""
    y = _parse_year(obs_row.get("obs_date"))
    if y is not None:
        return AnchorResult(year=y, source="obs_date")

    study_type = (study_row.get("type") or "").strip().lower()
    if study_type == "memoir":
        y = _parse_year(obs_row.get("period_start_year"))
        if y is not None:
            return AnchorResult(year=y, source="memoir_period_start")

    y = _parse_year(study_row.get("published_at"))
    if y is not None:
        return AnchorResult(year=y, source="study_published_at")

    raise AnchorResolutionError(
        f"no_anchor: obs_date={obs_row.get('obs_date')!r} "
        f"period_start_year={obs_row.get('period_start_year')!r} "
        f"study.type={study_type!r} study.published_at={study_row.get('published_at')!r}"
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
    assert is_window_elapsed(2023, 3, TODAY) is False  # 2026 not > 2026
    assert is_window_elapsed(2020, 5, TODAY) is True
    assert is_window_elapsed(2021, 5, TODAY) is False  # 2026 not > 2026

    # Anchor: obs_date wins
    r = resolve_anchor_year({"obs_date": "2024-03-15"}, {"type": "x", "published_at": "2020"})
    assert r.year == 2024 and r.source == "obs_date"

    # Anchor: memoir period_start_year used only for memoirs
    r = resolve_anchor_year({"period_start_year": "1998"},
                            {"type": "memoir", "published_at": "2024"})
    assert r.year == 1998 and r.source == "memoir_period_start"

    # Anchor: non-memoir falls through to study.published_at
    r = resolve_anchor_year({"period_start_year": "1998"},
                            {"type": "research_brief", "published_at": "2024"})
    assert r.year == 2024 and r.source == "study_published_at"

    # Anchor: obs_date empty, study fallback
    r = resolve_anchor_year({"obs_date": ""}, {"type": "x", "published_at": "2019-06-01"})
    assert r.year == 2019 and r.source == "study_published_at"

    # Hard fail
    try:
        resolve_anchor_year({}, {"type": "memoir", "published_at": None})
    except AnchorResolutionError:
        pass
    else:
        raise AssertionError("expected AnchorResolutionError")

    # Pending rationale shape
    assert pending_rationale(3, TODAY) == "window_not_elapsed:3y:cutoff_2022"
    assert pending_rationale(5, TODAY) == "window_not_elapsed:5y:cutoff_2020"

    # Pete's Anthropic IPO case: obs in 2024, today 2026 → both pending
    r = resolve_anchor_year({"obs_date": "2024-03-15"}, {"type": "rb", "published_at": "2024"})
    assert not is_window_elapsed(r.year, 3, TODAY)
    assert not is_window_elapsed(r.year, 5, TODAY)

    print("self-test: PASS")