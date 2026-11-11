#!/usr/bin/env python3
"""Telt per slide de overtredingen van de kwaliteitslat en geeft een totaal.

De lat, in volgorde van belang:
  1. juist        elk getal komt uit een actuele bewering, gecontroleerd bij de primaire bron
  2. onderbouwd   de slide staat niet meer in deck/werklijst.md
  3. actueel      geen verlopen beweringen
  4. leesbaar     titel max twee regels, ondertitel één regel, max drie punten, niets onder 920 px
  5. stijl        deck/stijl.md: geen gedachtestreepjes, geen marketingtaal, tekst >= 24px, voetregel
  6. te toetsen   slide haalt 1 tot en met 5 maar staat nog niet op gereed (oordeel: draagt de
                  titel, raken labels elkaar niet)

Een slide op status gereed telt niet mee. Keuzes voor Joan (werklijst) worden getoond maar niet geteld.
Een bewering die nog te verifiëren is, telt niet als de slide zichtbaar "volgens berichten" vermeldt (besluit Joan, 2026-11-11).

Gebruik: python3 scripts/check_kwaliteit.py [--datum JJJJ-MM-DD] [--alles] [--slide ID]
"""
import argparse
import datetime as dt
import glob
import html
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SLIDES = ROOT / "deck/artifact/project/slides"
CATEGORIEEN = ["juist", "onderbouwd", "actueel", "leesbaar", "stijl", "te toetsen"]
MARKETING = ["transformatief", "transformationeel", "game-changer", "gamechanger", "ecosysteem", "ontsluiten",
             "baanbrekend", "revolutionair", "naadloos", "synergie", "holistisch", "best-in-class",
             "wereldklasse", "next level", "disruptief"]
ONGECONTROLEERD = re.compile(
    r"niet zelf (gecontroleerd|ingezien|gelezen|geopend)|zelf niet (gecontroleerd|ingezien|gelezen|geopend)"
    r"|nog niet (bij de primaire bron |zelf )?gecontroleerd"
    r"|primaire (bron|publicatie)[^.]*(nog niet|niet) (gevonden|gecontroleerd|ingezien)", re.I)
ID = re.compile(r"\b[A-Z]{3}-\d{2}\b")


def laad_beweringen():
    uit = {}
    for f in sorted(glob.glob(str(ROOT / "kennisbank/beweringen/*.yaml"))):
        for b in yaml.safe_load(Path(f).read_text(encoding="utf-8")) or []:
            uit[b["id"]] = b
    return uit


def laad_betrouwbaarheid():
    doc = yaml.safe_load((ROOT / "bronnen/bronnen.yaml").read_text(encoding="utf-8"))
    return {b["id"]: b.get("betrouwbaarheid") for groep in doc.values() for b in groep}


def laad_werklijst():
    """slide-ID -> lijst (kop, tekst) uit deck/werklijst.md"""
    pad = ROOT / "deck/werklijst.md"
    open_, keuzes, kop = {}, {}, ""
    if not pad.exists():
        return open_, keuzes
    for regel in pad.read_text(encoding="utf-8").splitlines():
        if regel.startswith("## "):
            kop = regel[3:].strip()
            continue
        if not regel.strip().startswith(("|", "-")) or set(regel.strip()) <= set("|- "):
            continue
        doel = keuzes if kop.lower().startswith("keuzes") else open_
        tekst = regel.strip(" |-").replace(" | ", ": ")
        for sid in ID.findall(regel):
            doel.setdefault(sid, []).append(f"{kop}: {tekst}")
    return open_, keuzes


def zichtbare_tekst(t):
    t = re.sub(r"<aside>.*?</aside>", " ", t, flags=re.S)
    t = re.sub(r"<svg.*?</svg>", " ", t, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", " ", t))


def check_html(sid, pad):
    fouten = []
    if not pad.exists():
        return [("stijl", "slidebestand ontbreekt")]
    t = pad.read_text(encoding="utf-8")
    m = re.match(r"\s*<section id=\"([^\"]+)\"", t)
    if not m or m.group(1) != sid or t.count("<section") != 1:
        fouten.append(("stijl", "bestand bevat niet precies één <section> met dit ID"))
    if "—" in t or re.search(r"\s–\s", zichtbare_tekst(t)):
        fouten.append(("stijl", "gedachtestreepje in de tekst"))
    for w in MARKETING:
        if re.search(rf"\b{re.escape(w)}", zichtbare_tekst(t), re.I):
            fouten.append(("stijl", f"marketingtaal: '{w}'"))
    klein = sorted({int(x) for x in re.findall(r"font-size:(\d+)px", t) if int(x) < 24})
    if klein:
        fouten.append(("stijl", f"tekst kleiner dan 24px ({', '.join(map(str, klein))}px)"))
    if "<text" in t:
        fouten.append(("stijl", "<text> in SVG; labels horen als <p> boven de SVG"))
    if not re.search(r"bottom:64px", t) or "stand 20" not in t:
        fouten.append(("stijl", "voetregel met stand ontbreekt"))
    elif not sid.endswith("-opener") and f"{sid} · stand" not in t:
        fouten.append(("stijl", "voetregel noemt het slide-ID niet"))
    if not sid.endswith("-opener") and "<aside>" not in t:
        fouten.append(("stijl", "sprekersnotities ontbreken"))
    if re.search(r"\d\.\d{1,2}(?!\d)\s?(%|procent)", zichtbare_tekst(t)):  # 1.127 procent is een duizendtal
        fouten.append(("stijl", "decimaalpunt in een percentage; gebruik een komma"))

    h2 = re.search(r"<h2[^>]*>(.*?)</h2>", t, re.S)
    if h2:
        titel = zichtbare_tekst(h2.group(1)).strip()
        if len(titel) > 100:
            fouten.append(("leesbaar", f"titel waarschijnlijk langer dan twee regels ({len(titel)} tekens)"))
        na = t[h2.end():]
        sub = re.match(r"\s*<p style=\"font-size:32px[^\"]*\">(.*?)</p>", na, re.S)
        if sub and len(zichtbare_tekst(sub.group(1)).strip()) > 90:
            fouten.append(("leesbaar", f"ondertitel waarschijnlijk langer dan één regel ({len(zichtbare_tekst(sub.group(1)).strip())} tekens)"))
    punten = len(re.findall(r"<p style=\"font-size:26px;line-height:1.35;color:#2A2E35;border-left:4px solid #1F4E9E", t))
    if punten > 3:
        fouten.append(("leesbaar", f"{punten} toelichtingspunten (max drie)"))
    for blok in re.findall(r"<(?:p|div|svg|table|img)[^>]*position:absolute[^>]*>", t):
        if "bottom:64px" in blok:
            continue
        top = re.search(r"top:(\d+)px", blok)
        hoogte = re.search(r"height:(\d+)px", blok)
        if top and int(top.group(1)) + (int(hoogte.group(1)) if hoogte and "<svg" not in blok else 0) > 920:
            fouten.append(("leesbaar", f"element eindigt onder 920 px (top {top.group(1)})"))
            break
    return fouten


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--datum", default=dt.date.today().isoformat())
    p.add_argument("--alles", action="store_true", help="toon alle overtredingen, niet alleen de eerste 15")
    p.add_argument("--slide", help="alleen deze slide")
    a = p.parse_args()
    vandaag = dt.date.fromisoformat(a.datum)

    opzet = yaml.safe_load((ROOT / "deck/opzet.yaml").read_text(encoding="utf-8"))
    beweringen, betrouw = laad_beweringen(), laad_betrouwbaarheid()
    werklijst, keuzes = laad_werklijst()

    rij = []  # (categorie-index, volgorde, slide, tekst)
    gereed = 0
    actieve = [s for s in opzet["slides"] if s.get("status") != "vervallen"]
    codes = [s["code"] for s in opzet["secties"]]
    openers = [f"{c}-opener" for c in codes if c != "OPN"]
    for n, s in enumerate(actieve):
        sid = s["id"]
        if a.slide and sid != a.slide:
            continue
        if s.get("status") == "gereed":
            gereed += 1
            continue
        fouten = []
        if s.get("status") == "herzien":
            fouten.append(("onderbouwd", "status herzien: voorstel wacht op verwerking"))
        gekoppeld = s.get("beweringen", [])
        pad = SLIDES / f"{sid}.html"
        slidetekst = zichtbare_tekst(pad.read_text(encoding="utf-8")).lower() if pad.exists() else ""
        for k in gekoppeld:
            b = beweringen.get(k)
            if not b:
                fouten.append(("juist", f"{k} bestaat niet"))
                continue
            if b.get("status") == "vervangen":
                # volg de keten van vervangingen tot de actuele bewering
                opvolger, gezien = b.get("vervangen_door"), set()
                while opvolger and opvolger not in gezien and beweringen.get(opvolger, {}).get("status") == "vervangen":
                    gezien.add(opvolger)
                    opvolger = beweringen[opvolger].get("vervangen_door")
                if opvolger and opvolger not in gekoppeld:
                    fouten.append(("juist", f"{k} is vervangen door {opvolger}, die niet aan de slide hangt"))
                continue
            if b.get("status") == "te_verifieren":
                if "volgens berichten" not in slidetekst:
                    fouten.append(("juist", f"{k} is nog te verifiëren (en de slide zegt niet 'volgens berichten')"))
            elif betrouw.get(b.get("bron")) == "C":
                fouten.append(("juist", f"{k} komt uit een secundaire bron ({b['bron']}, betrouwbaarheid C)"))
            elif ONGECONTROLEERD.search(b.get("noot", "") or ""):
                fouten.append(("juist", f"{k}: primaire bron nog niet zelf gecontroleerd"))
            vast = b["vastgesteld"]
            vast = dt.date.fromisoformat(vast) if isinstance(vast, str) else vast
            vervalt = vast + dt.timedelta(days=int(b["houdbaarheid_dagen"]))
            if vervalt <= vandaag:
                fouten.append(("actueel", f"{k} verliep op {vervalt}"))
        for item in werklijst.get(sid, []):
            fouten.append(("onderbouwd", f"werklijst, {item}"))
        fouten += check_html(sid, SLIDES / f"{sid}.html")
        if not fouten:
            fouten.append(("te toetsen", "haalt de automatische lat; toets titel en labels en zet dan op gereed"))
        rij += [(CATEGORIEEN.index(c), n, sid, f"[{c}] {tekst}") for c, tekst in fouten]

    if not a.slide:
        for n, sid in enumerate(openers):
            rij += [(CATEGORIEEN.index(c), 1000 + n, sid, f"[{c}] {tekst}") for c, tekst in check_html(sid, SLIDES / f"{sid}.html")]

    rij.sort()
    per_cat = {c: sum(1 for r in rij if CATEGORIEEN[r[0]] == c) for c in CATEGORIEEN}
    print(f"Kwaliteitslat, peildatum {vandaag}")
    print(f"Totaal: {len(rij)} overtredingen  (" + ", ".join(f"{c} {per_cat[c]}" for c in CATEGORIEEN) + ")")
    print(f"Slides op gereed: {gereed} van {len(actieve)}; slides met overtredingen: {len({r[2] for r in rij})}")
    print(f"Keuzes voor Joan (tellen niet mee): {sum(len(v) for v in keuzes.values())}")
    print()
    for r in rij if a.alles or a.slide else rij[:15]:
        print(f"  {r[2]:<11} {r[3]}")
    if not (a.alles or a.slide) and len(rij) > 15:
        print(f"  ... en nog {len(rij) - 15} (gebruik --alles)")


if __name__ == "__main__":
    main()
