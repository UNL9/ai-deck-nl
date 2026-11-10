# AI-deck NL

Nederlandstalig overzichtsdeck over AI, circa 100 slides, wekelijks bijgewerkt. Ruggengraat voor de AI-trainingen voor bestuurders en commissarissen (Ebbinge). Het dekt de volledige breedte van AI. Een naslagwerk, geen presentatie: losse slides worden overgenomen in trainingsdecks en zijn te herkennen aan hun vaste ID.

## Hoe het werkt

1. **Bronnen** (`bronnen/bronnen.yaml`): een vaste lijst van de beste openbare bronnen, met betrouwbaarheid en frequentie.
2. **Kennisbank** (`kennisbank/`): elke feitelijke bewering met cijfer, peildatum, bron en houdbaarheid. Elke slide verwijst naar zijn beweringen.
3. **Opzet** (`deck/opzet.yaml`): de 100 slides met titel, kernboodschap en volatiliteit. Leesbaar overzicht: [`deck/opzet.md`](deck/opzet.md).
4. **Wekelijkse update**: een geplande taak loopt elke maandag de bronnen langs, werkt de kennisbank bij, markeert slides die herzien moeten worden en opent een pull request met een weekverslag in `updates/`. Niets gaat live zonder goedkeuring.
5. **Het deck zelf**: wordt uit de opzet en de kennisbank gebouwd en gepubliceerd als Slides-deck (te downloaden als .pptx en PDF).

De volledige werkafspraken staan in [`CLAUDE.md`](CLAUDE.md).

## Fasen

- [x] Fase 1: structuur, bronnenregister, opzet van 100 slides
- [x] Fase 2: kennisbank vullen en grafiekdata verzamelen per sectie
- [ ] Fase 3: slides uitwerken en deck publiceren
- [ ] Fase 4: wekelijkse update aanzetten

## Handige commando's

```
python3 scripts/render_opzet.py          # opzet.md bijwerken en verwijzingen controleren
python3 scripts/check_houdbaarheid.py    # verlopen en te verifiëren beweringen
```
Vereist Python 3 met PyYAML (`pip install pyyaml`).
