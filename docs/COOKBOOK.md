# Cookbook

Common recipes for turning existing data into a heatmap without hand-rolling a
CSV first.

## Git commit history

```
git log --pretty=format:'%ad' --date=short > /tmp/commits.csv
(echo date; cat /tmp/commits.csv) > commits.csv
habit-heatmap commits.csv -o commits.svg --label "Commit history"
```

Each commit is a row with no value column, so rows are counted per day —
exactly a GitHub-style contribution graph, built from your own `git log`.

## A habit-tracking app's CSV export

Most habit trackers export one row per logged entry with a timestamp column
that isn't necessarily named `date`, and sometimes includes a time component:

```
habit-heatmap export.csv -o heatmap.svg \
  --date-col logged_at \
  --date-format "%Y-%m-%d %H:%M:%S"
```

If the export uses full ISO 8601 timestamps (e.g. `2024-03-01T08:15:00Z`), drop
`--date-format` entirely — `load_events` parses those automatically — and add
`--tz` if the app logs in UTC but you want days bucketed in your own timezone:

```
habit-heatmap export.csv -o heatmap.svg --tz America/Chicago
```

## A spreadsheet time log

Export the sheet as CSV with a date column and a numeric duration column
(minutes, hours, whatever unit you tracked in), then sum it per day:

```
habit-heatmap timelog.csv -o timelog.svg --value-col hours --theme purple
```

## Data that isn't a CSV at all

If your data already lives in Python (a database query, an API response),
skip file I/O entirely with `load_events_from_rows` — see the README's
"Piping data in" section for an example.
