#!/usr/bin/env python3
"""Scraper de https://ao.winrest360.com/ — guarda conteúdo limpo em doc/scraping/."""
from __future__ import annotations
import re
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "doc" / "scraping" / "winrest360-ao"
SITEMAP = "https://ao.winrest360.com/page-sitemap.xml"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
EXCLUDE_RE = re.compile(r"\.(png|jpe?g|svg|gif|webp|ico|pdf)$", re.I)
TODAY = date.today().isoformat()


def fetch(url: str, retries: int = 4) -> str:
    headers = {
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "pt-PT,pt;q=0.9,en;q=0.8",
        "Accept-Encoding": "identity",
        "Referer": "https://ao.winrest360.com/",
        "Connection": "keep-alive",
    }
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=25) as r:
                return r.read().decode("utf-8", errors="replace")
        except Exception as exc:
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise last  # type: ignore[misc]


def list_pages() -> list[str]:
    xml = fetch(SITEMAP)
    urls = re.findall(r"<loc>([^<]+)</loc>", xml)
    return sorted({u for u in urls if not EXCLUDE_RE.search(u)})


def slugify(url: str) -> str:
    path = urlparse(url).path.strip("/")
    return path.replace("/", "-") if path else "index"


def clean_text(s: str) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return s


def extract(url: str, html: str) -> str:
    soup = BeautifulSoup(html, "lxml")

    for tag in soup(["script", "style", "noscript", "iframe", "svg",
                     "header", "footer", "nav", "form"]):
        tag.decompose()
    for sel in [".elementor-widget-wp-widget-nav_menu", ".menu-principal",
                ".menu-rodape", ".widget", ".breadcrumb", ".breadcrumbs",
                ".cookie", "#cookie-notice", ".social"]:
        for tag in soup.select(sel):
            tag.decompose()

    title_tag = soup.find("title")
    title = clean_text(title_tag.text) if title_tag else slugify(url)
    title = re.sub(r"\s*[-|]\s*WinRest 360.*$", "", title).strip() or slugify(url)

    desc = ""
    md = soup.find("meta", attrs={"name": "description"}) or \
        soup.find("meta", attrs={"property": "og:description"})
    if md and md.get("content"):
        desc = clean_text(md["content"])

    main = soup.find("main") or soup.find(class_=re.compile("(content|elementor)")) or soup.body
    if main is None:
        return ""

    lines: list[str] = []
    seen: set[str] = set()
    for el in main.find_all(["h1", "h2", "h3", "h4", "p", "li"]):
        txt = clean_text(el.get_text(" ", strip=True))
        if not txt or len(txt) < 3:
            continue
        if txt in seen:
            continue
        seen.add(txt)
        if el.name == "h1":
            lines.append(f"\n## {txt}\n")
        elif el.name == "h2":
            lines.append(f"\n### {txt}\n")
        elif el.name in ("h3", "h4"):
            lines.append(f"\n#### {txt}\n")
        elif el.name == "li":
            lines.append(f"- {txt}")
        else:
            lines.append(txt + "\n")

    body = "\n".join(lines).strip()

    head = [
        "---",
        f'title: "{title}"',
        f"source: {url}",
        f"scraped_at: {TODAY}",
        "tags: [scraping, winrest360, referencia]",
        "---",
        "",
        f"# {title}",
        "",
        f"> Fonte: <{url}>  |  Capturado em: {TODAY}",
        "",
    ]
    if desc:
        head += [f"**Resumo:** {desc}", ""]
    return "\n".join(head) + body + "\n"


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    pages = list_pages()
    print(f"📄 Páginas encontradas: {len(pages)}")
    written = 0
    index_lines = [
        "---",
        'title: "WinRest 360 Angola — Scraping"',
        "tags: [scraping, indice, winrest360]",
        "---",
        "",
        "# WinRest 360 Angola — Scraping",
        "",
        f"Capturado em: **{TODAY}**  |  Fonte: <https://ao.winrest360.com/>",
        "",
        "## Páginas",
        "",
    ]

    for url in pages:
        slug = slugify(url)
        try:
            html = fetch(url)
            md = extract(url, html)
            if not md:
                print(f"  ⚠️  vazio: {url}")
                continue
            (OUT_DIR / f"{slug}.md").write_text(md, encoding="utf-8")
            title_match = re.search(r'title: "([^"]+)"', md)
            title = title_match.group(1) if title_match else slug
            index_lines.append(f"- [[{slug}|{title}]] — <{url}>")
            written += 1
            print(f"  ✓ {slug}")
            time.sleep(1.2)
        except Exception as exc:
            print(f"  ✗ {url} → {exc}")

    (OUT_DIR / "_index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"\n✅ {written}/{len(pages)} notas escritas em {OUT_DIR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
