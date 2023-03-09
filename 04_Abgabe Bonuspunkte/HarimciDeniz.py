from snscrape.modules.twitter import *
import json
from datetime import datetime

search = TwitterUserScraper("HSGStGallen").get_items()
# convert to datetime to compare time https://www.programiz.com/python-programming/datetime
datetime_str = '2015-01-01 00:00:01'
datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
dictionary = []
for item in search:
    # remove timezone information to compare values in if statement: https://www.geeksforgeeks.org/how-to-remove-timezone-information-from-datetime-object-in-python/
    item.date = item.date.replace(tzinfo=None)
    datetime_item = datetime.strptime(str(item.date), '%Y-%m-%d %H:%M:%S')
    if  datetime_item >= datetime_object:
        print({
            "date": item.date,
            "tweet": item.rawContent,
            "url": item.url,
        })
        # add element to list https://java2blog.com/add-tuple-to-list-python/
        dictionary.append({"tweet": item.rawContent, "url": item.url,})
        
    else:
        pass
# List to json output file https://pythonexamples.org/python-list-to-json/
with open('new_data.json', 'w') as outfile:
    json.dump(dictionary, outfile)

