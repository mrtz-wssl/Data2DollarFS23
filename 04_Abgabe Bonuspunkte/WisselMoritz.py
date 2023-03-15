# Quelle: MartinBeckUT,
# https://github.com/MartinKBeck/TwitterScraper/blob/master/snscrape/python-wrapper/snscrape-python-wrapper.py ,
# Stand: 13.03.2023, 15:00 Uhr


# Importieren von Pandas und snscrape
import pandas as pd
import snscrape.modules.twitter as sntwitter

# Erstellen einer Liste, um die Tweets darin zu speichern
tweets = []

# Scraping der Daten durch eine For-Schleife, die alle Tweets des Users HSGStGallen seit dem 01.01.2015 scraped
# und der "tweets" Liste anhängt. Von den Tweets werden ebenfalls Datum, Uhrzeit, ID, Inhalt und Username gespeichert.
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:HSGStGallen since:2014-12-31').get_items()):
  tweets.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

# Umwandlung der Liste in einen Dataframe und Export dessen als JSON-Datei
tweets_df = pd.DataFrame(tweets, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
tweets_df.to_json('HSG_tweets.json', index=True)
