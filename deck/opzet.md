# AI in 2026: een overzicht voor bestuurders en commissarissen

Opzet, stand 2026-11-10. 100 slides. Gegenereerd uit `deck/opzet.yaml`; niet met de hand bewerken.

Volatiliteit: **W** = wekelijks gecontroleerd, **K** = per kwartaal, **S** = stabiel.

## Opening (3)

**OPN-01** [W] **AI in 2026: een overzicht voor bestuurders en commissarissen**  
Naslagwerk, wekelijks bijgewerkt. Elke slide heeft een vast ID, een bron en een peildatum.

**OPN-02** [W] **Wat is er deze week veranderd**  
Maximaal tien punten uit het weekverslag, met per punt de geraakte slides.

**OPN-03** [K] **Tien dingen die je nu moet weten over AI**  
De stand van zaken in tien zinnen. Wordt elk kwartaal herschreven.

## Hoe het werkt (11)

**BAS-01** [S] **Elke 10 tot 15 jaar verschuift het platform, en AI is de volgende verschuiving**  
Mainframe, pc, web, smartphone, generatieve AI. Elke verschuiving herverdeelde de techsector en daarna de rest van de economie.
<br><sub>Bronnen: evans</sub>

**BAS-02** [S] **Een taalmodel voorspelt het volgende woord, en op grote schaal levert dat bruikbare intelligentie op**  
Het principe is eenvoudig. Schaal in data, rekenkracht en modelgrootte maakt het verschil.

**BAS-03** [S] **Een model ontstaat in drie stappen: voortraining, natraining en versterkend leren**  
Voortraining op tekst, natraining op voorbeelden en voorkeuren, versterkend leren op taken met controleerbare uitkomst. Het recept is inmiddels grotendeels openbaar.
<br><sub>Bronnen: soai</sub>

**BAS-04** [S] **Redeneermodellen denken eerst na, en dat kost rekentijd per antwoord**  
Meer rekentijd bij het antwoorden geeft betere antwoorden. Daardoor zegt de prijs per token weinig over de prijs van een antwoord.
<br><sub>Bronnen: soai</sub>

**BAS-05** [S] **Een agent is een model met gereedschap. Zelfde model, beter harnas, betere agent.**  
Het harnas (instructies, tools, skills, geheugen) bepaalt een groot deel van de prestatie. Agents kiezen steeds vaker zelf hun gereedschap.
<br><sub>Bronnen: soai</sub>

**BAS-06** [S] **Context is het werkgeheugen: wat het model niet ziet, weet het niet**  
Contextvenster, ophalen van documenten en geheugen. Het samenstellen van de juiste context wordt een vak op zich.
<br><sub>Bronnen: soai, iconiq</sub>

**BAS-07** [K] **Modellen zien, horen en spreken nu in één doorlopende interactie**  
Multimodaal is realtime geworden: spraak, beeld en video in gesprek, en video die je tijdens het genereren kunt bijsturen.
<br><sub>Bronnen: soai</sub>

**BAS-08** [K] **Open of gesloten gewichten is een strategische keuze, geen technisch detail**  
Open modellen geven controle, lagere kosten en onafhankelijkheid. Gesloten modellen lopen voorop in prestaties. Chinese labs domineren het open segment.
<br><sub>Bronnen: soai</sub>

**BAS-09** [S] **Modellen maken fouten die overtuigend klinken**  
Verzonnen feiten en taken die 'klaar' heten maar dat niet zijn. In labtaken was bijna de helft van de 'klaar'-meldingen onvolledig. Controle blijft nodig.
<br><sub>Bronnen: soai</sub>

**BAS-10** [K] **Intelligentie wordt snel goedkoper, en toch stijgen de totale uitgaven**  
De prijs per eenheid prestatie daalt hard. Het gebruik groeit harder, vooral door agents en redeneermodellen.
<br><sub>Bronnen: soai, epoch, artificial-analysis</sub>

**BAS-11** [K] **Wereldmodellen leren hoe de fysieke wereld werkt**  
Gesimuleerde werelden waarin agents, robots en auto's oefenen voordat ze de echte wereld in gaan.
<br><sub>Bronnen: soai</sub>

## Het front (13)

**FRT-01** [W] **De race aan de top is een driestrijd: Anthropic, OpenAI en Google**  
Op de Intelligence Index leidt Claude Opus 5.5 (58), GPT-6 Astra en Gemini 4 Argon volgen (53). Op andere ranglijsten is de volgorde anders.
<br><sub>Bronnen: artificial-analysis, soai</sub>

**FRT-02** [W] **Welk model het beste is, hangt af van wie meet en wat er gemeten wordt**  
Op LMArena leidt Gemini 4 Argon en staat het beste OpenAI-model op plaats 20. Bij lange codeertaken wisselt de ranglijst per taak en budget.
<br><sub>Bronnen: lmarena, artificial-analysis, soai</sub>

**FRT-03** [K] **China leidt bij open modellen, maar loopt aan de top achter**  
Het beste Chinese open model scoort 46 op de Intelligence Index, tegen 58 voor de koploper. Chinese open modellen zijn wel de standaard in onderzoekspapers.
<br><sub>Bronnen: soai, artificial-analysis</sub>

**FRT-04** [W] **Benchmarks die jaren moesten meegaan, zijn binnen maanden verzadigd**  
De zwaarste wiskundetest ging in veertien maanden van 22 naar 100 procent. ARC-AGI-3 hield vijf maanden stand.
<br><sub>Bronnen: epoch, soai</sub>

**FRT-05** [W] **Agents voeren steeds langere taken zelfstandig uit**  
De lengte van taken die agents zelfstandig afronden blijft snel groeien. METR heeft zwaardere taken nodig om de sterkste modellen nog te meten.
<br><sub>Bronnen: metr, soai · Open: Actuele METR-cijfers ophalen</sub>

**FRT-06** [K] **Programmeren is de eerste toepassing die echt kantelt**  
Codeeragents zijn de grootste zakelijke AI-toepassing. Codex ging van 1,6 naar 25 miljoen gebruikers in zeven maanden.
<br><sub>Bronnen: soai, evans</sub>

**FRT-07** [K] **AI helpt AI bouwen: Claude leidt een kwart van het modelonderzoek bij Anthropic**  
Het aandeel taken waarin AI de leiding heeft steeg van minder dan 1 naar 26 procent in zes maanden, onder menselijk toezicht. Volledig autonoom is nog niets.
<br><sub>Bronnen: soai</sub>

**FRT-08** [K] **AI lost open wiskundeproblemen op**  
Epoch volgt 49 onopgeloste onderzoeksproblemen. AI kreeg voor negen daarvan de oplossing op zijn naam, vier zonder menselijke hulp.
<br><sub>Bronnen: epoch, soai</sub>

**FRT-09** [K] **AI versnelt wetenschappelijk werk, maar menselijke controle blijft nodig**  
Scores op wetenschappelijke taken verdubbelden in weken. Verificatie vermindert verzonnen resultaten, maar haalt ze niet weg.
<br><sub>Bronnen: soai</sub>

**FRT-10** [K] **Door AI ontdekte medicijnen zitten in fase 3**  
Eiwitmodellen, ontworpen antilichamen en de eerste kandidaten in de laatste klinische fase.
<br><sub>Bronnen: soai</sub>

**FRT-11** [K] **Robotica heeft zijn GPT-2-moment: generalisatie groeit mee met voortraining**  
Robotmodellen generaliseren beter naarmate ze meer voortraining krijgen. Data over handelen is het knelpunt, simulatie een deel van de oplossing.
<br><sub>Bronnen: soai</sub>

**FRT-12** [K] **Zelfrijdende auto's zijn een dienst geworden, geen experiment**  
Waymo reed 220 miljoen mijl zonder chauffeur en doet ruim 500.000 betaalde ritten per week in 14 Amerikaanse steden, met 94 procent minder ernstige ongevallen dan menselijke bestuurders.
<br><sub>Bronnen: soai</sub>

**FRT-13** [K] **Hoge scores verbergen nog veel half werk**  
Agents die goed scoren op benchmarks laten in de praktijk analyses onaf, missen fraude en ontdekken de regels van onbekende situaties slecht.
<br><sub>Bronnen: soai</sub>

## Markt en economie (14)

**MKT-01** [W] **OpenAI en Anthropic groeien elk jaar meer dan drie keer, vanaf een steeds hogere basis**  
Samen ruim 105 miljard dollar omzet op jaarbasis, tegen 30 miljard begin 2026. Anthropic is OpenAI voorbijgestreefd.
<br><sub>Bronnen: soai, lab-blogs · Open: Boekhoudverschil vermelden: OpenAI zegt dat bruto-boeking Anthropic tot 8 miljard dollar hoger laat uitkomen</sub>

**MKT-02** [K] **De omzet van twee AI-labs is al groter dan hele sectoren die ze willen veranderen**  
105 miljard dollar is twee keer TCS en Infosys samen, en bijna de helft van de Big Four.
<br><sub>Bronnen: soai</sub>

**MKT-03** [K] **Bijna een miljard mensen gebruikt ChatGPT, maar meestal oppervlakkig**  
Ruim 900 miljoen wekelijkse gebruikers, van wie 5 procent betaalt. Voor minstens 80 procent is het nog geen dagelijks gereedschap.
<br><sub>Bronnen: evans, openai-research</sub>

**MKT-04** [W] **Zakelijke AI-uitgaven gaan vrijwel volledig naar twee labs**  
Van de tokenuitgaven die Ramp meet, gaat 52 procent naar Anthropic en 43 procent naar OpenAI. De rest deelt 4 procent.
<br><sub>Bronnen: ramp, soai</sub>

**MKT-05** [K] **Agents breken door buiten de IT-afdeling**  
Niet-ontwikkelaars gebruiken codeeragents in hoger tempo dan ontwikkelaars. Ruim 1.000 bedrijven geven meer dan een miljoen dollar per jaar uit bij Anthropic.
<br><sub>Bronnen: soai</sub>

**MKT-06** [K] **Eén productlancering kostte softwarebedrijven 285 miljard dollar aan beurswaarde**  
Na de lancering van Claude Cowork daalde de softwarebeurs in februari scherp. In september was het verlies goedgemaakt, maar de vraag blijft of prijzen per gebruiker overleven.
<br><sub>Bronnen: soai</sub>

**MKT-07** [S] **Voor de meeste toepassingen lijken modellen sterk op elkaar**  
Er zijn geen netwerkeffecten tussen modellen. Waarde verschuift naar product, distributie en integratie in werkprocessen.
<br><sub>Bronnen: evans</sub>

**MKT-08** [K] **AI verkoopt steeds vaker het werk, niet het gereedschap**  
Prijzen op basis van verbruik en resultaat nemen toe. Aanbieders rekenen af per afgehandelde taak in plaats van per gebruiker.
<br><sub>Bronnen: iconiq, soai</sub>

**MKT-09** [K] **AI-producten zijn een omzet- en margeverhaal geworden**  
Bij AI-bouwers stijgt het aandeel AI in de omzet van 32 naar 42 procent, met brutomarges van 45 naar 53 procent.
<br><sub>Bronnen: iconiq</sub>

**MKT-10** [K] **Bedrijven gebruiken meerdere modellen naast elkaar**  
AI-bouwers gebruiken gemiddeld 3,3 aanbieders. Betrouwbaarheid en kosten bepalen de keuze, beveiliging weegt steeds zwaarder.
<br><sub>Bronnen: iconiq</sub>

**MKT-11** [K] **Het meeste gebruik is serieus werk, met de mens aan het stuur**  
56 procent van de onderzochte gesprekken ging over belangrijk werk. In 72 procent leidde de mens en assisteerde AI.
<br><sub>Bronnen: soai, anthropic-econ</sub>

**MKT-12** [K] **Waarderingen van AI-bedrijven verdubbelen in maanden**  
Verdubbeltijden van 3,5 tot 13 maanden. Megarondes nemen het grootste deel van het kapitaal, en vrijwel alleen AI trekt nog durfkapitaal.
<br><sub>Bronnen: soai</sub>

**MKT-13** [K] **De labs worden ook adviesbureau**  
OpenAI en Anthropic zetten eigen adviesbedrijven op met private-equitygeld. Invoering in organisaties blijft handwerk.
<br><sub>Bronnen: soai, evans</sub>

**MKT-14** [K] **Grote techbedrijven kopen teams zonder het bedrijf te kopen**  
Licentie-plus-overnamedeals omzeilen fusietoezicht. Het venster voor beursgangen gaat weer open.
<br><sub>Bronnen: soai</sub>

## Infrastructuur (11)

**INF-01** [K] **De vier grote clouds investeren dit jaar 733 miljard dollar**  
Een stijging van 349 miljard in één jaar. Ter vergelijking: de wereldwijde telecomsector investeert circa 300 miljard per jaar.
<br><sub>Bronnen: earnings, soai, evans</sub>

**INF-02** [K] **Bijna twee derde van die investeringen gaat naar AI**  
Geschat 563 miljard dollar AI-investering in 2026. Voor 2027 tot 2030 verwacht de markt meer dan 1.000 miljard per jaar.
<br><sub>Bronnen: soai</sub>

**INF-03** [K] **Kapitaalarme techbedrijven zijn kapitaalintensief geworden**  
Investeringen als aandeel van de omzet zijn verveelvoudigd. Financiering loopt steeds vaker via constructies buiten de balans.
<br><sub>Bronnen: evans, soai</sub>

**INF-04** [K] **NVIDIA blijft de standaard, maar concurrenten winnen terrein bij inferentie**  
Google, Amazon en Huawei bouwen eigen chips. NVIDIA verlegt telkens de lat.
<br><sub>Bronnen: soai, earnings</sub>

**INF-05** [K] **Zonder ASML geen AI: de keten loopt via Veldhoven en Taiwan**  
ASML verkocht in 2025 zes EUV-machines meer dan in 2021, tegen een 61 procent hogere gemiddelde prijs. De capaciteit van TSMC begrenst het aanbod.
<br><sub>Bronnen: soai, earnings</sub>

**INF-06** [K] **Rekenkracht is schaars: oude chips blijven verhuurd en prijzen stijgen weer**  
GPU-huurprijzen liggen boven hun dieptepunt. Chips van zes en negen jaar oud worden nog verhuurd.
<br><sub>Bronnen: soai</sub>

**INF-07** [K] **Stroom is het nieuwe knelpunt**  
AI-bedrijven overbieden energiebedrijven voor turbines. Oude kolencentrales worden gascampussen voor datacenters.
<br><sub>Bronnen: soai, iea-energy-ai</sub>

**INF-08** [K] **Europa betaalt veel meer voor stroom, en dat weegt zwaar bij datacenters**  
Eén cent per kWh extra kost een datacenter van 1 GW bijna 88 miljoen dollar per jaar. Finland en de VS zitten rond 8,5 cent, het VK op 37 cent.
<br><sub>Bronnen: soai, iea-energy-ai · Open: Nederlandse prijs toevoegen</sub>

**INF-09** [K] **Europa heeft 5 procent van de rekenkracht, de VS 80 procent**  
Exclusief China. Eén cluster van xAI in Memphis heeft 3,5 keer zoveel rekenkracht als de hele EU.
<br><sub>Bronnen: epoch, soai</sub>

**INF-10** [K] **Europa zet 1 miljard euro in, Amerika honderden miljarden**  
Het eerste EU-bedrag voor AI-gigafabrieken is 1 miljard euro. De groei van de Amerikaanse investeringen in één jaar is ruim tien keer zo groot.
<br><sub>Bronnen: soai</sub>

**INF-11** [S] **Is dit een bubbel? De betere vraag is wanneer gebruik en kosten in evenwicht komen**  
Prijs, gebruik en investeringen zijn niet in evenwicht. Mobiele netwerken rond 2010 zijn een leerzame vergelijking.
<br><sub>Bronnen: evans</sub>

## Werk en organisatie (11)

**WRK-01** [S] **Eerst automatiseren we het voor de hand liggende, daarna verandert het werk zelf**  
Nieuwe technologie wordt eerst ingepast in bestaand werk, dan ontstaan nieuwe werkwijzen, pas daarna nieuwe bedrijven en markten.
<br><sub>Bronnen: evans</sub>

**WRK-02** [K] **Iedereen heeft een pilot, weinigen hebben productie**  
Per bedrijfsfunctie is de kloof tussen proef en productie groot. Bedrijfssoftware kost tijd.
<br><sub>Bronnen: evans, mckinsey-sai</sub>

**WRK-03** [K] **De meeste winst zit nu in programmeren, klantenservice en marketing**  
Programmeerhulp levert de grootste productiviteitswinst. In Nederland is marketing en verkoop de meest genoemde toepassing.
<br><sub>Bronnen: iconiq, cbs</sub>

**WRK-04** [K] **Agents hebben nog vaak een mens nodig om de taak af te maken**  
Bij taken met meerdere stappen of veel context grijpt een mens vaak in. De gemeten productiviteitswinst van agents blijft daardoor beperkt.
<br><sub>Bronnen: iconiq</sub>

**WRK-05** [S] **Een taak automatiseren is iets anders dan een baan vervangen**  
De liftbediende verdween, de accountant niet. Automatisering verandert vaker het werk dan dat ze het opheft.
<br><sub>Bronnen: evans</sub>

**WRK-06** [K] **Jonge werknemers lijken het eerst geraakt**  
De instroom van 22- tot 25-jarigen in beroepen die AI raakt is vertraagd. De oorzaak is onzeker, de werkloosheid in die beroepen is niet duidelijk gestegen.
<br><sub>Bronnen: soai, anthropic-econ</sub>

**WRK-07** [S] **AI kan ook kennis kosten**  
Ontwikkelaars die met AI een nieuwe bibliotheek leerden, konden de code daarna slechter uitleggen en fouten slechter vinden.
<br><sub>Bronnen: soai</sub>

**WRK-08** [K] **De bouw van AI levert ook banen op**  
In de VS naar schatting 320.000 extra banen in infrastructuur en 730.000 in AI-gerelateerde beroepen.
<br><sub>Bronnen: soai</sub>

**WRK-09** [K] **Organisaties worden platter, met een andere mix van rollen**  
45 procent van de AI-bouwers plant een andere rolverdeling, 33 procent een kleiner team. Forward deployed engineers zijn de nieuwe schakel naar de klant.
<br><sub>Bronnen: iconiq</sub>

**WRK-10** [K] **De koplopers besteden honderden keren meer aan AI per medewerker**  
De top 1 procent besteedt 580 keer zoveel als de mediaan. Zware gebruikers groeiden in omzet drie keer zo snel; oorzaak en gevolg zijn niet gescheiden.
<br><sub>Bronnen: soai, ramp</sub>

**WRK-11** [K] **De kosten van interne AI zijn moeilijk te voorspellen**  
Overschrijdingen komen uit tokens, data-infrastructuur en training van medewerkers. Tokenuitgaven zeggen weinig over succes.
<br><sub>Bronnen: iconiq</sub>

## Geopolitiek en regelgeving (11)

**GEO-01** [K] **Washington bepaalt wie toegang krijgt tot de frontier**  
Amerikaanse exportregels maken toegang tot de beste modellen voorwaardelijk.
<br><sub>Bronnen: soai</sub>

**GEO-02** [K] **Wie bepaalt de grenzen van militair AI-gebruik: de overheid of het lab?**  
Het conflict tussen Anthropic en het Pentagon, terwijl frontier-AI al in militaire operaties wordt ingezet.
<br><sub>Bronnen: soai</sub>

**GEO-03** [K] **67 landen bouwen aan soevereine AI**  
Buiten de VS en China lopen 184 overheidsprojecten met samen circa 84 miljard dollar aan bekende budgetten.
<br><sub>Bronnen: cnas-sovereign, soai</sub>

**GEO-04** [S] **Soevereiniteit kun je niet huren, dus moeten de meeste landen onderhandelen**  
Wie niet aan de frontier meedoet, bedient inferentie. Europa kan onderhandelen met locaties, stroom en chipmachines.
<br><sub>Bronnen: soai</sub>

**GEO-05** [K] **China bouwt een eigen keten, van stroom tot chips**  
Goedkope stroom bevoordeelt Chinese chips. China beperkt nu ook de export van kennis.
<br><sub>Bronnen: soai</sub>

**GEO-06** [K] **De AI Act: hoog-risicoregels uitgesteld, transparantieplichten gaan door**  
Regels voor algemene modellen gelden sinds augustus 2025, transparantieplichten sinds augustus 2026. Hoog-risico schuift naar december 2027 en augustus 2028.
<br><sub>Bronnen: eu-ai-act, soai</sub>

**GEO-07** [K] **In de VS reguleren de staten, ondanks Washington**  
Californië bouwt onafhankelijk toezicht op veiligheidsclaims en regelt AI-gezelschap voor kinderen.
<br><sub>Bronnen: soai</sub>

**GEO-08** [K] **Auteursrecht: veel deals met uitgevers, de kernvragen liggen nog bij de rechter**  
Licentieovereenkomsten nemen toe. Uitgevers verzetten zich tegen antwoordmachines die hun werk hergebruiken.
<br><sub>Bronnen: soai</sub>

**GEO-09** [K] **Deepfakes: wat is er inmiddels geregeld**  
Labelplicht voor synthetische inhoud in de EU en een nieuw verbod op niet-consensuele seksuele deepfakes.
<br><sub>Bronnen: eu-ai-act, soai</sub>

**GEO-10** [K] **Verzet tegen datacenters groeit**  
Amerikaanse staten stellen strengere voorwaarden. Het antwoord van Washington: betaal je eigen stroom.
<br><sub>Bronnen: soai</sub>

**GEO-11** [S] **Een Europees frontierlab kost honderden miljarden**  
Eén berekening komt op 790 miljard euro in drie jaar. Dat is de prijs van meedoen aan de top.
<br><sub>Bronnen: soai</sub>

## Veiligheid en risico (9)

**VEI-01** [K] **Agents doen soms wat werkt in plaats van wat bedoeld is**  
In tests spanden agents samen om hun beoordelaar te misleiden. Een cybertest liep uit op een aanval op Hugging Face.
<br><sub>Bronnen: soai</sub>

**VEI-02** [K] **AI voert in testomgevingen complete cyberaanvallen uit**  
Op een aanvalsparcours van 32 stappen (ongeveer 20 uur werk voor een expert) slaagde het sterkste model in 6 van de 10 pogingen.
<br><sub>Bronnen: uk-aisi, soai</sub>

**VEI-03** [K] **Misbruik is geen theorie meer**  
Gedocumenteerd misbruik voor cyberaanvallen, surveillance, beïnvloeding en fraude.
<br><sub>Bronnen: soai, lab-blogs</sub>

**VEI-04** [K] **Open modellen lopen 4 tot 7 maanden achter, en verdedigers hebben ze ook nodig**  
Open modellen vergroten de dreiging, maar verdedigers gebruiken ze ook als gesloten modellen weigeren.
<br><sub>Bronnen: uk-aisi, soai</sub>

**VEI-05** [K] **Agents staan al op laptops voordat de beveiliging het weet**  
Beveiliging hangt af van het model én het harnas. Schaduw-AI met brede rechten is een acuut risico.
<br><sub>Bronnen: soai</sub>

**VEI-06** [K] **Agents lekken al privégegevens**  
Modellen onthouden trainingsdata en agents met geheugen geven gegevens prijs.
<br><sub>Bronnen: soai</sub>

**VEI-07** [K] **Meekijken in het denken van een model werkt maar half**  
Monitors die alleen de redenering zien, missen sabotage. Auditors vinden verborgen gedrag ongeveer de helft van de keren.
<br><sub>Bronnen: soai</sub>

**VEI-08** [K] **Waarden aanleren werkt: chantage in tests daalde van 65 naar 19 procent**  
Of dit in de praktijk standhoudt, is nog niet bewezen.
<br><sub>Bronnen: soai</sub>

**VEI-09** [K] **De leiders van de labs vragen zelf om een rem**  
Labbazen en 1.386 medewerkers willen dat overheden het tempo kunnen vertragen. Wie mag pauzeren en wie controleert, is onbeslist.
<br><sub>Bronnen: soai</sub>

## Nederland (8)

**NLD-01** [K] **Eén op de zes Nederlandse bedrijven gebruikt AI, bij grote bedrijven twee derde**  
17 procent in 2025, tegen 8 procent in 2023. Bij bedrijven met 250 of meer medewerkers 66 procent.
<br><sub>Bronnen: cbs</sub>

**NLD-02** [K] **Het verschil tussen sectoren is groot: ICT 54 procent, bouw en horeca 6 tot 7**  
Marketing en verkoop, administratie en R&D zijn de meest genoemde toepassingen.
<br><sub>Bronnen: cbs</sub>

**NLD-03** [K] **Waar staat Nederland in Europa?**  
Vergelijking van AI-gebruik door bedrijven met de rest van de EU.
<br><sub>Bronnen: eurostat · Open: Eurostat-cijfers 2025 ophalen</sub>

**NLD-04** [K] **De AI-fabriek in Groningen: 200 miljoen euro voor Nederlandse rekenkracht**  
Rijk, regio en Defensie investeren samen in rekenkracht voor onderzoek, bedrijven en overheid.
<br><sub>Bronnen: rijksoverheid · Open: Huidige status en capaciteit verifiëren</sub>

**NLD-05** [S] **Nederland is onmisbaar in de keten, en dat is een onderhandelingspositie**  
Zonder machines van ASML geen geavanceerde chips. Dat geeft Nederland en Europa iets om mee te onderhandelen.
<br><sub>Bronnen: earnings, soai</sub>

**NLD-06** [K] **GPT-NL en andere Nederlandse modellen: wat is het doel?**  
Een eigen taalmodel draait niet om de frontier, maar om transparantie, taal en onafhankelijkheid.
<br><sub>Bronnen: tno · Open: Status GPT-NL verifiëren</sub>

**NLD-07** [K] **Wie houdt in Nederland toezicht op AI?**  
De AP coördineert het toezicht op algoritmes. DNB en AFM kijken naar de financiële sector.
<br><sub>Bronnen: ap-ran, dnb-afm · Open: Aanwijzing markttoezichthouders AI Act in Nederland verifiëren</sub>

**NLD-08** [K] **Netcongestie maakt stroom ook in Nederland een knelpunt voor datacenters**  
Wachtlijsten voor netaansluitingen en beleid voor hyperscale datacenters bepalen waar rekenkracht kan komen.
<br><sub>Bronnen: rijksoverheid · Open: Cijfers netbeheerders en datacenterbeleid ophalen</sub>

## Wat betekent dit voor bestuurders (6)

**BES-01** [S] **Vijf vragen die elke raad van commissarissen nu moet stellen**  
Strategie, waarde, risico, mensen en leveranciers. Brug naar het middagdeel over governance.

**BES-02** [K] **AI-geletterdheid is een wettelijke plicht**  
Artikel 4 van de AI Act verplicht organisaties die AI inzetten om te zorgen dat hun mensen er voldoende van weten.
<br><sub>Bronnen: eu-ai-act · Open: Verifiëren of de Digital Omnibus deze plicht heeft gewijzigd</sub>

**BES-03** [S] **Bouwen, kopen of laten doen: de keuze verschuift**  
Modellen worden uitwisselbaar, aanbieders verkopen werk in plaats van software, en de labs bieden zelf implementatie aan.

**BES-04** [S] **Meet waarde, niet gebruik**  
Aantal gebruikers en tokenuitgaven zeggen weinig. Meet doorlooptijd, kwaliteit en kosten per proces.
<br><sub>Bronnen: iconiq</sub>

**BES-05** [S] **Ken je risico's: schaduw-AI, datalekken en afhankelijkheid van twee leveranciers**  
De drie risico's die nu het vaakst onderschat worden.

**BES-06** [K] **Wat de komende twaalf maanden op de bestuursagenda hoort**  
Concrete agendapunten per kwartaal, afgeleid van de ontwikkelingen in dit deck.

## Vooruitblik (3)

**VBK-01** [K] **Negen voorspellingen voor de komende twaalf maanden, en welke al uitkomen**  
De voorspellingen uit het State of AI Report, met per voorspelling de stand van zaken.
<br><sub>Bronnen: soai</sub>

**VBK-02** [S] **Niemand weet hoe dit afloopt, maar we kunnen wel de goede vragen stellen**  
Bij elke platformverschuiving mislukten de meeste ideeën. Is dit een taak of een baan? Welke nieuwe vragen worden mogelijk?
<br><sub>Bronnen: evans</sub>

**VBK-03** [S] **Bronnen en verder lezen**  
De vaste bronnen achter dit deck, met waar je ze vindt.
<br><sub>Bronnen: soai, evans, iconiq, ai-index, epoch, cbs</sub>
