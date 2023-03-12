from snscrape.modules.twitter import *
import pandas as pd

# Startdatum ist der 01.01.2015
since_date = '2015-01-01'

# Bestimmung des Suchbegriffs und Startdatum (from um nur die eigenen Tweets zu ziehen)
search_query = 'from:HSGStGallen since:' + since_date

# Ausführen der Suchanfrage
search_results = TwitterSearchScraper(search_query).get_items()

# Initialisieren der Liste
tweets_list = []

# Loop durch die Ergebnisse und Anhängen dieser an die Liste
for tweet in search_results:
    tweets_list.append({
        'tweet_content': tweet.rawContent,
        'tweet_url': tweet.url
    })

# Pandas Data Frame
df = pd.DataFrame(tweets_list)

# Konvertieren in JSON file
df.to_json('RafeinerIsabel.json', orient='records')
