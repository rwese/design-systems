#!/usr/bin/env python3
"""Generate a single-page document using the design-system stylesheet."""

from __future__ import annotations

import argparse
import html
from pathlib import Path


DEFAULT_CSS_URL = "https://raw.githubusercontent.com/rwese/design-systems/main/design-system-cdn.css"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="HTML file to write")
    parser.add_argument("--title", default="Document title", help="Document title and h1 text")
    parser.add_argument("--status", default="Draft", help="Status metadata value")
    parser.add_argument("--owner", default="Team", help="Owner metadata value")
    parser.add_argument(
        "--custom-css-url",
        default=DEFAULT_CSS_URL,
        help=f"Stylesheet URL to include. Defaults to {DEFAULT_CSS_URL}",
    )
    return parser.parse_args()


def render(title: str, status: str, owner: str, css_url: str) -> str:
    title_text = html.escape(title)
    status_text = html.escape(status)
    owner_text = html.escape(owner)
    css_href = html.escape(css_url, quote=True)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title_text}</title>
  <link rel="stylesheet" href="{css_href}">
</head>
<body class="ds-page">
  <article class="ds-doc">
    <header class="ds-doc__header">
      <h1>{title_text}</h1>
      <ul class="ds-meta">
        <li>Status: {status_text}</li>
        <li>Owner: {owner_text}</li>
      </ul>
      <p class="ds-summary">One concise summary paragraph.</p>
      <nav class="ds-toc" aria-labelledby="toc-title">
        <h2 id="toc-title">Contents</h2>
        <ol>
          <li><a href="#section">Section</a></li>
        </ol>
      </nav>
    </header>

    <div class="ds-doc__body">
      <section id="section">
        <h2>Section</h2>
        <p>Write semantic HTML and use documentation patterns only where useful.</p>
      </section>
    </div>

    <footer class="ds-doc__footer">
      <p>Footer note.</p>
    </footer>
  </article>
</body>
</html>
"""


def main() -> None:
    args = parse_args()
    args.output.write_text(
        render(args.title, args.status, args.owner, args.custom_css_url),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
