import json
import csv
import datetime
from snscrape.modules.twitter import *

# Set the start date for the tweet search
start_date = datetime.datetime(2015, 1, 1)

# Create a filter for tweets posted after the start date
filter_str = f"from:HSGStGallen since:{start_date.strftime('%Y-%m-%d')}"

# Use the filter with the TwitterSearchScraper to retrieve the tweets
search = TwitterSearchScraper(filter_str).get_items()

output = []

for item in search:
    output.append({
        "tweet": item.rawContent,
        "url": item.url,
        "date": item.date.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "replies": item.replyCount,
        "retweets": item.retweetCount,
        "likes": item.likeCount,
    })

# Save the output to a JSON file
with open("AudreyHermann.json", "w") as f:
    json.dump(output, f)

#Save the output as CSV file
#with open("AudreyHermann.csv", "w", newline="", encoding="utf-8") as f:
    #writer = csv.DictWriter(f, fieldnames=output[0].keys())
    #writer.writeheader()
    #writer.writerows(output)

#Message that code is completed
print("Done, it worked finally :)")

