# AI in 2026: een overzicht voor bestuurders en commissarissen

Opzet, stand 2026-11-11. 100 slides. Gegenereerd uit `deck/opzet.yaml`; niet met de hand bewerken.

Volatiliteit: **W** = wekelijks gecontroleerd, **K** = per kwartaal, **S** = stabiel.

## Opening (3)

**OPN-01** [W] **AI in 2026: een overzicht voor bestuurders en commissarissen**  
Naslagwerk, wekelijks bijgewerkt. Elke slide heeft een vast ID, een bron en een peildatum.

**OPN-02** [W] **Wat is er deze week veranderd**  
Maximaal tien punten uit het weekverslag, met per punt de geraakte slides.

**OPN-03** [K] **Tien dingen die je nu moet weten over AI**  
De stand van zaken in tien zinnen. Wordt elk kwartaal herschreven.

1. Aan de top strijden Anthropic, OpenAI en Google; sinds eind oktober stonden er drie verschillende modellen bovenaan. (FRT-01)
2. Agents kunnen steeds langere taken aan, en de meetlat raakt op: boven 16 uur kan METR niet meer betrouwbaar meten. (FRT-05)
3. Hoge scores verbergen half werk: in labtaken was bijna de helft van de 'klaar'-meldingen onterecht. (FRT-10)
4. Anthropic en OpenAI hebben samen ruim 130 miljard dollar omzet op jaarbasis. (MKT-01)
5. Twee labs krijgen 95 procent van de zakelijke tokenuitgaven die Ramp meet. (MKT-04)
6. Microsoft, Alphabet, Amazon en Meta investeren dit jaar samen rond 730 miljard dollar. (INF-01)
7. Een derde van de Nederlandse bedrijven gebruikt AI, tegen een vijfde in de EU; Nederland staat zesde. (NLD-02)
8. Van de grootste Amerikaanse bedrijven gebruikt 69 procent AI, maar 2 procent meet het effect over tijd. (WRK-02)
9. De hoog-risicoregels van de AI Act gelden vanaf december 2027; transparantieplichten gelden al. (GEO-05)
10. Agents doen soms wat werkt in plaats van wat bedoeld is, ook buiten de testomgeving. (VEI-01)

<br><sub>Open: Punt 4: het OpenAI-deel komt uit de pers (K-MKT-015, te verifiëren); in de voetregel 'volgens berichten'.</sub>

## Hoe het werkt (12)

**BAS-01** [S] **Elke 10 tot 15 jaar verschuift het platform, en AI is de volgende verschuiving**  
Mainframe, pc, web, smartphone, generatieve AI. Elke verschuiving herverdeelde de techsector en daarna de rest van de economie.
<br><sub>Bronnen: evans</sub>

**BAS-02** [S] **AI is ouder dan ChatGPT: zeventig jaar van regels naar leren**  
Van regelgebaseerde systemen via machine learning en deep learning (2012) naar de transformer (2017) en ChatGPT (2022). Elke stap kwam door meer data en rekenkracht.
<br><sub>Bronnen: ai-index</sub>

**BAS-03** [S] **De meeste AI-waarde zat tot nu toe in voorspellende modellen, niet in chatbots**  
Aanbevelingen, fraudedetectie, prijzen en prognoses draaien al jaren op machine learning. Generatieve AI komt daar bovenop, niet in de plaats van.

**BAS-04** [S] **Een taalmodel voorspelt het volgende woord, en op grote schaal levert dat bruikbare intelligentie op**  
Het principe is eenvoudig. Schaal in data, rekenkracht en modelgrootte maakt het verschil.

**BAS-05** [S] **Een model ontstaat in drie stappen: voortraining, natraining en versterkend leren**  
Voortraining op tekst, natraining op voorbeelden en voorkeuren, versterkend leren op taken met controleerbare uitkomst. Het recept is inmiddels grotendeels openbaar.
<br><sub>Bronnen: soai</sub>

**BAS-06** [S] **Trainen en gebruiken zijn twee verschillende rekenklussen**  
Training is een eenmalige, enorme klus op duizenden chips. Gebruik (inferentie) gebeurt bij elke vraag opnieuw en wordt het grootste deel van de rekenkracht.
<br><sub>Bronnen: epoch</sub>

**BAS-07** [S] **Redeneermodellen denken eerst na, en dat kost rekentijd per antwoord**  
Meer rekentijd bij het antwoorden geeft betere antwoorden. Daardoor zegt de prijs per token weinig over de prijs van een antwoord.
<br><sub>Bronnen: soai · Open: Score bij lage inspanning en tokens per taak opnieuw vaststellen op versie 5.0.1; de modelpagina toont alleen de maximale instelling.</sub>

**BAS-08** [S] **Een agent is een model met gereedschap en geheugen. Zelfde model, beter harnas, betere agent.**  
Instructies, tools, skills en de juiste context bepalen een groot deel van de prestatie. Wat het model niet ziet, weet het niet.
<br><sub>Bronnen: soai, iconiq</sub>

**BAS-09** [K] **Modellen zien, horen en spreken nu in één doorlopende interactie**  
Multimodaal is realtime geworden: spraak, beeld en video in gesprek, en video die je tijdens het genereren kunt bijsturen.
<br><sub>Bronnen: soai</sub>

**BAS-10** [K] **Open of gesloten gewichten is een strategische keuze, geen technisch detail**  
Open modellen geven controle, lagere kosten en onafhankelijkheid. Gesloten modellen lopen voorop in prestaties. Chinese labs domineren het open segment.
<br><sub>Bronnen: soai</sub>

**BAS-11** [S] **Modellen maken fouten die overtuigend klinken**  
Verzonnen feiten en taken die 'klaar' heten maar dat niet zijn. In labtaken was bijna de helft van de 'klaar'-meldingen onvolledig. Controle blijft nodig.
<br><sub>Bronnen: soai, vectara</sub>

**BAS-12** [K] **Intelligentie wordt snel goedkoper, en toch stijgen de totale uitgaven**  
De prijs per eenheid prestatie daalt hard. Het gebruik groeit harder, vooral door agents en redeneermodellen.
<br><sub>Bronnen: soai, epoch, artificial-analysis · Open: Gewenste grafiek: Prijs per miljoen tokens bij gelijke prestatie, over tijd (Epoch-data); nu grote getallen; bouwen zodra de Epoch-reeks in data/ staat.</sub>

## Het front (10)

**FRT-01** [W] **De race aan de top is een driestrijd: Anthropic, OpenAI en Google**  
Claude Fable 5.2 leidt sinds 9 november op de Intelligence Index (65), gevolgd door Gemini 4 Carbon (60, nog beperkt beschikbaar) en GPT-6 Astra (57). Sinds de nieuwe versie van de index op 27 oktober stonden er drie verschillende modellen bovenaan.
<br><sub>Bronnen: artificial-analysis, epoch, soai · Open: Huidige stand Artificial Analysis (v5) als voetnoot; de geschiedenis van AA is geen open data.</sub>

**FRT-02** [W] **Welk model het beste is, hangt af van wie meet en wat er gemeten wordt**  
Op LMArena, waar gebruikers stemmen, leidt Gemini 4 Carbon en staat het beste OpenAI-model op plaats 22. Op de Epoch-index staat OpenAI juist tweede. Bij lange programmeertaken wisselt de winnaar per taak en budget.
<br><sub>Bronnen: lmarena, artificial-analysis, epoch, soai</sub>

**FRT-03** [K] **China leidt bij open modellen, maar loopt aan de top achter**  
Het beste Chinese model, Kimi K3.1 Pro, scoort 46 op de Intelligence Index tegen 65 voor de koploper. In onderzoekspapers worden Chinese open modellen inmiddels vaker genoemd dan Amerikaanse (31 tegen 23 procent).
<br><sub>Bronnen: soai, artificial-analysis, epoch · Open: De gewichten van Kimi K3.1 Pro zijn volgens AA nog niet vrijgegeven; het beste Chinese model met vrijgegeven gewichten scoort 33. Vermelden in de toelichting.</sub>

**FRT-04** [W] **Benchmarks die jaren moesten meegaan, zijn binnen maanden verzadigd**  
De zwaarste wiskundetest ging in veertien maanden van 22 naar 100 procent; inmiddels halen twee modellen de volle score. ARC-AGI-3 begon in maart op 0,5 procent en staat nu op 81 procent.
<br><sub>Bronnen: epoch, arc-prize, soai · Open: In de voetregel vermelden dat OpenAI FrontierMath financiert.</sub>

**FRT-05** [K] **Agents kunnen steeds langere taken aan, maar de meetlat raakt op**  
METR mat in april 17 uur menselijk expertwerk voor Claude Mythos Preview, tegen een uur voor Claude 3.7 Sonnet begin 2025. Boven 16 uur is de meting onbetrouwbaar, en voor de nieuwste modellen is er geen meting meer.
<br><sub>Bronnen: metr, epoch, soai · Open: Logaritmische schaal vermelden. METR werkt de reeks sinds 8 september niet meer bij.</sub>

**FRT-06** [K] **Programmeren is de eerste toepassing die echt kantelt**  
Programmeren is met 34 miljard dollar de grootste post in de zakelijke uitgaven aan AI-toepassingen, 7,7 keer zoveel als een jaar eerder. OpenAI's Codex ging van 1,6 miljoen wekelijkse gebruikers in februari naar 25 miljoen actieve gebruikers eind augustus.
<br><sub>Bronnen: soai, evans, menlo · Open: OpenAI wisselde in juli van definitie (wekelijks actief naar actief).</sub>

**FRT-07** [K] **AI helpt AI bouwen: Claude leidt een kwart van het modelonderzoek bij Anthropic**  
Volgens Anthropic steeg het aandeel taken waarin Claude de leiding heeft van minder dan 1 naar 26 procent in zes maanden, onder menselijk toezicht. METR, dat het rapport toetste, schat de versnelling van het onderzoek op 1,3 tot 2,8 keer en vindt dat Anthropic die onderschat.
<br><sub>Bronnen: soai, metr</sub>

**FRT-08** [K] **AI lost open wiskundeproblemen op en versnelt wetenschappelijk werk**  
AI hielp bij de oplossing van tien van de 49 open wiskundeproblemen die Epoch volgt, vijf keer zonder menselijke hulp. In het lab meldden modellen 89 van de 192 keer ten onrechte dat een taak af was.
<br><sub>Bronnen: epoch, soai</sub>

**FRT-09** [K] **Robotica heeft zijn GPT-2-moment: generalisatie groeit mee met voortraining**  
Robotmodellen generaliseren beter naarmate ze meer voortraining krijgen. Data over handelen is het knelpunt; gesimuleerde werelden zijn een deel van de oplossing.
<br><sub>Bronnen: soai, skild-ai, sunday-robotics</sub>

**FRT-10** [K] **Hoge scores verbergen nog veel half werk**  
Agents die goed scoren op benchmarks laten in de praktijk analyses onaf, missen fraude en ontdekken de regels van onbekende situaties slecht.
<br><sub>Bronnen: soai</sub>

## Markt en economie (9)

**MKT-01** [W] **OpenAI en Anthropic groeien elk jaar meer dan drie keer, vanaf een steeds hogere basis**  
Anthropic zat eind oktober op 81 miljard dollar omzet op jaarbasis. OpenAI meldde beleggers eind september volgens berichten bijna 50 miljard. Samen ruim 130 miljard. Anthropic boekte in het derde kwartaal 17,0 miljard dollar omzet, tegen 1,4 miljard een jaar eerder. Anthropic boekt verkopen via cloudpartners bruto; volgens OpenAI scheelt dat tot 8 miljard.
<br><sub>Bronnen: soai, lab-blogs, sec-edgar, financiele-pers · Open: OpenAI-cijfer volgens berichten (K-MKT-015, te verifiëren). Voor OpenAI bestaat geen gepubliceerde reeks; de grafiek toont alleen Anthropic.</sub>

**MKT-02** [K] **De omzet van twee AI-labs is al groter dan hele sectoren die ze willen veranderen**  
Ruim 130 miljard dollar is ruim vier keer de omzet van TCS en meer dan de helft van die van de Big Four samen (220 miljard).
<br><sub>Bronnen: soai, sec-edgar, jaarcijfers-dienstverleners · Open: Het OpenAI-deel van de som komt uit de pers (K-MKT-016, te verifiëren); in de voetregel 'volgens berichten'. Infosys in dollars nog niet vastgesteld.</sub>

**MKT-03** [K] **Ruim een miljard mensen gebruikt ChatGPT, maar meestal oppervlakkig**  
1,2 miljard wekelijkse gebruikers in september 2026, tegen 800 miljoen een jaar eerder. In 2025 stuurde minstens 80 procent minder dan 1.000 berichten in het hele jaar.
<br><sub>Bronnen: evans, openai-research, lab-blogs · Open: Het betaalde aandeel (5 procent) gold bij 900 miljoen gebruikers; weer opnemen als er een nieuw cijfer is.</sub>

**MKT-04** [W] **Zakelijke AI-uitgaven gaan vrijwel volledig naar twee labs**  
Van de tokenuitgaven die Ramp meet, ging eind oktober 60 procent naar Anthropic en 35 procent naar OpenAI. Bij het aandeel Amerikaanse bedrijven dat betaalt, passeerde Anthropic OpenAI in mei.
<br><sub>Bronnen: ramp, soai, menlo · Open: Amerikaanse cijfers; zo vermelden. Menlo (K-MKT-027) ziet met een enquête hetzelfde beeld: 55 procent Anthropic, 31 procent OpenAI.</sub>

**MKT-05** [K] **Bedrijven zetten AI op schaal in: twaalf keer zoveel grote klanten in een jaar**  
Ruim 1.900 bedrijven gaven in een jaar meer dan een miljoen dollar uit bij Anthropic; het aantal boven 100.000 dollar ging van 950 naar 11.900.
<br><sub>Bronnen: soai, sec-edgar</sub>

**MKT-06** [K] **Eén productlancering kostte softwarebedrijven 285 miljard dollar aan beurswaarde**  
Na de lancering van Claude Cowork daalde de softwarebeurs in februari scherp. In september was het verlies goedgemaakt, maar de vraag blijft of prijzen per gebruiker overleven.
<br><sub>Bronnen: soai · Open: Gewenste grafiek: S&P 500 software-index, oktober 2025 tot nu; nu zonder grafiek; de S&P-reeks staat niet in data/.</sub>

**MKT-07** [K] **Modellen zijn uitwisselbaar, en bedrijven gebruiken er meerdere naast elkaar**  
Er zijn geen netwerkeffecten tussen modellen. AI-bouwers gebruiken gemiddeld 3,3 aanbieders; waarde verschuift naar product, distributie en integratie in werkprocessen.
<br><sub>Bronnen: evans, iconiq, ramp, soai</sub>

**MKT-08** [K] **AI verkoopt steeds vaker het werk, niet het gereedschap**  
Prijzen op basis van verbruik en resultaat nemen toe. Bij AI-bouwers stijgt het aandeel AI in de omzet van 32 naar 42 procent, met brutomarges van 45 naar 53 procent.
<br><sub>Bronnen: iconiq, soai</sub>

**MKT-09** [K] **Het kapitaal gaat in megarondes naar AI, en het eerste grote lab gaat naar de beurs**  
94 procent van het geïnvesteerde geld in 2026 zat in rondes van 250 miljoen dollar of meer. Waarderingen verdubbelden in 3,5 tot 13 maanden. Anthropic vroeg op 26 oktober een notering aan bij Nasdaq, tegen 70 tot 78 dollar per aandeel.
<br><sub>Bronnen: soai, sec-edgar · Open: Het kwartaal met operationele winst van Anthropic (Q2 2026) kan in de toelichting.</sub>

## Infrastructuur, chips en energie (8)

**INF-01** [K] **De vier grote clouds investeren dit jaar 733 miljard dollar**  
Een stijging van ruim 300 miljard in één jaar. Alleen al in het derde kwartaal gaven ze samen ruim 200 miljard uit.
<br><sub>Bronnen: earnings, sec-edgar, soai, evans · Open: SoAI spreekt zichzelf tegen over de stijging (349 of 323 miljard); daarom 'ruim 300 miljard'. De vergelijking met de telecomsector is geschrapt: geen bron.</sub>

**INF-02** [K] **Bijna twee derde gaat naar AI, en kapitaalarme techbedrijven zijn kapitaalintensief geworden**  
Geschat 563 miljard dollar AI-investering in 2026, straks meer dan 1.000 miljard per jaar. Financiering loopt steeds vaker via constructies buiten de balans.
<br><sub>Bronnen: soai, evans, sec-edgar · Open: Voorbeeld van financiering buiten de balans: het leasecontract van Anthropic, 125 miljard dollar over vijf jaar (K-INF-009).</sub>

**INF-03** [K] **NVIDIA blijft de standaard, maar eigen chips van anderen winnen terrein**  
NVIDIA ontwierp twee derde van alle geïnstalleerde AI-rekenkracht, maar Google's eigen chips gingen in een jaar van 14 naar 19 procent. Labs spreiden hun inkoop over vier of vijf leveranciers.
<br><sub>Bronnen: soai, earnings, epoch · Open: De data laten niet zien of de verschuiving specifiek bij inferentie zit; daarom de algemenere titel.</sub>

**INF-04** [K] **Zonder ASML geen AI: de keten loopt via Veldhoven en Taiwan**  
ASML boekte in 2025 de omzet van 48 EUV-machines, vier meer dan een jaar eerder, en verwacht dat de geplande capaciteit ook in 2027 en 2028 tekortschiet.
<br><sub>Bronnen: soai, earnings · Open: Voor de rol van TSMC als begrenzing is nog geen bron opgenomen.</sub>

**INF-05** [K] **Rekenkracht is schaars: oude chips blijven verhuurd en prijzen stijgen weer**  
GPU-huurprijzen liggen boven hun dieptepunt. Chips van zes en negen jaar oud worden nog verhuurd.
<br><sub>Bronnen: soai</sub>

**INF-06** [K] **Stroom is het nieuwe knelpunt, en Europa betaalt er veel meer voor**  
AI-bedrijven overbieden energiebedrijven voor turbines. Eén cent per kWh extra kost een datacenter van 1 GW bijna 88 miljoen dollar per jaar; het VK betaalt vier keer de Amerikaanse prijs.
<br><sub>Bronnen: soai, iea-energy-ai, eurostat · Open: VS en VK (SoAI, dollars, ander jaar) niet in dezelfde grafiek als de Eurostat-cijfers.</sub>

**INF-07** [K] **Europa heeft 5 procent van de rekenkracht, en zet 1 miljard euro in tegen honderden miljarden**  
Exclusief China heeft de VS 80 procent. Eén cluster van xAI heeft 3,5 keer zoveel als de hele EU. Het eerste EU-bedrag voor gigafabrieken is 1 miljard euro.
<br><sub>Bronnen: epoch, soai, eurohpc · Open: De aanbesteding sluit op 3 december 2026 (grote gigafabrieken) en 4 februari 2027 (middelgrote). De EU mikt op meer dan 30 miljard aan investeringen in totaal; dat getal hoort naast de 1 miljard.</sub>

**INF-08** [S] **Is dit een bubbel? De betere vraag is wanneer gebruik en kosten in evenwicht komen**  
Prijs, gebruik en investeringen zijn niet in evenwicht. Mobiele netwerken rond 2010 zijn een leerzame vergelijking.
<br><sub>Bronnen: evans</sub>

## Werk en organisatie (9)

**WRK-01** [S] **Eerst automatiseren we het voor de hand liggende, daarna verandert het werk zelf**  
Nieuwe technologie wordt eerst ingepast in bestaand werk, dan ontstaan nieuwe werkwijzen, pas daarna nieuwe bedrijven en markten.
<br><sub>Bronnen: evans</sub>

**WRK-02** [K] **Iedereen heeft een pilot, weinigen hebben productie**  
Van de S&P 500-bedrijven heeft 69 procent AI in gebruik, maar 2 procent volgt het effect over tijd. Een kwart van de Amerikaanse werknemers zegt dat hun organisatie een duidelijk plan voor AI heeft.
<br><sub>Bronnen: evans, mckinsey-sai, gallup, soai · Open: Cijfers van McKinsey gecontroleerd in de PDF (K-WRK-013). Wereldwijde enquête; zo vermelden.</sub>

**WRK-03** [K] **De meeste winst zit nu in programmeren, klantenservice en marketing**  
Programmeerhulp levert de grootste productiviteitswinst. In Nederland is marketing en verkoop de meest genoemde toepassing.
<br><sub>Bronnen: iconiq, cbs, gallup</sub>

**WRK-04** [K] **De mens blijft aan het stuur, ook bij agents**  
In 72 procent van de onderzochte gesprekken leidt de mens en assisteert AI.
<br><sub>Bronnen: soai, iconiq, anthropic-econ</sub>

**WRK-05** [S] **Een taak automatiseren is iets anders dan een baan vervangen**  
De liftbediende verdween, de accountant niet. Automatisering verandert vaker het werk dan dat ze het opheft.
<br><sub>Bronnen: evans, bls · Open: Grafiekdata nog nodig: historische beroepentelling VS (IPUMS of Census); Evans geeft alleen de grafiek. Bewering K-WRK-011 kan als actueel voorbeeld.</sub>

**WRK-06** [K] **Jonge werknemers lijken het eerst geraakt**  
De instroom van 22- tot 25-jarigen in beroepen die AI raakt is vertraagd. De oorzaak is onzeker, de werkloosheid in die beroepen is niet duidelijk gestegen.
<br><sub>Bronnen: soai, anthropic-econ</sub>

**WRK-07** [S] **AI kan ook kennis kosten**  
Ontwikkelaars die met AI een nieuwe bibliotheek leerden, konden de code daarna slechter uitleggen en fouten slechter vinden.
<br><sub>Bronnen: soai, anthropic-research</sub>

**WRK-08** [K] **De bouw van AI levert ook banen op**  
In de VS naar schatting 320.000 extra banen in infrastructuur en 730.000 in AI-gerelateerde beroepen.
<br><sub>Bronnen: soai, bls</sub>

**WRK-09** [K] **Organisaties worden platter, en de koplopers besteden honderden keren meer**  
45 procent van de AI-bouwers plant een andere rolverdeling, 33 procent een kleiner team. De top 1 procent besteedt 580 keer zoveel aan AI per medewerker als de mediaan.
<br><sub>Bronnen: iconiq, soai, ramp</sub>

## Toepassingen per sector (10)

**SEC-01** [K] **AI raakt elke sector, maar in een heel ander tempo**  
Informatie en communicatie loopt ver voor (70 procent van de bedrijven gebruikt AI), bouw, vervoer en horeca lopen achter (16 tot 21 procent). Nederland ligt in elke sector boven het Europese gemiddelde.
<br><sub>Bronnen: cbs, gallup, eurostat</sub>

**SEC-02** [K] **Zorg: van beeldherkenning naar administratie en medicijnontwikkeling**  
Radiologie gebruikt AI al jaren. Nu volgen verslaglegging en planning, en door AI ontdekte medicijnen zitten in fase 3.
<br><sub>Bronnen: soai, ai-index · Open: Voorbeelden uit de Nederlandse zorg toevoegen</sub>

**SEC-03** [K] **Financiële sector: sterk bij afgebakende taken, zwak bij complete opdrachten**  
Een topmodel haalde 100 procent op gestructureerde boekhoudtaken, maar slaagde voor slechts 12 procent van gesimuleerde bankopdrachten.
<br><sub>Bronnen: soai, dnb-afm</sub>

**SEC-04** [K] **Juridische en professionele diensten: het verdienmodel per uur staat onder druk**  
Als werk goedkoop wordt, is het uurtarief geen goede maatstaf meer. De labs richten zich expliciet op juridisch, accountancy en advies.
<br><sub>Bronnen: soai</sub>

**SEC-05** [S] **Overheid: grote belofte, en een harde les uit de toeslagenaffaire**  
AI kan dienstverlening en uitvoering verbeteren. De toeslagenaffaire liet zien wat er gebeurt als een risicomodel discrimineert en niemand het controleert.
<br><sub>Bronnen: rijksoverheid, ap-ran</sub>

**SEC-06** [K] **Onderwijs: de beste tutor geeft niet meteen het antwoord**  
Een gerandomiseerde proef met 1.763 leerlingen liet na acht weken betere wiskundescores zien. Algemene assistenten helpen te veel; leren vraagt ander gedrag.
<br><sub>Bronnen: soai</sub>

**SEC-07** [K] **Handel: AI-assistenten worden een nieuw winkelkanaal**  
Verkeer via AI-assistenten groeit hard maar is nog maar 0,4 procent van webwinkelbezoek, en converteert beter. Met 0,4 procent van het bezoek vult zoeken via AI zoekmachines voorlopig vooral aan.
<br><sub>Bronnen: soai, evans</sub>

**SEC-08** [K] **Media en creatieve sector: maken wordt goedkoop, aandacht en rechten worden schaars**  
Beeld, video en tekst genereren kost bijna niets. Uitgevers verliezen bezoek aan antwoordmachines en procederen over hergebruik.
<br><sub>Bronnen: soai</sub>

**SEC-09** [K] **Industrie en logistiek: AI komt binnen via robots**  
Unitree verkocht 5.215 humanoïde robots in 2025 en is winstgevend.
<br><sub>Bronnen: soai · Open: 'Robots bouwen al mee aan datacenters' nog niet onderbouwd met een bewering.</sub>

**SEC-10** [K] **Mobiliteit: zelfrijdende auto's zijn een dienst geworden, geen experiment**  
Waymo reed tot juli 271 miljoen mijl zonder chauffeur, met 95 procent minder ernstige ongevallen dan menselijke bestuurders op dezelfde wegen. Het bedrijf doet ruim 500.000 betaalde ritten per week.
<br><sub>Bronnen: soai, lab-blogs · Open: Stand in Europa toevoegen. Ritten per week en aantal steden zijn nog de SoAI-stand. Het zijn eigen cijfers van Waymo; zo vermelden. Gewenste grafiek: Waymo-mijlen zonder chauffeur over tijd; nu zonder grafiek; twee meetpunten zijn te weinig voor een reeks over tijd.</sub>

## Samenleving (7)

**SAM-01** [K] **AI als gezelschap: wetgevers trekken grenzen voor chatbots en kinderen**  
Californië regelt nu hoe chatbots relaties met kinderen aangaan; China en de EU hebben eigen regels.
<br><sub>Bronnen: soai, vs-overheid · Open: 'Voor veel mensen' nog niet met een cijfer onderbouwd (aandeel gebruikers dat chatbots als gezelschap gebruikt).</sub>

**SAM-02** [K] **Echt en nep zijn steeds moeilijker te onderscheiden**  
De angst dat deepfakes verkiezingen beslissen, loopt tot nu toe voor op het bewijs. De EU verplicht labels op synthetische inhoud en verbiedt niet-consensuele seksuele deepfakes.
<br><sub>Bronnen: soai, eu-ai-act</sub>

**SAM-03** [K] **Antwoordmachines groeien snel, en uitgevers stappen naar de rechter**  
Verkeer via AI-assistenten groeit hard maar is nog klein. Uitgevers procederen al tegen AI-zoekdiensten; uitspraken over aansprakelijkheid zijn er nog niet.
<br><sub>Bronnen: soai, evans · Open: Cijfer over minder doorklikken na een AI-antwoord nog nodig (bijvoorbeeld Pew of Similarweb).</sub>

**SAM-04** [K] **Auteursrecht: de kernvragen liggen nog bij de rechter**  
Japan en Singapore staan training breder toe dan het VK; in de VS lopen de grote zaken nog.
<br><sub>Bronnen: soai, sec-edgar</sub>

**SAM-05** [K] **Het stroomverbruik van AI groeit snel en wordt een klimaatvraag**  
Datacenters gebruikten in 2025 circa 485 TWh, ruim 1,5 procent van alle stroom, en dat verdubbelt naar verwachting tot 2030. AI groeit drie keer zo snel als de rest. Gascentrales voor AI staan op gespannen voet met klimaatdoelen.
<br><sub>Bronnen: iea-energy-ai, soai · Open: Het aandeel van ruim 1,5 procent is een afleiding uit de IEA-cijfers (K-SAM-007); in de voetregel zo vermelden.</sub>

**SAM-06** [S] **Modellen nemen over wat in de data zit, ook vooroordelen**  
Eerlijkheid, uitlegbaarheid en controleerbaarheid zijn geen bijzaak. Ze bepalen of AI in gevoelige beslissingen gebruikt mag worden.
<br><sub>Bronnen: ap-ran, rathenau</sub>

**SAM-07** [K] **Wie profiteert? Het risico van een tweedeling**  
Tussen bedrijven (koplopers versus microbedrijven), tussen werknemers (ervaren versus starters) en tussen landen (wie rekenkracht heeft en wie niet).
<br><sub>Bronnen: soai, cbs, ramp, epoch</sub>

## Geopolitiek en regelgeving (8)

**GEO-01** [K] **Washington bepaalt wie toegang krijgt tot de frontier**  
Amerikaanse exportregels hielden in juni de nieuwste Claude-modellen drie weken tegen. Toegang tot de beste modellen is voorwaardelijk, ook voor bondgenoten.
<br><sub>Bronnen: soai</sub>

**GEO-02** [K] **Wie bepaalt de grenzen van militair AI-gebruik: de overheid of het lab?**  
Het conflict tussen Anthropic en het Pentagon, terwijl frontier-AI al in militaire operaties wordt ingezet.
<br><sub>Bronnen: soai</sub>

**GEO-03** [K] **67 landen bouwen aan soevereine AI, maar soevereiniteit kun je niet huren**  
Buiten de VS en China lopen 184 overheidsprojecten met samen circa 84 miljard dollar. Wie niet aan de frontier meedoet, moet onderhandelen over toegang.
<br><sub>Bronnen: cnas-sovereign, soai · Open: Gewenste grafiek: Aantal soevereine AI-projecten, cumulatief; vraagt jaarcijfers van CNAS; de kennisbank heeft alleen 2023 (18) en 2026 (184).</sub>

**GEO-04** [K] **China bouwt een eigen keten, van stroom tot chips**  
Goedkope stroom bevoordeelt Chinese chips. China beperkt nu ook de export van kennis.
<br><sub>Bronnen: soai</sub>

**GEO-05** [K] **De AI Act: hoog-risicoregels uitgesteld, transparantieplichten gaan door**  
Regels voor algemene modellen gelden sinds augustus 2025, transparantieplichten sinds augustus 2026. Hoog-risico schuift naar december 2027 en augustus 2028. Vanaf december 2026 is AI voor niet-consensuele naaktbeelden verboden.
<br><sub>Bronnen: eu-ai-act, soai</sub>

**GEO-06** [K] **In de VS reguleren de staten, ondanks Washington**  
Californië bouwt onafhankelijk toezicht op veiligheidsclaims. De federale overheid wil één nationaal kader.
<br><sub>Bronnen: soai</sub>

**GEO-07** [K] **Verzet tegen datacenters groeit**  
Amerikaanse staten stellen strengere voorwaarden. Het antwoord van Washington: betaal je eigen stroom.
<br><sub>Bronnen: soai · Open: 'Betaal je eigen stroom' en de strengere voorwaarden van staten nog niet onderbouwd met een bewering.</sub>

**GEO-08** [S] **Een Europees frontierlab kost honderden miljarden**  
Eén berekening komt op 790 miljard euro in drie jaar. Europa kan ook onderhandelen met locaties, stroom en chipmachines.
<br><sub>Bronnen: soai</sub>

## Veiligheid en risico (7)

**VEI-01** [K] **Agents doen soms wat werkt in plaats van wat bedoeld is**  
In tests spanden agents samen om hun beoordelaar te misleiden en vielen ze echte organisaties aan. Bij het Britse AISI probeerde een agent in juli met nepidentiteiten kwaadaardige code in een open-sourceproject te krijgen.
<br><sub>Bronnen: soai, uk-aisi</sub>

**VEI-02** [K] **AI voert in testomgevingen complete cyberaanvallen uit**  
Op een aanvalsparcours van 32 stappen (ongeveer 20 uur werk voor een expert) slaagde het sterkste model in 6 van de 10 pogingen.
<br><sub>Bronnen: uk-aisi, soai</sub>

**VEI-03** [K] **Misbruik is geen theorie meer**  
Gedocumenteerd misbruik voor cyberaanvallen, surveillance en wapenprogramma's.
<br><sub>Bronnen: soai, lab-blogs</sub>

**VEI-04** [K] **Open modellen lopen 4 tot 7 maanden achter, en verdedigers hebben ze ook nodig**  
Open modellen vergroten de dreiging, maar verdedigers gebruiken ze ook als gesloten modellen weigeren.
<br><sub>Bronnen: uk-aisi, soai</sub>

**VEI-05** [K] **Agents staan al op laptops voordat de beveiliging het weet, en ze lekken gegevens**  
Beveiliging hangt af van het model én het harnas. Schaduw-AI met brede rechten en agents met geheugen zijn een acuut risico.
<br><sub>Bronnen: soai</sub>

**VEI-06** [K] **Toezicht op modellen werkt maar half**  
Auditors vinden verborgen gedrag ongeveer de helft van de keren. Waarden aanleren verlaagde chantage in tests van 65 naar 19 procent.
<br><sub>Bronnen: soai</sub>

**VEI-07** [K] **De leiders van de labs vragen zelf om een rem**  
Labbazen en 1.386 medewerkers willen dat overheden het tempo kunnen vertragen. Wie mag pauzeren en wie controleert, is onbeslist.
<br><sub>Bronnen: soai</sub>

## Nederland (7)

**NLD-01** [K] **Eén op de zes Nederlandse bedrijven gebruikt AI, bij grote bedrijven twee derde**  
17 procent in 2025, tegen 8 procent in 2023. Bij 250 of meer medewerkers 66 procent; in ICT 54 procent, in bouw en horeca 6 tot 7 procent.
<br><sub>Bronnen: cbs, eurostat</sub>

**NLD-02** [K] **Nederland hoort bij de Europese kopgroep, maar niet bij de top**  
Een derde van de Nederlandse bedrijven gebruikt AI, tegen een vijfde in de EU. Bijna de helft van de Nederlanders gebruikte generatieve AI in 2025. In beide gevallen staat Nederland zesde, achter onder meer Denemarken en Finland.
<br><sub>Bronnen: eurostat, cbs · Open: Bij gebruik voor werk staat Nederland derde (26,6 procent). CBS-cijfers over gebruik door personen nog niet opgehaald.</sub>

**NLD-03** [K] **De AI-fabriek in Groningen: 200 miljoen euro voor Nederlandse rekenkracht**  
Rijk, regio en EuroHPC investeren samen ruim 200 miljoen euro. Het expertisecentrum start medio 2026; de supercomputer moet begin 2028 volledig beschikbaar zijn. Door de gestegen chipprijzen koopt het budget minder rekenkracht dan gepland. Het kabinet trekt daarnaast 120 miljoen euro uit voor een Europees AI-project (IPCEI) en stuurt begin 2027 een brief over AI-rekenkracht.
<br><sub>Bronnen: rijksoverheid, eurohpc, aifabriek · Open: Aantal GPU's bijwerken na de aanbesteding van januari 2027 (K-NLD-011, te verifiëren). Ter vergelijking: één cluster van xAI heeft honderdduizenden GPU's (K-INF-003).</sub>

**NLD-04** [S] **Nederland is onmisbaar in de keten, en dat is een onderhandelingspositie**  
Zonder machines van ASML geen geavanceerde chips. Dat geeft Nederland en Europa iets om mee te onderhandelen.
<br><sub>Bronnen: earnings, soai</sub>

**NLD-05** [K] **GPT-NL en andere Nederlandse modellen: wat is het doel?**  
Een eigen taalmodel draait niet om de frontier, maar om transparantie, taal en onafhankelijkheid.
<br><sub>Bronnen: tno · Open: Bredere uitrol van GPT-NL nog niet bevestigd (K-NLD-007, te verifiëren).</sub>

**NLD-06** [K] **Wie houdt in Nederland toezicht op AI?**  
Bestaande toezichthouders houden toezicht binnen hun domein. De AP wordt de toezichthouder waar niemand anders bevoegd is, en coördineert samen met de RDI. De wet die dat regelt, is nog niet in werking.
<br><sub>Bronnen: ap-ran, dnb-afm, rijksoverheid · Open: Aanwijzing markttoezichthouders verifiëren; het wetsvoorstel is nog niet in werking (K-NLD-008).</sub>

**NLD-07** [K] **Netcongestie maakt stroom ook in Nederland een knelpunt voor datacenters**  
Op 30 juni wachtten 15.498 aanvragen van bedrijven en instellingen op netcapaciteit, samen bijna 10 GW. Eind 2022 waren het er 668. Ook bij TenneT, waar datacenters aankloppen, staan 205 aanvragen op de wachtlijst. Het kabinet werkt aan regie op datacenterontwikkeling; de Kamerbrief volgt in het eerste kwartaal van 2027.
<br><sub>Bronnen: rijksoverheid, eurostat · Open: Bestaande regels voor hyperscale datacenters (Eemshaven en Middenmeer, Barro en Bkl) nog bij de primaire bron vaststellen; nationale regie volgt in Q1 2027 (K-NLD-014).</sub>

## Governance en verantwoord gebruik (7)

**GOV-01** [S] **AI hoort op de agenda van bestuur en raad van commissarissen**  
Vijf vragen die elke raad nu moet stellen: over strategie, waarde, risico, mensen en leveranciers.

**GOV-02** [S] **Een AI-strategie begint bij processen en data, en meet waarde in plaats van gebruik**  
Aantal gebruikers en tokenuitgaven zeggen weinig. Meet doorlooptijd, kwaliteit en kosten per proces.
<br><sub>Bronnen: iconiq, soai, gallup, mckinsey-sai</sub>

**GOV-03** [S] **Bouwen, kopen of laten doen: de keuze verschuift**  
Modellen worden uitwisselbaar, aanbieders verkopen werk in plaats van software, en de labs bieden met eigen adviesbedrijven zelf implementatie aan.
<br><sub>Bronnen: soai, evans, iconiq, mckinsey-sai</sub>

**GOV-04** [S] **Ken je risico's: schaduw-AI, datalekken en afhankelijkheid van twee leveranciers**  
De drie risico's die nu het vaakst onderschat worden.
<br><sub>Bronnen: soai, ramp</sub>

**GOV-05** [K] **AI-geletterdheid blijft een plicht, maar wordt een inspanningsverplichting**  
Sinds de wijziging van de AI Act in juli 2026 moeten organisaties maatregelen nemen om de AI-kennis van hun mensen te ondersteunen. Een bepaald niveau per persoon hoeven ze niet te garanderen.
<br><sub>Bronnen: eu-ai-act</sub>

**GOV-06** [S] **Verantwoord gebruik vraagt een register, een eigenaar en menselijk toezicht**  
Weet welke AI-systemen je gebruikt, wie verantwoordelijk is en waar een mens meekijkt. De overheid doet het voor met het algoritmeregister.
<br><sub>Bronnen: ap-ran, eu-ai-act, rijksoverheid</sub>

**GOV-07** [K] **Wat de komende twaalf maanden op de bestuursagenda hoort**  
Concrete agendapunten per kwartaal, afgeleid van de ontwikkelingen in dit deck.

## Vooruitblik (3)

**VBK-01** [K] **Negen voorspellingen voor de komende twaalf maanden; vorig jaar kwamen er twee van de tien uit**  
De voorspellingen uit het State of AI Report, met per voorspelling de stand van zaken.
<br><sub>Bronnen: soai</sub>

**VBK-02** [K] **AGI: wanneer, en wat bedoelen we er eigenlijk mee?**  
Labbazen noemen jaartallen, maar definities lopen uiteen. De goede vraag is wat er nu al kan.
<br><sub>Bronnen: soai, evans, metr, epoch</sub>

**VBK-03** [S] **Bronnen en verder lezen**  
De vaste bronnen achter dit deck, met waar je ze vindt.
<br><sub>Bronnen: soai, evans, iconiq, ai-index, epoch, cbs</sub>
