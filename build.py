#!/usr/bin/env python3
"""Static site generator for the Dr. Giuseppe Colombo website.

Usage:  python3 build.py            -> writes the site into ./dist
Serve:  python3 -m http.server -d dist 8000
"""
import json
import math
import os
import random
import re
import shutil
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup

import content as C
import hashlib

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
SCRAPED = ROOT.parent / "scraped" / "html"          # only needed to refresh data/journal.json
JOURNAL_JSON = ROOT / "data" / "journal.json"

env = Environment(
    loader=FileSystemLoader(ROOT / "templates"),
    autoescape=select_autoescape(["html"]),
    trim_blocks=True,
    lstrip_blocks=True,
)

# ----------------------------------------------------------------- drawings
DRAWINGS = {}
for f in (ROOT / "data" / "drawings").glob("*.json"):
    DRAWINGS[f.stem] = json.loads(f.read_text())


def drawing(key, cls="", mode="enter", fill=False, label=""):
    """Inline SVG for one of the doctor's line drawings."""
    d = DRAWINGS[key]
    aria = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    if fill:
        body = f'<path d="{" ".join(d["paths"])}" fill="currentColor" fill-rule="evenodd"/>'
    else:
        body = "".join(f'<path d="{p}"/>' for p in d["paths"])
    return (
        f'<svg class="ln {cls}" viewBox="0 0 {d["w"]} {d["h"]}" data-draw="{mode}" '
        f'preserveAspectRatio="xMidYMid meet" {aria}><g>{body}</g></svg>'
    )


env.globals["drawing"] = lambda *a, **k: Markup(drawing(*a, **k))


def doctor_svg():
    """Dr. Colombo's line portrait, aligned over Portrait A (1483×1920).
    Alignment (glasses on glasses) measured on the original files."""
    d = DRAWINGS["doctor"]
    body = "".join(f'<path d="{p}"/>' for p in d["paths"])
    return (
        '<svg class="ln doc__lines" viewBox="0 0 1483 1920" data-draw="scene" aria-hidden="true">'
        f'<g transform="translate(199 0) scale(0.744)">{body}</g></svg>'
    )


env.globals["doctor_svg"] = lambda *a, **k: Markup(doctor_svg(*a, **k))


# ------------------------------------------------- generated illustrations
def anatomy_svg():
    """Cross-section of the facial soft tissues: skin, fat, SMAS, deep layer.
    Layers named after Dr. Colombo's own facelift article."""
    rnd = random.Random(7)
    W = 1000

    def wave(y, amp, n, phase=0.0, x0=0, x1=W, steps=60):
        pts = []
        for i in range(steps + 1):
            x = x0 + (x1 - x0) * i / steps
            yy = y + amp * math.sin(phase + n * math.pi * 2 * i / steps)
            pts.append((x, yy))
        d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
        for x, yy in pts[1:]:
            d += f" L{x:.1f} {yy:.1f}"
        return d

    skin = [wave(100, 5, 3, 0.4), wave(122, 4, 3, 0.9)]
    fat = []
    y = 160
    row = 0
    while y < 268:
        x = 18 + (row % 2) * 20
        while x < W - 10:
            r = rnd.uniform(12, 19)
            cx, cy = x + rnd.uniform(-3, 3), y + rnd.uniform(-3, 3)
            fat.append(f"M{cx - r:.1f} {cy:.1f} a{r:.1f} {r * 0.82:.1f} 0 1 0 {2 * r:.1f} 0 a{r:.1f} {r * 0.82:.1f} 0 1 0 {-2 * r:.1f} 0")
            x += 2 * r + rnd.uniform(4, 9)
        y += 36
        row += 1
    smas = [wave(300, 3, 2, 0.2), wave(334, 3, 2, 0.5)]
    for i in range(46):
        x = 12 + i * 21.5
        smas.append(f"M{x:.1f} {306:.1f} L{x + 14:.1f} {328:.1f}")
    deep = [wave(392, 10, 2.5, 1.2)]
    for i in range(7):
        x = 70 + i * 135
        yb = 392 + 10 * math.sin(1.2 + 2.5 * math.pi * 2 * x / W)
        deep.append(f"M{x:.1f} {yb:.1f} q 18 22 46 30")
    deep += [wave(446, 6, 1.5, 0.3), wave(460, 6, 1.5, 0.3)]
    for k in range(5):
        deep.append(wave(500 + k * 12, 3, 1, k * 0.6))

    def g(cls, paths):
        return f'<g class="{cls}">' + "".join(f'<path d="{p}"/>' for p in paths) + "</g>"

    return (
        f'<svg class="anat" viewBox="0 0 {W} 570" aria-hidden="true">'
        + g("layer layer-skin", skin)
        + g("layer layer-fat", fat)
        + g("layer layer-smas", smas)
        + g("layer layer-deep", deep)
        + "</svg>"
    )


def lake_svg():
    """Line illustration of Lake Lugano: mountains, horizon, reflections, lights."""
    rnd = random.Random(3)
    mountains = (
        "M0 352 C 120 340 220 312 300 262 C 352 228 382 168 418 150 C 446 160 470 214 508 252 "
        "C 566 304 668 330 782 338 C 902 344 1004 318 1104 290 C 1204 260 1296 236 1396 246 "
        "C 1478 254 1548 276 1600 292"
    )
    ridge = "M560 330 C 640 300 720 296 800 312 M1150 300 C 1220 270 1300 262 1380 270"
    horizon = "M0 380 L1600 380"
    refl = []
    for _ in range(70):
        y = rnd.uniform(400, 590)
        w = rnd.uniform(18, 140) * (1 - (y - 400) / 380)
        x = rnd.uniform(0, 1600 - w)
        refl.append(f'<path class="refl" d="M{x:.0f} {y:.0f} h{w:.0f}" style="opacity:{rnd.uniform(.25, .8):.2f}"/>')
    lights = []
    for _ in range(46):
        x = rnd.choice([rnd.uniform(860, 1180), rnd.uniform(1240, 1520), rnd.uniform(120, 300)])
        y = 376 - rnd.uniform(0, 26) * (1 if x > 800 else 0.5)
        lights.append(f'<circle class="light" cx="{x:.0f}" cy="{y:.0f}" r="{rnd.uniform(1.4, 2.6):.1f}"/>')
    return (
        '<svg class="lake" viewBox="0 0 1600 600" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
        '<defs><clipPath id="skyclip"><rect x="0" y="0" width="1600" height="379"/></clipPath></defs>'
        '<circle class="sun" cx="1180" cy="170" r="30" clip-path="url(#skyclip)"/>'
        f'<path class="mount" d="{mountains}"/><path class="mount ridge" d="{ridge}"/>'
        f'<path class="horizon" d="{horizon}"/>' + "".join(refl) + "".join(lights) + "</svg>"
    )


env.globals["anatomy_svg"] = lambda *a, **k: Markup(anatomy_svg(*a, **k))
env.globals["lake_svg"] = lambda *a, **k: Markup(lake_svg(*a, **k))

# ---------------------------------------------------------------- languages
import content_de
import content_it

LANGS = ["it", "de", "en"]
MODS = {"it": content_it, "de": content_de, "en": C}


def g(mod, name):
    """Language value with English fallback."""
    return getattr(mod, name, getattr(C, name))


def fmt_date(iso, lang):
    y, m, d = iso.split("-")
    month = g(MODS[lang], "MONTHS")[int(m) - 1]
    return f"{int(d)}. {month} {y}" if lang == "de" else f"{int(d)} {month} {y}"


# ------------------------------------------------------------------ journal
def load_journal():
    """Journal articles. Read from data/journal.json (committed), so the build works
    anywhere (e.g. Cloudflare). If the original scrape is present, refresh the JSON from it."""
    if not SCRAPED.exists():
        return json.loads(JOURNAL_JSON.read_text(encoding="utf-8"))
    from bs4 import BeautifulSoup
    arts = []
    for slug, (en_title, cat) in C.JOURNAL_EN_TITLES.items():
        f = SCRAPED / f"{slug}.html"
        soup = BeautifulSoup(f.read_text(encoding="utf-8"), "html.parser")
        it_title = soup.find("meta", property="og:title")["content"].replace(" - Giuseppe Colombo", "").strip()
        published = soup.find("meta", property="article:published_time")["content"][:10]
        body = soup.select_one(".entry-content")
        blocks = []
        for el in body.find_all(["p", "h2", "h3", "h4", "ul", "ol"]):
            if el.name in ("ul", "ol"):
                if el.find_parent(["ul", "ol"]):
                    continue
                items = [li.get_text(" ", strip=True) for li in el.find_all("li")]
                items = [i for i in items if i]
                if items:
                    blocks.append({"t": "list", "items": items})
                continue
            if el.find_parent(["ul", "ol"]):
                continue
            text = re.sub(r"\s+([,.;:])", r"\1", el.get_text(" ", strip=True))
            if not text:
                continue
            if el.name != "p" or (len(text) < 70 and not text.endswith((".", ":", "?", "!"))):
                blocks.append({"t": "h", "text": text})
            else:
                blocks.append({"t": "p", "text": text})
        if blocks and blocks[0]["t"] == "h":
            blocks = blocks[1:]
        words = sum(len(b.get("text", " ".join(b.get("items", []))).split()) for b in blocks)
        excerpt = next((b["text"] for b in blocks if b["t"] == "p"), "")
        excerpt = (excerpt[:220].rsplit(" ", 1)[0] + "…") if len(excerpt) > 220 else excerpt
        arts.append({"slug": slug, "it_title": it_title, "category": cat, "date": published,
                     "blocks": blocks, "minutes": max(1, round(words / 220)), "excerpt": excerpt})
    arts.sort(key=lambda a: a["date"], reverse=True)
    JOURNAL_JSON.write_text(json.dumps(arts, ensure_ascii=False, indent=0), encoding="utf-8")
    return arts


# -------------------------------------------------------------------- build
def write(path, html):
    out = DIST / path.lstrip("/")
    if path.endswith("/"):
        out = out / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


def lang_data(lang, base_journal):
    M = MODS[lang]
    P = g(M, "PATHS")
    slugs = g(M, "PROC_SLUGS")
    procs = {}
    for key, base in C.PROCEDURES.items():
        p = dict(base)
        p.update(g(M, "PROCEDURES").get(key, {}) if M is not C else {})
        p["key"] = key
        p["slug"] = slugs[key]
        p["href"] = P[base["area"]] + slugs[key] + "/"
        procs[key] = p
    areas = {}
    for key, base in C.AREAS.items():
        a = dict(base)
        if M is not C:
            a.update(g(M, "AREAS").get(key, {}))
        titles = a.get("group_titles") or [x["title"] for x in base["groups"]]
        a["slug"] = key
        a["href"] = P[key]
        a["groups"] = [{"title": titles[i], "items": [procs[k] for k in grp["items"]]} for i, grp in enumerate(base["groups"])]
        areas[key] = a
    titles = g(M, "JOURNAL_TITLES")
    journal = []
    for a in base_journal:
        x = dict(a)
        x["title"] = titles.get(a["slug"]) or a["it_title"]
        x["date_fmt"] = fmt_date(a["date"], lang)
        x["href"] = P["journal"] + a["slug"] + "/"
        journal.append(x)
    courses = []
    for yi, y in enumerate(C.COURSES):
        ly = g(M, "COURSES")[yi]
        courses.append({"year": y["year"], "place": ly["place"],
                        "items": [dict(it, **ly["items"][ii]) for ii, it in enumerate(y["items"])]})
    vids = g(M, "VIDEOS")
    nav = [{"label": g(M, "NAV_LABELS")[k], "href": P[k]} for k in ["philosophy", "face", "breast", "academy", "contact"]]
    return dict(M=M, P=P, procs=procs, areas=areas, journal=journal, courses=courses, vids=vids, nav=nav)


SITE_URL = os.environ.get("SITE_URL", C.SITE["url"]).rstrip("/")


def asset_version():
    """Short content hash of CSS/JS, appended as ?v= so browsers and Cloudflare can cache them long."""
    h = hashlib.sha1()
    for f in sorted((ROOT / "assets").rglob("*")):
        if f.suffix in (".css", ".js"):
            h.update(f.read_bytes())
    return h.hexdigest()[:10]


env.globals["v"] = asset_version()
env.globals["site_url"] = SITE_URL

# Old WordPress URLs -> new URLs (301). Same-path URLs are omitted.
REDIRECTS = [
    ("/giuseppe-colombo-chirugo-plastico/", "/filosofia/"),
    ("/curriculum-vitae-dr-giuseppe-colombo/", "/filosofia/"),
    ("/chirurgia-plastica-viso/", "/viso/"),
    ("/medicina-estetica-viso/", "/viso/acido-ialuronico/"),
    ("/chirurgia-plastica-seno/", "/seno/"),
    ("/area-scientifica/", "/academy/"),
    ("/attivita-scientifica-e-libri/", "/academy/#publications"),
    ("/eventi-passati/", "/academy/#courses"),
    ("/eventi-futuri-fellowship-2/", "/academy/#fellowship"),
    ("/atlante-di-chirurgia-plastica-ed-estetica/", "/academy/#atlas"),
    ("/blog/", "/academy/journal/"),
    ("/blog/page/*", "/academy/journal/"),
    ("/category/chirurgia-plastica/", "/academy/journal/"),
    ("/author/giuseppecolombo/", "/academy/journal/"),
    ("/video-dr-giuseppe-colombo/", "/academy/#videos"),
    ("/colombo-chirurgia-plastica-savona/", "/contatti/"),
    ("/gallery/", "/academy/#courses"),
    ("/protezione-dei-dati/", "/contatti/"),
    ("/liposuzione-laser-liposuzione-tessuto-adiposo-grasso/", "/academy/journal/il-tessuto-adiposo-anatomia-e-patologia-come-trattarlo-le-diverse-metodiche-di-liposuzione/"),
    ("/en/dr-giuseppe-colombo/", "/en/philosophy/"),
    ("/en/plastic-surgery/", "/en/face/"),
    ("/en/aesthetic-medicine/", "/en/face/hyaluronic-acid/"),
    ("/en/breast-cosmetic-surgery/", "/en/breast/"),
    ("/en/reconstructive-surgery/", "/en/reconstructive/"),
    ("/en/science-area/", "/en/academy/"),
    ("/en/past-events/", "/en/academy/#courses"),
    ("/en/future-events-and-fellowships/", "/en/academy/#fellowship"),
    ("/en/gallery/", "/en/academy/#courses"),
    ("/en/video/", "/en/academy/#videos"),
    ("/feed/", "/academy/journal/"),
    ("/en/feed/", "/en/academy/journal/"),
]

HEADERS = """/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
  Permissions-Policy: camera=(), microphone=(), geolocation=(), interest-cohort=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https://i.ytimg.com; font-src 'self'; frame-src https://www.youtube-nocookie.com https://maps.google.com https://www.google.com; connect-src 'self'; base-uri 'self'; form-action 'self' mailto:; frame-ancestors 'self'

/assets/fonts/*
  Cache-Control: public, max-age=31536000, immutable

/assets/vendor/*
  Cache-Control: public, max-age=31536000, immutable

/assets/css/*
  Cache-Control: public, max-age=31536000, immutable

/assets/js/*
  Cache-Control: public, max-age=31536000, immutable

/assets/img/*
  Cache-Control: public, max-age=2592000
"""


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(ROOT / "assets", DIST / "assets")
    sym = DRAWINGS["symbol"]
    (DIST / "assets" / "img" / "favicon.svg").write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {sym["w"]} {sym["h"]}">'
        f'<path fill="#1B1A18" fill-rule="evenodd" d="{" ".join(sym["paths"])}"/></svg>'
    )
    base_journal = load_journal()
    D = {lang: lang_data(lang, base_journal) for lang in LANGS}

    # page id -> url in every language (for the language switcher and hreflang)
    def urls(pid):
        out = {}
        for lang in LANGS:
            d = D[lang]
            kind, _, key = pid.partition(":")
            if kind == "proc":
                out[lang] = d["procs"][key]["href"]
            elif kind == "article":
                out[lang] = d["P"]["journal"] + key + "/"
            else:
                out[lang] = d["P"][kind]
        return out

    written = []

    def render(lang, tpl, pid, **ctx):
        d = D[lang]
        M = d["M"]
        alts = urls(pid)
        ui = g(M, "UI")
        site = g(M, "SITE")
        html = env.get_template(tpl).render(
            lang=lang, t=ui, h=g(M, "HOME"), P=d["P"], nav=d["nav"], site=site, quotes=g(M, "QUOTES"),
            alts=alts, current=ctx.pop("current", alts[lang]), year=date.today().year,
            js_i18n=json.dumps(ui["js"], ensure_ascii=False), **ctx)
        write(alts[lang], html)
        written.append(alts[lang])

    for lang in LANGS:
        d = D[lang]
        M = d["M"]
        ui = g(M, "UI")
        sfx = ui["suffix"]
        site = g(M, "SITE")

        render(lang, "home.html", "home", procs=d["procs"], atlas=g(M, "ATLAS"), locations=site["locations"],
               title=ui["home_title"], meta=ui["home_meta"], body_class="page-home")

        for key, area in d["areas"].items():
            render(lang, "area.html", key, area=area, groups=area["groups"],
                   title=f"{area['title']} — {sfx}", meta=area["meta"], body_class="page-area")
            flat = [p for grp in area["groups"] for p in grp["items"]]
            for idx, p in enumerate(flat):
                art = next((a for a in d["journal"] if a["slug"] == p["article"]), None)
                render(lang, "procedure.html", "proc:" + p["key"], p=p, area=area,
                       siblings=[s for s in flat if s["key"] != p["key"]], index=idx + 1, article=art,
                       videos=[(v, d["vids"][v]) for v in p["videos"]],
                       title=f"{p['title']} ({p['subtitle']}) — {sfx}", meta=p["meta"],
                       current=area["href"], body_class="page-procedure")

        rec = g(M, "RECONSTRUCTIVE")
        render(lang, "reconstructive.html", "reconstructive", r=rec, area=d["areas"]["face"],
               title=f"{rec['title']} — {sfx}", meta=rec["meta"], current=d["P"]["face"], body_class="page-procedure")

        render(lang, "philosophy.html", "philosophy", about=g(M, "ABOUT"), milestones=g(M, "MILESTONES"),
               cv=g(M, "CV_GROUPS"), videos=[(v, d["vids"][v]) for v in ["rIZn6oLeCpI", "-9COFP65Fl8"]],
               title=f"{ui['phil_title']} — {sfx}", meta=ui["phil_meta"], body_class="page-philosophy")

        render(lang, "academy.html", "academy", atlas=g(M, "ATLAS"), fellowship=g(M, "FELLOWSHIP"),
               courses=d["courses"], courses_early=g(M, "COURSES_EARLY"), pubs=C.PUBLICATIONS,
               journal=d["journal"][:3], videos=list(d["vids"].items()),
               title=f"{g(M, 'NAV_LABELS')['academy']} — {sfx}", meta=ui["acad_meta"], body_class="page-academy")

        cats = sorted({a["category"] for a in d["journal"]})
        render(lang, "journal.html", "journal", journal=d["journal"], cats=cats,
               title=f"Journal — {sfx}", meta=ui["journal_meta"], current=d["P"]["academy"], body_class="page-journal")
        proc_by_article = {}
        for p in d["procs"].values():
            if p["article"]:
                proc_by_article.setdefault(p["article"], p)
        for a in d["journal"]:
            others = [o for o in d["journal"] if o["slug"] != a["slug"]][:2]
            render(lang, "article.html", "article:" + a["slug"], a=a, others=others,
                   proc=proc_by_article.get(a["slug"]), title=f"{a['title']} — {sfx}", meta=a["excerpt"],
                   current=d["P"]["academy"], body_class="page-article")

        render(lang, "contact.html", "contact", locations=site["locations"],
               title=f"{ui['contact_title']} — {sfx}", meta=ui["contact_meta"], body_class="page-contact")

    # 404 (Italian, at the root — the server's default error page)
    d = D["it"]
    M = d["M"]
    ui = g(M, "UI")
    html = env.get_template("404.html").render(
        lang="it", t=ui, h=g(M, "HOME"), P=d["P"], nav=d["nav"], site=g(M, "SITE"), quotes=g(M, "QUOTES"),
        alts={l: D[l]["P"]["home"] for l in LANGS}, current="", year=date.today().year,
        js_i18n=json.dumps(ui["js"], ensure_ascii=False), title=f"{ui['nf_title']} — {ui['suffix']}", meta="",
        body_class="page-404")
    write("/404.html", html)

    sm = "".join(f"<url><loc>{SITE_URL}{u}</loc></url>" for u in written)
    write("/sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>')
    write("/robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    # Cloudflare (Pages and Workers static assets) read these two files from the output root
    write("/_redirects", "".join(f"{a} {b} 301\n" for a, b in REDIRECTS))
    write("/_headers", HEADERS)
    print(f"Built {len(written)} pages ({len(written) // len(LANGS)} per language) + 404 into {DIST}")


if __name__ == "__main__":
    main()
