from snscrape.modules.twitter import *
from datetime import datetime
import json
import csv

since_date = datetime(2015, 1, 1)
query = "from:HSGStGallen since:2014-12-31"

search = TwitterSearchScraper(query).get_items()
tweets =[]
for item in search:
    tweets.append({"tweet": item.rawContent, "url": item.url,})

# Writing json file
json_object = json.dumps(tweets)
json_file = open("HausmannJohannes.json", "w")
json_file.write(json_object)
json_file.close()