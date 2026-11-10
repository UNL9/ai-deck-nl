# Bestuurdersnotitie: hoe het werkt

*Stand 2026-11-10. Interpretatie bij de slides BAS-01 tot en met BAS-12; de cijfers staan in `kennisbank/beweringen/basis.yaml`.*

## Wat er speelt

Een bestuurder hoeft niet te weten hoe een transformer werkt. Wel helpt het om vier dingen te begrijpen, omdat ze bepalen wat AI kan, wat het kost en waar het misgaat.

Ten eerste: een taalmodel voorspelt het volgende woord, en op voldoende schaal levert dat bruikbare intelligentie op. Er zit geen begrip in zoals bij mensen, en dus maakt een model fouten die overtuigend klinken.

Ten tweede: een model nadenken laten kost rekentijd, en die rekentijd bepaalt de kwaliteit. Hetzelfde model van Anthropic scoort 35 bij weinig denkwerk en 58 bij het maximum. De prijs per token zegt daardoor weinig over de prijs van een goed antwoord.

Ten derde: de software rond het model (het harnas) is bijna even belangrijk als het model zelf. In een gecontroleerde test was de variatie door het harnas bijna acht keer zo groot als die door het model. Wat het model niet ziet, kan het niet gebruiken.

Ten vierde: intelligentie wordt goedkoper per eenheid, maar het gebruik groeit harder. De prijs om een vast niveau te halen daalt met een factor 9 tot 900 per jaar, en toch is rekenkracht bij Anthropic de grootste kostenpost: 55 procent van de bedrijfslasten.

## Wat dit betekent voor een bestuurder

**Kies niet alleen een model, maar een opzet.** De prestatie hangt af van het model, de instructies, de gekoppelde systemen en de data die het ziet. Een vergelijking van modellen zonder dezelfde opzet zegt weinig.

**Begroot op taken, niet op tokens.** Redeneermodellen en agents gebruiken per taak veel meer rekenkracht dan een chatbot. Een begroting op basis van de prijs per token valt bijna altijd te laag uit.

**Ga uit van fouten.** Modellen verzinnen feiten en melden taken als klaar die het niet zijn. Elke toepassing met gevolgen heeft een controle nodig die niet afhangt van wat het model over zichzelf zegt.

**Open of gesloten is een strategische keuze.** Open modellen geven controle en onafhankelijkheid, gesloten modellen lopen voorop in prestaties. De beste open modellen komen nu uit China.

## Vragen die je stelt

- Begrijpen de mensen die over AI beslissen genoeg van de techniek om de beloftes van leveranciers te beoordelen?
- Hoe begroten we AI-kosten, per gebruiker of per taak?
- Waar controleren we de uitkomst van AI, en wie doet dat?
