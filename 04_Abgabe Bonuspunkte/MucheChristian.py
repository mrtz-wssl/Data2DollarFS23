# Code abgegeben von Christian Muche 18-615-575
# Abgabedatum 07.03.2023

# Importieren der nötigen Module
import os
import json
from snscrape.modules.twitter import *

# Ausführen des command line argument, um die seit dem 01.01.2015 geposteten Tweets des Accounts HSGStGallen abzurufen und als JSON File zu speichern.
# Mit jsonl wird jede line des Outputs als JSON Objekt gespeichert
os.system("snscrape --jsonl --since 2015-01-01 twitter-search 'from:HSGStGallen' > HSG-tweets.json")

# Mit untenstehendem Code wird das JSON File eingelesen und als Pandas dataframe namens "data" gespeichert. Anmerkung: Auf meinem PC hatte ich für den untenstehenden Code (inkl. import json) ein neues File erstellt.
# with open('HSG-tweets.json') as json_file:
#     data = pd.DataFrame([json.loads(line) for line in json_file])

# Diese code line habe ich genutzt, um zu kontrollieren, dass die ältesten Tweets tatsächlich nicht älter sind als vom 01.01.2015
# print(data['date'].tail(10))

# Mit dieser line habe ich die neusten Tweets ausgegeben, um einen weiteren Plausibilitätscheck durchzuführen.
# print(data['date'].head(10))

# Um auch eine CSV Datei ausgeben zu lassen, habe ich den Code in Zeile 25 verwendet. 
# Das abgegebene File zeigt den Originaloutput. Wenn ich mit den Daten weiterarbeiten würde, würde ich die Daten mit Pandas vor dem Export zu einer CSV Datei erst noch bereinigen.
# data.to_csv('HSG-tweets.csv', index=False)