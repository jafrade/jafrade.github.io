#!/usr/bin/env python3
"""Build the home page and case study pages from content/projects/*.md.

    python3 tools/build.py

No dependencies. Reads the front matter and markdown body described in each
project file and writes work/<slug>.html, plus index.html with a card for
every project (sorted by `order`). Only projects with a file in
content/projects appear; the old pages in work/ are kept but not linked. Supports the subset of markdown the
project files use: ## / ### headings with {#id}, paragraphs, - lists,
> pull quotes (last line = attribution), ![alt](src) images, **bold**,
*italic*, [links](url) and <!-- comments --> (dropped). Images between
<!-- carousel --> and <!-- /carousel --> become one carousel, with each
image's alt text as its slide caption.
"""
import hashlib
import html
import json
import re
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content" / "projects"
OUT = ROOT / "work"

# Diagrams on white sit on a sheet; composed boards (already on a cream
# background) break out of the reading column as they are; anything else is
# a product screen on a panel.
SHEET_HINTS = ("audit", "all-workflows", "vision", "pros-cons", "tier-map", "jobs-by-stage",
               "direction-1", "direction-2", "impact-1", "impact-2", "naming", "v2-concepts",
               "v2-canvas-explorations")

# Images a project file refers to that aren't in images/ yet; they're left out
# of the page and listed when the build finishes.
MISSING = []


def exists(src):
    if (ROOT / src).is_file():
        return True
    MISSING.append(src)
    return False
WIDE_HINTS = ("iterations", "final-panel", "research-styles", "explorations", "ab-test", "concepts", "fit-diagram", "problem-map")


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
        if cont and key:
            if data[key] == []:
                data[key] = {}  # a nested group of fields, like page_contact
            target = data[key] if isinstance(data[key], dict) else data[key][-1]
            target[cont.group(1)] = scalar(cont.group(2))
    return data


# --- Markdown body ----------------------------------------------------------

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', s)
    return s


def image_size(src):
    """Width and height of a JPEG or PNG, so pages reserve space before images load."""
    try:
        data = (ROOT / src).read_bytes()
    except OSError:
        return None
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", data[16:24])
    i = 2
    while i < len(data) - 9 and data[i] == 0xFF:
        marker, length = data[i + 1], struct.unpack(">H", data[i + 2:i + 4])[0]
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
            h, w = struct.unpack(">HH", data[i + 5:i + 9])
            return w, h
        i += 2 + length
    return None


def img_tag(src, alt, prefix="../"):
    size = image_size(src)
    dims = f' width="{size[0]}" height="{size[1]}"' if size else ""
    return f'<img src="{prefix}{src}" alt="{html.escape(alt)}"{dims} loading="lazy">'


def figure(alt, src):
    name = Path(src).name
    caption = f'<figcaption>{inline(alt)}</figcaption>'
    img = img_tag(src, alt)
    if any(h in name for h in SHEET_HINTS):
        return "sheet", f'<figure class="fig-sheet">{img}{caption}</figure>'
    if any(h in name for h in WIDE_HINTS):
        # Composed boards already carry their own background and labels.
        return "board", f'<figure class="fig-board wide">{img}{caption}</figure>'
    return "screen", f'<figure class="fig-screen"><div class="stage-panel">{img}</div>{caption}</figure>'


def carousel(images):
    slides = "".join(
        f'<div class="slide" data-caption="{html.escape(inline(alt))}">'
        f'{img_tag(src, alt)}</div>' for alt, src in images)
    # Thumbnails let readers scan every slide at a glance and jump to one.
    thumbs = "".join(
        f'<button class="thumb" aria-label="Show slide {i + 1}: {html.escape(alt)}">'
        f'<img src="../{src}" alt="" loading="lazy"></button>' for i, (alt, src) in enumerate(images))
    return (f'<figure class="carousel wide"><div class="carousel-track" tabindex="0">{slides}</div>'
            f'<div class="carousel-thumbs">{thumbs}</div>'
            f'<div class="carousel-bar"><figcaption aria-live="polite">{inline(images[0][0])}</figcaption>'
            f'<div class="carousel-nav"><span class="label count">1 / {len(images)}</span>'
            f'<button class="prev" aria-label="Previous slide">←</button>'
            f'<button class="next" aria-label="Next slide">→</button></div></div></figure>')


def render_blocks(lines, media_first=False):
    """Turn one chapter's lines into HTML, grouping runs of quotes.

    With media_first, carousels move to the top of the chapter, right under
    the headline.
    """
    blocks, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif line == "::carousel":
            images = []
            i += 1
            while i < len(lines) and lines[i] != "::/carousel":
                m = re.match(r"!\[(.*?)\]\((.*?)\)", lines[i])
                if m and exists(m.group(2)):
                    images.append((m.group(1), m.group(2)))
                i += 1
            if images:
                blocks.append(("carousel", images))
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
            if exists(m.group(2)):
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
            while i < len(lines) and lines[i].strip() and not re.match(r"^(>|!\[|- |::)", lines[i]):
                para.append(lines[i].strip())
                i += 1
            blocks.append(("p", " ".join(para)))

    if media_first:
        blocks = [b for b in blocks if b[0] == "carousel"] + [b for b in blocks if b[0] != "carousel"]

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
        if kind == "carousel":
            out.append(carousel(blocks[j][1]))
        elif kind == "figure":
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
    text = re.sub(r"<!--\s*(/?)carousel\s*-->", r"::\1carousel", text)
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


# --- Shared chrome ----------------------------------------------------------

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,300;0,400;0,500;1,400'
         '&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')

# Changes whenever site.css does, so browsers fetch the new file instead of a cached one
CSS_VERSION = hashlib.md5((ROOT / "css" / "site.css").read_bytes()).hexdigest()[:8]

# Card panel colours, in order down the page
CARD_COLOURS = ("sage", "oak", "stone", "walnut")


def nav(root):
    home = root or "./"
    return f"""<div class="wrap">
  <nav class="site-nav">
    <a class="mark" href="{home}"><span class="disc"></span>JASON FRADE</a>
    <ul><li><a href="{root}#work">Work</a></li><li><a href="{root}about.html">About</a></li><li><a href="{root}documents/Frade_resume.pdf">Résumé</a></li></ul>
  </nav>
</div>"""


FOOTER = """<footer class="site-footer">
  <div class="wrap">
    <span class="label">Jason Frade · Product designer</span>
    <a class="label" href="mailto:jason.a.frade@gmail.com">jason.a.frade@gmail.com</a>
  </div>
</footer>"""


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
            f'{render_blocks(ch["lines"], media_first=ch["id"] == "solution")}\n</section>')

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
    # Facts with no value (like a project without a timeline) are left out.
    other_facts = "\n".join(
        f'        <div><dt class="label">{label}</dt><dd>{esc(meta[key])}</dd></div>'
        for label, key in (("Timeline", "page_timeline"), ("Shipped to", "page_shipped_to")) if meta.get(key))
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
{FONTS}
<link rel="stylesheet" href="../css/site.css?v={CSS_VERSION}">
</head>
<body>

{nav("../")}

<main>
  <header class="wrap cs-hero">
    <p class="label">{esc(meta.get("card_context", ""))}</p>
    <h1>{esc(meta["title"])}</h1>
    <p class="lede">{esc(meta.get("page_subtitle", ""))}</p>
    <ul class="tags">{focus}</ul>
  </header>

  <div class="wrap cs-hero-media">
    <div class="stage-panel"><img src="../{esc(hero)}" alt="{esc(meta.get("page_hero_alt") or meta["title"])}"></div>
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
{other_facts}
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

{FOOTER}

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

  // Carousels: arrows and thumbnails move between slides; the caption and count follow.
  document.querySelectorAll('.carousel').forEach(c => {{
    const track = c.querySelector('.carousel-track');
    const slides = [...track.children];
    const cap = c.querySelector('figcaption'), count = c.querySelector('.count');
    const prev = c.querySelector('.prev'), next = c.querySelector('.next');
    const thumbs = [...c.querySelectorAll('.thumb')];
    let current = 0, target = null;
    // Slides are spaced apart so a neighbour's edge never shows at the border.
    const step = () => slides[1].offsetLeft - slides[0].offsetLeft;
    const show = i => {{
      current = i;
      thumbs.forEach((t, j) => t.setAttribute('aria-current', j === i));
      cap.innerHTML = slides[i].dataset.caption;
      count.textContent = `${{i + 1}} / ${{slides.length}}`;
      prev.disabled = i === 0;
      next.disabled = i === slides.length - 1;
    }};
    // Arrows step from the slide we're heading to, so quick clicks add up.
    const go = i => {{
      target = Math.max(0, Math.min(slides.length - 1, i));
      show(target);
      track.scrollTo({{ left: target * step(), behavior: 'smooth' }});
    }};
    prev.onclick = () => go(current - 1);
    next.onclick = () => go(current + 1);
    thumbs.forEach((t, j) => t.onclick = () => go(j));
    track.addEventListener('keydown', e => {{
      if (e.key === 'ArrowLeft') {{ e.preventDefault(); go(current - 1); }}
      if (e.key === 'ArrowRight') {{ e.preventDefault(); go(current + 1); }}
    }});
    // Swipes and trackpad scrolls update the caption once they settle on a slide.
    track.addEventListener('scroll', () => {{
      const i = Math.round(track.scrollLeft / step());
      if (target === null || i === target) {{ target = null; if (i !== current) show(i); }}
    }}, {{ passive: true }});
    show(0);
  }});
</script>
</body>
</html>
"""


# --- Home -------------------------------------------------------------------

def card(meta, colour):
    esc = html.escape
    focus = "".join(f"<li>{esc(t)}</li>" for t in meta.get("focus", []))
    cls = "project-card" + (" featured" if meta.get("featured") else "")
    return f"""    <a class="{cls}" href="work/{esc(meta["slug"])}.html" style="--c: var(--{colour})">
      <div class="stage"><div class="art screen"><img src="{esc(meta["card_thumbnail"])}" alt=""></div></div>
      <div class="info">
        <p class="label">{esc(meta.get("card_context", ""))}</p>
        <h3>{esc(meta["title"])}</h3>
        <p class="outcome">{esc(meta.get("card_summary", ""))}</p>
        <ul class="tags">{focus}</ul>
      </div>
    </a>"""


def home(projects):
    cards = "\n".join(card(m, CARD_COLOURS[i % len(CARD_COLOURS)]) for i, m in enumerate(projects))
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Jason Frade — Product designer</title>
<meta name="description" content="Product design portfolio of Jason Frade.">
<link rel="icon" href="favicon.ico">
{FONTS}
<link rel="stylesheet" href="css/site.css?v={CSS_VERSION}">
</head>
<body>

{nav("")}

<main>
  <header class="home-hero dotted">
    <div class="wrap">
      <h1>Hi, I’m Jason.</h1>
      <p class="lede">I design simple, well-crafted software for people doing complicated work.</p>
    </div>
  </header>

  <section class="wrap home-work" id="work">
    <p class="label">Selected work</p>
    <div class="projects">
{cards}
    </div>
  </section>

</main>

{FOOTER}
</body>
</html>
"""


# --- About ------------------------------------------------------------------

EMAIL = "jason.a.frade@gmail.com"     # used until about.md has a real email
RESUME = "documents/Frade_resume.pdf"  # used until about.md's resume file exists


def known(v):
    """False for values still marked TBD in about.md, so they stay off the page."""
    return bool(v) and "TBD" not in str(v)


def about_sections(body):
    """Split about.md into {id: (label, lines)} by its ## headings."""
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    sections, cur = {}, None
    for line in body.splitlines():
        h2 = re.match(r"^##\s+(.*?)\s*\{#([\w-]+)\}\s*$", line)
        if h2:
            cur = sections.setdefault(h2.group(2), (h2.group(1), []))
        elif cur:
            cur[1].append(line.rstrip())
    return sections


def paragraphs(lines):
    return [p.strip().replace("\n", " ") for p in "\n".join(lines).split("\n\n") if p.strip()]


# Where each photo sits in the desktop mosaic (column / row / span), from about.md's notes.
# On phones the mosaic is two columns; "wide" photos span both.
MOSAIC = {
    "england":     ("1 / 1 / span 2 / span 2", "wide"),
    "woodworking": ("1 / 3 / span 2 / span 1", ""),
    "sourdough":   ("1 / 4 / span 1 / span 1", ""),
    "van":         ("1 / 5 / span 2 / span 1", ""),
    "cooking":     ("2 / 4 / span 1 / span 1", ""),
    "travel":      ("3 / 1 / span 1 / span 2", "wide"),
    "cats":        ("3 / 3 / span 1 / span 1", ""),
    "epcot":       ("3 / 4 / span 1 / span 2", ""),
}


def original(src):
    """The uncropped version of an About photo, if there is one. Prefers the
    web-sized copy in web/ (made by tools/resize-about-photos.sh) over the
    full-size file in originals/."""
    for folder in ("web", "originals"):
        o = Path(src).parent / folder / Path(src).name
        if (ROOT / o).is_file():
            return str(o)
    return src


LAZY = ' loading="lazy"'


def outside_photos(photos, style):
    """The Outside of work photos as a mosaic, or as an auto-scrolling strip."""
    esc = html.escape
    if style == "mosaic":
        cells = []
        for alt, src in photos:
            area, wide = MOSAIC.get(Path(src).stem, ("auto", ""))
            cells.append(f'<figure class="{wide}" style="grid-area: {area}">'
                         f'{img_tag(original(src), alt, prefix="")}</figure>')
        return f'<div class="mosaic">{"".join(cells)}</div>'
    # The strip holds two copies of the photos and slides left by one copy,
    # so the loop is seamless. The second copy is hidden from screen readers.
    def copy(hidden):
        attr = ' aria-hidden="true"' if hidden else ""
        return (f'<div class="marquee-set"{attr}>' + "".join(
            # Not lazy: photos waiting off to the side of the strip would never load.
            f'<figure>{img_tag(original(src), "" if hidden else alt, prefix="").replace(LAZY, "")}</figure>'
            for alt, src in photos) + "</div>")
    return f'<div class="marquee"><div class="marquee-track">{copy(False)}{copy(True)}</div></div>'


def about(meta, body, photo_style="mosaic"):
    esc = html.escape
    sec = about_sections(body)

    intro = paragraphs(sec.get("intro", ("", []))[1])
    # Only the first sentence is the large opening line; the rest of that
    # paragraph reads as body text.
    if intro:
        first, _, rest = intro[0].partition(". ")
        intro[:1] = [first + "."] + ([rest] if rest else [])
    photo = meta.get("page_photo")
    photo_html = (f'<img class="about-photo" src="{esc(photo)}" alt="{esc(meta.get("page_photo_alt", ""))}">'
                  if photo and (ROOT / photo).is_file() else "")

    values_label, value_lines = sec.get("values", ("", []))
    cards, cur = [], None
    for line in value_lines:
        h3 = re.match(r"^###\s+(.*)$", line)
        if h3:
            cur = [h3.group(1), []]
            cards.append(cur)
        elif cur and line.strip():
            cur[1].append(line.strip())
    values = "".join(f'<li><h3>{inline(t)}</h3><p>{inline(" ".join(p))}</p></li>' for t, p in cards)

    def dates(d):
        return f'<span class="label">{esc(d)}</span>' if known(d) else ""
    jobs = "".join(
        f'<li><b>{esc(j["company"])}</b><span>{esc(j["role"])}<small>{esc(j.get("note", ""))}</small></span>'
        f'{dates(j.get("dates"))}</li>' for j in meta.get("page_experience", []))

    t = meta.get("page_testimonial") or {}
    testimonial = ""
    if isinstance(t, dict) and known(t.get("quote")):
        who = " · ".join(x for x in (t.get("name"), t.get("role")) if known(x))
        testimonial = f"""
  <section class="wrap about-section">
    <p class="label">Kind words</p>
    <blockquote class="pull"><p>{inline(t["quote"])}</p><cite class="label">{esc(who)}</cite></blockquote>
  </section>"""

    outside_label, outside_lines = sec.get("outside", ("", []))
    outside_text = [l for l in outside_lines if l.strip() and not l.startswith("![")]
    photos = [(m.group(1), m.group(2))
              for m in (re.match(r"!\[(.*?)\]\((.*?)\)", l) for l in outside_lines if l.startswith("!["))
              if m and exists(m.group(2))]
    photos_html = outside_photos(photos, photo_style) if photos else ""

    c = meta.get("page_contact") or {}
    email = c.get("email") if known(c.get("email")) else EMAIL
    resume = c.get("resume") if known(c.get("resume")) and (ROOT / c["resume"]).is_file() else RESUME
    links = [f'<li><a href="mailto:{esc(email)}">{esc(email)}</a></li>']
    if known(c.get("linkedin")):
        links.append(f'<li><a href="{esc(c["linkedin"])}">LinkedIn</a></li>')
    links.append(f'<li><a href="{esc(resume)}">Résumé</a></li>')

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>About — Jason Frade</title>{'<meta name="robots" content="noindex">' if photo_style != "mosaic" else ""}
<meta name="description" content="{esc(meta.get("meta_description", ""))}">
<link rel="icon" href="favicon.ico">
{FONTS}
<link rel="stylesheet" href="css/site.css?v={CSS_VERSION}">
</head>
<body>

{nav("")}

<main>
  <header class="wrap about-intro{" has-photo" if photo_html else ""}">
    <div>
      <h1 class="label">{esc(meta.get("title", "About"))}</h1>
      {"".join(f"<p>{inline(p)}</p>" for p in intro)}
    </div>
    {photo_html}
  </header>

  <section class="wrap about-section">
    <p class="label">{esc(values_label)}</p>
    <ul class="values">{values}</ul>
  </section>

  <section class="wrap about-section">
    <p class="label">Experience</p>
    <ul class="experience">{jobs}</ul>
  </section>
{testimonial}
  <section class="wrap about-section about-outside">
    <p class="label">{esc(outside_label)}</p>
    <div>
      {"".join(f"<p>{inline(l)}</p>" for l in outside_text)}
    </div>
    {photos_html if photo_style == "mosaic" else ""}
  </section>
  {photos_html if photo_style != "mosaic" else ""}

  <section class="wrap about-section about-contact">
    <p class="label">Contact</p>
    <div>
      <h2>{esc(c.get("heading") or "Get in touch")}</h2>
      <ul class="links">{"".join(links)}</ul>
    </div>
  </section>
</main>

{FOOTER}
</body>
</html>
"""


def build():
    OUT.mkdir(exist_ok=True)
    projects = []
    for md in sorted(CONTENT.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        _, fm, body = text.split("---", 2)
        meta = parse_front_matter(fm)
        chapters = parse_body(body)
        projects.append((meta, chapters))
    projects.sort(key=lambda p: p[0].get("order", 99))
    for i, (meta, chapters) in enumerate(projects):
        # Each case study links to the next one, wrapping back to the first.
        nxt = projects[(i + 1) % len(projects)][0] if len(projects) > 1 else None
        nxt = (f'{nxt["slug"]}.html', nxt["title"]) if nxt else None
        out = OUT / f'{meta["slug"]}.html'
        out.write_text(page(meta, chapters, nxt), encoding="utf-8")
        print(f"built {out.relative_to(ROOT)}  ({len(chapters)} chapters)")
    projects = [m for m, _ in projects]
    (ROOT / "index.html").write_text(home(projects), encoding="utf-8")
    print(f"built index.html  ({len(projects)} projects)")

    about_md = ROOT / "content" / "about.md"
    if about_md.is_file():
        _, fm, body = about_md.read_text(encoding="utf-8").split("---", 2)
        meta = parse_front_matter(fm)
        (ROOT / "about.html").write_text(about(meta, body), encoding="utf-8")
        # Preview only, not linked anywhere: the same page with a scrolling photo strip.
        (ROOT / "about-scroll.html").write_text(about(meta, body, photo_style="scroll"), encoding="utf-8")
        print("built about.html (and the about-scroll.html preview)")

    if MISSING:
        print("\nLeft out because the image isn't in images/ yet:")
        for src in dict.fromkeys(MISSING):
            print(f"  {src}")


if __name__ == "__main__":
    build()
