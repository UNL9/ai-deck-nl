# AI-deck NL: werkafspraken voor Claude

Dit is de bron van een Nederlandstalig overzichtsdeck over AI (circa 100 slides) van Joan Arensman. Het deck is de ruggengraat voor de AI-trainingen voor bestuurders en commissarissen via Ebbinge. Het wordt niet als geheel gepresenteerd. Het is een naslagwerk waaruit Joan slides haalt, en het moet altijd actueel zijn. Het deck dekt de volledige breedte van AI, los van wat in een specifieke training aan bod komt.

## Hoe de repo in elkaar zit

| Map / bestand | Wat erin staat |
|---|---|
| `bronnen/bronnen.yaml` | Register van vaste bronnen, met frequentie, betrouwbaarheid en licentie |
| `kennisbank/beweringen/*.yaml` | Feitelijke beweringen per thema: cijfer, peildatum, bron, houdbaarheid, gekoppelde slides |
| `kennisbank/bestuurdersnotities/*.md` | Per thema: wat moet een bestuurder of commissaris hiermee |
| `deck/opzet.yaml` | De 100 slides: ID, sectie, titel, kernboodschap, volatiliteit, gekoppelde beweringen |
| `deck/stijl.md` | Huisstijl en schrijfregels voor slides |
| `data/` | CSV's achter elke grafiek, met bron in de kop |
| `updates/JJJJ-MM-DD.md` | Wekelijks verslag: wat is nieuw, wat is gewijzigd, wat is verlopen |
| `scripts/` | `render_opzet.py` (opzet naar leesbare markdown), `check_houdbaarheid.py` (verlopen beweringen) |

## Harde regels

1. **Elke bewering heeft een bron en een peildatum.** Geen cijfer in een slide zonder regel in de kennisbank.
2. **Beweringen worden niet stilletjes overschreven.** Bij een nieuw cijfer: oude regel krijgt `vervangen_door`, nieuwe regel komt erbij. Zo blijft de geschiedenis zichtbaar.
3. **Geen grafieken of afbeeldingen overnemen uit andere decks.** De voorbeelddecks (State of AI, Benedict Evans, ICONIQ) zijn stijlreferentie en bron van cijfers. Grafieken bouwen we zelf, uit data in `data/`, met bronvermelding. Voorkeur voor bronnen met open data (Epoch AI is CC-BY, Stanford AI Index, CBS, Eurostat).
4. **Primair boven secundair.** Een cijfer uit een nieuwsbrief (betrouwbaarheid C) wordt pas gebruikt na controle bij de primaire bron.
5. **Slide-ID's zijn vast** vanaf de eerste publicatie van het deck. Een slide die vervalt krijgt `status: vervallen`, het ID wordt niet hergebruikt. Joan verwijst vanuit trainingsdecks naar deze ID's.
6. **Taal en stijl van slides:** Nederlands, regels uit `deck/stijl.md` en de joan-writing-style skill. Geen gedachtestreepjes (em-dashes) in slideteksten. Geen marketingtaal.
7. **Niets gaat live zonder Joan.** Wijzigingen gaan via een branch en pull request, nooit direct op `main`.

## Wekelijkse update (procedure)

Draait elke maandagochtend als geplande taak. Werk altijd op een nieuwe branch `update/JJJJ-MM-DD`.

1. **Scannen.** Loop de bronnen in `bronnen/bronnen.yaml` met `frequentie: wekelijks` of `dagelijks` langs, plus een gerichte zoekronde op het nieuws van de afgelopen 7 dagen (modelreleases, benchmarks, omzet- en adoptiecijfers, regelgeving, Nederland). Bronnen met `frequentie: jaarlijks` of `halfjaarlijks`: alleen controleren of er een nieuwe editie is.
2. **Kennisbank bijwerken.** Nieuwe of gewijzigde cijfers als nieuwe beweringen toevoegen (regel 2). Alleen opnemen wat materieel is voor het overzicht; geen nieuwsoverzicht van alles wat er gebeurde.
3. **Houdbaarheid controleren.** Draai `python3 scripts/check_houdbaarheid.py`. Verlopen beweringen opnieuw verifiëren of markeren.
4. **Slides markeren.** Elke slide waarvan een gekoppelde bewering is vervangen of verlopen: `status: herzien` en een voorstel voor nieuwe titel of kernboodschap in `voorstel`. Wijzig slides met `volatiliteit: stabiel` alleen bij een echte trendbreuk, en zeg dat er expliciet bij.
5. **Verslag schrijven.** `updates/JJJJ-MM-DD.md`: maximaal 10 punten "wat is er deze week veranderd", per punt de geraakte slide-ID's en de bron. Werk ook slide `OPN-02` (wat is er veranderd) bij.
6. **Pull request openen** met het verslag als beschrijving. Niet zelf mergen.

Als er in een week niets materieels is veranderd, zeg dat in het verslag. Dat is een geldige uitkomst.

## Werken in VS Code

- `python3 scripts/render_opzet.py` maakt `deck/opzet.md` (leesbaar overzicht) uit `deck/opzet.yaml`. Draai dit na elke wijziging in de opzet.
- Vraag bij inhoudelijke keuzes over de verhaallijn eerst Joan; de opzet is van hem.
