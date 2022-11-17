![Alt text](https://pixabay.com/get/gac17440c200cecd8ee6c99c22c26eb775dc7a36c0a9fe25f87730b0776c78157808daa05d2fbfc79893a2bfdd4946f50aac3ffd198594c871961a702c506f30b6fb31a2f5aa6f5f0e043fbf2137ee162_640.png "Workshop")

## Welkom

In deze workshop gaan we een model maken dat tekst kan classificeren. Jullie krijgen een bestand dat al een dataset inleest, die vervolgens 
omzet in een lijst met vectoren, om daarna een model te maken.

De opzet van het programma is als volgt:
- regels 8 tm 14 lezen de noodzakelijke libraries in
- regel 16 wordt een variable gezet (True of False) die aangeeft os je extra print regels wil
- regel 20 importeert de documenten. In dit voorbeeld zijn het iets midner dan 2000 (1972 om precies te zijn) documenten uit twee nieuwsgroepen. De ene gaat over pc.hardware de andere gaat over autos. Let wel deze nieuws groepen zijn uit 1997.
- regel 41 splits de documenten in twee groepen. De training en test data. Bij iedere set hoort ook de nieuwsgroep waartoe elke bericht hoort. training_data en testing_data zijn hier nog tekst
- regel 47 en 48 maken we een vectorizer aan. Een vectorizer zet tekst om in getallen
- regel 51 leert de vectorizer welke woorden gebruikt worden. Je kunt die woorden hier ook bekijken door vectorizer.vocabulary_ af te drukken. 
- regel 62 en 63 worden de documenten omgezet in vectoren. 
- regel 67 of 68 maken we een classifier aan. Regel 68 komt als laatste, dat is het model dat gebruikt wordt
- regel 75 wordt het model getraind met de voorbeelden 
- regel 82 passen we het model toe op onze training_vectors. Zou het model goed werken of maakt het nog fouten?
- regel 85,86,87 drukt een aantal kenmerken van het model af.
- regel 90 to 97 is een voorbeeld hoe een zin omgezet wordt in een vector, en voorspelt wordt tot welke klasse deze zin hoort. Het model kan een zwart-wit antwoord geven, maar ook een percentage per resultaat aangeven


Zoals je ziet werkt echter niet optimaal. Ondanks dat de scores erg hoog zijn.

1. **"My new game card is not working."** wordt correct aangeven bij klasse 0 te horen (pc gerelateerd )
1. **"I prefer a BMW over a Mercedes any day."** wordt correct bij de auto gerelateerde documenten gezet.
1. **"Does the new Honda have a sound system?."** wordt ten onrechte bij de pc gerelateerde documenten gezet.

# verbeter het model
- je kunt experimenteren met verschillende modellen. Probeer eens regel 67 en 68 te wisselen
- je kunt extra stopwoorden toevoegen
- je kunt de verhouding train (70%) / test (30%)  aanpassen. Werkt dat?
- je kunt zelf experimenteren met zinnetje om te kijken of je aanpassingen werken
- je kunt kijken welke documenten verkeerd worden beoordeeld? Herken je iets aan deze documente?

# je hebt 45 minuten
dan komt er een zin, wie die zin het beste kan classificeren wint.

