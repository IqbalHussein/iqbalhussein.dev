#!/usr/bin/env python3
"""Builds the portfolio as static HTML.

Edit the content below, then run:  python3 build.py
Output: index.html, about.html, contact.html, work/<slug>.html
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent

NAME = "Iqbal Hussein"
EMAIL = "iqbalabdishakur15@gmail.com"
GITHUB = "https://github.com/IqbalHussein"

# ---------------------------------------------------------------------------
# Pictograms. Each is drawn on a 120 x 120 grid. Strokes use the ink colour,
# anything with class "s" uses the signal colour.
# ---------------------------------------------------------------------------
MARKS = {
    "pitch": """
      <rect x="10" y="22" width="100" height="76"/>
      <line x1="60" y1="22" x2="60" y2="98"/>
      <circle cx="60" cy="60" r="10"/>
      <rect x="90" y="40" width="20" height="40"/>
      <circle class="dot" cx="74" cy="36" r="3.4"/>
      <circle class="dot" cx="70" cy="76" r="3.4"/>
      <circle class="dot" cx="78" cy="84" r="3.4"/>
      <circle class="hollow" cx="100" cy="48" r="3.4"/>
      <circle class="hollow" cx="88" cy="62" r="3.4"/>
      <circle class="hollow" cx="100" cy="74" r="3.4"/>
      <circle class="s fill" cx="76" cy="52" r="3.8"/>""",
    "scope": """
      <circle cx="60" cy="60" r="46"/>
      <line x1="14" y1="60" x2="106" y2="60"/>
      <line x1="60" y1="14" x2="60" y2="106"/>
      <circle cx="60" cy="60" r="23"/>
      <g class="s fill">
        <circle cx="72" cy="44" r="2.2"/><circle cx="78" cy="40" r="2.2"/>
        <circle cx="68" cy="50" r="2.2"/><circle cx="82" cy="34" r="2.2"/>
        <circle cx="75" cy="48" r="2.2"/><circle cx="64" cy="54" r="2.2"/>
        <circle cx="86" cy="38" r="2.2"/><circle cx="70" cy="38" r="2.2"/>
        <circle cx="79" cy="46" r="2.2"/><circle cx="62" cy="58" r="2.2"/>
      </g>""",
    "week": """
      <line x1="8" y1="100" x2="112" y2="100"/>
      <rect x="12" y="62" width="10" height="38" class="fill"/>
      <rect x="26" y="44" width="10" height="56"/>
      <rect x="40" y="70" width="10" height="30" class="fill"/>
      <rect x="54" y="30" width="10" height="70" class="s fill"/>
      <rect x="68" y="30" width="10" height="70" class="s"/>
      <rect x="82" y="80" width="10" height="20"/>
      <rect x="96" y="96" width="10" height="4" class="fill"/>""",
    "sequence": """
      <rect x="8" y="12" width="24" height="14"/>
      <rect x="48" y="12" width="24" height="14"/>
      <rect x="88" y="12" width="24" height="14"/>
      <line x1="20" y1="26" x2="20" y2="110" class="dash"/>
      <line x1="60" y1="26" x2="60" y2="110" class="dash"/>
      <line x1="100" y1="26" x2="100" y2="110" class="dash"/>
      <path d="M20 42 H58 M53 38 L58 42 L53 46"/>
      <path class="s" d="M60 58 H98 M93 54 L98 58 L93 62"/>
      <path d="M100 74 H62 M67 70 L62 74 L67 78"/>
      <path d="M60 90 H22 M27 86 L22 90 L27 94"/>""",
    "venn": """
      <circle cx="46" cy="60" r="32"/>
      <circle cx="74" cy="60" r="32"/>
      <path class="s fill" d="M60 31.2 A32 32 0 0 1 60 88.8 A32 32 0 0 1 60 31.2 Z"/>""",
    "uml": """
      <rect x="36" y="10" width="48" height="34"/>
      <line x1="36" y1="22" x2="84" y2="22"/>
      <rect x="8" y="76" width="44" height="34"/>
      <line x1="8" y1="88" x2="52" y2="88"/>
      <rect x="68" y="76" width="44" height="34"/>
      <rect x="68" y="76" width="44" height="12" class="s fill"/>
      <path d="M30 76 V60 H90 V76 M60 60 V52"/>
      <path class="tri" d="M54 52 L60 44 L66 52 Z"/>""",
    "calendar": """
      <rect x="10" y="18" width="100" height="84"/>
      <line x1="10" y1="32" x2="110" y2="32"/>
      <g class="thin">
        <line x1="24.3" y1="32" x2="24.3" y2="102"/><line x1="38.6" y1="32" x2="38.6" y2="102"/>
        <line x1="52.9" y1="32" x2="52.9" y2="102"/><line x1="67.1" y1="32" x2="67.1" y2="102"/>
        <line x1="81.4" y1="32" x2="81.4" y2="102"/><line x1="95.7" y1="32" x2="95.7" y2="102"/>
        <line x1="10" y1="49.5" x2="110" y2="49.5"/><line x1="10" y1="67" x2="110" y2="67"/>
        <line x1="10" y1="84.5" x2="110" y2="84.5"/>
      </g>
      <rect class="s fill" x="10" y="32" width="14.3" height="17.5"/>
      <rect class="s fill" x="38.6" y="32" width="14.3" height="17.5"/>
      <rect class="s fill" x="52.9" y="67" width="14.3" height="17.5"/>
      <rect class="s fill" x="67.1" y="67" width="14.3" height="17.5"/>""",
}

# ---------------------------------------------------------------------------
# Projects, in the order they appear.
# ---------------------------------------------------------------------------
PROJECTS = [
    dict(
        slug="pitchscanner", title="PitchScanner", mark="pitch",
        short="Sketch a football situation and find the real match moments that look most like it.",
        lede=("Place the ball, the attackers and the defenders on a pitch, and PitchScanner searches "
              "StatsBomb's open 360 data, about 1.3 million frames from 426 matches, for the closest "
              "real situations. Then it shows what those moments led to: how often they produced a "
              "shot, how much xG they were worth, how often possession was lost."),
        points=[
            "Every outcome comes with a confidence interval and the baseline for that part of the pitch, so a claim that a shape is dangerous can be checked.",
            "Filters are written in plain language, like “Bayern at home, last fifteen minutes, trailing”. Rules parse them first; a model is only a fallback.",
            "Situations are encoded three ways (grid, polar and tactical) and searched with pgvector.",
            "The query path is built for a 150 ms p95.",
        ],
        stack="Python, FastAPI, Postgres with pgvector, React, TypeScript",
        live="https://pitchscanner.vercel.app",
        demo="Moving a player and the ball, opening a real match on the pitch, and filtering in plain language.",
        repo="https://github.com/IqbalHussein/pitchscanner",
    ),
    dict(
        slug="apricity", title="Apricity", mark="scope",
        short="Colour grading in the browser. Describe a look in words and see every adjustment it makes.",
        lede=("Type a look such as “cold, desaturated noir” and an on-device agent turns it into "
              "explicit colour adjustments. Each change is listed with the reason for it and a link to "
              "the control, so you can take over by hand. Nothing is uploaded: rendering, the agent "
              "and storage all run in your browser."),
        points=[
            "Two stages kept apart: correction (exposure, white balance, log camera profiles), then the grade.",
            "Waveform, RGB parade and vectorscope.",
            "Lift, gamma and gain wheels, eight-band HSL, curves, split tone, grain and LUTs.",
            "Works offline as an installable app, and falls back to the CPU without WebGPU.",
        ],
        stack="Rust, WebAssembly, WebGPU, Solid.js, TypeScript",
        live="https://iqbalhussein.github.io/Apricity/",
        demo="Describing a look in words, reading why each change was made, then adjusting saturation by hand and checking the scopes.",
        repo="https://github.com/IqbalHussein/Apricity",
    ),
    dict(
        slug="protohybrid", title="ProtoHybrid", mark="week",
        short="Plan lifting and running as one training week, with warnings when they clash.",
        lede=("Lifting apps and running apps don't know about each other. ProtoHybrid puts runs and "
              "lifts on one weekly plan, shows each day's load, and flags the clashes you set rules "
              "for, such as heavy legs within 24 hours of a hard run."),
        points=[
            "Drag sessions to reschedule, and compare what was planned with what happened.",
            "Log sets against an exercise library, with routines, a rest timer and personal records.",
            "Pulls busy time from Google Calendar so training fits around everything else.",
            "Sign in with a one-time email link.",
        ],
        stack="Next.js, TypeScript, Supabase, Postgres",
        live="https://protohybrid.vercel.app",
        repo="https://github.com/IqbalHussein/protohybrid",
    ),
    dict(
        slug="mycelium", title="Mycelium", mark="sequence",
        short="A Chrome DevTools panel that draws your app's network calls as a live sequence diagram.",
        lede=("The Network tab lists requests in time order, which makes it hard to see which action "
              "set off which chain of API calls. Mycelium captures fetch and XHR traffic, drops static "
              "assets, and draws the flow between the browser and each service as a sequence diagram "
              "that updates as you use the page."),
        points=[
            "Click an arrow in the diagram to see that request's headers and status.",
            "Pause the diagram to study a complicated flow without it moving.",
            "Updates are batched every 500 ms so the diagram doesn't flicker.",
            "Follows the DevTools light or dark theme.",
        ],
        stack="TypeScript, React, Mermaid, Chrome extension APIs",
        live=None,
        repo="https://github.com/IqbalHussein/mycelium",
    ),
    dict(
        slug="cvsyncai", title="CVSyncAI", mark="venn",
        short="Rank job postings against a resume and see which skills match and which are missing.",
        lede=("CVSyncAI pulls the skills out of job postings, from a vocabulary of about 250 across "
              "software, finance, healthcare, law and more, and ranks the postings against a resume. "
              "The score blends skill overlap with semantic similarity; the weighting was tuned on a "
              "hand-labelled benchmark against keyword, TF-IDF and embedding-only baselines."),
        points=[
            "Shows matched and missing skills, with the line of the posting that mentions each one.",
            "Suggests resources for the missing skills.",
            "Drafts a cover letter for a chosen posting and exports it as a PDF.",
            "Runs from the command line or as a Streamlit web app.",
        ],
        stack="Python, spaCy, sentence-transformers, scikit-learn, Streamlit",
        live=None,
        repo="https://github.com/IqbalHussein/cv-sync-ai",
    ),
    dict(
        slug="java-to-uml", title="Java to UML", mark="uml",
        short="Drop in Java files and get a UML class diagram back.",
        lede=("Upload .java files and the app parses them with an ANTLR grammar, works out visibility, "
              "abstract members, inheritance and composition, and draws the class diagram. Standard "
              "library types like ArrayList and HashMap are left out, so the diagram shows only your code."),
        points=[
            "Upload several files at once by dragging them in.",
            "Pan and zoom around large diagrams.",
            "Export as SVG or as a high-resolution PNG.",
        ],
        stack="Next.js, TypeScript, ANTLR4, Mermaid",
        demo="Choosing six Java files, generating the class diagram, then zooming and panning around it.",
        live=None,
        repo="https://github.com/IqbalHussein/UML-generator",
    ),
    dict(
        slug="room-booker", title="Room Booker", mark="calendar",
        short="Books a Carleton library study room every night, on a fixed weekly schedule.",
        lede=("Study rooms at Carleton's library fill up fast. This service runs every night in Docker "
              "and books the same room seven days ahead. It reads slot times from the booking system's "
              "own availability data instead of guessing from the page, and refuses to click if the "
              "two disagree."),
        points=[
            "Every run ends as succeeded, skipped, unavailable or failed. A room that's already taken isn't a failure.",
            "Failures name the step that broke and what the booker actually saw.",
            "Slot matching and parsing are unit-tested against recorded responses, without a browser.",
        ],
        stack="Java, Spring Boot, Selenium, Docker",
        live=None,
        repo="https://github.com/IqbalHussein/room-booking-system",
    ),
]

# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;600&display=swap" rel="stylesheet">')

FAVICON = ("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'>"
           "<rect width='32' height='32' fill='%239E1A1F'/><circle cx='16' cy='16' r='8' fill='none' "
           "stroke='white' stroke-width='3'/></svg>")


def mark(name, cls="mark", label=None):
    aria = f'role="img" aria-label="{escape(label)}"' if label else 'aria-hidden="true"'
    return f'<svg class="{cls}" viewBox="0 0 120 120" {aria}>{MARKS[name]}</svg>'


def host(url):
    return url.split("//", 1)[1].rstrip("/")


def page(title, body, prefix="", current=None, description=None, home=False):
    nav = []
    for label, href in (("Work", "work.html"), ("About", "about.html"), ("Contact", "contact.html")):
        cur = ' aria-current="page"' if current == label else ""
        nav.append(f'<a href="{prefix}{href}"{cur}>{label.lower()}</a>')
    desc = escape(description or f"{NAME} builds software. Selected projects, with live sites and source code.")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{FAVICON}">
{FONTS}
<link rel="stylesheet" href="{prefix}styles.css">
</head>
<body{' class="is-home"' if home else ''}>
<header class="top">
  {'<span></span>' if home else f'<a class="wordmark" href="{prefix}index.html">{NAME.lower()}</a>'}
  <nav aria-label="Main">{''.join(nav)}</nav>
</header>
{body}
{'' if home else f"""<footer class="foot">
  <a href="mailto:{EMAIL}">{EMAIL}</a>
  <a href="{GITHUB}">GitHub</a>
</footer>"""}
</body>
</html>
"""


def links(p):
    out = []
    if p["live"]:
        out.append(f'<a class="ext" href="{p["live"]}">Open {escape(host(p["live"]))}</a>')
    out.append(f'<a class="ext" href="{p["repo"]}">Source on GitHub</a>')
    return "".join(out)


def build_index():
    first, last = NAME.split(" ", 1)
    body = f"""
<main class="home">
  <h1 class="home-name">{escape(first.lower())}<br>{escape(last.lower())}</h1>
  <div class="home-actions">
    <a class="btn btn-solid" href="mailto:{EMAIL}">Email me</a>
    <a class="btn" href="{GITHUB}">GitHub</a>
  </div>
</main>"""
    return page(NAME, body, home=True)


def build_work():
    rows = []
    for p in PROJECTS:
        rows.append(f"""
    <li class="row">
      <a class="row-main" href="work/{p['slug']}.html">
        {mark(p['mark'])}
        <span class="row-title">{escape(p['title'])}</span>
        <span class="row-short">{escape(p['short'])}</span>
      </a>
      <span class="row-links">{links(p)}</span>
    </li>""")
    body = f"""
<main class="work-page">
  <h1>work</h1>
  <ol class="index" aria-label="Projects">{''.join(rows)}
  </ol>
</main>"""
    return page(f"Work \u2014 {NAME}", body, current="Work")


def build_project(i):
    p = PROJECTS[i]
    prev_p = PROJECTS[i - 1]
    next_p = PROJECTS[(i + 1) % len(PROJECTS)]
    points = "".join(f"<li>{escape(x)}</li>" for x in p["points"])
    status = "Live" if p["live"] else "Source code"
    demo = ""
    if p.get("demo"):
        demo = f"""
  <figure class="demo">
    <video src="../media/{p['slug']}.mp4" poster="../media/{p['slug']}.jpg" autoplay muted loop playsinline
      preload="metadata" aria-label="Demo of {escape(p['title'])}: {escape(p['demo'])}"></video>
    <figcaption>{escape(p['demo'])}</figcaption>
  </figure>"""
    body = f"""
<main class="project">
  <div class="project-figure">{mark(p['mark'], 'mark mark-large', label=p['title'] + ' pictogram')}</div>
  <header class="project-head">
    <h1>{escape(p['title'])}</h1>
    <p class="lede">{escape(p['lede'])}</p>
    <div class="actions">{links(p)}</div>
  </header>{demo}
  <section class="project-body">
    <dl class="facts">
      <dt>Built with</dt><dd>{escape(p['stack'])}</dd>
      <dt>Status</dt><dd>{status}</dd>
    </dl>
    <h2>What it does</h2>
    <ul class="points">{points}</ul>
  </section>
  <nav class="pager" aria-label="More projects">
    <a href="{prev_p['slug']}.html"><span>Previous</span>{escape(prev_p['title'])}</a>
    <a href="{next_p['slug']}.html"><span>Next</span>{escape(next_p['title'])}</a>
  </nav>
</main>
<script>
  // Videos play on their own unless the visitor prefers reduced motion; a click pauses or resumes.
  document.querySelectorAll('.demo video').forEach(function (v) {{
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) {{ v.removeAttribute('autoplay'); v.pause(); v.controls = true; return; }}
    v.addEventListener('click', function () {{ v.paused ? v.play() : v.pause(); }});
  }});
</script>"""
    return page(f"{p['title']} — {NAME}", body, prefix="../", current="Work", description=p["short"])


def build_about():
    langs = "Python, TypeScript, Rust, Java"
    body = f"""
<main class="prose-page">
  <h1>about</h1>
  <div class="prose">
    <p class="lede">I'm a developer who likes problems where the interesting part is hidden: the shape of a
    football attack, the load of a training week, the chain of requests behind one click.</p>
    <p>Most of what I build tries to make that hidden part visible and checkable. PitchScanner puts a
    confidence interval on every number. Apricity lists every adjustment its agent makes and why.
    Room Booker reports exactly which step failed and what it saw. I'd rather a tool admit what it
    doesn't know than look certain.</p>
    <p>I work across the stack, from data pipelines and search to interfaces, and I like writing the
    benchmark before trusting the result.</p>
    <dl class="facts">
      <dt>Languages</dt><dd>{langs}</dd>
      <dt>Frameworks</dt><dd>FastAPI, Next.js, React, Solid.js, Spring Boot</dd>
      <dt>Data</dt><dd>Postgres, pgvector, Supabase, sentence-transformers, spaCy</dd>
    </dl>
  </div>
</main>"""
    return page(f"About — {NAME}", body, current="About")


def build_contact():
    body = f"""
<main class="prose-page">
  <h1>contact</h1>
  <div class="prose">
    <p class="lede">Email is the best way to reach me.</p>
    <p class="big-link"><a href="mailto:{EMAIL}">{EMAIL.replace("@", "<wbr>@")}</a></p>
    <dl class="facts">
      <dt>GitHub</dt><dd><a href="{GITHUB}">github.com/IqbalHussein</a></dd>
    </dl>
  </div>
</main>"""
    return page(f"Contact — {NAME}", body, current="Contact")


def main():
    (ROOT / "work").mkdir(exist_ok=True)
    (ROOT / "index.html").write_text(build_index())
    (ROOT / "work.html").write_text(build_work())
    (ROOT / "about.html").write_text(build_about())
    (ROOT / "contact.html").write_text(build_contact())
    for i, p in enumerate(PROJECTS):
        (ROOT / "work" / f"{p['slug']}.html").write_text(build_project(i))
    print(f"Built {4 + len(PROJECTS)} pages.")


if __name__ == "__main__":
    main()
