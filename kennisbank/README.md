# Kennisbank

## Beweringen (`beweringen/<thema>.yaml`)

Eén regel per feitelijke bewering:

```yaml
- id: K-MKT-001                 # vast, nooit hergebruiken
  bewering: "..."               # één of twee zinnen, met cijfer
  peildatum: 2026-08            # waarop het cijfer betrekking heeft
  bron: soai                    # ID uit bronnen/bronnen.yaml
  vindplaats: "..."             # pagina, slide of URL
  vastgesteld: 2026-11-10       # wanneer wij het controleerden
  houdbaarheid_dagen: 30        # na deze termijn opnieuw controleren
  status: actueel               # actueel | te_verifieren | vervangen
  vervangen_door: K-MKT-014     # alleen bij status vervangen
  slides: [MKT-01]
  noot: "..."                   # optioneel
```

Richtlijn houdbaarheid: ranglijsten en benchmarks 14 dagen; omzet en marktaandeel 30 dagen; investeringen en adoptie 90 dagen; enquêtes en structurele cijfers 180 tot 400 dagen.

Een nieuw cijfer vervangt een oud cijfer nooit door overschrijven. De oude regel krijgt `status: vervangen` en `vervangen_door`.

## Bestuurdersnotities (`bestuurdersnotities/<thema>.md`)

Per thema een korte notitie: wat betekent dit voor een bestuurder of commissaris, welke vragen stel je, waar zit het risico. Dit is interpretatie, geen feit, en wordt dus niet automatisch bijgewerkt.
