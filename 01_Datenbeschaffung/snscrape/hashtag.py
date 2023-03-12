from snscrape.modules.twitter import *

search = TwitterHashtagScraper("HSGStGallen").get_items()
for item in search:
    print({
        "tweet": item.rawContent,
        "url": item.url,
    })

