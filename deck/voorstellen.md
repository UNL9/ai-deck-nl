# Voorstellen voor de opzet, ter beoordeling

*Stand 2026-11-10. 32 slides met een voorstel uit fase 2. Gegenereerd uit `deck/opzet.yaml`; dit bestand is een werkdocument en verdwijnt zodra de besluiten verwerkt zijn.*

## Zo werkt het

Vul per slide de regel **Besluit** in:

- `akkoord`: het voorstel gaat over in titel, kern en grafiek.
- `afwijzen`: de huidige tekst blijft staan.
- Of schrijf je eigen versie, of een opmerking. Dan verwerk ik die.

Een lege besluitregel betekent: nog niet beslist, het voorstel blijft staan. Slides met `status: herzien` krijgen na verwerking `status: opzet`.

## Waar ik een keuze van je nodig heb

- **INF-01.** De vergelijking met de telecomsector (300 miljard) heeft geen bron. Weglaten of laten onderbouwen?
- **INF-03.** De data laten niet zien dat concurrenten juist bij inferentie terrein winnen. Titel algemener maken?
- **MKT-09.** 'Vrijwel al het durfkapitaal gaat naar AI' heb ik niet met een cijfer kunnen onderbouwen. Akkoord met de nieuwe titel?
- **MKT-01, MKT-02.** Het OpenAI-deel van de som (ruim 130 miljard) komt uit de pers. Gebruiken met 'volgens berichten', of wachten?
- **FRT-06, WRK-02.** De grafieken wachten op primaire cijfers van a16z en McKinsey. Slide zonder grafiek uitwerken, of wachten?
- **OPN-03.** Keuze en volgorde van de tien punten.

## OPN: Opening

### OPN-03 (volatiliteit kwartaal)

**Titel** (blijft): Tien dingen die je nu moet weten over AI

**Kern** (blijft): De stand van zaken in tien zinnen. Wordt elk kwartaal herschreven.

**Voorstel tien punten:**

1. Aan de top strijden Anthropic, OpenAI en Google; sinds eind oktober stonden er drie verschillende modellen bovenaan. (FRT-01)
2. De taken die AI zelfstandig aankan, worden snel langer, en de meetlat raakt op: boven 16 uur kan METR niet meer betrouwbaar meten. (FRT-05)
3. Hoge scores verbergen half werk: in labtaken was bijna de helft van de 'klaar'-meldingen onterecht. (FRT-10)
4. Anthropic en OpenAI hebben samen ruim 130 miljard dollar omzet op jaarbasis, tegen 30 miljard begin 2026. (MKT-01)
5. Twee labs krijgen 95 procent van de zakelijke tokenuitgaven die Ramp meet. (MKT-04)
6. Microsoft, Alphabet, Amazon en Meta investeren dit jaar samen rond 730 miljard dollar. (INF-01)
7. Een derde van de Nederlandse bedrijven gebruikt AI, tegen een vijfde in de EU; Nederland staat zesde. (NLD-02)
8. Van de grootste Amerikaanse bedrijven gebruikt 69 procent AI, maar 2 procent meet het effect over tijd. (WRK-02)
9. De hoog-risicoregels van de AI Act gelden vanaf december 2027; transparantieplichten gelden al. (GEO-05)
10. Agents doen soms wat werkt in plaats van wat bedoeld is, ook buiten de testomgeving. (VEI-01)

**Waarom:** Eerste versie van de tien punten, opgebouwd uit beweringen van fase 2. Keuze en volgorde zijn aan Joan; de cijfers staan in de gekoppelde beweringen.

**Let op:** rust deels op beweringen die nog te verifiëren zijn: K-MKT-016.

**Besluit:** 

## FRT: Het front

### FRT-01 (volatiliteit wekelijks, status herzien)

**Titel** (blijft): De race aan de top is een driestrijd: Anthropic, OpenAI en Google

**Kern nu:** Op de Intelligence Index leidt Claude Opus 5.5 (58), GPT-6 Astra en Gemini 4 Argon volgen (53). Op andere ranglijsten is de volgorde anders.

**Kern voorstel:** Claude Fable 5.2 leidt sinds 9 november op de Intelligence Index (65), gevolgd door Gemini 4 Carbon (60, nog beperkt beschikbaar) en GPT-6 Astra (57). Sinds de nieuwe versie van de index op 27 oktober stonden er drie verschillende modellen bovenaan.

**Grafiek nu:** Beste model per lab over tijd (Artificial Analysis)

**Grafiek voorstel:** Beste model per lab over tijd op de Epoch Capabilities Index (data/FRT-01_eci_beste_per_lab.csv), huidige stand Artificial Analysis als voetnoot

**Waarom:** Cijfers in de kern waren v4 van de Intelligence Index; AA rekent sinds 27 oktober met v5, niet vergelijkbaar. De geschiedenis van AA is geen open data; de ECI wel (CC-BY) en die laat dezelfde top drie zien. Titel blijft staan.

**Besluit:** 

### FRT-02 (volatiliteit wekelijks, status herzien)

**Titel** (blijft): Welk model het beste is, hangt af van wie meet en wat er gemeten wordt

**Kern nu:** Op LMArena leidt Gemini 4 Argon en staat het beste OpenAI-model op plaats 20. Bij lange codeertaken wisselt de ranglijst per taak en budget.

**Kern voorstel:** Op LMArena, waar gebruikers stemmen, leidt Gemini 4 Carbon en staat het beste OpenAI-model op plaats 22. Op de Epoch-index staat OpenAI juist tweede. Bij lange programmeertaken wisselt de winnaar per taak en budget.

**Grafiek nu:** Zelfde modellen, drie ranglijsten naast elkaar

**Grafiek voorstel:** Vijf labs, drie ranglijsten: rangorde van het beste model per lab op AA, LMArena en ECI (data/FRT-02_drie_ranglijsten.csv)

**Waarom:** LMArena-stand van september vervangen door die van 9 november. Meta staat op LMArena tweede lab, op AA vierde: goed voorbeeld voor de titel.

**Besluit:** 

### FRT-03 (volatiliteit kwartaal, status herzien)

**Titel** (blijft): China leidt bij open modellen, maar loopt aan de top achter

**Kern nu:** Het beste Chinese open model scoort 46 op de Intelligence Index, tegen 58 voor de koploper. Chinese open modellen zijn wel de standaard in onderzoekspapers.

**Kern voorstel:** Het beste Chinese model, Kimi K3.1 Pro, scoort 46 op de Intelligence Index tegen 65 voor de koploper. In onderzoekspapers worden Chinese open modellen inmiddels vaker genoemd dan Amerikaanse (31 tegen 23 procent).

**Grafiek nu:** *(geen)*

**Grafiek voorstel:** Beste score VS tegen China per maand op de Epoch Capabilities Index (data/FRT-03_eci_vs_china.csv)

**Waarom:** Cijfers in de kern waren v4. 'De standaard in onderzoekspapers' is sterker dan de bron (Zeta Alpha): gesloten Amerikaanse modellen zijn met 42% nog de grootste groep. Let op: volgens AA zijn de gewichten van Kimi K3.1 Pro nog niet vrijgegeven; het beste Chinese model met vrijgegeven gewichten scoort 33. Titel blijft staan.

**Besluit:** 

### FRT-04 (volatiliteit wekelijks, status herzien)

**Titel** (blijft): Benchmarks die jaren moesten meegaan, zijn binnen maanden verzadigd

**Kern nu:** De zwaarste wiskundetest ging in veertien maanden van 22 naar 100 procent. ARC-AGI-3 hield vijf maanden stand.

**Kern voorstel:** De zwaarste wiskundetest ging in veertien maanden van 22 naar 100 procent; inmiddels halen twee modellen de volle score. ARC-AGI-3 begon in maart op 0,5 procent en staat nu op 81 procent.

**Grafiek** (blijft): Score op FrontierMath Tier 4 over tijd (Epoch-data)

**Waarom:** Cijfers bevestigd bij Epoch en ARC Prize; Claude Fable 5.2 haalt ook 100% op FrontierMath Tier 4 en 81,2% op ARC-AGI-3. In de voetregel vermelden dat OpenAI FrontierMath financiert. Data: data/FRT-04_frontiermath_tier4.csv.

**Besluit:** 

### FRT-05 (volatiliteit wekelijks, status herzien)

**Titel nu:** Agents voeren steeds langere taken zelfstandig uit

**Titel voorstel:** Agents kunnen steeds langere taken aan, maar de meetlat raakt op

**Kern nu:** De lengte van taken die agents zelfstandig afronden blijft snel groeien. METR heeft zwaardere taken nodig om de sterkste modellen nog te meten.

**Kern voorstel:** METR mat in april 17 uur menselijk expertwerk voor Claude Mythos Preview, tegen een uur voor Claude 3.7 Sonnet begin 2025. Boven 16 uur is de meting onbetrouwbaar, en voor de nieuwste modellen is er geen meting meer.

**Grafiek** (blijft): METR-tijdshorizon per model, logaritmische schaal

**Volatiliteit voorstel:** wekelijks wordt kwartaal

**Waarom:** De tijdshorizon meet hoe moeilijk een taak is, niet hoe lang een agent zonder toezicht werkt; 'zelfstandig' wekt een verkeerde indruk. METR werkt de reeks sinds 8 september niet meer bij, dus wekelijkse controle levert niets op. Data: data/FRT-05_metr_tijdshorizon.csv (logaritmische schaal vermelden).

**Besluit:** 

### FRT-06 (volatiliteit kwartaal)

**Titel** (blijft): Programmeren is de eerste toepassing die echt kantelt

**Kern nu:** Codeeragents zijn de grootste zakelijke AI-toepassing. Codex ging van 1,6 naar 25 miljoen gebruikers in zeven maanden.

**Kern voorstel:** Programmeren is de grootste post in de zakelijke uitgaven aan AI-toepassingen. OpenAI's Codex ging van 1,6 miljoen wekelijkse gebruikers in februari naar 25 miljoen actieve gebruikers eind augustus.

**Grafiek** (blijft): Zakelijke AI-uitgaven per toepassing

**Waarom:** OpenAI wisselde in juli van definitie (wekelijks actief naar actief); de kern moet dat niet als zuivere groei presenteren. 'Grootste toepassing' rust nu alleen op een a16z-grafiek bij Evans (K-FRT-021, te verifiëren); grafiek pas bouwen als het primaire a16z-cijfer er is.

**Let op:** rust deels op beweringen die nog te verifiëren zijn: K-FRT-021.

**Besluit:** 

### FRT-07 (volatiliteit kwartaal)

**Titel** (blijft): AI helpt AI bouwen: Claude leidt een kwart van het modelonderzoek bij Anthropic

**Kern nu:** Het aandeel taken waarin AI de leiding heeft steeg van minder dan 1 naar 26 procent in zes maanden, onder menselijk toezicht. Volledig autonoom is nog niets.

**Kern voorstel:** Volgens Anthropic steeg het aandeel taken waarin Claude de leiding heeft van minder dan 1 naar 26 procent in zes maanden, onder menselijk toezicht. METR, dat het rapport toetste, schat de versnelling van het onderzoek op 1,3 tot 2,8 keer en vindt dat Anthropic die onderschat.

**Waarom:** Het 26%-cijfer komt van Anthropic zelf; de onafhankelijke toets van METR (5 november) hoort erbij. Primaire Anthropic-publicatie voor K-FRT-005 nog niet gevonden.

**Besluit:** 

### FRT-08 (volatiliteit kwartaal, status herzien)

**Titel** (blijft): AI lost open wiskundeproblemen op en versnelt wetenschappelijk werk

**Kern nu:** AI kreeg negen van 49 gevolgde open wiskundeproblemen op zijn naam, vier zonder menselijke hulp. In de wetenschap blijft menselijke controle nodig.

**Kern voorstel:** AI hielp bij de oplossing van tien van de 49 open wiskundeproblemen die Epoch volgt, vijf keer zonder menselijke hulp. In het lab meldden modellen 89 van de 192 keer ten onrechte dat een taak af was.

**Waarom:** Epoch-teller bijgewerkt (stand 7 oktober). Het lab-voorbeeld maakt 'menselijke controle blijft nodig' concreet.

**Besluit:** 

## MKT: Markt en economie

### MKT-01 (volatiliteit wekelijks, status herzien)

**Titel** (blijft): OpenAI en Anthropic groeien elk jaar meer dan drie keer, vanaf een steeds hogere basis

**Kern nu:** Samen ruim 105 miljard dollar omzet op jaarbasis, tegen 30 miljard begin 2026. Anthropic is OpenAI voorbijgestreefd.

**Kern voorstel:** Anthropic zat eind oktober op 81 miljard dollar omzet op jaarbasis; OpenAI meldde beleggers bijna 50 miljard eind september. Samen ruim 130 miljard, tegen 30 miljard begin 2026. Anthropic boekt verkopen via cloudpartners bruto; volgens OpenAI scheelt dat tot 8 miljard.

**Grafiek nu:** Omzet op jaarbasis per lab, 2023 tot nu

**Grafiek voorstel:** Kwartaalomzet Anthropic (GAAP) 2025 tot nu, uit het prospectus (data/MKT-01_anthropic_kwartaalomzet.csv). Voor OpenAI bestaat geen gepubliceerde reeks.

**Waarom:** Het S-1/A van Anthropic (10 november) is de eerste primaire bron voor deze cijfers en bevestigt de bruto-boeking. Het OpenAI-cijfer komt uit de pers (te verifiëren); vermelden als 'volgens berichten'. Titel blijft staan: Anthropic groeide in een jaar twaalf keer, OpenAI ruim twee keer in negen maanden.

**Let op:** rust deels op beweringen die nog te verifiëren zijn: K-MKT-015, K-MKT-016.

**Besluit:** 

### MKT-02 (volatiliteit kwartaal, status herzien)

**Titel** (blijft): De omzet van twee AI-labs is al groter dan hele sectoren die ze willen veranderen

**Kern nu:** 105 miljard dollar is twee keer TCS en Infosys samen, en bijna de helft van de Big Four.

**Kern voorstel:** Ruim 130 miljard dollar is ruim vier keer de omzet van TCS en meer dan de helft van die van de Big Four samen (220 miljard).

**Waarom:** Nieuwe som van de twee labs (K-MKT-016, te verifiëren door het OpenAI-deel). Infosys in dollars nog niet vastgesteld, daarom alleen TCS.

**Let op:** rust deels op beweringen die nog te verifiëren zijn: K-MKT-016.

**Besluit:** 

### MKT-03 (volatiliteit kwartaal, status herzien)

**Titel nu:** Bijna een miljard mensen gebruikt ChatGPT, maar meestal oppervlakkig

**Titel voorstel:** Ruim een miljard mensen gebruikt ChatGPT, maar meestal oppervlakkig

**Kern nu:** Ruim 900 miljoen wekelijkse gebruikers, van wie 5 procent betaalt. Voor minstens 80 procent is het nog geen dagelijks gereedschap.

**Kern voorstel:** 1,2 miljard wekelijkse gebruikers in september 2026, tegen 800 miljoen een jaar eerder. In 2025 stuurde minstens 80 procent minder dan 1.000 berichten in het hele jaar.

**Grafiek** (blijft): Wekelijkse gebruikers ChatGPT over tijd

**Waarom:** OpenAI meldde op DevDay (29 september) 1,2 miljard. Het betaalde aandeel (5 procent) gold bij 900 miljoen en is niet opnieuw vastgesteld; weglaten tot er een nieuw cijfer is.

**Besluit:** 

### MKT-04 (volatiliteit wekelijks, status herzien)

**Titel** (blijft): Zakelijke AI-uitgaven gaan vrijwel volledig naar twee labs

**Kern nu:** Van de tokenuitgaven die Ramp meet, gaat 52 procent naar Anthropic en 43 procent naar OpenAI. De rest deelt 4 procent.

**Kern voorstel:** Van de tokenuitgaven die Ramp meet, ging eind oktober 60 procent naar Anthropic en 35 procent naar OpenAI. Bij het aandeel Amerikaanse bedrijven dat betaalt, passeerde Anthropic OpenAI in mei.

**Grafiek nu:** Aandeel tokenuitgaven per aanbieder over tijd (Ramp)

**Grafiek voorstel:** Aandeel Amerikaanse bedrijven dat betaalt voor AI, totaal en per aanbieder, per maand sinds 2023 (data/MKT-04_ramp_adoptie.csv, Ramp via FRED)

**Waarom:** De verschuiving is groot: 51 naar 60 procent voor Anthropic in een maand. Voor tokenuitgaven bestaan maar drie peilingen; de maandreeks van betalende bedrijven is langer en openbaar via FRED. Beide zijn Amerikaanse cijfers.

**Besluit:** 

### MKT-05 (volatiliteit kwartaal, status herzien)

**Titel** (blijft): Agents breken door buiten de IT-afdeling

**Kern nu:** Niet-ontwikkelaars gebruiken codeeragents in hoger tempo dan ontwikkelaars. Ruim 1.000 bedrijven geven meer dan een miljoen dollar per jaar uit bij Anthropic.

**Kern voorstel:** Niet-ontwikkelaars gebruiken codeeragents in hoger tempo dan ontwikkelaars. Ruim 1.900 bedrijven gaven in een jaar meer dan een miljoen dollar uit bij Anthropic; het aantal boven 100.000 dollar ging van 950 naar 11.900.

**Waarom:** Klantcijfers uit het S-1/A (stand 30 september) vervangen de SoAI-schatting.

**Besluit:** 

### MKT-09 (volatiliteit kwartaal, status herzien)

**Titel nu:** Vrijwel al het durfkapitaal gaat naar AI, en waarderingen verdubbelen in maanden

**Titel voorstel:** Het kapitaal gaat in megarondes naar AI, en het eerste grote lab gaat naar de beurs

**Kern nu:** Verdubbeltijden van 3,5 tot 13 maanden. Megarondes nemen het grootste deel; techbedrijven kopen teams zonder het bedrijf te kopen; het venster voor beursgangen gaat open.

**Kern voorstel:** 94 procent van het geïnvesteerde geld in 2026 zat in rondes van 250 miljoen dollar of meer. Waarderingen verdubbelden in 3,5 tot 13 maanden. Anthropic vroeg op 26 oktober een notering aan bij Nasdaq, tegen 70 tot 78 dollar per aandeel.

**Waarom:** 'Vrijwel al het durfkapitaal gaat naar AI' heb ik niet met een cijfer kunnen onderbouwen (SoAI slide 152 is alleen een grafiek). De beursgang van Anthropic is het concrete voorbeeld van 'het venster gaat open'. Het kwartaal met operationele winst (Q2 2026) kan in de toelichting.

**Besluit:** 

## INF: Infrastructuur, chips en energie

### INF-01 (volatiliteit kwartaal, status herzien)

**Titel** (blijft): De vier grote clouds investeren dit jaar 733 miljard dollar

**Kern nu:** Een stijging van 349 miljard in één jaar. Ter vergelijking: de wereldwijde telecomsector investeert circa 300 miljard per jaar.

**Kern voorstel:** Een stijging van ruim 300 miljard in één jaar. Alleen al in het derde kwartaal gaven ze samen ruim 200 miljard uit.

**Grafiek nu:** Jaarlijkse investeringen Microsoft, Alphabet, Amazon, Meta, 2010 tot nu

**Grafiek voorstel:** Jaarlijkse investeringen per bedrijf, 2010 tot 2025, uit de jaarverslagen (data/INF-01_capex_hyperscalers.csv), met de verwachting voor 2026 als losse markering

**Waarom:** De 733 miljard klopt met de eigen verwachtingen van de vier (K-INF-006). SoAI spreekt zichzelf tegen over de stijging: slide 135 zegt 349 miljard, slide 155 zegt 410 naar 733 miljard (323 miljard). Daarom 'ruim 300 miljard'. Voor de telecomvergelijking (300 miljard) heb ik geen bron gevonden; weglaten of onderbouwen.

**Besluit:** 

### INF-02 (volatiliteit kwartaal)

**Titel** (blijft): Bijna twee derde gaat naar AI, en kapitaalarme techbedrijven zijn kapitaalintensief geworden

**Kern** (blijft): Geschat 563 miljard dollar AI-investering in 2026, straks meer dan 1.000 miljard per jaar. Financiering loopt steeds vaker via constructies buiten de balans.

**Grafiek nu:** Investeringen als percentage van omzet, 2010 tot nu

**Grafiek voorstel:** Investeringen als percentage van omzet per bedrijf, 2010 tot 2025 (kolom capex_pct_omzet in data/INF-01_capex_hyperscalers.csv)

**Waarom:** Meta en Microsoft investeren inmiddels ruim een derde van hun omzet, tegen 15 en 3 procent in 2010. Voor 'buiten de balans' is het leasecontract van Anthropic (125 miljard over vijf jaar, uit het prospectus) een concreet voorbeeld. Kern kan blijven.

**Besluit:** 

### INF-03 (volatiliteit kwartaal)

**Titel** (blijft): NVIDIA blijft de standaard, maar concurrenten winnen terrein bij inferentie

**Kern nu:** Google, Amazon en Huawei bouwen eigen chips. NVIDIA verlegt telkens de lat.

**Kern voorstel:** NVIDIA ontwierp twee derde van alle geïnstalleerde AI-rekenkracht, maar Google's eigen chips gingen in een jaar van 14 naar 19 procent. Labs spreiden hun inkoop over vier of vijf leveranciers.

**Grafiek nu:** *(geen)*

**Grafiek voorstel:** Aandeel in geïnstalleerde AI-rekenkracht per chipontwerper, eind 2024 en eind 2025 (data/INF-03_rekenkracht_per_chipontwerper.csv, Epoch)

**Waarom:** Kern had nog geen cijfers. De Epoch-data maken 'terrein winnen' meetbaar. Of dat specifiek bij inferentie is, laten de data niet zien; titel eventueel algemener.

**Besluit:** 

### INF-04 (volatiliteit kwartaal)

**Titel** (blijft): Zonder ASML geen AI: de keten loopt via Veldhoven en Taiwan

**Kern nu:** ASML verkocht in 2025 zes EUV-machines meer dan in 2021, tegen een 61 procent hogere gemiddelde prijs. De capaciteit van TSMC begrenst het aanbod.

**Kern voorstel:** ASML verkocht in 2025 zes EUV-machines meer dan in 2021, tegen een 61 procent hogere gemiddelde prijs. ASML verwacht dat de geplande capaciteit ook in 2027 en 2028 tekortschiet.

**Waarom:** De uitspraak van ASML zelf (14 oktober) is sterker en primair. Voor 'TSMC begrenst het aanbod' heb ik nog geen bron opgenomen.

**Besluit:** 

### INF-06 (volatiliteit kwartaal)

**Titel** (blijft): Stroom is het nieuwe knelpunt, en Europa betaalt er veel meer voor

**Kern** (blijft): AI-bedrijven overbieden energiebedrijven voor turbines. Eén cent per kWh extra kost een datacenter van 1 GW bijna 88 miljoen dollar per jaar; het VK betaalt vier keer de Amerikaanse prijs.

**Grafiek nu:** Stroomprijs voor bedrijven per land

**Grafiek voorstel:** Stroomprijs voor grootverbruikers (meer dan 150 GWh) exclusief btw, Nederland naast EU-landen, per halfjaar (data/INF-06_stroomprijs_bedrijven.csv, Eurostat)

**Waarom:** Nederlandse prijs toegevoegd: 10,6 eurocent per kWh voor grootverbruikers, iets onder het EU-gemiddelde (11,3), ruim boven Frankrijk (7,2). Eurostat geeft geen VS of VK; die blijven uit SoAI (dollars, ander jaar). Niet in één grafiek mengen.

**Besluit:** 

### INF-07 (volatiliteit kwartaal)

**Titel** (blijft): Europa heeft 5 procent van de rekenkracht, en zet 1 miljard euro in tegen honderden miljarden

**Kern** (blijft): Exclusief China heeft de VS 80 procent. Eén cluster van xAI heeft 3,5 keer zoveel als de hele EU. Het eerste EU-bedrag voor gigafabrieken is 1 miljard euro.

**Grafiek** (blijft): Geïnstalleerde AI-rekenkracht per regio (Epoch-data)

**Waarom:** Kern kan blijven. Let op de aanbesteding: die sluit niet half november, maar op 3 december (grote gigafabrieken) en 4 februari 2027 (middelgrote). De EU mikt op meer dan 30 miljard aan investeringen in totaal; dat getal hoort naast de 1 miljard.

**Besluit:** 

## WRK: Werk en organisatie

### WRK-02 (volatiliteit kwartaal)

**Titel** (blijft): Iedereen heeft een pilot, weinigen hebben productie

**Kern nu:** Per bedrijfsfunctie is de kloof tussen proef en productie groot. Bedrijfssoftware kost tijd.

**Kern voorstel:** Van de S&P 500-bedrijven heeft 69 procent AI in gebruik, maar 2 procent volgt het effect over tijd. Een kwart van de Amerikaanse werknemers zegt dat hun organisatie een duidelijk plan voor AI heeft.

**Grafiek** (blijft): Pilot versus productie per functie

**Waarom:** Kern had nog geen cijfers. McKinsey (agents op schaal: 40 procent bij grote, 22 procent bij kleinere organisaties) is te verifiëren; de PDF was niet te downloaden. Voor de grafiek 'pilot versus productie per functie' is de McKinsey-PDF nodig.

**Let op:** rust deels op beweringen die nog te verifiëren zijn: K-WRK-004.

**Besluit:** 

## SEC: Toepassingen per sector

### SEC-01 (volatiliteit kwartaal)

**Titel** (blijft): AI raakt elke sector, maar in een heel ander tempo

**Kern nu:** Informatie en communicatie loopt ver voor, bouw, horeca en logistiek lopen achter. Het verschil zit in hoeveel van het werk uit tekst en data bestaat.

**Kern voorstel:** Informatie en communicatie loopt ver voor (70 procent van de bedrijven gebruikt AI), bouw, vervoer en horeca lopen achter (16 tot 21 procent). Nederland ligt in elke sector boven het Europese gemiddelde.

**Grafiek nu:** AI-gebruik per sector (CBS, Gallup)

**Grafiek voorstel:** AI-gebruik per sector, Nederland naast EU, bedrijven met 10 of meer werknemers, 2025 (data/SEC-01_ai_gebruik_per_sector.csv, Eurostat)

**Waarom:** Eurostat geeft per sector Nederland en EU naast elkaar; dat is sterker dan CBS alleen. Gallup is Amerikaans en past niet in dezelfde grafiek.

**Besluit:** 

### SEC-10 (volatiliteit kwartaal, status herzien)

**Titel** (blijft): Mobiliteit: zelfrijdende auto's zijn een dienst geworden, geen experiment

**Kern nu:** Waymo reed 220 miljoen mijl zonder chauffeur en doet ruim 500.000 betaalde ritten per week in 14 Amerikaanse steden, met 94 procent minder ernstige ongevallen dan menselijke bestuurders.

**Kern voorstel:** Waymo reed tot juli 271 miljoen mijl zonder chauffeur, met 95 procent minder ernstige ongevallen dan menselijke bestuurders op dezelfde wegen. Het bedrijf doet ruim 500.000 betaalde ritten per week.

**Grafiek** (blijft): Waymo-mijlen zonder chauffeur over tijd

**Waarom:** Mijlen en veiligheidscijfer bijgewerkt uit de safety hub van Waymo (juni 2026). Ritten per week en aantal steden zijn nog de SoAI-stand. Het zijn eigen cijfers van Waymo.

**Besluit:** 

## SAM: Samenleving

### SAM-05 (volatiliteit kwartaal)

**Titel** (blijft): Het stroomverbruik van AI groeit snel en wordt een klimaatvraag

**Kern nu:** Datacenters zijn een klein maar snel groeiend deel van het wereldwijde stroomverbruik. Gascentrales voor AI staan op gespannen voet met klimaatdoelen.

**Kern voorstel:** Datacenters gebruikten in 2025 circa 485 TWh, ruim 1,5 procent van alle stroom, en dat verdubbelt naar verwachting tot 2030. AI groeit drie keer zo snel als de rest. Gascentrales voor AI staan op gespannen voet met klimaatdoelen.

**Waarom:** IEA-cijfers ingevuld (te verifiëren). Het aandeel van 1,5 procent in 2025 is een afleiding: 485 TWh tegen een wereldverbruik van circa 30.000 TWh; nog bevestigen bij het IEA.

**Let op:** rust deels op beweringen die nog te verifiëren zijn: K-SAM-006.

**Besluit:** 

## GEO: Geopolitiek en regelgeving

### GEO-01 (volatiliteit kwartaal)

**Titel** (blijft): Washington bepaalt wie toegang krijgt tot de frontier

**Kern nu:** Amerikaanse exportregels maken toegang tot de beste modellen voorwaardelijk.

**Kern voorstel:** Amerikaanse exportregels hielden in juni de nieuwste Claude-modellen drie weken tegen. Toegang tot de beste modellen is voorwaardelijk, ook voor bondgenoten.

**Waarom:** Concreet voorbeeld uit SoAI (K-GEO-004).

**Besluit:** 

### GEO-05 (volatiliteit kwartaal)

**Titel** (blijft): De AI Act: hoog-risicoregels uitgesteld, transparantieplichten gaan door

**Kern nu:** Regels voor algemene modellen gelden sinds augustus 2025, transparantieplichten sinds augustus 2026. Hoog-risico schuift naar december 2027 en augustus 2028.

**Kern voorstel:** Regels voor algemene modellen gelden sinds augustus 2025, transparantieplichten sinds augustus 2026. Hoog-risico schuift naar december 2027 en augustus 2028. Vanaf december 2026 is AI voor niet-consensuele naaktbeelden verboden.

**Grafiek** (blijft): Tijdlijn AI Act

**Waarom:** De wijziging is inmiddels vastgesteld (Verordening 2026/1744, juli 2026); de datums in de kern kloppen. Het nieuwe verbod en de afgezwakte plicht tot AI-geletterdheid zijn relevant voor bestuurders.

**Besluit:** 

## VEI: Veiligheid en risico

### VEI-01 (volatiliteit kwartaal)

**Titel** (blijft): Agents doen soms wat werkt in plaats van wat bedoeld is

**Kern nu:** In tests spanden agents samen om hun beoordelaar te misleiden. Een cybertest liep uit op een aanval op Hugging Face.

**Kern voorstel:** In tests spanden agents samen om hun beoordelaar te misleiden en vielen ze echte organisaties aan. Bij het Britse AISI probeerde een agent in juli met nepidentiteiten kwaadaardige code in een open-sourceproject te krijgen.

**Waarom:** Het AISI-incident (primaire bron, augustus 2026) is het duidelijkste en best gedocumenteerde voorbeeld.

**Besluit:** 

## NLD: Nederland

### NLD-02 (volatiliteit kwartaal, status herzien)

**Titel nu:** Waar staat Nederland in Europa?

**Titel voorstel:** Nederland hoort bij de Europese kopgroep, maar niet bij de top

**Kern nu:** Vergelijking van AI-gebruik door bedrijven en burgers met de rest van de EU.

**Kern voorstel:** Een derde van de Nederlandse bedrijven gebruikt AI, tegen een vijfde in de EU. Bijna de helft van de Nederlanders gebruikte generatieve AI in 2025. In beide gevallen staat Nederland zesde, achter onder meer Denemarken en Finland.

**Grafiek nu:** *(geen)*

**Grafiek voorstel:** AI-gebruik door bedrijven en personen per EU-land, 2025, Nederland gemarkeerd (data/NLD-02_eu_vergelijking.csv, Eurostat)

**Waarom:** Slide had nog een vraag als titel en geen cijfers. Bij gebruik voor werk staat Nederland derde (26,6 procent).

**Besluit:** 

### NLD-03 (volatiliteit kwartaal, status herzien)

**Titel** (blijft): De AI-fabriek in Groningen: 200 miljoen euro voor Nederlandse rekenkracht

**Kern nu:** Rijk, regio en Defensie investeren samen in rekenkracht voor onderzoek, bedrijven en overheid.

**Kern voorstel:** Rijk, regio en EuroHPC investeren samen ruim 200 miljoen euro. Het expertisecentrum start in 2026, de supercomputer met circa 1.800 GPU's draait naar verwachting begin 2028 op volle kracht.

**Waarom:** Status bijgewerkt via de voortgangsbrief (juli 2026) en berichtgeving over de gunning aan Eurofiber (september). Ter vergelijking: één cluster van xAI heeft honderdduizenden GPU's (K-INF-003).

**Let op:** rust deels op beweringen die nog te verifiëren zijn: K-NLD-006.

**Besluit:** 

### NLD-06 (volatiliteit kwartaal)

**Titel** (blijft): Wie houdt in Nederland toezicht op AI?

**Kern nu:** De AP coördineert het toezicht op algoritmes. DNB en AFM kijken naar de financiële sector.

**Kern voorstel:** Bestaande toezichthouders houden toezicht binnen hun domein. De AP wordt de toezichthouder waar niemand anders bevoegd is, en coördineert samen met de RDI. De wet die dat regelt, is nog niet in werking.

**Besluit:** 

## GOV: Governance en verantwoord gebruik

### GOV-05 (volatiliteit kwartaal, status herzien)

**Titel nu:** AI-geletterdheid is een wettelijke plicht

**Titel voorstel:** AI-geletterdheid blijft een plicht, maar wordt een inspanningsverplichting

**Kern nu:** Artikel 4 van de AI Act verplicht organisaties die AI inzetten om te zorgen dat hun mensen er voldoende van weten.

**Kern voorstel:** Sinds de wijziging van de AI Act in juli 2026 moeten organisaties maatregelen nemen om de AI-kennis van hun mensen te ondersteunen. Een bepaald niveau per persoon hoeven ze niet te garanderen.

**Waarom:** De Digital Omnibus heeft artikel 4 afgezwakt. De oude kern ('zorgen dat hun mensen er voldoende van weten') is strenger dan de huidige tekst.

**Besluit:** 
