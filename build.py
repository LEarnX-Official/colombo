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

# ------------------------------------------------------------- monogram
def monogram(cls=""):
    """The 'Luce' monogram: an arch (a window of light) holding the initials GC."""
    return Markup(
        f'<span class="mono {cls}" aria-hidden="true"><svg viewBox="0 0 40 52"><path d="M2 51 V20 A18 18 0 0 1 38 20 V51"/></svg><b>GC</b></span>'
    )


env.globals["monogram"] = monogram


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
    (DIST / "assets" / "img" / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#F7F2EC"/>'
        '<path d="M14 56V28a18 18 0 0 1 36 0v28" fill="none" stroke="#A9834F" stroke-width="2.5"/>'
        '<text x="32" y="47" text-anchor="middle" font-family="Georgia,serif" font-style="italic" font-size="19" fill="#2E211C">GC</text></svg>'
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
            lang=lang, t=ui, h=g(M, "HOME"), L=g(M, "LUCE"), P=d["P"], nav=d["nav"], site=site, quotes=g(M, "QUOTES"),
            concerns=C.CONCERNS, proc_concern=C.PROC_CONCERN, procs_all=d["procs"],
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
               rec=g(M, "RECONSTRUCTIVE"),
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
        lang="it", t=ui, h=g(M, "HOME"), L=g(M, "LUCE"), P=d["P"], nav=d["nav"], site=g(M, "SITE"), quotes=g(M, "QUOTES"),
        concerns=C.CONCERNS, proc_concern=C.PROC_CONCERN, procs_all=d["procs"],
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
