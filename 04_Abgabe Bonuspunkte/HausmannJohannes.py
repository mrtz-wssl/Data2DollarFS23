from snscrape.modules.twitter import *
from datetime import datetime
import json
import csv

since_date = datetime(2015, 1, 1)
query = "from:HSGStGallen since:2015-01-01"

search = TwitterSearchScraper(query).get_items()
tweets =[]
for item in search:
    tweets.append({"tweet": item.rawContent, "url": item.url,})

# Writing json file
json_object = json.dumps(tweets)
json_file = open("HausmannJohannes.json", "w")
json_file.write(json_object)
json_file.close()

# Writing csv file
with open("HausmannJohannes.csv", "w", newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["tweet", "url"])
    for tweet in tweets:
        writer.writerow([tweet["tweet"], tweet["url"]])