#!/usr/bin/env python3
"""Builds every page of the site from the data below, so all pages share one
header, one card, one project template. Run from the repo root:

    python3 tools/build.py

Edit the text here, not in the generated .html files (they are overwritten).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EMAIL = "dilafazan@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/dianalafazan/"
BEHANCE = "https://www.behance.net/dilafazan"
CV_BRAND = "assets/Diana-Lafazan-CV-Brand-Designer.pdf"
CV_UX = "assets/Diana-Lafazan-CV-UX-UI-Designer.pdf"

# ── Projects ────────────────────────────────────────────────────────────────
# slides: (alt text) for each assets/img/projects/<slug>/NN.jpg, in order.
PROJECTS = {
    "automotor": dict(
        title="Automotor",
        card_tag="Website · 2025",
        card_line="Nine vehicle brands, rebuilt around what each visitor came to do.",
        cover="card-automotor.jpg",
        eyebrow="Website · Framer build · live in production",
        h1="Nine vehicle brands, three audiences, and a site built for none of them.",
        lede="Automotor is Paraguay’s multi-brand vehicle group. Its site was a full-screen brand carousel with no menu: no route to book a service, no way to find a branch. I mapped who actually arrives (buyers, owners and authorized workshops), took two structural questions back to the client, then designed the site in Figma and built it in Framer myself.",
        decision="<strong>The decision I’d defend:</strong> navigation named by intent, not by department (“¡Quiero el mío!”, “Soy cliente”, “Talleres”), with the two logins kept separate so nobody has to identify themselves before the site can help them. I still maintain the site, and the group has since given me Carmotor, Empedril and BOGA.",
        facts=[("Client", "Automotor Paraguay (Grupo BOGA)"), ("Year", "2025"),
               ("Role", "Sole designer: research, IA, UI, Framer build"), ("Scope", "9 brands · 21 branch pages · 4 cities")],
        live=("automotor.com.py", "https://automotor.com.py"),
        behance="https://www.behance.net/gallery/232098707/Automotor-Paraguay-Multi-Brand-Dealership-Platform",
        slides=["The redesigned Automotor site on desktop and phone",
                "The brief: one site for nine brands and three kinds of visitor",
                "Before: the 2022 brand carousel with no visible menu",
                "Research: who arrives at automotor.com.py and what they came to do",
                "The audience map that reorganized the site",
                "Navigation named by intent",
                "Branch pages with three sets of opening hours",
                "The branch page system: 21 pages, four cities"],
    ),
    "showtime": dict(
        title="Showtime Boxing",
        card_tag="Campaign · 2023",
        card_line="A pay-per-view campaign system, from countdown to fight night.",
        cover="card-showtime.jpg",
        eyebrow="Campaign & broadcast · Malka Media",
        h1="Spence Jr vs Crawford: selling a pay-per-view over a month, not a night.",
        lede="July 29, 2023: two unbeaten champions, one undisputed welterweight title, sold on Showtime pay-per-view. Fans had to feel the fight getting closer every week, and every live stream had to look like the same event.",
        decision="<strong>The decision I’d defend:</strong> treat it as a system, not a poster. Countdowns, fighter stats, live-stream slates and result cards in every format, with win and loss versions ready before fight night, so the only live step was dropping in a photo.",
        facts=[("Client", "Showtime PPV & Premier Boxing Champions, via Malka Media"), ("Year", "2023"),
               ("Role", "Senior designer, in a design team of three at Malka Media"), ("Scope", "Countdown, live-stream slates and fight-week social")],
        live=None,
        behance="https://www.behance.net/gallery/255116029/Spence-Jr-vs-Crawford-Showtime-PPV-Campaign",
        slides=["Spence Jr vs Crawford key art",
                "The brief: two unbeaten champions, one undisputed title",
                "Fight-week countdown",
                "The campaign system across formats",
                "Live-stream slates",
                "Stream graphics on the night"],
    ),
    "america-coffee": dict(
        title="America Coffee Co.",
        card_tag="Packaging · 2024",
        card_line="A label system that lets 22 designs cover 44 SKUs.",
        cover="card-america.jpg",
        eyebrow="Rebrand & packaging · in production",
        h1="22 coffees, 44 SKUs, one system on the shelf.",
        lede="America Coffee Co. is a U.S. coffee brand that needed a rebrand able to carry its whole line: 8 blends and 14 single origins, each sold whole bean and ground. Every bag had to read as one company, and a shopper still had to find their coffee at a glance.",
        decision="<strong>The decision I’d defend:</strong> whole bean and ground differ by a single line of text, so 22 designs cover all 44 SKUs. When the line grew to pods and 5 lb bags, the system took them with no new rules.",
        facts=[("Client", "America Coffee Co."), ("Year", "2024"),
               ("Role", "Sole designer: identity, label system, production files"), ("Scope", "22 coffees × 2 formats = 44 SKUs")],
        live=None,
        behance="https://www.behance.net/gallery/197494519/America-Coffee-Company",
        slides=["The America Coffee line, blends and single origins side by side",
                "The brief",
                "One label, built from fixed and variable parts",
                "Dark for the 8 blends, cream for the 14 single origins",
                "The format is one line of text, so 22 designs cover 44 SKUs",
                "Pods and 5 lb bags, with no new rules",
                "The full line"],
    ),
    "empedril": dict(
        title="Empedril",
        card_tag="Website · 2024",
        card_line="A 1971 agro group, presented as one family.",
        cover="card-empedril.jpg",
        eyebrow="Website · Framer build · live since February 2024",
        h1="A family agro group that read like four companies.",
        lede="Empedril has farmed the same Paraguayan land since 1971, across agriculture, livestock, real estate and finance. Four business lines and two audiences made it read like a conglomerate with no center. It needed to read as one family.",
        decision="<strong>The decision I’d defend:</strong> real photographs of the company’s own fields, no generated images, because the site’s whole argument is “this land is ours.” When the developer left the day before launch, I rebuilt the site myself in Framer in 24 hours and launched on schedule.",
        facts=[("Client", "Empedril (J3 group)"), ("Launched", "February 2024"),
               ("Role", "Sole designer: art direction, IA, UI, photo direction, Framer build"), ("Scope", "Corporate site · 4 business lines")],
        live=("empedril.com.py", "https://empedril.com.py"),
        behance="https://www.behance.net/gallery/232097089/Empedril-Corporate-Site-for-a-Family-Agro-Group",
        slides=["The Empedril site on desktop and phone",
                "The brief: one family, four business lines",
                "Leading with the family and its history",
                "Photography of the company’s own land"],
    ),
    "ueno": dict(
        title="ueno Bank",
        card_tag="Brand launch · 2021–23",
        card_line="Launching a digital bank across screens, cards and billboards.",
        cover="card-ueno.jpg",
        video=("ueno-logo-animation.mp4", "ueno-logo-still.jpg", "ueno logo animation: the wordmark draws itself like flowing water"),
        eyebrow="Brand launch · in-house team",
        h1="Launching a bank: countdown, event, motion and every screen in town.",
        lede="ueno is a Paraguayan digital bank. As a senior designer on the in-house team, I designed its launch: the countdown campaign, the event invitation and screens, and the manifesto. I animated the logo from the brand’s idea that it flows like water.",
        decision="Then the identity had to hold everywhere at once: animated billboards in 18 sizes at 15 locations, Visa cards, ATMs and print.",
        facts=[("Client", "ueno Bank (Grupo Vázquez)"), ("Years", "2021–2023"),
               ("Role", "Senior designer, in-house team"), ("Scope", "Launch campaign, event screens, motion, brand rollout")],
        live=None,
        behance="https://www.behance.net/gallery/151566793/ueno-Bank-Brand-Campaigns",
        slides=["ueno launch countdown", "The launch teaser", "The ueno logo", "The launch event invitation"],
    ),
    "stephen-a-smith": dict(
        title="The Stephen A. Smith Show",
        card_tag="Broadcast · 2023",
        card_line="One weekly package, a new guest cast every episode.",
        cover="card-sas.jpg",
        eyebrow="Weekly series design · Malka Media",
        h1="A new guest cast every week, one lockup that never moves.",
        lede="The Stephen A. Smith Show is a weekly sports and culture show produced by Malka Media for YouTube and podcast. I designed the episodic graphics package across a season: thumbnails, on-screen name plates and social assets. The constraint was cadence and click-through: a new episode every week, and a thumbnail that had to earn the click in a feed.",
        decision="<strong>The decision I’d defend:</strong> twelve consecutive episodes from one master file. The purple field and the show lockup never move; the guest cutouts are rebuilt weekly. Consistency is the product; the variation is the work.",
        facts=[("Client", "The Stephen A. Smith Show, via Malka Media"), ("Year", "2023"),
               ("Role", "Senior designer, as part of Malka Media’s design team"), ("Scope", "Weekly thumbnails, podcast art, name plates")],
        live=None,
        behance="https://www.behance.net/gallery/255116809/The-Stephen-A-Smith-Show-Weekly-Series-Design",
        slides=["The Stephen A. Smith Show thumbnails",
                "The system: one master file",
                "Special episodes",
                "The channel view",
                "Square social assets",
                "On-screen name plates"],
    ),
}

ALL = ["automotor", "showtime", "america-coffee", "empedril", "ueno", "stephen-a-smith"]
BRAND = ["showtime", "ueno", "america-coffee", "stephen-a-smith"]
DIGITAL = ["automotor", "empedril"]


# ── Shared pieces ───────────────────────────────────────────────────────────
def page(title, description, body, pre):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="stylesheet" href="{pre}assets/css/site.css">
</head>
<body>
<!-- Generated by tools/build.py: edit the text there, not here. -->
{body}
<footer class="site-footer">
  <div class="wrap"><span>© 2026 Diana Lafazan</span><span>Austin, TX · English &amp; Español</span></div>
</footer>
</body>
</html>
"""


def header(home):
    """home: where the name links. On the role pages it links to the page itself,
    so a recruiter sent to /brand stays on the brand story."""
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand-name" href="{home}">Diana Lafazan</a>
    <nav class="site-nav" aria-label="Main">
      <a href="{home}#work">Work</a>
      <a href="{home}#about">About</a>
      <a class="cta" href="{home}#contact">Contact</a>
    </nav>
  </div>
</header>"""


def card(slug, pre):
    p = PROJECTS[slug]
    if "video" in p:
        mp4, still, label = p["video"]
        media = (f'<video autoplay muted loop playsinline preload="metadata" poster="{pre}assets/img/{still}" aria-label="{label}">'
                 f'<source src="{pre}assets/img/{mp4}" type="video/mp4"></video>'
                 f'<img class="still" src="{pre}assets/img/{still}" alt="{label}">')
    else:
        media = f'<img src="{pre}assets/img/{p["cover"]}" alt="{p["title"]} project cover" loading="lazy">'
    return f"""      <a class="card" href="{pre}work/{slug}.html">
        <div class="thumb">{media}</div>
        <div class="meta"><h3>{p["title"]}</h3><span class="tag">{p["card_tag"]}</span></div>
        <p>{p["card_line"]}</p>
        <span class="go">View project →</span>
      </a>"""


def grid(slugs, pre):
    return '    <div class="grid">\n' + "\n".join(card(s, pre) for s in slugs) + "\n    </div>"


def hero(eyebrow, h1, lede, cv, pre):
    return f"""  <section class="hero">
    <div class="wrap">
      <div class="stack" style="gap: 22px;">
        <span class="eyebrow">{eyebrow}</span>
        <h1>{h1}</h1>
        <p class="lede">{lede}</p>
        <p class="note">Open to full-time roles, hybrid or remote. U.S. permanent resident, no sponsorship needed.</p>
        <div class="btn-row" style="padding-top: 6px;">
          <a class="btn primary" href="#work">See the work</a>
          <a class="btn" href="{pre}{cv}" download>Download CV</a>
        </div>
      </div>
      <figure class="portrait">
        <img src="{pre}assets/img/diana.jpg" alt="Diana Lafazan working on a laptop by a window">
      </figure>
    </div>
  </section>"""


def numbers(items):
    cells = "\n".join(f"      <div><b>{b}</b><span>{s}</span></div>" for b, s in items)
    return f'    <section class="numbers" aria-label="At a glance">\n{cells}\n    </section>'


def how(steps):
    cells = "\n".join(f"      <div><h3>{h}</h3><p>{t}</p></div>" for h, t in steps)
    return f'    <section class="section"><div class="how" aria-label="How I work">\n{cells}\n    </div></section>'


ABOUT_PARAS = [
    "Packaging and 3D renders early on, then brand systems and national campaigns at agencies in Asunción. After that came two years as senior designer at ueno Bank, then broadcast design in California at Malka Media. Now I design and ship websites end to end, and I still do the brand work.",
    "That path wasn’t a detour. Industrial design taught me to work inside real constraints. A master’s in art direction taught me to hold a whole system in view at once. Campaign work taught me to make something land in three seconds.",
    "I work in English and Spanish, and most of my career has meant translating between markets as much as between languages.",
]
EDU = """        <div class="edu">
          <span><strong>2021</strong> · Master’s in Art Direction, Barcelona H. School of Design</span>
          <span><strong>2020</strong> · Industrial Design, Graphic Design specialization, National University of Asunción</span>
          <span><strong>In progress</strong> · Google UX Design Certificate</span>
        </div>"""


def about(rows):
    paras = "\n".join(f"        <p>{p}</p>" for p in ABOUT_PARAS)
    cells = "\n".join(f"          <div><b>{b}</b><span>{s}</span></div>" for b, s in rows)
    return f"""    <section class="section about" id="about">
      <div class="stack">
        <h2>About me</h2>
{paras}
      </div>
      <div class="stack">
        <h2>What I do</h2>
        <div class="rows">
{cells}
        </div>
{EDU}
      </div>
    </section>"""


def contact(h2, cv_buttons, pre):
    btns = "\n".join(f'          <a class="btn white" href="{pre}{path}" download>{label}</a>' for label, path in cv_buttons)
    return f"""    <section class="hire" id="contact">
      <div class="stack" style="gap: 20px;">
        <h2>{h2}</h2>
        <p>Austin, Texas · hybrid or remote · full-time · English &amp; Español. I reply the same day.</p>
        <div class="btn-row">
          <a class="btn primary" href="mailto:{EMAIL}">{EMAIL}</a>
{btns}
          <a class="btn" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
          <a class="btn" href="{BEHANCE}" target="_blank" rel="noopener">Behance</a>
        </div>
      </div>
      <div class="rows">
        <div><span>Based in</span><b>Austin, TX</b></div>
        <div><span>Setup</span><b>Hybrid or remote</b></div>
        <div><span>Authorization</span><b>U.S. permanent resident</b></div>
        <div><span>Sponsorship</span><b>Not required</b></div>
      </div>
    </section>"""


def work_section(title, note, slugs, pre, extra=""):
    return f"""    <section class="section" id="work">
      <div class="section-head"><h2>{title}</h2><span>{note}</span></div>
{grid(slugs, pre)}{extra}
    </section>"""


# ── Pages ───────────────────────────────────────────────────────────────────
ROWS_ALL = [("Brand identity", "Systems, type, color, guidelines"), ("Packaging &amp; print", "Labels, SKU systems, production files"),
            ("Campaign &amp; broadcast", "Social, out-of-home, live graphics"), ("Web design", "Research, IA, flows, UI in Figma"),
            ("Front-end build", "Framer, shipped and maintained"), ("AI in my workflow", "Claude, Claude Code, generated imagery")]
ROWS_BRAND = [("Brand identity", "Systems, type, color, guidelines"), ("Packaging &amp; print", "Labels, SKU systems, production files"),
              ("Campaign &amp; motion", "Social, out-of-home, broadcast, animation"), ("3D &amp; product", "Renders in Rhino and KeyShot"),
              ("AI imagery", "Generated and art-directed, where a shoot can’t go"), ("Tools", "Illustrator, Photoshop, InDesign, After Effects")]
ROWS_DIGITAL = [("Research", "Audience mapping, flows, usability testing"), ("UX &amp; IA", "Information architecture, navigation, wireframes"),
                ("UI &amp; systems", "Responsive UI, components, accessibility"), ("Build", "Framer: production sites and CMS page systems"),
                ("AI in my workflow", "Claude and Claude Code, Figma AI, generated imagery"), ("Visual", "Brand identity, art direction, motion")]

HOW_DIGITAL = [("01 · Ask who arrives", "Every project starts by mapping who lands here against what they came to do. On Automotor that surfaced three groups with almost nothing in common."),
               ("02 · Send the hard questions back", "Structural questions go to the client before any screen exists, because the answer changes the navigation. Two of them reshaped the Automotor menu."),
               ("03 · Own it to production", "I design in Figma and build in Framer myself, so I’m accountable for how it behaves in a browser, not just how it looks in a file.")]
HOW_BRAND = [("01 · Read the brand first", "On Showtime I worked from what the network had already published, and put the invention into structure and pacing rather than new styles."),
             ("02 · Design the system, then the piece", "22 label designs cover 44 SKUs. Win and loss templates exist before fight night. The system does the repetitive work so the craft goes where it shows."),
             ("03 · Own it to production", "Production files for every SKU, billboards in 18 sizes, walls measured on site. I’m accountable for how it looks in the world, not just in the file.")]


def build_home():
    body = "\n".join([
        header("./"),
        "<main>",
        hero("Brand &amp; digital designer · Austin, TX · English &amp; Español",
             "I design brands and ship the websites that carry them.",
             "Identity, packaging, campaigns and broadcast on one side. On the other, websites I design in Figma, then build and launch in Framer myself. Thirteen years, two markets, two languages.",
             CV_BRAND, ""),
        '  <div class="wrap">',
        numbers([("13 years", "Brand, campaign, banking, broadcast and web"), ("4 companies", "One client group, two and a half years, since March 2024"),
                 ("44 SKUs", "America Coffee label system, in production"), ("21 branches", "One page system across four cities")]),
        work_section("Selected work", "Brand and digital, six projects", ALL, ""),
        how(HOW_DIGITAL[:2] + [("03 · Own it to production", "A live site I built myself, a coffee line on the shelf, a launch on every screen in town. I’m accountable for how it works in the world, not just in the file.")]),
        about(ROWS_ALL),
        contact("Hiring someone who can design the brand and get the site live?",
                [("CV · Brand &amp; graphic", CV_BRAND), ("CV · UX/UI &amp; web", CV_UX)], ""),
        "  </div>",
        "</main>",
    ])
    return page("Diana Lafazan — Brand &amp; Digital Designer",
                "Diana Lafazan designs brands and ships the websites that carry them. Brand, packaging and campaign work, plus websites built and launched in Framer. Austin, TX.",
                body, "")


def build_role(kind):
    pre = "../"
    if kind == "brand":
        h = hero("Brand &amp; graphic designer · Austin, TX · English &amp; Español",
                 "Brands that hold together on the shelf, on screen and on the street.",
                 "Thirteen years of identity, packaging, campaign and broadcast design in the U.S. and Latin America. I do my best work inside a brand, at volume: a pay-per-view campaign in every format, a bank’s launch across 18 billboard sizes, a 44-SKU coffee line.",
                 CV_BRAND, pre)
        nums = numbers([("13 years", "Brand, campaign and broadcast design"), ("44 SKUs", "From 22 label designs, one system"),
                        ("18 sizes", "Of animated billboard for ueno’s launch"), ("7 accounts", "At once, as part of Malka Media’s design team")])
        work = work_section("Brand work", "Campaign, broadcast, launch and packaging", BRAND, pre)
        rest = [how(HOW_BRAND), about(ROWS_BRAND),
                contact("Looking for a designer who keeps the brand right at volume?", [("Download CV", CV_BRAND)], pre)]
        title, desc = "Diana Lafazan — Brand &amp; Graphic Designer", "Brand, packaging, campaign and broadcast design by Diana Lafazan: Showtime, ueno Bank, America Coffee, The Stephen A. Smith Show."
    else:
        h = hero("UX/UI &amp; web designer · Austin, TX · English &amp; Español",
                 "I design websites around what people came to do, and ship them myself.",
                 "Research, information architecture and UI in Figma, then built, launched and maintained in Framer, with no handoff. Four production sites for one client group since 2024, on top of 13 years of brand and campaign design.",
                 CV_UX, pre)
        nums = numbers([("4 sites", "One client group, since March 2024"), ("21 branches", "One page template, four cities"),
                        ("9 brands", "One navigation, built by intent"), ("24 hours", "To rebuild Empedril and launch on schedule")])
        also = ('\n      <p class="also">Also for the same group: <a href="https://carmotor.com.py" target="_blank" rel="noopener">Carmotor ↗</a>, '
                "heavy machinery and trucks, with quote and service-booking routes; and the BOGA holding group’s site, with art-directed generated imagery.</p>")
        work = work_section("Digital work", "Researched, designed and built by me", DIGITAL, pre, also)
        rest = [how(HOW_DIGITAL), about(ROWS_DIGITAL),
                contact("Need a site designed and live, not just designed?", [("Download CV", CV_UX)], pre)]
        title, desc = "Diana Lafazan — UX/UI &amp; Web Designer", "Websites researched, designed and built in Framer by Diana Lafazan: Automotor and Empedril."
    body = "\n".join([header("./"), "<main>", h, '  <div class="wrap">', nums, work, *rest, "  </div>", "</main>"])
    return page(title, desc, body, pre)


BACK_SCRIPT = """<script>
  // "Back" returns to whichever page sent the visitor (home, /brand or /digital).
  document.querySelector('[data-back]').addEventListener('click', function (e) {
    if (document.referrer && new URL(document.referrer).origin === location.origin) { e.preventDefault(); history.back(); }
  });
</script>"""


def build_project(slug):
    p = PROJECTS[slug]
    pre = "../"
    facts = "\n".join(f'        <div><span class="eyebrow">{k}</span><span>{v}</span></div>' for k, v in p["facts"])
    buttons = []
    if p["live"]:
        buttons.append(f'<a class="btn primary" href="{p["live"][1]}" target="_blank" rel="noopener">Visit {p["live"][0]} ↗</a>')
    buttons.append(f'<a class="btn" href="{p["behance"]}" target="_blank" rel="noopener">Full project on Behance ↗</a>')
    btns = "\n        ".join(buttons)

    figs = []
    for i, alt in enumerate(p["slides"], 1):
        figs.append(f'      <img src="{pre}assets/img/projects/{slug}/{i:02d}.jpg" alt="{alt}" loading="{"eager" if i == 1 else "lazy"}">')
        if i == 1 and "video" in p:
            mp4, still, label = p["video"]
            figs.append(f'      <figure><video autoplay muted loop playsinline preload="metadata" poster="{pre}assets/img/{still}" aria-label="{label}">'
                        f'<source src="{pre}assets/img/{mp4}" type="video/mp4"></video><figcaption>The logo animation.</figcaption></figure>')
    slides = "\n".join(figs)

    body = f"""{header("../")}
<main class="wrap">
  <section class="project-head">
    <a class="back" href="../#work" data-back>← Back</a>
    <span class="eyebrow">{p["eyebrow"]}</span>
    <h1>{p["h1"]}</h1>
    <p class="lede">{p["lede"]}</p>
    <p class="decision">{p["decision"]}</p>
    <div class="facts">
{facts}
    </div>
    <div class="btn-row">
        {btns}
    </div>
  </section>
  <section class="slides" aria-label="Project images">
{slides}
  </section>
  <div class="project-foot">
    <a class="back" href="../#work" style="margin: 0;">← All work</a>
    <div class="btn-row">
        {btns}
    </div>
  </div>
</main>
{BACK_SCRIPT}"""
    return page(f"{p['title']} — Diana Lafazan", p["card_line"], body, pre)


REDIRECT = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Work — Diana Lafazan</title>
<meta http-equiv="refresh" content="0; url=../#work"><link rel="canonical" href="../#work"></head>
<body><a href="../#work">Diana Lafazan — work</a></body></html>
"""


def main():
    out = {
        "index.html": build_home(),
        "brand/index.html": build_role("brand"),
        "digital/index.html": build_role("digital"),
        "work/index.html": REDIRECT,
    }
    for slug in PROJECTS:
        out[f"work/{slug}.html"] = build_project(slug)
    for path, html in out.items():
        f = ROOT / path
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(html, encoding="utf-8")
        print("wrote", path)


if __name__ == "__main__":
    main()
