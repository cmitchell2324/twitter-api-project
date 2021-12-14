# Running this file will append tweets to the Tesla cars CSV

from FinalProject import twitter_keys
import tweepy
import pandas as pd

# Variables to be used in the search for tweets.
num_tweets = 20     # How many tweets to retrieve.
search_term = '"model x" OR "model 3" OR "model y" OR "model s" OR roadster -filter:retweets'      # Seach query. Disregards retweets.
file_name = 'carstweets.csv'    # Name of the csv file the dataframe of tweets will be written to.


# Create authentication object
authenticate = tweepy.OAuthHandler(twitter_keys.consumer_key, twitter_keys.consumer_secret)
#Set access token and secret
authenticate.set_access_token(twitter_keys.access_token, twitter_keys.access_token_secret)
# Create API object
api = tweepy.API(authenticate, wait_on_rate_limit=True)


# Gather tweets into a list using the variables specified above. 
tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang='en', tweet_mode='extended').items(num_tweets)
# Store tweets in a variable and get the full text.
all_tweets = [tweet.full_text for tweet in tweets]

# Create a dataframe to store the tweets with a column called 'Tweets'.
df = pd.DataFrame(all_tweets, columns=['Tweets'])

pd.read_csv(file_name).append(df).drop_duplicates().to_csv(file_name,index=False)

df2 = pd.read_csv(file_name)

print("Tesla cars df shape:")
print(df2.shape)    # This shows how many tweets are in the dataframe after the append.