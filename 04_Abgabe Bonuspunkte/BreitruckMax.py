#Import of the two used libraries snscrape as well as pandas
import snscrape.modules.twitter as sntwitter
import pandas as pd

# List where tweets can get appended to
tweets_list = []

# Using the TwitterSearchScraper from the snscrape library to scrape data and append the tweets to the list
# Definition of 8k limit as query always stopped when inserting since:2015-01-01 until:2023-03-08 therefore workaround with pd Dataframe
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:hsgstgallen').get_items()):
    if i>8000:
        break
    tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    
# Creating a dataframe from the tweets list above 
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# Convert the "Datetime" column to a pandas datetime format
tweets_df['Datetime'] = pd.to_datetime(tweets_df['Datetime'])

# Filter the dataframe to remove rows with "Datetime" earlier than 2015
df_tweets_filtered = tweets_df[tweets_df['Datetime'].dt.year >= 2015]

#gfenerates a json
df_tweets_filtered.to_json

# will of course only work if path is set to the right directory 
df_tweets_filtered.to_json(r'/Users/maxbreitruck/Library/CloudStorage/OneDrive-UniversitätSt.Gallen/01_Master/2. Semester/Data2Dollar/Challenge 1\Challenge_1.json')