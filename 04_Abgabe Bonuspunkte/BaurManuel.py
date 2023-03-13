import json
from snscrape.modules.twitter import *


# https://datasciencedojo.com/blog/scrape-twitter-data-using-snscrape/
# Liste um einzelne Tweets abzuspeichern
tweetList = []

#speichert in einer for-loop alle Tweets seit dem 01.01.2015 in tweetList ab
# https://github.com/JustAnotherArchivist/snscrape/issues/81
for tweet in TwitterSearchScraper('from:HSGStGallen since:2015-01-01').get_items():
	

# Datum von twitter umwandeln: https://stackoverflow.com/questions/7703865/going-from-twitter-date-to-python-datetime-date
	i = {
		"date": tweet.date.strftime('%Y-%m-%d %H:%M:%S'),	        
		"tweet": tweet.rawContent,
		"url": tweet.url     
	}

	tweetList.append(i)


# Schreibt tweets in json file : https://www.geeksforgeeks.org/json-dump-in-python/
# damit es schön formatiert: https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file
with open('tweets_HSGSTGallen.json', 'w', encoding='utf-8') as json_file:
    json.dump(tweetList, json_file, ensure_ascii=False, indent=4)