# Code abgegeben von Christian Muche 18-615-575
# Abgabedatum 07.03.2023
# Update "since Date" (siehe Kommentar unten) und auskommentierte Zeilen am 13.03.2023 

# Importieren der nötigen Module
import os
import json
import pandas as pd
from snscrape.modules.twitter import *

# Ausführen des command line argument, um die seit dem 01.01.2015 geposteten Tweets des Accounts HSGStGallen abzurufen und als JSON File zu speichern.
# Mit jsonl wird jede line des Outputs als JSON Objekt gespeichert
# Update des Datums auf Vortag, da gemäss documentation das angegebene Datum bei since nicht inkludiert wird, weshalb der Vortag des gewünschten Datums ausgewählt werden muss.
os.system("snscrape --jsonl --since 2014-12-31 twitter-search 'from:HSGStGallen' > HSG-tweets.json")

# Mit untenstehendem Code wird das JSON File eingelesen und als Pandas dataframe namens "data" gespeichert. 
# data = pd.read_json (r'MeinPfad\HSG-tweets.json', lines=True)

# Mit diesem Code wird der pandas dataframe als csv Datei exportiert
# data.to_csv (r'MeinPfad\HSG-tweets.csv', index = None)
# Das abgegebene csv und json File zeigt den Originaloutput. Wenn ich mit den Daten weiterarbeiten würde, würde ich die Daten mit Pandas vor dem Export zu einer csv Datei erst noch bereinigen bzw.
# die einzelnen Tweet-Items nur selektiv in eine Liste einlesen und dann über pandas in ein csv exportieren.


# Diese code line habe ich genutzt, um zu kontrollieren, dass die ältesten Tweets tatsächlich nicht älter sind als vom 01.01.2015.
# print(data['date'].tail(10))

# Mit dieser line habe ich die neusten Tweets ausgegeben, um einen weiteren Plausibilitätscheck durchzuführen.
# print(data['date'].head(10))


