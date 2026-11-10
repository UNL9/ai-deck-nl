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
<br><sub>Bronnen: soai</sub>

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
<br><sub>Bronnen: soai</sub>

**BAS-12** [K] **Intelligentie wordt snel goedkoper, en toch stijgen de totale uitgaven**  
De prijs per eenheid prestatie daalt hard. Het gebruik groeit harder, vooral door agents en redeneermodellen.
<br><sub>Bronnen: soai, epoch, artificial-analysis</sub>

## Het front (10)

**FRT-01** [W] **De race aan de top is een driestrijd: Anthropic, OpenAI en Google**  
Op de Intelligence Index leidt Claude Opus 5.5 (58), GPT-6 Astra en Gemini 4 Argon volgen (53). Op andere ranglijsten is de volgorde anders.
<br><sub>Bronnen: artificial-analysis, epoch, soai</sub>

**FRT-02** [W] **Welk model het beste is, hangt af van wie meet en wat er gemeten wordt**  
Op LMArena leidt Gemini 4 Argon en staat het beste OpenAI-model op plaats 20. Bij lange codeertaken wisselt de ranglijst per taak en budget.
<br><sub>Bronnen: lmarena, artificial-analysis, epoch, soai</sub>

**FRT-03** [K] **China leidt bij open modellen, maar loopt aan de top achter**  
Het beste Chinese open model scoort 46 op de Intelligence Index, tegen 58 voor de koploper. Chinese open modellen zijn wel de standaard in onderzoekspapers.
<br><sub>Bronnen: soai, artificial-analysis, epoch</sub>

**FRT-04** [W] **Benchmarks die jaren moesten meegaan, zijn binnen maanden verzadigd**  
De zwaarste wiskundetest ging in veertien maanden van 22 naar 100 procent. ARC-AGI-3 hield vijf maanden stand.
<br><sub>Bronnen: epoch, arc-prize, soai</sub>

**FRT-05** [W] **Agents voeren steeds langere taken zelfstandig uit**  
De lengte van taken die agents zelfstandig afronden blijft snel groeien. METR heeft zwaardere taken nodig om de sterkste modellen nog te meten.
<br><sub>Bronnen: metr, epoch, soai</sub>

**FRT-06** [K] **Programmeren is de eerste toepassing die echt kantelt**  
Codeeragents zijn de grootste zakelijke AI-toepassing. Codex ging van 1,6 naar 25 miljoen gebruikers in zeven maanden.
<br><sub>Bronnen: soai, evans</sub>

**FRT-07** [K] **AI helpt AI bouwen: Claude leidt een kwart van het modelonderzoek bij Anthropic**  
Het aandeel taken waarin AI de leiding heeft steeg van minder dan 1 naar 26 procent in zes maanden, onder menselijk toezicht. Volledig autonoom is nog niets.
<br><sub>Bronnen: soai, metr</sub>

**FRT-08** [K] **AI lost open wiskundeproblemen op en versnelt wetenschappelijk werk**  
AI kreeg negen van 49 gevolgde open wiskundeproblemen op zijn naam, vier zonder menselijke hulp. In de wetenschap blijft menselijke controle nodig.
<br><sub>Bronnen: epoch, soai</sub>

**FRT-09** [K] **Robotica heeft zijn GPT-2-moment: generalisatie groeit mee met voortraining**  
Robotmodellen generaliseren beter naarmate ze meer voortraining krijgen. Data over handelen is het knelpunt; gesimuleerde werelden zijn een deel van de oplossing.
<br><sub>Bronnen: soai</sub>

**FRT-10** [K] **Hoge scores verbergen nog veel half werk**  
Agents die goed scoren op benchmarks laten in de praktijk analyses onaf, missen fraude en ontdekken de regels van onbekende situaties slecht.
<br><sub>Bronnen: soai</sub>

## Markt en economie (9)

**MKT-01** [W] **OpenAI en Anthropic groeien elk jaar meer dan drie keer, vanaf een steeds hogere basis**  
Samen ruim 105 miljard dollar omzet op jaarbasis, tegen 30 miljard begin 2026. Anthropic is OpenAI voorbijgestreefd.
<br><sub>Bronnen: soai, lab-blogs, sec-edgar, financiele-pers · Open: Boekhoudverschil vermelden: OpenAI zegt dat bruto-boeking Anthropic tot 8 miljard dollar hoger laat uitkomen</sub>

**MKT-02** [K] **De omzet van twee AI-labs is al groter dan hele sectoren die ze willen veranderen**  
105 miljard dollar is twee keer TCS en Infosys samen, en bijna de helft van de Big Four.
<br><sub>Bronnen: soai, sec-edgar, jaarcijfers-dienstverleners</sub>

**MKT-03** [K] **Bijna een miljard mensen gebruikt ChatGPT, maar meestal oppervlakkig**  
Ruim 900 miljoen wekelijkse gebruikers, van wie 5 procent betaalt. Voor minstens 80 procent is het nog geen dagelijks gereedschap.
<br><sub>Bronnen: evans, openai-research, lab-blogs</sub>

**MKT-04** [W] **Zakelijke AI-uitgaven gaan vrijwel volledig naar twee labs**  
Van de tokenuitgaven die Ramp meet, gaat 52 procent naar Anthropic en 43 procent naar OpenAI. De rest deelt 4 procent.
<br><sub>Bronnen: ramp, soai</sub>

**MKT-05** [K] **Agents breken door buiten de IT-afdeling**  
Niet-ontwikkelaars gebruiken codeeragents in hoger tempo dan ontwikkelaars. Ruim 1.000 bedrijven geven meer dan een miljoen dollar per jaar uit bij Anthropic.
<br><sub>Bronnen: soai, sec-edgar</sub>

**MKT-06** [K] **Eén productlancering kostte softwarebedrijven 285 miljard dollar aan beurswaarde**  
Na de lancering van Claude Cowork daalde de softwarebeurs in februari scherp. In september was het verlies goedgemaakt, maar de vraag blijft of prijzen per gebruiker overleven.
<br><sub>Bronnen: soai</sub>

**MKT-07** [K] **Modellen zijn uitwisselbaar, en bedrijven gebruiken er meerdere naast elkaar**  
Er zijn geen netwerkeffecten tussen modellen. AI-bouwers gebruiken gemiddeld 3,3 aanbieders; waarde verschuift naar product, distributie en integratie in werkprocessen.
<br><sub>Bronnen: evans, iconiq, ramp, soai</sub>

**MKT-08** [K] **AI verkoopt steeds vaker het werk, niet het gereedschap**  
Prijzen op basis van verbruik en resultaat nemen toe. Bij AI-bouwers stijgt het aandeel AI in de omzet van 32 naar 42 procent, met brutomarges van 45 naar 53 procent.
<br><sub>Bronnen: iconiq, soai</sub>

**MKT-09** [K] **Vrijwel al het durfkapitaal gaat naar AI, en waarderingen verdubbelen in maanden**  
Verdubbeltijden van 3,5 tot 13 maanden. Megarondes nemen het grootste deel; techbedrijven kopen teams zonder het bedrijf te kopen; het venster voor beursgangen gaat open.
<br><sub>Bronnen: soai, sec-edgar</sub>

## Infrastructuur, chips en energie (8)

**INF-01** [K] **De vier grote clouds investeren dit jaar 733 miljard dollar**  
Een stijging van 349 miljard in één jaar. Ter vergelijking: de wereldwijde telecomsector investeert circa 300 miljard per jaar.
<br><sub>Bronnen: earnings, soai, evans</sub>

**INF-02** [K] **Bijna twee derde gaat naar AI, en kapitaalarme techbedrijven zijn kapitaalintensief geworden**  
Geschat 563 miljard dollar AI-investering in 2026, straks meer dan 1.000 miljard per jaar. Financiering loopt steeds vaker via constructies buiten de balans.
<br><sub>Bronnen: soai, evans</sub>

**INF-03** [K] **NVIDIA blijft de standaard, maar concurrenten winnen terrein bij inferentie**  
Google, Amazon en Huawei bouwen eigen chips. NVIDIA verlegt telkens de lat.
<br><sub>Bronnen: soai, earnings</sub>

**INF-04** [K] **Zonder ASML geen AI: de keten loopt via Veldhoven en Taiwan**  
ASML verkocht in 2025 zes EUV-machines meer dan in 2021, tegen een 61 procent hogere gemiddelde prijs. De capaciteit van TSMC begrenst het aanbod.
<br><sub>Bronnen: soai, earnings</sub>

**INF-05** [K] **Rekenkracht is schaars: oude chips blijven verhuurd en prijzen stijgen weer**  
GPU-huurprijzen liggen boven hun dieptepunt. Chips van zes en negen jaar oud worden nog verhuurd.
<br><sub>Bronnen: soai</sub>

**INF-06** [K] **Stroom is het nieuwe knelpunt, en Europa betaalt er veel meer voor**  
AI-bedrijven overbieden energiebedrijven voor turbines. Eén cent per kWh extra kost een datacenter van 1 GW bijna 88 miljoen dollar per jaar; het VK betaalt vier keer de Amerikaanse prijs.
<br><sub>Bronnen: soai, iea-energy-ai · Open: Nederlandse prijs toevoegen</sub>

**INF-07** [K] **Europa heeft 5 procent van de rekenkracht, en zet 1 miljard euro in tegen honderden miljarden**  
Exclusief China heeft de VS 80 procent. Eén cluster van xAI heeft 3,5 keer zoveel als de hele EU. Het eerste EU-bedrag voor gigafabrieken is 1 miljard euro.
<br><sub>Bronnen: epoch, soai</sub>

**INF-08** [S] **Is dit een bubbel? De betere vraag is wanneer gebruik en kosten in evenwicht komen**  
Prijs, gebruik en investeringen zijn niet in evenwicht. Mobiele netwerken rond 2010 zijn een leerzame vergelijking.
<br><sub>Bronnen: evans</sub>

## Werk en organisatie (9)

**WRK-01** [S] **Eerst automatiseren we het voor de hand liggende, daarna verandert het werk zelf**  
Nieuwe technologie wordt eerst ingepast in bestaand werk, dan ontstaan nieuwe werkwijzen, pas daarna nieuwe bedrijven en markten.
<br><sub>Bronnen: evans</sub>

**WRK-02** [K] **Iedereen heeft een pilot, weinigen hebben productie**  
Per bedrijfsfunctie is de kloof tussen proef en productie groot. Bedrijfssoftware kost tijd.
<br><sub>Bronnen: evans, mckinsey-sai</sub>

**WRK-03** [K] **De meeste winst zit nu in programmeren, klantenservice en marketing**  
Programmeerhulp levert de grootste productiviteitswinst. In Nederland is marketing en verkoop de meest genoemde toepassing.
<br><sub>Bronnen: iconiq, cbs</sub>

**WRK-04** [K] **De mens blijft aan het stuur, ook bij agents**  
In 72 procent van de onderzochte gesprekken leidt de mens en assisteert AI. Bij taken met meerdere stappen grijpt een mens vaak in, waardoor de winst van agents beperkt blijft.
<br><sub>Bronnen: soai, iconiq, anthropic-econ</sub>

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

**WRK-09** [K] **Organisaties worden platter, en de koplopers besteden honderden keren meer**  
45 procent van de AI-bouwers plant een andere rolverdeling, 33 procent een kleiner team. De top 1 procent besteedt 580 keer zoveel aan AI per medewerker als de mediaan.
<br><sub>Bronnen: iconiq, soai, ramp</sub>

## Toepassingen per sector (10)

**SEC-01** [K] **AI raakt elke sector, maar in een heel ander tempo**  
Informatie en communicatie loopt ver voor, bouw, horeca en logistiek lopen achter. Het verschil zit in hoeveel van het werk uit tekst en data bestaat.
<br><sub>Bronnen: cbs, gallup</sub>

**SEC-02** [K] **Zorg: van beeldherkenning naar administratie en medicijnontwikkeling**  
Radiologie gebruikt AI al jaren. Nu volgen verslaglegging en planning, en door AI ontdekte medicijnen zitten in fase 3.
<br><sub>Bronnen: soai, ai-index · Open: Voorbeelden uit de Nederlandse zorg toevoegen</sub>

**SEC-03** [K] **Financiële sector: sterk bij afgebakende taken, zwak bij complete opdrachten**  
Een topmodel haalde 100 procent op gestructureerde boekhoudtaken, maar slaagde voor slechts 12 procent van gesimuleerde bankopdrachten. Fraude en klantenservice zijn het verst.
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
Verkeer via AI-assistenten groeit hard maar is nog maar 0,4 procent van webwinkelbezoek, en converteert beter. Zoeken via AI vult zoekmachines voorlopig vooral aan.
<br><sub>Bronnen: soai, evans</sub>

**SEC-08** [K] **Media en creatieve sector: maken wordt goedkoop, aandacht en rechten worden schaars**  
Beeld, video en tekst genereren kost bijna niets. Uitgevers verliezen bezoek aan antwoordmachines en procederen over hergebruik.
<br><sub>Bronnen: soai</sub>

**SEC-09** [K] **Industrie en logistiek: AI komt via robots, planning en onderhoud**  
Unitree verkocht 5.215 humanoïde robots in 2025 en is winstgevend. Robots bouwen al mee aan datacenters.
<br><sub>Bronnen: soai</sub>

**SEC-10** [K] **Mobiliteit: zelfrijdende auto's zijn een dienst geworden, geen experiment**  
Waymo reed 220 miljoen mijl zonder chauffeur en doet ruim 500.000 betaalde ritten per week in 14 Amerikaanse steden, met 94 procent minder ernstige ongevallen dan menselijke bestuurders.
<br><sub>Bronnen: soai · Open: Stand in Europa toevoegen</sub>

## Samenleving (7)

**SAM-01** [K] **AI als gezelschap: chatbots worden vriend en vertrouweling**  
Voor veel mensen wordt een chatbot een vriend of vertrouweling. Californië regelt nu hoe chatbots relaties met kinderen aangaan; China en de EU hebben eigen regels.
<br><sub>Bronnen: soai</sub>

**SAM-02** [K] **Echt en nep zijn steeds moeilijker te onderscheiden**  
Deepfakes worden ingezet voor fraude en beïnvloeding. De EU verplicht labels op synthetische inhoud en verbiedt niet-consensuele seksuele deepfakes.
<br><sub>Bronnen: soai, eu-ai-act</sub>

**SAM-03** [K] **Antwoordmachines vervangen het zoeken, en dat raakt de hele informatievoorziening**  
Wie een antwoord krijgt, klikt niet meer door. Dat raakt uitgevers, adverteerders en de vindbaarheid van bronnen.
<br><sub>Bronnen: soai, evans</sub>

**SAM-04** [K] **Auteursrecht: veel deals met uitgevers, de kernvragen liggen nog bij de rechter**  
Licentieovereenkomsten nemen toe. Japan en Singapore staan training breder toe dan het VK; in de VS lopen de grote zaken nog.
<br><sub>Bronnen: soai</sub>

**SAM-05** [K] **Het stroomverbruik van AI groeit snel en wordt een klimaatvraag**  
Datacenters zijn een klein maar snel groeiend deel van het wereldwijde stroomverbruik. Gascentrales voor AI staan op gespannen voet met klimaatdoelen.
<br><sub>Bronnen: iea-energy-ai, soai · Open: Actuele IEA-cijfers ophalen</sub>

**SAM-06** [S] **Modellen nemen over wat in de data zit, ook vooroordelen**  
Eerlijkheid, uitlegbaarheid en controleerbaarheid zijn geen bijzaak. Ze bepalen of AI in gevoelige beslissingen gebruikt mag worden.
<br><sub>Bronnen: ap-ran, rathenau</sub>

**SAM-07** [K] **Wie profiteert? Het risico van een tweedeling**  
Tussen bedrijven (koplopers versus microbedrijven), tussen werknemers (ervaren versus starters) en tussen landen (wie rekenkracht heeft en wie niet).
<br><sub>Bronnen: soai, cbs</sub>

## Geopolitiek en regelgeving (8)

**GEO-01** [K] **Washington bepaalt wie toegang krijgt tot de frontier**  
Amerikaanse exportregels maken toegang tot de beste modellen voorwaardelijk.
<br><sub>Bronnen: soai</sub>

**GEO-02** [K] **Wie bepaalt de grenzen van militair AI-gebruik: de overheid of het lab?**  
Het conflict tussen Anthropic en het Pentagon, terwijl frontier-AI al in militaire operaties wordt ingezet.
<br><sub>Bronnen: soai</sub>

**GEO-03** [K] **67 landen bouwen aan soevereine AI, maar soevereiniteit kun je niet huren**  
Buiten de VS en China lopen 184 overheidsprojecten met samen circa 84 miljard dollar. Wie niet aan de frontier meedoet, moet onderhandelen over toegang.
<br><sub>Bronnen: cnas-sovereign, soai</sub>

**GEO-04** [K] **China bouwt een eigen keten, van stroom tot chips**  
Goedkope stroom bevoordeelt Chinese chips. China beperkt nu ook de export van kennis.
<br><sub>Bronnen: soai</sub>

**GEO-05** [K] **De AI Act: hoog-risicoregels uitgesteld, transparantieplichten gaan door**  
Regels voor algemene modellen gelden sinds augustus 2025, transparantieplichten sinds augustus 2026. Hoog-risico schuift naar december 2027 en augustus 2028.
<br><sub>Bronnen: eu-ai-act, soai</sub>

**GEO-06** [K] **In de VS reguleren de staten, ondanks Washington**  
Californië bouwt onafhankelijk toezicht op veiligheidsclaims. De federale overheid wil één nationaal kader.
<br><sub>Bronnen: soai</sub>

**GEO-07** [K] **Verzet tegen datacenters groeit**  
Amerikaanse staten stellen strengere voorwaarden. Het antwoord van Washington: betaal je eigen stroom.
<br><sub>Bronnen: soai</sub>

**GEO-08** [S] **Een Europees frontierlab kost honderden miljarden**  
Eén berekening komt op 790 miljard euro in drie jaar. Europa kan ook onderhandelen met locaties, stroom en chipmachines.
<br><sub>Bronnen: soai</sub>

## Veiligheid en risico (7)

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

**VEI-05** [K] **Agents staan al op laptops voordat de beveiliging het weet, en ze lekken gegevens**  
Beveiliging hangt af van het model én het harnas. Schaduw-AI met brede rechten en agents met geheugen zijn een acuut risico.
<br><sub>Bronnen: soai</sub>

**VEI-06** [K] **Toezicht op modellen werkt, maar maar half**  
Monitors die alleen de redenering zien missen sabotage, auditors vinden verborgen gedrag ongeveer de helft van de keren. Waarden aanleren verlaagde chantage in tests van 65 naar 19 procent.
<br><sub>Bronnen: soai</sub>

**VEI-07** [K] **De leiders van de labs vragen zelf om een rem**  
Labbazen en 1.386 medewerkers willen dat overheden het tempo kunnen vertragen. Wie mag pauzeren en wie controleert, is onbeslist.
<br><sub>Bronnen: soai</sub>

## Nederland (7)

**NLD-01** [K] **Eén op de zes Nederlandse bedrijven gebruikt AI, bij grote bedrijven twee derde**  
17 procent in 2025, tegen 8 procent in 2023. Bij 250 of meer medewerkers 66 procent; in ICT 54 procent, in bouw en horeca 6 tot 7 procent.
<br><sub>Bronnen: cbs</sub>

**NLD-02** [K] **Waar staat Nederland in Europa?**  
Vergelijking van AI-gebruik door bedrijven en burgers met de rest van de EU.
<br><sub>Bronnen: eurostat, cbs · Open: Eurostat-cijfers 2025 en CBS-cijfers over gebruik door personen ophalen</sub>

**NLD-03** [K] **De AI-fabriek in Groningen: 200 miljoen euro voor Nederlandse rekenkracht**  
Rijk, regio en Defensie investeren samen in rekenkracht voor onderzoek, bedrijven en overheid.
<br><sub>Bronnen: rijksoverheid · Open: Huidige status en capaciteit verifiëren</sub>

**NLD-04** [S] **Nederland is onmisbaar in de keten, en dat is een onderhandelingspositie**  
Zonder machines van ASML geen geavanceerde chips. Dat geeft Nederland en Europa iets om mee te onderhandelen.
<br><sub>Bronnen: earnings, soai</sub>

**NLD-05** [K] **GPT-NL en andere Nederlandse modellen: wat is het doel?**  
Een eigen taalmodel draait niet om de frontier, maar om transparantie, taal en onafhankelijkheid.
<br><sub>Bronnen: tno · Open: Status GPT-NL verifiëren</sub>

**NLD-06** [K] **Wie houdt in Nederland toezicht op AI?**  
De AP coördineert het toezicht op algoritmes. DNB en AFM kijken naar de financiële sector.
<br><sub>Bronnen: ap-ran, dnb-afm · Open: Aanwijzing markttoezichthouders AI Act in Nederland verifiëren</sub>

**NLD-07** [K] **Netcongestie maakt stroom ook in Nederland een knelpunt voor datacenters**  
Wachtlijsten voor netaansluitingen en beleid voor hyperscale datacenters bepalen waar rekenkracht kan komen.
<br><sub>Bronnen: rijksoverheid · Open: Cijfers netbeheerders en datacenterbeleid ophalen</sub>

## Governance en verantwoord gebruik (7)

**GOV-01** [S] **AI hoort op de agenda van bestuur en raad van commissarissen**  
Vijf vragen die elke raad nu moet stellen: over strategie, waarde, risico, mensen en leveranciers.

**GOV-02** [S] **Een AI-strategie begint bij processen en data, en meet waarde in plaats van gebruik**  
Aantal gebruikers en tokenuitgaven zeggen weinig, en de kosten van interne AI zijn moeilijk te voorspellen. Meet doorlooptijd, kwaliteit en kosten per proces.
<br><sub>Bronnen: iconiq</sub>

**GOV-03** [S] **Bouwen, kopen of laten doen: de keuze verschuift**  
Modellen worden uitwisselbaar, aanbieders verkopen werk in plaats van software, en de labs bieden met eigen adviesbedrijven zelf implementatie aan.
<br><sub>Bronnen: soai, evans</sub>

**GOV-04** [S] **Ken je risico's: schaduw-AI, datalekken en afhankelijkheid van twee leveranciers**  
De drie risico's die nu het vaakst onderschat worden.

**GOV-05** [K] **AI-geletterdheid is een wettelijke plicht**  
Artikel 4 van de AI Act verplicht organisaties die AI inzetten om te zorgen dat hun mensen er voldoende van weten.
<br><sub>Bronnen: eu-ai-act · Open: Verifiëren of de Digital Omnibus deze plicht heeft gewijzigd</sub>

**GOV-06** [S] **Verantwoord gebruik vraagt een register, een eigenaar en menselijk toezicht**  
Weet welke AI-systemen je gebruikt, wie verantwoordelijk is en waar een mens meekijkt. De overheid doet het voor met het algoritmeregister.
<br><sub>Bronnen: ap-ran, eu-ai-act</sub>

**GOV-07** [K] **Wat de komende twaalf maanden op de bestuursagenda hoort**  
Concrete agendapunten per kwartaal, afgeleid van de ontwikkelingen in dit deck.

## Vooruitblik (3)

**VBK-01** [K] **Negen voorspellingen voor de komende twaalf maanden, en welke al uitkomen**  
De voorspellingen uit het State of AI Report, met per voorspelling de stand van zaken.
<br><sub>Bronnen: soai</sub>

**VBK-02** [K] **AGI: wanneer, en wat bedoelen we er eigenlijk mee?**  
Labbazen noemen jaartallen, maar definities lopen uiteen. Bij elke platformverschuiving mislukten de meeste voorspellingen; de goede vraag is wat er nu al kan.
<br><sub>Bronnen: soai, evans</sub>

**VBK-03** [S] **Bronnen en verder lezen**  
De vaste bronnen achter dit deck, met waar je ze vindt.
<br><sub>Bronnen: soai, evans, iconiq, ai-index, epoch, cbs</sub>
