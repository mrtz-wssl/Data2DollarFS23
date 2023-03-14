#Abgabe Twitter Challenge Eduard Ebert
#Importieren der nötigen Elemente (snsrape, pandas, jason, csv)
from snscrape.modules.twitter import *
import pandas as pd
import json
import csv

#Via TwitterSearchScraper Twitter-User und Datum festlegen für die gesucht werden soll
search = TwitterSearchScraper("from:HSGStGallen since:2015-01-01").get_items()

#Liste für Tweets definieren
tweets_list = []
for item in search:
    tweet_dict = {
        "tweet": item.rawContent,
        "date": item.date, 
        "url": item.url
    }
    tweets_list.append(tweet_dict)

#Liste in einem Dataframe aufbereiten 
tweets_df = pd.DataFrame(tweets_list)

#Ausgabe als Json File 
tweets_df.to_json("EbertEduard.json", orient="records")

#Ausgabe als CSV File
tweets_df.to_csv("EbertEduard.csv", index=False)