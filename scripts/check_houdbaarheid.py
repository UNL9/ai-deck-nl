#!/usr/bin/env python3
"""Toont beweringen waarvan de houdbaarheid verlopen is of die nog geverifieerd moeten worden,
met de slides die erdoor geraakt worden.

Gebruik: python3 scripts/check_houdbaarheid.py [--datum JJJJ-MM-DD]
"""
import argparse
import datetime as dt
import glob
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--datum", default=dt.date.today().isoformat())
    vandaag = dt.date.fromisoformat(p.parse_args().datum)

    verlopen, te_verifieren = [], []
    for f in sorted(glob.glob(str(ROOT / "kennisbank/beweringen/*.yaml"))):
        for b in yaml.safe_load(Path(f).read_text(encoding="utf-8")) or []:
            if b.get("status") == "vervangen":
                continue
            vastgesteld = b["vastgesteld"]
            if isinstance(vastgesteld, str):
                vastgesteld = dt.date.fromisoformat(vastgesteld)
            vervalt = vastgesteld + dt.timedelta(days=int(b["houdbaarheid_dagen"]))
            if vervalt <= vandaag:
                verlopen.append((vervalt, b))
            if b.get("status") == "te_verifieren":
                te_verifieren.append(b)

    print(f"Peildatum controle: {vandaag}\n")
    print(f"Verlopen ({len(verlopen)}):")
    for vervalt, b in sorted(verlopen, key=lambda x: x[0]):
        print(f"  {b['id']}  verliep {vervalt}  slides {', '.join(b.get('slides', []))}")
    print(f"\nTe verifiëren ({len(te_verifieren)}):")
    for b in te_verifieren:
        print(f"  {b['id']}  slides {', '.join(b.get('slides', []))}  {b.get('noot', '')}")


if __name__ == "__main__":
    main()
