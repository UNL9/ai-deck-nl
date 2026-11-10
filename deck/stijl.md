# Huisstijl AI-deck NL

Het midden tussen Benedict Evans en het State of AI Report van Air Street. Van Evans de rust en de stelling als titel, van Air Street de toelichting, de bronvermelding en de navigatie.

## Opbouw van een slide (16:9)

| Element | Regel |
|---|---|
| Sectiebalk | Bovenaan, klein: alle secties, de huidige gemarkeerd (zoals Air Street). |
| Titel | De boodschap als stelling, maximaal twee regels. Geen label ("Omzet") maar een bewering ("OpenAI en Anthropic groeien elk jaar meer dan drie keer"). |
| Ondertitel | Eén regel die de titel preciseert of nuanceert (zoals Evans). |
| Beeld | Eén grafiek of schema, links of over de volle breedte. Nooit twee grafieken die om aandacht vechten. |
| Toelichting | Maximaal drie of vier korte punten rechts van de grafiek, elk een volledige zin. Alleen als de grafiek dat nodig heeft. |
| Voetregel | Bron met peildatum, slide-ID en "stand JJJJ-MM-DD". Altijd. |

Sectieopeners: één slide met alleen de sectienaam en de drie belangrijkste boodschappen van die sectie.

## Grafieken

- Zelf gebouwd uit `data/`, nooit gekopieerd uit een ander deck.
- Eén kleur voor de hoofdreeks, grijs voor de rest. Het accent wijst naar wat de titel beweert.
- Labels direct bij de lijn of balk, geen losse legenda als het kan.
- As met eenheid; peildatum in de voetregel.
- Logaritmische schaal alleen als de titel over groeitempo gaat, en dan vermelden.

## Taal

- Nederlands, "je"-vorm waar een lezer wordt aangesproken.
- Getallen: tot en met tien in letters, daarboven in cijfers; geld, percentages en vergelijkingen altijd in cijfers. Decimaalkomma, punt als scheiding van duizendtallen (1.386).
- Bedragen in de valuta van de bron; "miljard dollar", niet "$B".
- Geen gedachtestreepjes. Gebruik een punt, dubbele punt of haakjes.
- Geen marketingtaal (geen "transformatief", "game-changer", "ecosysteem", "ontsluiten").
- Engelse vaktermen alleen als er geen gangbaar Nederlands woord is (agent, token, benchmark mogen; "alignen" niet). Bij eerste gebruik kort uitleggen.
- Specifiek boven algemeen: een getal, een naam, een datum.

## Kleur en typografie (voorstel, nog vast te stellen)

- Achtergrond wit, tekst bijna-zwart, één accentkleur (diepblauw) en één signaalkleur (rood) voor wat wijzigde.
- Schreefloze letter voor titels en tekst, één familie.
- Slides die deze week gewijzigd zijn, krijgen een klein label "gewijzigd JJJJ-MM-DD".
