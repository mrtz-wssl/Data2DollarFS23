# Marc Sieber 17-603-473
# Import snscrape und pandas
from snscrape.modules.twitter import *
import pandas as pd

# Funktion TwitterSearchScraper von snscrape verwendet um nach User und Datum zu suchen
search = TwitterSearchScraper("from:HSGStGallen since:2015-01-01").get_items()

# Leere Liste erstellt um Tweets zu speichern
data = []
for item in search:
    # Tweets mit URL in die Liste einfügen
    data.append("tweet: " + item.rawContent + "url: " + item.url)

# Liste in einen Dataframe konvertieren
df = pd.DataFrame(data)

# JSON Datei aus dem Dataframe machen
df.to_json("SieberMarc.json", orient="records")