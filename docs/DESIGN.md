# Design direction — the Quilt landing page

Quilt is a command-line tool, so this direction governs one surface: the marketing
landing page in `site/`. The page exists to show a spreadsheet-keeper the grid they
could have, then hand them the one command to make it.

## 1. Aesthetic direction

**Warm paper and ink with a real heatmap as the hero.** Off-white paper background,
near-black ink, and a single sheet of content the width of a page. The one hit of
color is the heatmap grid itself, in GitHub green, so the sample output is the
brightest thing on the page. The vibe is a well-set README printed on good stock, not
a neon SaaS splash. It fits the audience: people who keep a quiet spreadsheet and want
something legible, not loud.

## 2. Tokens

| Token | Value |
| --- | --- |
| bg (paper) | `#faf7f0` |
| surface | `#fffdf8` |
| surface (sunken) | `#f1ece1` |
| ink (text) | `#1c1a17` |
| muted text | `#6b655c` |
| hairline / border | `#e2dcce` |
| accent (green) | `#216e39` |
| accent bright | `#40c463` |
| support accent (amber) | `#b8860b` |
| display font | `"Fraunces"`, Georgia, serif |
| UI font | `"Inter"`, system-ui, sans-serif |
| spacing unit | 8px scale (8 / 16 / 24 / 40 / 64) |
| corner radius | 10px cards, 3px cells |
| shadow | `0 1px 2px rgba(28,26,23,.06)`, `0 8px 30px rgba(28,26,23,.08)` |
| motion | 160ms ease-out on hover/press |

## 3. Layout intent

A single centered column, max width ~72ch, that fills the viewport top to bottom with
no empty seas. Top-left wordmark (the mark plus "Quilt"). The hero headline and
subhead sit directly above the sample heatmap, which spans the full column width and
scales with it (inline SVG, `viewBox`, `width:100%`). Below the fold: a benefit list,
the install and usage blocks, a short FAQ, and the CTA. At 390px the column becomes
full-bleed with 20px gutters; the heatmap keeps its aspect ratio and never forces a
horizontal scroll. The heatmap is the hero and gets the most visual weight.

## 4. Signature detail

An SVG monogram beside the wordmark: a three-by-three quilt of rounded squares in
graded greens, the same shape language as the product's output. On load the squares
fade in one row at a time (a two-thirds-second stagger), a quiet nod to a grid filling
up day by day. It respects `prefers-reduced-motion` by rendering fully shown.

## 5. Cross-surface consistency

There is no separate web app, so "app and page as one brand" reduces to: the page's
green is the product's default `github` theme green, and the hero image is genuine
tool output (`examples/workouts.csv` rendered by `render_svg`), not a mockup. What you
see on the page is exactly what the command produces.
