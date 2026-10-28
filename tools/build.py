#!/usr/bin/env python3
"""Build case study pages from content/projects/*.md.

    python3 tools/build.py

No dependencies. Reads the front matter and markdown body described in each
project file and writes work/<slug>.html. Supports the subset of markdown the
project files use: ## / ### headings with {#id}, paragraphs, - lists,
> pull quotes (last line = attribution), ![alt](src) images, **bold**,
*italic*, [links](url) and <!-- comments --> (dropped).
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content" / "projects"
OUT = ROOT / "work"

# Whiteboard diagrams sit on a white sheet; composed boards break out of the
# reading column as they are; anything else is a product screen on a panel.
SHEET_HINTS = ("audit", "all-workflows", "vision", "pros-cons", "tier-map")
WIDE_HINTS = ("iterations", "final-panel", "research-styles")


# --- Front matter -----------------------------------------------------------

def strip_comment(s):
    out, q = [], False
    for i, ch in enumerate(s):
        if ch == '"' and (i == 0 or s[i - 1] != "\\"):
            q = not q
        if ch == "#" and not q and (i == 0 or s[i - 1].isspace()):
            break
        out.append(ch)
    return "".join(out).strip()


def scalar(v):
    v = strip_comment(v)
    if v.startswith("["):
        return json.loads(v)
    if v.startswith('"'):
        return json.loads(v)
    if v in ("true", "false"):
        return v == "true"
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    return v


def flow_map(s):
    body = s.strip()[1:-1]
    return {k: (json.loads(q) if q else raw.strip())
            for k, q, raw in re.findall(r'(\w+):\s*(?:("(?:[^"\\]|\\.)*")|([^,}]+))', body)}


def parse_front_matter(text):
    data, key, lines = {}, None, text.splitlines()
    for line in lines:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        top = re.match(r"^(\w+):\s*(.*)$", line)
        if top:
            key, val = top.group(1), top.group(2)
            data[key] = scalar(val) if strip_comment(val) else []
            continue
        item = re.match(r"^\s+-\s*(.*)$", line)
        if item and key:
            rest = item.group(1)
            if rest.startswith("{"):
                data[key].append(flow_map(rest))
            else:
                k, v = rest.split(":", 1)
                data[key].append({k.strip(): scalar(v)})
            continue
        cont = re.match(r"^\s+(\w+):\s*(.*)$", line)
        if cont and key and data[key]:
            data[key][-1][cont.group(1)] = scalar(cont.group(2))
    return data


# --- Markdown body ----------------------------------------------------------

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', s)
    return s


def figure(alt, src):
    name = Path(src).name
    path = "../" + src
    caption = f'<figcaption>{inline(alt)}</figcaption>'
    img = f'<img src="{path}" alt="{html.escape(alt)}" loading="lazy">'
    if any(h in name for h in SHEET_HINTS):
        return "sheet", f'<figure class="fig-sheet">{img}{caption}</figure>'
    if any(h in name for h in WIDE_HINTS):
        # Composed boards already carry their own background and labels.
        return "board", f'<figure class="fig-board wide">{img}{caption}</figure>'
    return "screen", f'<figure class="fig-screen"><div class="stage-panel">{img}</div>{caption}</figure>'


def render_blocks(lines):
    """Turn one chapter's lines into HTML, grouping runs of quotes and sheets."""
    blocks, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif line.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].startswith(">"):
                quote.append(lines[i][1:].strip())
                i += 1
            parts = [p for p in quote if p]
            blocks.append(("quote", parts))
        elif line.startswith("!["):
            m = re.match(r"!\[(.*?)\]\((.*?)\)", line)
            blocks.append(("figure",) + figure(m.group(1), m.group(2)))
            i += 1
        elif line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(lines[i][2:].strip())
                i += 1
            blocks.append(("list", items))
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(r"^(>|!\[|- )", lines[i]):
                para.append(lines[i].strip())
                i += 1
            blocks.append(("p", " ".join(para)))

    out, j = [], 0
    while j < len(blocks):
        kind = blocks[j][0]
        if kind == "quote":
            run = []
            while j < len(blocks) and blocks[j][0] == "quote":
                run.append(blocks[j][1])
                j += 1
            quotes = [
                f'<blockquote class="pull"><p>{inline(" ".join(q[:-1]))}</p>'
                f'<cite class="label">{inline(q[-1])}</cite></blockquote>' for q in run
            ]
            out.append(quotes[0] if len(quotes) == 1 else f'<div class="pulls">{"".join(quotes)}</div>')
            continue
        if kind == "figure" and blocks[j][1] == "sheet" and j + 1 < len(blocks) \
                and blocks[j + 1][0] == "figure" and blocks[j + 1][1] == "sheet":
            out.append(f'<div class="fig-row">{blocks[j][2]}{blocks[j + 1][2]}</div>')
            j += 2
            continue
        if kind == "figure":
            out.append(blocks[j][2])
        elif kind == "list":
            items = blocks[j][1]
            if all(", so " in it for it in items):
                lis = "".join(
                    f'<li><span class="was">{inline(a)},</span><span class="now">so {inline(b)}</span></li>'
                    for a, b in (it.split(", so ", 1) for it in items))
                out.append(f'<ul class="shifts">{lis}</ul>')
            else:
                out.append('<ul class="points">' + "".join(f"<li>{inline(it)}</li>" for it in items) + "</ul>")
        else:
            out.append(f"<p>{inline(blocks[j][1])}</p>")
        j += 1
    return "\n".join(out)


def parse_body(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    chapters, cur = [], None
    for line in text.splitlines():
        h2 = re.match(r"^##\s+(.*?)\s*\{#([\w-]+)\}\s*$", line)
        h3 = re.match(r"^###\s+(.*)$", line)
        if h2:
            cur = {"label": h2.group(1), "id": h2.group(2), "headline": "", "lines": []}
            chapters.append(cur)
        elif h3 and cur and not cur["headline"]:
            cur["headline"] = h3.group(1).strip()
        elif cur is not None:
            cur["lines"].append(line.rstrip())
    return chapters


# --- Page -------------------------------------------------------------------

def page(meta, chapters, next_project=None):
    esc = html.escape
    focus = "".join(f"<li>{esc(t)}</li>" for t in meta.get("focus", []))
    metrics = "".join(
        f'<li><b>{esc(m["value"])}</b><span>{esc(m["label"])}</span></li>' for m in meta.get("page_metrics", []))

    def bullets(s):
        return "<ul>" + "".join(f"<li>{esc(x.strip())}</li>" for x in s.split("·")) + "</ul>"

    toc, body = [], []
    for ch in chapters:
        m = re.match(r"(\d+)\s*·\s*(.*)", ch["label"])
        num, name = (m.group(1), m.group(2)) if m else ("", ch["label"])
        toc.append(f'<li><a href="#{ch["id"]}"><span>{num}</span>{esc(name)}</a></li>')
        cls = "chapter" + (" reflection" if ch["id"] == "reflection" else "")
        if ch["headline"]:
            heading = f'<p class="label num">{esc(ch["label"])}</p>\n<h2>{inline(ch["headline"])}</h2>'
        else:
            heading = f'<h2>{esc(name)}</h2>'
        body.append(
            f'<section class="{cls}" id="{ch["id"]}">\n{heading}\n'
            f'{render_blocks(ch["lines"])}\n</section>')

    if meta.get("page_role_summary"):
        # The Timeline fact already shows the dates, so leave them out of the role.
        timeline = meta.get("page_timeline", "")
        role = " · ".join(x.strip() for x in meta["page_role_summary"].split("·")
                          if not (timeline and timeline.startswith(x.strip())))
        role_facts = f'        <div><dt class="label">My role</dt><dd>{bullets(role)}</dd></div>'
    else:
        role_facts = (f'        <div><dt class="label">My role</dt><dd>{bullets(meta.get("page_role_me", ""))}</dd></div>\n'
                      f'        <div><dt class="label">Team</dt><dd>{bullets(meta.get("page_role_team", ""))}</dd></div>')

    hero = meta.get("page_hero_fallback") or meta.get("card_thumbnail")
    nxt = ""
    if next_project:
        nxt = (f'<div class="wrap cs-next"><a href="{next_project[0]}"><p class="label">Next project</p>'
               f'<h2>{esc(next_project[1])} →</h2></a></div>')

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(meta["title"])} — Jason Frade</title>
<meta name="description" content="{esc(meta.get("page_subtitle", ""))}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,300;0,400;0,500;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/site.css">
</head>
<body>

<div class="wrap">
  <nav class="site-nav">
    <a class="mark" href="../"><span class="disc"></span>JASON FRADE</a>
    <ul><li><a href="../#work">Work</a></li><li><a href="../#about">About</a></li><li><a href="../documents/Frade_resume.pdf">Résumé</a></li></ul>
  </nav>
</div>

<main>
  <header class="wrap cs-hero">
    <p class="label">{esc(meta.get("card_context", ""))}</p>
    <h1>{esc(meta["title"])}</h1>
    <p class="lede">{esc(meta.get("page_subtitle", ""))}</p>
    <ul class="tags">{focus}</ul>
  </header>

  <div class="wrap cs-hero-media">
    <div class="stage-panel"><img src="../{esc(hero)}" alt="The Automate panel open beside a HubSpot contacts list"></div>
  </div>

  <div class="wrap">
    <div class="cs-summary">
      <div class="cs-problem">
        <p class="label">The problem</p>
        <p>{esc(meta.get("page_problem", ""))}</p>
      </div>
      <div>
        <p class="label">Results</p>
        <ul class="metrics">{metrics}</ul>
      </div>
      <dl class="facts">
{role_facts}
        <div><dt class="label">Timeline</dt><dd>{esc(meta.get("page_timeline", ""))}</dd></div>
        <div><dt class="label">Shipped to</dt><dd>{esc(meta.get("page_shipped_to", ""))}</dd></div>
      </dl>
    </div>
  </div>

  <div class="wrap">
    <article class="cs-body">
      <nav class="toc" aria-label="Chapters">
        <p class="label">Contents</p>
        <ol>{"".join(toc)}</ol>
      </nav>
{chr(10).join(body)}
    </article>
  </div>
  {nxt}
</main>

<footer class="site-footer">
  <div class="wrap">
    <span class="label">Jason Frade · Product designer</span>
    <a class="label" href="mailto:jason.a.frade@gmail.com">jason.a.frade@gmail.com</a>
  </div>
</footer>

<script>
  // Highlight the chapter currently in view in the contents list.
  const links = [...document.querySelectorAll('.toc a')];
  const seen = new Set();
  const observer = new IntersectionObserver(entries => {{
    entries.forEach(e => e.isIntersecting ? seen.add(e.target.id) : seen.delete(e.target.id));
    const first = links.find(a => seen.has(a.hash.slice(1)));
    if (first) links.forEach(a => a.classList.toggle('active', a === first));
  }}, {{ rootMargin: '-20% 0px -60% 0px' }});
  document.querySelectorAll('.chapter').forEach(el => observer.observe(el));
</script>
</body>
</html>
"""


def build():
    OUT.mkdir(exist_ok=True)
    for md in sorted(CONTENT.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        _, fm, body = text.split("---", 2)
        meta = parse_front_matter(fm)
        chapters = parse_body(body)
        out = OUT / f'{meta["slug"]}.html'
        out.write_text(page(meta, chapters), encoding="utf-8")
        print(f"built {out.relative_to(ROOT)}  ({len(chapters)} chapters)")


if __name__ == "__main__":
    build()
