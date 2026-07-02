import subprocess
import sys
from pathlib import Path

FIXTURE = Path(__file__).parent / "fixtures" / "sample.csv"


def test_cli_writes_svg_file(tmp_path):
    output = tmp_path / "heatmap.svg"
    result = subprocess.run(
        [sys.executable, "-m", "habit_heatmap", str(FIXTURE), "-o", str(output)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert output.exists()
    assert output.read_text().startswith("<svg")


def test_cli_reports_missing_column(tmp_path):
    output = tmp_path / "heatmap.svg"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "habit_heatmap",
            str(FIXTURE),
            "-o",
            str(output),
            "--date-col",
            "not_a_column",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert not output.exists()
