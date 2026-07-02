#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_gene_info.py
==================
Pre-build a local JSON of MedlinePlus Genetics summaries for the genes shown
in the Figure 4 BEST4 widget.

WHY a build step (and not a live fetch in the browser)?
-------------------------------------------------------
The blog is hosted statically (GitHub Pages). A client-side fetch() to
medlineplus.gov is blocked by the browser's same-origin / CORS policy, so the
widget cannot pull the data live. Instead we fetch it once, here, and commit a
small JSON file alongside the expression data. The widget then reads that local
file (same origin -> no CORS, instant clicks, works offline).

Data source: MedlinePlus Genetics API (public, no key required)
    https://medlineplus.gov/about/developers/geneticsdatafilesapi/
    Page : https://medlineplus.gov/genetics/gene/aldob/
    JSON : https://medlineplus.gov/download/genetics/gene/aldob.json
Content is from the U.S. National Library of Medicine (public domain).

USAGE
-----
    python3 build_gene_info.py \
        --expression assets/figures/elmentaite-2021/fig4_best4_marker_expression.json \
        --out        assets/figures/elmentaite-2021/fig4_best4_gene_info.json \
        --email      you@example.com

The gene list is read straight from the *keys* of the expression JSON, so the
output always matches exactly the genes your widget displays. Re-run it whenever
that gene list changes.

Only the Python standard library is used (no pip install needed).
"""

import argparse
import html
import json
import sys
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from xml.etree import ElementTree as ET

# macOS often ships Python without access to the system CA store, which makes
# every HTTPS call fail with CERTIFICATE_VERIFY_FAILED. If certifi is available,
# use its bundle so the script "just works" on a fresh machine.
try:
    import ssl as _ssl
    import certifi as _certifi
    _ssl._create_default_https_context = lambda: _ssl.create_default_context(cafile=_certifi.where())
except Exception:  # noqa: BLE001
    pass

API_TMPL   = "https://medlineplus.gov/download/genetics/gene/{slug}.json"
PAGE_TMPL  = "https://medlineplus.gov/genetics/gene/{slug}/"
SEARCH_URL = "https://wsearch.nlm.nih.gov/ws/query"
NCBI_ESEARCH  = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
NCBI_ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
NCBI_ELINK    = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi"
UA = "fig4-best4-widget/1.0 (Jekyll blog; non-commercial research)"

# Tags we allow to survive into the page (everything else is unwrapped/stripped).
ALLOWED_TAGS = {"p", "em", "i", "strong", "b", "br", "ul", "ol", "li", "a", "sub", "sup"}


# --------------------------------------------------------------------------- #
# Minimal whitelist HTML sanitizer
# --------------------------------------------------------------------------- #
class _Sanitizer(HTMLParser):
    """Keep a small set of formatting tags; on <a> keep only safe href values."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []

    def handle_starttag(self, tag, attrs):
        if tag not in ALLOWED_TAGS:
            return
        if tag == "a":
            href = dict(attrs).get("href", "")
            if href.startswith(("http://", "https://")):
                self.out.append(f'<a href="{href}">')
            else:
                self.out.append("<a>")
        else:
            self.out.append(f"<{tag}>")

    def handle_startendtag(self, tag, attrs):
        if tag == "br":
            self.out.append("<br>")

    def handle_endtag(self, tag):
        if tag in ALLOWED_TAGS and tag != "br":
            self.out.append(f"</{tag}>")

    def handle_data(self, data):
        self.out.append(data)

    def result(self):
        return "".join(self.out).strip()


def clean_html(raw):
    if not raw:
        return ""
    p = _Sanitizer()
    p.feed(raw)
    return p.result()


# --------------------------------------------------------------------------- #
# HTTP helpers
# --------------------------------------------------------------------------- #
def _get(url, accept="application/json"):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace"), r.status


def fetch_gene_json(slug):
    """Return parsed JSON for a gene slug, or None on 404/error."""
    try:
        body, status = _get(API_TMPL.format(slug=slug))
        if status == 200:
            return json.loads(body)
    except urllib.error.HTTPError as e:
        if e.code != 404:
            print(f"    ! HTTP {e.code} for {slug}", file=sys.stderr)
    except Exception as e:  # noqa: BLE001
        print(f"    ! {type(e).__name__} for {slug}: {e}", file=sys.stderr)
    return None


def resolve_slug_via_search(symbol):
    """If the direct slug 404s, ask the MedlinePlus search API for the gene page."""
    params = urllib.parse.urlencode({"db": "ghr", "term": symbol, "retmax": "5"})
    try:
        body, _ = _get(f"{SEARCH_URL}?{params}", accept="application/xml")
        root = ET.fromstring(body)
        for doc in root.iter("document"):
            url = doc.attrib.get("url", "")
            if "/genetics/gene/" in url:
                return url.rstrip("/").split("/genetics/gene/")[-1]
    except Exception as e:  # noqa: BLE001
        print(f"    ! search fallback failed for {symbol}: {e}", file=sys.stderr)
    return None


# --------------------------------------------------------------------------- #
# Parse the MedlinePlus gene JSON into our compact schema
# --------------------------------------------------------------------------- #
def _iter_text_objs(text_list):
    for el in text_list or []:
        t = el.get("text") if isinstance(el, dict) else None
        if isinstance(t, dict):
            yield t


def _html_for_role(text_list, role):
    """Return cleaned HTML for a given text-role; fall back to the first block."""
    first = ""
    for t in _iter_text_objs(text_list):
        html = t.get("html", "")
        if not first:
            first = html
        if t.get("text-role") == role:
            return clean_html(html)
    return clean_html(first)


def _ncbi_params(extra, email, key):
    p = dict(extra)
    p["tool"] = "fig4-best4-widget"
    if email:
        p["email"] = email
    if key:
        p["api_key"] = key
    return urllib.parse.urlencode(p)


def _eget(url):
    """E-utilities GET with a small delay to stay under the 3 req/s keyless limit."""
    time.sleep(0.34)
    return _get(url)


# Generic MedGen concepts to skip (not real conditions).
_MEDGEN_STOP = {
    "not provided", "see cases", "inborn genetic diseases",
    "tumor predisposition syndrome", "neoplasm", "disease", "abnormality",
}


def ncbi_medgen_conditions(uid, gene, email="", key=""):
    """Curated gene->condition associations from NCBI MedGen (literature-derived).

    Returns a list of {name, html:"", url} - NAMES + MedGen links only. Definition
    prose is deliberately NOT copied: MedGen pulls some definitions from sources
    with restrictive licenses (e.g. GeneReviews), so we link out instead.
    """
    try:
        q = _ncbi_params({"dbfrom": "gene", "db": "medgen", "id": uid,
                          "retmode": "json"}, email, key)
        body, _ = _eget(f"{NCBI_ELINK}?{q}")
        med_ids = []
        for ls in json.loads(body).get("linksets", []) or []:
            for ldb in ls.get("linksetdbs", []) or []:
                if "medgen" in (ldb.get("linkname", "") or ""):
                    med_ids += ldb.get("links", []) or []
        med_ids = list(dict.fromkeys(med_ids))[:10]
        if not med_ids:
            return []

        q2 = _ncbi_params({"db": "medgen", "id": ",".join(med_ids),
                           "retmode": "json"}, email, key)
        body2, _ = _eget(f"{NCBI_ESUMMARY}?{q2}")
        res = json.loads(body2).get("result", {})

        conds = []
        for mid in res.get("uids", []):
            rec = res.get(mid, {}) or {}
            title = (rec.get("title") or rec.get("name") or "").strip()
            if not title or title.lower() in _MEDGEN_STOP:
                continue
            cid = rec.get("conceptid") or mid
            conds.append({"name": title, "html": "",
                          "url": f"https://www.ncbi.nlm.nih.gov/medgen/{cid}"})
        return conds[:6]
    except Exception as e:  # noqa: BLE001
        print(f"    ! MedGen lookup failed for {gene}: {e}", file=sys.stderr)
        return []


def ncbi_lookup(symbol, email="", key="", want_conditions=True):
    """Fallback for genes with no MedlinePlus Genetics page.

    Pulls the RefSeq functional summary + aliases from NCBI Gene (E-utilities),
    and (optionally) gene->condition associations from NCBI MedGen. All NLM /
    public-domain, so safe to re-display (unlike OMIM, which needs a JHU license).
    Returns an info dict (source='ncbi') or None.
    """
    try:
        q = _ncbi_params(
            {"db": "gene", "term": f"{symbol}[sym] AND human[orgn]",
             "retmode": "json", "retmax": "1"}, email, key)
        body, _ = _eget(f"{NCBI_ESEARCH}?{q}")
        ids = json.loads(body).get("esearchresult", {}).get("idlist", [])
        if not ids:
            return None
        uid = ids[0]

        q2 = _ncbi_params({"db": "gene", "id": uid, "retmode": "json"}, email, key)
        body2, _ = _eget(f"{NCBI_ESUMMARY}?{q2}")
        rec = json.loads(body2).get("result", {}).get(uid, {})
        if not rec:
            return None

        summary = (rec.get("summary") or "").strip()
        function_html = f"<p>{html.escape(summary)}</p>" if summary else ""
        aliases = [a.strip() for a in (rec.get("otheraliases") or "").split(",") if a.strip()]
        full_name = rec.get("nomenclaturename") or rec.get("description") or ""

        conditions = []   # MedGen elink gene->medgen returns empty for most functional genes;
                          # no structured phenotype associations available via public APIs
                          # without an OMIM redistribution license.
        mim_numbers = rec.get("mim") or []
        omim_url = (f"https://omim.org/entry/{mim_numbers[0]}" if mim_numbers else
                    f"https://omim.org/search?search={urllib.parse.quote(symbol)}")
        pubmed_url = ("https://pubmed.ncbi.nlm.nih.gov/?term="
                      + urllib.parse.quote(f"{symbol}[tiab] AND (disease[tiab] OR "
                                           f"disorder[tiab] OR deficiency[tiab] OR mutation[tiab])"))

        return {
            "found": True,
            "symbol": rec.get("name", symbol),
            "full_name": full_name,
            "function_html": function_html,
            "conditions": conditions,
            "synonyms": aliases,
            "url": f"https://www.ncbi.nlm.nih.gov/gene/{uid}",
            "reviewed": "",
            "source": "ncbi",
            "source_name": "NCBI Gene",
            "pubmed_url": pubmed_url,
            "omim_url": omim_url,
        }
    except Exception as e:  # noqa: BLE001
        print(f"    ! NCBI lookup failed for {symbol}: {e}", file=sys.stderr)
        return None


CONDITION_API_TMPL = "https://medlineplus.gov/download/genetics/condition/{slug}.json"


def fetch_condition_description(ghr_page_url):
    """Fetch the description paragraph from a MedlinePlus condition page.

    The gene-level JSON only has name + URL for each condition.
    The description text lives on the condition's own JSON page,
    at text-list[0].text.html (no text-role key on condition pages).
    Returns cleaned HTML string, or "" on error/miss.
    """
    if not ghr_page_url:
        return ""
    try:
        slug = ghr_page_url.rstrip("/").split("/genetics/condition/")[-1]
        if not slug or "/" in slug:
            return ""
        body, status = _get(CONDITION_API_TMPL.format(slug=slug))
        if status != 200:
            return ""
        data = json.loads(body)
        for item in data.get("text-list") or []:
            raw = (item.get("text") or {}).get("html", "") if isinstance(item, dict) else ""
            if raw:
                return clean_html(raw)
    except Exception:  # noqa: BLE001
        pass
    return ""


def parse_gene(symbol, data):
    full_name = (
        data.get("full-name")
        or data.get("fullName")
        or data.get("full_name")
        or ""
    )
    url = (data.get("ghr_page") or data.get("ghr-page")
           or PAGE_TMPL.format(slug=symbol.lower())).rstrip("/")

    function_html = _html_for_role(data.get("text-list"), "function")

    conditions = []
    for key in ("health-condition-list", "related-health-condition-list"):
        for it in data.get(key, []) or []:
            hc = (it.get("health-condition")
                  or it.get("related-health-condition")
                  or it if isinstance(it, dict) else {})
            name = hc.get("name")
            if not name:
                continue
            ghr_url = (hc.get("ghr-page") or hc.get("ghr_page") or "").rstrip("/")
            # Description text is not in the gene JSON — fetch from the condition page.
            desc_html = (_html_for_role(hc.get("text-list"), "description")
                         or fetch_condition_description(ghr_url))
            conditions.append({
                "name": name,
                "html": desc_html,
                "url": ghr_url,
            })

    synonyms = []
    for s in data.get("synonym-list", []) or []:
        val = s.get("synonym") if isinstance(s, dict) else s
        if val:
            synonyms.append(val)

    return {
        "found": True,
        "symbol": data.get("name", symbol),
        "full_name": full_name,
        "function_html": function_html,
        "conditions": conditions,
        "synonyms": synonyms,
        "url": url,
        "reviewed": data.get("reviewed", ""),
        "source": "medlineplus",
        "source_name": "MedlinePlus Genetics",
    }


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--expression",
                    default="assets/figures/elmentaite-2021/fig4_best4_marker_expression.json",
                    help="Path to the expression JSON (its keys are the gene list).")
    ap.add_argument("--out",
                    default="assets/figures/elmentaite-2021/fig4_best4_gene_info.json",
                    help="Where to write the gene-info JSON.")
    ap.add_argument("--genes", nargs="*",
                    help="Override: explicit list of gene symbols instead of reading --expression.")
    ap.add_argument("--sleep", type=float, default=0.5,
                    help="Seconds to pause between requests (be polite to NLM).")
    ap.add_argument("--email", default="",
                    help="Optional contact email (sent to NLM / NCBI as a courtesy).")
    ap.add_argument("--ncbi-key", default="",
                    help="Optional NCBI API key (raises the E-utilities rate limit).")
    ap.add_argument("--no-medgen", action="store_true",
                    help="Skip NCBI MedGen condition lookups for NCBI-sourced genes.")
    args = ap.parse_args()

    # --- gene list -------------------------------------------------------- #
    if args.genes:
        genes = args.genes
    else:
        try:
            with open(args.expression, encoding="utf-8") as f:
                genes = list(json.load(f).keys())
        except FileNotFoundError:
            print(f"Expression file not found: {args.expression}\n"
                  f"Pass genes directly with --genes SYMBOL SYMBOL ...", file=sys.stderr)
            sys.exit(1)

    print(f"Building gene info for {len(genes)} genes "
          f"(MedlinePlus Genetics, with NCBI Gene fallback)...\n")

    out = {
        "_meta": {
            "source": "MedlinePlus Genetics + NCBI Gene (U.S. National Library of Medicine)",
            "api": "https://medlineplus.gov/about/developers/geneticsdatafilesapi/",
            "generated": time.strftime("%Y-%m-%d"),
        }
    }
    found, ncbi_found, missing = [], [], []

    for i, gene in enumerate(genes, 1):
        slug = gene.lower()
        print(f"[{i}/{len(genes)}] {gene}", end=" ... ")
        data = fetch_gene_json(slug)

        if data is None:
            alt = resolve_slug_via_search(gene)
            if alt and alt != slug:
                data = fetch_gene_json(alt)

        if data is None:
            info = ncbi_lookup(gene, args.email, args.ncbi_key,
                               want_conditions=not args.no_medgen)
            if info is None:
                print("not found (MedlinePlus or NCBI)")
                out[gene] = {"found": False, "symbol": gene}
                missing.append(gene)
            else:
                out[gene] = info
                nc = len(info["conditions"])
                print(f"ok via NCBI Gene ({len(info['synonyms'])} aliases, "
                      f"{nc} condition{'s' if nc != 1 else ''})")
                ncbi_found.append(gene)
        else:
            out[gene] = parse_gene(gene, data)
            nc = len(out[gene]["conditions"])
            print(f"ok via MedlinePlus ({nc} condition{'s' if nc != 1 else ''})")
            found.append(gene)

        time.sleep(args.sleep)

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"\nWrote {args.out}")
    print(f"  MedlinePlus: {len(found)}")
    print(f"  NCBI Gene:   {len(ncbi_found)}")
    print(f"  not found:   {len(missing)}")
    if missing:
        print(f"  missing: {', '.join(missing)}")
        print("  (no entry on MedlinePlus Genetics or NCBI Gene; "
              "the widget shows lookup links for these.)")


if __name__ == "__main__":
    main()
