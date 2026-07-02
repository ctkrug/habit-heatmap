"""Render a date -> value mapping as a GitHub-style SVG contribution heatmap."""

from __future__ import annotations

from datetime import date, timedelta
from typing import Optional

from .colors import THEMES, bucket_color

CELL_SIZE = 11
CELL_GAP = 3
MARGIN = 20


def _week_start(day: date) -> date:
    """Return the Sunday on or before ``day`` (weeks run Sun-Sat, GitHub-style)."""
    return day - timedelta(days=(day.weekday() + 1) % 7)


def render_svg(
    counts: dict[date, float],
    start: Optional[date] = None,
    end: Optional[date] = None,
    theme: str = "github",
    cell_size: int = CELL_SIZE,
    gap: int = CELL_GAP,
) -> str:
    """Render ``counts`` as a self-contained SVG contribution heatmap.

    Defaults to spanning the earliest to latest date present in
    ``counts``; pass ``start``/``end`` to render an explicit range
    (required if ``counts`` is empty).
    """
    if not counts and (start is None or end is None):
        raise ValueError("counts is empty; pass explicit start and end dates")

    end = end or max(counts)
    start = start or min(counts)
    if start > end:
        raise ValueError("start date must be on or before end date")

    palette = THEMES.get(theme, THEMES["github"])
    max_value = max(counts.values()) if counts else 0.0

    grid_start = _week_start(start)
    total_days = (end - grid_start).days + 1
    weeks = (total_days + 6) // 7

    stride = cell_size + gap
    width = MARGIN * 2 + weeks * stride
    height = MARGIN * 2 + 7 * stride

    cells = []
    day = grid_start
    while day <= end:
        if day >= start:
            week_index = (day - grid_start).days // 7
            weekday = (day.weekday() + 1) % 7  # Sunday = 0
            x = MARGIN + week_index * stride
            y = MARGIN + weekday * stride
            value = counts.get(day, 0.0)
            color = bucket_color(value, max_value, palette)
            cells.append(
                f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" '
                f'rx="2" ry="2" fill="{color}"><title>{day.isoformat()}: {value:g}</title></rect>'
            )
        day += timedelta(days=1)

    body = "\n  ".join(cells)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">\n  {body}\n</svg>\n'
    )
