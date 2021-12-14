#This generates the tweets in tsldata.csv. Don't run this.


import pandas as pd
import tweepy as tw

#Your keys go here
CONSUMER_KEY = "dB3bFw9FaHZZIPzblZiVWQFpF"
CONSUMER_SECRET = "LqvaHy4okTp6Gw8FlhWsV3lIqY68qsBIPLWYfY0zZ6fNTZLuFB"
OAUTH_TOKEN = "4825730011-yzrM5K96EYBrggIHqCaUeGNmbpUXkYsds4dv3oo"
OAUTH_TOKEN_SECRET = "hKEa8kVIbMU0QQhHX3ffmSsbEDuJUWxWsOCdLFqy7KJUj"
    
auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    
api = tw.API(auth, wait_on_rate_limit=True)

data = []

t_keywords = "$TSLA "
t_datelimit = "2021-12-11"
t_until = "2021-12-12"
t_finalq = t_keywords + " since:" + t_datelimit + " until:" + t_until + " -filter:retweets"

toyota_keywords = "$TOYOF "
toyota_finalq = toyota_keywords + " since:" + t_datelimit + " until:" + t_until + " -filter:retweets"

v_keywords = "$VWAGY "
v_finalq = v_keywords + " since:" + t_datelimit + " until:" + t_until + " -filter:retweets"

h_keywords = "$HMC "
h_finalq = h_keywords + " since:" + t_datelimit + " until:" + t_until + " -filter:retweets"

f_keywords = "$RACE "
f_finalq = f_keywords + " since:" + t_datelimit + " until:" + t_until + " -filter:retweets"

teslaTweets = tw.Cursor(api.search_tweets, q=t_finalq,lang='en').items(200)
toyotaTweets = tw.Cursor(api.search_tweets, q=toyota_finalq,lang='en').items(200)
vTweets = tw.Cursor(api.search_tweets, q=v_finalq,lang='en').items(200)
hTweets = tw.Cursor(api.search_tweets, q=h_finalq,lang='en').items(200)
fTweets = tw.Cursor(api.search_tweets, q=f_finalq,lang='en').items(200)

for tweet in teslaTweets:
    data.append(["TSLA", tweet.text.encode('utf-8')])

for tweet in toyotaTweets:
    data.append(["TOYOF", tweet.text.encode('utf-8')])

for tweet in vTweets:
    data.append(["VWAGY", tweet.text.encode('utf-8')])

for tweet in hTweets:
    data.append(["HMC", tweet.text.encode('utf-8')])

for tweet in fTweets:
    data.append(["RACE", tweet.text.encode('utf-8')])

df = pd.DataFrame(data, columns=['Ticker', 'Tweet'])
df.to_csv('tickerdata.csv', encoding='utf-8', index=False)
