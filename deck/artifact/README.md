# Het deck als Slides-artifact

Hier staan de bronbestanden van het gepubliceerde deck (claude.ai, type Slides). Vanuit de viewer is het deck te downloaden als .pptx en als PDF.

- `project/deck.json`: titel, volgorde van de slides, secties en lettertype.
- `project/slides/<ID>.html`: één bestand per slide, genoemd naar het vaste slide-ID uit `deck/opzet.yaml`. Omslag en sectieopeners hebben (nog) geen vast ID.

Afspraken:

- Elk getal op een slide komt uit de kennisbank; de beweringen staan in de sprekersnotities (`<aside>`).
- Grafieken zijn eigen werk, getekend uit de CSV in `data/` die in de notities wordt genoemd.
- Voetregel: bron met peildatum, slide-ID en "stand JJJJ-MM-DD".
- Huisstijl: `deck/stijl.md`. Achtergrond #FAFAF7, tekst #16181D, accent #1F4E9E, grijs voor de rest; letter Inter.

Stand: proef met sectie Het front (FRT-01 tot en met FRT-10), 11 november 2026.
