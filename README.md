# Design Systems

Lean CSS for concise, handwritten single-page HTML documentation.

## Files

- `design-system-cdn.css` - reusable documentation stylesheet intended for CDN hosting
- `design-system-cdn-demo.html` - minimal documentation page example
- `design-system-variants-demo.html` - side-by-side concept variant example

## Goals

- No build step
- No JavaScript
- No external fonts, images, scripts, or generated assets
- Semantic HTML first, with a small `ds-` namespace for document patterns

## Minimal page

Use the stylesheet directly from GitHub:

```html
<link rel="stylesheet" href="https://raw.githubusercontent.com/rwese/design-systems/main/design-system-cdn.css">
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Document title</title>
  <link rel="stylesheet" href="https://raw.githubusercontent.com/rwese/design-systems/main/design-system-cdn.css">
</head>
<body class="ds-page">
  <article class="ds-doc">
    <header class="ds-doc__header">
      <h1>Document title</h1>
      <ul class="ds-meta">
        <li>Status: Draft</li>
        <li>Owner: Team</li>
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
```

## Supported patterns

Components use a `ds-` namespace with BEM conventions:

```text
.ds-component
.ds-component__element
.ds-component--modifier
```

V1 supports:

- `ds-page` - page background and viewport spacing
- `ds-doc` - centered document container
- `ds-doc__header`, `ds-doc__body`, `ds-doc__body--wide`, `ds-doc__footer` - document regions
- `ds-meta` - status, owner, dates, and other compact metadata
- `ds-summary` - one prominent orientation paragraph
- `ds-toc` - in-page table of contents
- `ds-callout ds-callout--info` - neutral context
- `ds-callout ds-callout--warning` - risks and caveats
- `ds-variants` and `ds-variant` - responsive side-by-side concept comparisons
- `ds-theme--core`, `ds-theme--console-light`, `ds-theme--console-dark`, `ds-theme--console-dimmed`, `ds-theme--console-paper` - complete theme directions applied to any document shell
- `ds-theme-grid`, `ds-theme-preview` - compact theme comparison layout
- `ds-theme-stage`, `ds-theme-switch`, `ds-theme-target` - CSS-driven theme switcher preview

The stylesheet also defines readable defaults for headings, paragraphs, links, lists, blockquotes, inline `code`, `kbd`, `pre code`, tables, captions, keyboard focus, mobile layouts, and basic print output.
