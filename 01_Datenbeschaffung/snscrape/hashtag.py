from snscrape.modules.twitter import *

search = TwitterHashtagScraper("borussia").get_items()
for item in search:
    print({
        "tweet": item.rawContent,
        "url": item.url,
    })

