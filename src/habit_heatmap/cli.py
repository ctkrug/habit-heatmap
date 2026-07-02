"""Command-line interface for habit-heatmap."""

from __future__ import annotations

import argparse
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Optional

from .parser import load_events
from .render_svg import render_svg


def _parse_iso_date(raw: str) -> date:
    return datetime.strptime(raw, "%Y-%m-%d").date()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="habit-heatmap",
        description="Generate a GitHub-style contribution heatmap from a CSV of dated events.",
    )
    parser.add_argument("csv", help="path to the input CSV file")
    parser.add_argument("-o", "--output", required=True, help="output file path (.svg or .png)")
    parser.add_argument("--date-col", default="date", help="name of the date column (default: date)")
    parser.add_argument(
        "--value-col", default=None, help="numeric column to sum per day (default: count rows)"
    )
    parser.add_argument("--date-format", default=None, help="explicit strptime format for the date column")
    parser.add_argument("--start", type=_parse_iso_date, default=None, help="first day to render (YYYY-MM-DD)")
    parser.add_argument("--end", type=_parse_iso_date, default=None, help="last day to render (YYYY-MM-DD)")
    parser.add_argument("--theme", default="github", help="color theme: github, blue, or purple")
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    counts = load_events(
        args.csv,
        date_col=args.date_col,
        value_col=args.value_col,
        date_format=args.date_format,
    )
    svg = render_svg(counts, start=args.start, end=args.end, theme=args.theme)

    output = Path(args.output)
    if output.suffix.lower() == ".png":
        from .render_png import svg_to_png

        svg_to_png(svg, str(output))
    else:
        output.write_text(svg, encoding="utf-8")

    print(f"wrote {output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
