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
import subprocess
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
WIDE_HINTS = ("diagram-", "iterations", "final-panel", "research-styles", "explorations", "ab-test", "concepts", "fit-diagram", "problem-map")


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
    # A bare slug links to that case study, which sits beside this page.
    s = re.sub(r"\[(.+?)\]\(([\w-]+)\)", r'<a href="\2.html">\1</a>', s)
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


# Pages show images at most about 820px wide, so 1640px is sharp on retina
# screens. Anything wider gets a smaller copy in images/web/, which the pages
# use instead; the original stays as it is.
WEB_WIDTH = 1640


def web(src):
    """The web-sized copy of an image, made with sips (part of macOS) the
    first time it's needed and again whenever the original changes."""
    size = image_size(src)
    if not size or size[0] <= WEB_WIDTH:
        return src
    out = Path("images/web") / Path(src).relative_to("images")
    source, target = ROOT / src, ROOT / out
    if not target.is_file() or target.stat().st_mtime < source.stat().st_mtime:
        target.parent.mkdir(parents=True, exist_ok=True)
        quality = ["-s", "formatOptions", "80"] if source.suffix.lower() in (".jpg", ".jpeg") else []
        subprocess.run(["sips", "--resampleWidth", str(WEB_WIDTH), *quality, str(source), "--out", str(target)],
                       check=True, capture_output=True)
    return str(out)



# --- Final design slideshow --------------------------------------------------
# The home page card and the case study hero both show the Final design
# carousel as a slideshow: hovering one of its dots fades to that slide. No
# arrows or thumbnails; the case study's also plays on its own.

CROPS = ROOT / "images" / "web" / "crops.json"

# Final design slides that are labelled boards rather than screens. Their
# labels sit on the cream, so they can't go on a card colour.
SLIDESHOW_SKIP = ("four-jobs",)


def _margin_box(src, tol=10):
    """Where the screenshot sits inside an image composed on a flat
    background, as (left, top, right, bottom), or None if it fills the image.
    Reads the pixels by converting to BMP with sips."""
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        bmp = Path(tmp) / "p.bmp"
        subprocess.run(["sips", "-s", "format", "bmp", str(ROOT / src), "--out", str(bmp)],
                       check=True, capture_output=True)
        d = bmp.read_bytes()
    off, = struct.unpack("<I", d[10:14])
    w, h = struct.unpack("<ii", d[18:26])
    bp = struct.unpack("<H", d[28:30])[0] // 8
    stride = (w * bp + 3) & ~3
    bottom_up = h > 0          # BMP rows run bottom to top unless the height is negative
    w, h = abs(w), abs(h)

    def px(x, y):
        i = off + ((h - 1 - y) if bottom_up else y) * stride + x * bp
        return d[i + 2], d[i + 1], d[i]
    bg = px(2, 2)

    def differs(p):
        return max(abs(a - b) for a, b in zip(p, bg)) > tol
    top = next(y for y in range(h) if any(differs(px(x, y)) for x in range(0, w, 2)))
    bottom = next(y for y in range(h - 1, -1, -1) if any(differs(px(x, y)) for x in range(0, w, 2)))
    left = next(x for x in range(w) if any(differs(px(x, y)) for y in range(0, h, 2)))
    right = next(x for x in range(w - 1, -1, -1) if any(differs(px(x, y)) for y in range(0, h, 2)))
    return left, top, right, bottom, w, h


def screen(src):
    """The image without the cream it was composed on, so only the screenshot
    sits on the card colour. Crops are cached in images/web/."""
    cache = json.loads(CROPS.read_text()) if CROPS.is_file() else {}
    # Keyed on the file's contents, not its date, so switching branches
    # doesn't make every crop look stale.
    digest = hashlib.md5((ROOT / src).read_bytes()).hexdigest()
    changed = cache.get(src, {}).get("md5") != digest
    if changed:
        cache[src] = {"md5": digest, "box": _margin_box(src)}
        CROPS.parent.mkdir(parents=True, exist_ok=True)
        CROPS.write_text(json.dumps(cache, indent=1, sort_keys=True))
    left, top, right, bottom, w, h = cache[src]["box"]
    # Composed images have background on all four sides. A screenshot whose
    # own top bar or edge matches its corner isn't one.
    if min(left, top, w - 1 - right, h - 1 - bottom) < min(w, h) * .02:
        return src
    out = Path("images/web") / Path(src).relative_to("images").with_name(Path(src).stem + "-screen.jpg")
    target = ROOT / out
    if changed or not target.is_file():
        target.parent.mkdir(parents=True, exist_ok=True)
        cw, ch = right - left + 1, bottom - top + 1
        subprocess.run(["sips", "--cropToHeightWidth", str(ch), str(cw),
                        "--cropOffset", str(top), str(left), "-s", "formatOptions", "85",
                        str(ROOT / src), "--out", str(target)], check=True, capture_output=True)
    return str(out)


def final_slides(chapters):
    """The first carousel in the Final design chapter, as (alt, src) pairs."""
    for ch in chapters:
        if ch["id"] != "solution":
            continue
        lines, inside, slides = ch["lines"], False, []
        for line in lines:
            if line == "::carousel":
                inside = True
            elif line == "::/carousel":
                if slides:
                    return slides
                inside = False
            elif inside:
                m = re.match(r"!\[(.*?)\]\((.*?)\)", line)
                if m and (ROOT / m.group(2)).is_file():
                    slides.append((m.group(1), m.group(2)))
    return []


def slideshow(slides, prefix, buttons):
    """Stacked slides that fade into each other, and a dot for each one. Dots
    are buttons on the case study; on a card (itself a link) they only show
    where you are."""
    slides = [(alt, screen(src)) for alt, src in slides if not any(h in src for h in SLIDESHOW_SKIP)]
    imgs = []
    for i, (alt, src) in enumerate(slides):
        cls = "slide is-current" if i == 0 else "slide"
        lazy = "" if i == 0 else ' loading="lazy"'
        # Only the slide showing is read out, or a card's link would read them all.
        hidden = "" if i == 0 else ' aria-hidden="true"'
        imgs.append(f'<img class="{cls}" src="{prefix}{html.escape(web(src))}" alt="{html.escape(alt)}"{hidden}{lazy}>')
    imgs = "".join(imgs)
    if len(slides) < 2:
        return imgs
    if buttons:
        current = ' aria-current="true"'
        dots = "".join(f'<button aria-label="Show screen {i + 1} of {len(slides)}"{current if i == 0 else ""}></button>'
                       for i in range(len(slides)))
        return f'<div class="slides">{imgs}</div><div class="dots">{dots}</div>'
    on = ' class="on"'
    dots = "".join(f'<span{on if i == 0 else ""}></span>' for i in range(len(slides)))
    return f'{imgs}<div class="dots" aria-hidden="true">{dots}</div>'


SLIDESHOW_JS = """<script>
  // Final design slideshows: hovering a dot shows that screen (clicking or
  // focusing one does too, for touch and keyboard). A card remembers its
  // screen so the case study opens on the same one.
  // On the case study the slideshow also plays on its own while it's on
  // screen, pausing while hovered or focused, and not at all with reduced motion.
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.slideshow').forEach(s => {
    const slides = [...s.querySelectorAll('.slide')];
    const dots = [...s.querySelectorAll('.dots > *')];
    if (slides.length < 2) return;
    const key = 'slide-' + s.dataset.key;
    let current = 0, settle = null;
    const show = n => {
      if (n === current) return;
      // The last screen stays visible underneath while the new one fades in,
      // then goes, in case it's taller than the new one.
      slides.forEach((el, i) => {
        el.classList.toggle('was-current', i === current);
        el.classList.toggle('is-current', i === n);
        el.setAttribute('aria-hidden', i !== n);
      });
      clearTimeout(settle);
      settle = setTimeout(() => slides.forEach(el => el.classList.remove('was-current')), 500);
      current = n;
      dots.forEach((d, i) => d.tagName === 'BUTTON' ? d.toggleAttribute('aria-current', i === n)
                                                     : d.classList.toggle('on', i === n));
      try { sessionStorage.setItem(key, n); } catch (e) {}
    };
    try { const saved = +sessionStorage.getItem(key); if (saved && saved < slides.length) show(saved); } catch (e) {}
    let timer = null, visible = false, paused = false;
    const play = () => {
      clearInterval(timer);
      if ('autoplay' in s.dataset && !still && visible && !paused)
        timer = setInterval(() => show((current + 1) % slides.length), 2000);
    };
    dots.forEach((d, i) => ['mouseenter', 'focus', 'click'].forEach(type => d.addEventListener(type, () => { show(i); play(); })));
    const hold = on => () => { paused = on; play(); };
    s.addEventListener('mouseenter', hold(true)); s.addEventListener('mouseleave', hold(false));
    s.addEventListener('focusin', hold(true)); s.addEventListener('focusout', hold(false));
    new IntersectionObserver(([e]) => { visible = e.isIntersecting; play(); }).observe(s);
  });
</script>"""

def img_tag(src, alt, prefix="../"):
    src = web(src)
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
        f'<button class="thumb"><img src="../{web(src)}" alt="Show slide {i + 1}: {html.escape(alt)}" loading="lazy"></button>'
        for i, (alt, src) in enumerate(images))
    return (f'<figure class="carousel wide"><div class="carousel-track" tabindex="0">{slides}</div>'
            f'<div class="carousel-thumbs">{thumbs}</div>'
            f'<div class="carousel-bar"><figcaption aria-live="polite">{inline(images[0][0])}</figcaption>'
            f'<div class="carousel-nav"><span class="label count">1 / {len(images)}</span>'
            f'<button class="prev" aria-label="Previous slide">←</button>'
            f'<button class="next" aria-label="Next slide">→</button></div></div></figure>')


# The sentence that frames each case study, pulled out of its paragraph into a panel.
QUESTION = re.compile(r"^(.*?)\s*That gave us our question: how might we (.*\?)$")


def paragraph(text):
    m = QUESTION.match(text)
    if not m:
        return f"<p>{inline(text)}</p>"
    before = f"<p>{inline(m.group(1))}</p>\n" if m.group(1) else ""
    return (f'{before}<div class="question"><span class="label">The question</span>'
            f'<p>How might we {inline(m.group(2))}</p></div>')


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
        elif line.startswith("#### "):
            blocks.append(("subhead", line[5:].strip()))
            i += 1
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(r"^(>|!\[|- |::|#### )", lines[i]):
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
        elif kind == "subhead":
            out.append(f'<h3 class="subhead">{inline(blocks[j][1])}</h3>')
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
            out.append(paragraph(blocks[j][1]))
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

# GoatCounter site code, from https://<code>.goatcounter.com. Empty means no
# analytics. Visits to a link like jasonfrade.com/?ref=acme show "acme" as the
# referrer, so each job application can get its own link.
GOATCOUNTER = "jafrade"


def analytics():
    if not GOATCOUNTER:
        return ""
    return (f'<script data-goatcounter="https://{GOATCOUNTER}.goatcounter.com/count" '
            'async src="https://gc.zgo.at/count.js"></script>')


def icons(prefix=""):
    """Tab and home-screen icons; make them with tools/make-favicons.py."""
    return (f'<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">\n'
            f'<link rel="icon" href="{prefix}favicon.ico" sizes="any">\n'
            f'<link rel="apple-touch-icon" href="{prefix}apple-touch-icon.png">')


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
    resume = resume_file()
    resume_item = f'<li><a href="{root}{resume}" data-goatcounter-click="resume-nav">Résumé</a></li>' if resume else ""
    return f"""<div class="wrap">
  <nav class="site-nav">
    <a class="mark" href="{home}"><span class="disc"></span>JASON FRADE</a>
    <ul><li><a href="{home}#work">Work</a></li><li><a href="{root}about.html">About</a></li>{resume_item}</ul>
  </nav>
</div>"""


def copy_email(email, text_class=""):
    """The address as a button that copies it, with a copy icon that turns into a check."""
    email = html.escape(email)
    icon = ('<svg class="copy-icon" viewBox="0 0 16 16" aria-hidden="true">'
            '<g class="icon-copy"><rect x="5.5" y="5.5" width="8" height="8" rx="1.5"/>'
            '<path d="M10.5 3.5v-.5a1.5 1.5 0 0 0-1.5-1.5H4A1.5 1.5 0 0 0 2.5 3v5A1.5 1.5 0 0 0 4 9.5h.5"/></g>'
            '<path class="icon-check" d="M3 8.5l3.5 3.5L13 4.5"/></svg>')
    return (f'<button type="button" class="copy-btn {text_class}" data-copy="{email}" '
            f'aria-label="Copy email address, {email}"><span class="copy-text">{email}</span>{icon}</button>'
            f'<span class="sr-only" role="status"></span>')


LINKEDIN = "https://www.linkedin.com/in/jasonfrade/"
LINKEDIN_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.063 2.063 0 1 1 0-4.126 2.063 2.063 0 0 1 0 4.126zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>')


COPY_JS = """<script>
  // Copy buttons. navigator.clipboard only exists over HTTPS, so fall back to
  // execCommand on http, and select the address if neither works.
  document.querySelectorAll('.copy-btn').forEach(b => {
    let timer = null;
    b.addEventListener('click', async () => {
      let ok = false;
      try {
        await navigator.clipboard.writeText(b.dataset.copy);
        ok = true;
      } catch (e) {
        const t = document.createElement('textarea');
        t.value = b.dataset.copy;
        t.setAttribute('readonly', '');
        t.style.cssText = 'position: fixed; opacity: 0';
        document.body.append(t);
        t.select();
        try { ok = document.execCommand('copy'); } catch (e2) {}
        t.remove();
        b.focus();
      }
      if (!ok) {
        getSelection().selectAllChildren(b.querySelector('.copy-text'));
        return;
      }
      b.classList.add('is-copied');
      b.nextElementSibling.textContent = 'Email address copied';
      if (window.goatcounter && goatcounter.count) goatcounter.count({ path: 'copy-email', title: 'Copied email address', event: true });
      clearTimeout(timer);
      timer = setTimeout(() => {
        b.classList.remove('is-copied');
        b.nextElementSibling.textContent = '';
      }, 2000);
    });
  });
</script>"""

FOOTER = f"""<footer class="site-footer">
  <div class="wrap">
    <span class="label">Jason Frade · Senior product designer</span>
    <span class="footer-links">
      {copy_email("jason.a.frade@gmail.com", "label")}
      <a class="footer-icon" href="{LINKEDIN}" data-goatcounter-click="linkedin" target="_blank" rel="noopener" aria-label="LinkedIn profile (opens in a new tab)">{LINKEDIN_ICON}</a>
    </span>
  </div>
</footer>
{COPY_JS}"""


# --- Page -------------------------------------------------------------------

def page(meta, chapters, colour, next_project=None):
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
    overview = meta.get("page_overview") or meta.get("page_subtitle", "")
    slug = esc(meta["slug"])
    slides = final_slides(chapters) or [(meta.get("page_hero_alt") or meta["title"], hero)]
    hero_media = slideshow(slides, "../", buttons=True)
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
<meta name="description" content="{esc(overview)}">
{icons("../")}
{analytics()}
{FONTS}
<link rel="stylesheet" href="../css/site.css?v={CSS_VERSION}">
</head>
<body>

{nav("../")}

<main>
  <header class="cs-hero" style="--c: var(--{colour}); view-transition-name: card-{slug}">
    <div class="wrap">
      <div class="cs-hero-title">
        <p class="label">{esc(meta.get("card_context", ""))}</p>
        <h1 style="view-transition-name: title-{slug}">{esc(meta["title"])}</h1>
      </div>
      <div class="cs-hero-intro">
        <p class="lede">{esc(overview)}</p>
        <ul class="tags">{focus}</ul>
      </div>
      <div class="cs-hero-media slideshow" data-key="{slug}" data-autoplay style="view-transition-name: shot-{slug}">
        {hero_media}
      </div>
    </div>
  </header>

  <div class="wrap">
    <div class="cs-summary">
      <div class="cs-results">
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
    <article class="cs-body" style="--c: var(--{colour})">
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
{SLIDESHOW_JS}
</body>
</html>
"""


# --- Home -------------------------------------------------------------------

def card(meta, colour):
    """A wide card: the story and two results on the left, the work on the
    right, running off the card's edge."""
    esc = html.escape
    focus = "".join(f"<li>{esc(t)}</li>" for t in meta.get("focus", []))
    results = "".join(f'<li><b>{esc(m["value"])}</b><span>{esc(m["label"])}</span></li>'
                      for m in meta.get("page_metrics", [])[:2])
    slug = esc(meta["slug"])
    media = slideshow(meta["_slides"] or [(meta["title"], meta["card_thumbnail"])], "", buttons=False)
    # These names match the case study hero, so the card grows into it.
    return f"""    <a class="project-card" href="work/{slug}.html" style="--c: var(--{colour}); view-transition-name: card-{slug}">
      <div class="info">
        <p class="label">{esc(meta.get("card_context", ""))}</p>
        <h3 style="view-transition-name: title-{slug}">{esc(meta["title"])}</h3>
        <ul class="card-results">{results}</ul>
        <ul class="tags">{focus}</ul>
      </div>
      <div class="stage slideshow" data-key="{slug}" style="view-transition-name: shot-{slug}">{media}</div>
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
{icons()}
{analytics()}
{FONTS}
<link rel="stylesheet" href="css/site.css?v={CSS_VERSION}">
</head>
<body>

{nav("")}

<main>
  <header class="home-hero dotted">
    <div class="wrap">
      <h1>Hi, I’m Jason.</h1>
      <p class="lede">A senior product designer with more than a decade of experience, most recently designing automation and AI agents that take repetitive work off small business teams.</p>
    </div>
  </header>

  <section class="wrap home-work" id="work">
    <div class="projects">
{cards}
    </div>
  </section>

</main>

{FOOTER}
{SLIDESHOW_JS}
</body>
</html>
"""


# --- About ------------------------------------------------------------------

EMAIL = "jason.a.frade@gmail.com"     # used until about.md has a real email
def resume_file():
    """The résumé to link to: the one about.md names, once that file exists.
    Until then there's no Résumé link (the old 2016 PDF stays unlinked)."""
    about_md = ROOT / "content" / "about.md"
    if not about_md.is_file():
        return None
    resume = (parse_front_matter(about_md.read_text(encoding="utf-8").split("---", 2)[1])
              .get("page_contact") or {}).get("resume")
    return resume if known(resume) and (ROOT / resume).is_file() else None


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


def mosaic(photos):
    """The Outside of work photos as a mosaic, placed using MOSAIC."""
    cells = []
    for alt, src in photos:
        area, wide = MOSAIC.get(Path(src).stem, ("auto", ""))
        cells.append(f'<figure class="{wide}" style="grid-area: {area}">'
                     f'{img_tag(original(src), alt, prefix="")}</figure>')
    return f'<div class="mosaic">{"".join(cells)}</div>'


def about(meta, body):
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
    photos_html = mosaic(photos) if photos else ""

    c = meta.get("page_contact") or {}
    email = c.get("email") if known(c.get("email")) else EMAIL
    resume = resume_file()
    links = [f"<li>{copy_email(email)}</li>"]
    if known(c.get("linkedin")):
        links.append(f'<li><a href="{esc(c["linkedin"])}">LinkedIn</a></li>')
    if resume:
        links.append(f'<li><a href="{esc(resume)}" data-goatcounter-click="resume-about">Résumé</a></li>')

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>About — Jason Frade</title>
<meta name="description" content="{esc(meta.get("meta_description", ""))}">
{icons()}
{analytics()}
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
    {photos_html}
  </section>

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
        colour = CARD_COLOURS[i % len(CARD_COLOURS)]   # the same colour as its home page card
        out.write_text(page(meta, chapters, colour, nxt), encoding="utf-8")
        print(f"built {out.relative_to(ROOT)}  ({len(chapters)} chapters)")
    for meta, chapters in projects:
        meta["_slides"] = final_slides(chapters)
    projects = [m for m, _ in projects]
    (ROOT / "index.html").write_text(home(projects), encoding="utf-8")
    print(f"built index.html  ({len(projects)} projects)")

    about_md = ROOT / "content" / "about.md"
    if about_md.is_file():
        _, fm, body = about_md.read_text(encoding="utf-8").split("---", 2)
        meta = parse_front_matter(fm)
        (ROOT / "about.html").write_text(about(meta, body), encoding="utf-8")
        print("built about.html")

    if MISSING:
        print("\nLeft out because the image isn't in images/ yet:")
        for src in dict.fromkeys(MISSING):
            print(f"  {src}")


if __name__ == "__main__":
    build()
