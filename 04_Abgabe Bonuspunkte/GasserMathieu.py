import snscrape.modules.twitter as sntwitter
import json

# set the search query parameters
username = 'HSGStGallen'
since_date = '2015-01-01'

# set up the scraper
tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{username} since:{since_date}').get_items()):
    tweet_dict = {
        'id': tweet.id,
        'date': tweet.date.strftime('%Y-%m-%d %H:%M:%S'),
        'content': tweet.content,
        'username': tweet.user.username,
        'url': tweet.url
    }
    tweets.append(tweet_dict)
    if i % 100 == 0:
        print(f'Scraped {i} tweets so far...')

# save the results to a file
with open('GasserMathieu.json', 'w', encoding='utf-8') as f:
    json.dump(tweets, f, ensure_ascii=False, indent=4)