#!/usr/bin/env python3
"""Maakt deck/opzet.md (leesbaar overzicht) uit deck/opzet.yaml en controleert de samenhang.

Controles:
- slide-ID's uniek en in een bekende sectie
- verwijzingen naar bronnen en beweringen bestaan
"""
import glob
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def laad():
    opzet = yaml.safe_load((ROOT / "deck/opzet.yaml").read_text(encoding="utf-8"))
    bronnen_doc = yaml.safe_load((ROOT / "bronnen/bronnen.yaml").read_text(encoding="utf-8"))
    bronnen = {b["id"] for groep in bronnen_doc.values() for b in groep}
    beweringen = {}
    for f in sorted(glob.glob(str(ROOT / "kennisbank/beweringen/*.yaml"))):
        for b in yaml.safe_load(Path(f).read_text(encoding="utf-8")) or []:
            beweringen[b["id"]] = b
    return opzet, bronnen, beweringen


def controleer(opzet, bronnen, beweringen):
    fouten = []
    codes = {s["code"] for s in opzet["secties"]}
    ids = [s["id"] for s in opzet["slides"]]
    for i in {x for x in ids if ids.count(x) > 1}:
        fouten.append(f"dubbel slide-ID: {i}")
    for s in opzet["slides"]:
        if s["id"].split("-")[0] not in codes:
            fouten.append(f"{s['id']}: onbekende sectie")
        for b in s.get("bronnen", []):
            if b not in bronnen:
                fouten.append(f"{s['id']}: onbekende bron '{b}'")
        for k in s.get("beweringen", []):
            if k not in beweringen:
                fouten.append(f"{s['id']}: onbekende bewering '{k}'")
    for k, b in beweringen.items():
        if b["bron"] not in bronnen:
            fouten.append(f"{k}: onbekende bron '{b['bron']}'")
        for sid in b.get("slides", []):
            if sid not in ids:
                fouten.append(f"{k}: verwijst naar onbekende slide '{sid}'")
    return fouten


def render(opzet):
    m = opzet["meta"]
    actief = [s for s in opzet["slides"] if s.get("status") != "vervallen"]
    regels = [
        f"# {m['titel']}",
        "",
        f"Opzet, stand {m['stand']}. {len(actief)} slides. Gegenereerd uit `deck/opzet.yaml`; niet met de hand bewerken.",
        "",
        "Volatiliteit: **W** = wekelijks gecontroleerd, **K** = per kwartaal, **S** = stabiel.",
        "",
    ]
    letter = {"wekelijks": "W", "kwartaal": "K", "stabiel": "S"}
    for sectie in opzet["secties"]:
        slides = [s for s in actief if s["id"].startswith(sectie["code"] + "-")]
        regels += [f"## {sectie['naam']} ({len(slides)})", ""]
        for s in slides:
            regels.append(f"**{s['id']}** [{letter.get(s['volatiliteit'], '?')}] **{s['titel']}**  ")
            regels.append(f"{s['kern']}")
            if s.get("punten"):
                regels.append("")
                regels += [f"{n}. {p}" for n, p in enumerate(s["punten"], 1)]
                regels.append("")
            extra = []
            if s.get("bronnen"):
                extra.append("Bronnen: " + ", ".join(s["bronnen"]))
            if s.get("noot"):
                extra.append("Open: " + s["noot"])
            if extra:
                regels.append("<br><sub>" + " · ".join(extra) + "</sub>")
            regels.append("")
    return "\n".join(regels)


def main():
    opzet, bronnen, beweringen = laad()
    fouten = controleer(opzet, bronnen, beweringen)
    (ROOT / "deck/opzet.md").write_text(render(opzet), encoding="utf-8")
    actief = [s for s in opzet["slides"] if s.get("status") != "vervallen"]
    print(f"{len(actief)} slides, {len(beweringen)} beweringen, {len(bronnen)} bronnen")
    for f in fouten:
        print("FOUT:", f)
    sys.exit(1 if fouten else 0)


if __name__ == "__main__":
    main()
