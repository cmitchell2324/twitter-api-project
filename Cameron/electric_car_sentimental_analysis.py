# This file contains creates dataframes that store sentiment
# analysis information that will be used to create visualizations.

from textblob import TextBlob
import pandas as pd
import re

tesla_stock_df = pd.read_csv('Jacob/tslatweets.csv')
kndi_stock_df = pd.read_csv('Cameron/kndi_tweets.csv')
rivian_stock_df = pd.read_csv('Cameron/rivn_tweets.csv')

# Function to clean the tweets
def cleanTwt(twt):
  twt = re.sub('#tsla', 'tlsa', twt)  # Remove the # symbol
  twt = re.sub('#TSLA', 'TSLA', twt)  # Remove the # symbol
  twt = re.sub('#kndi', 'kndi', twt) # Remove the # symbol
  twt = re.sub('#KNDI', 'KNDI', twt) # Remove the # symbol
  twt = re.sub('#rivn', 'rivn', twt)  # Remove the # symbol
  twt = re.sub('#RIVN', 'RIVN', twt)  # Remove the # symbol
  twt = re.sub('#[A-Za-xz0-9]+', '', twt) # Removes any string with a hashtag
  twt = re.sub('\\n', '', twt) # Remove newline characters
  twt = re.sub('https?:\/\/\S+', '', twt) # Remove URLS
  return twt

# Clean the tweets
tesla_stock_df['Cleaned_Tweets'] = tesla_stock_df['Tweets'].apply(cleanTwt)
kndi_stock_df['Cleaned_Tweets'] = kndi_stock_df['Tweets'].apply(cleanTwt)
rivian_stock_df['Cleaned_Tweets'] = rivian_stock_df['Tweets'].apply(cleanTwt)

# Function to get the subjectivity
def getSubjectivity(twt):
  return TextBlob(twt).sentiment.subjectivity

# Function to get the polarity
def getPolarity(twt):
  return TextBlob(twt).sentiment.polarity

#Create new columns 'subjectivity' and 'polarity'
tesla_stock_df['Subjectivity'] = tesla_stock_df['Cleaned_Tweets'].apply(getSubjectivity)
tesla_stock_df['Polarity'] = tesla_stock_df['Cleaned_Tweets'].apply(getPolarity)
kndi_stock_df['Subjectivity'] = kndi_stock_df['Cleaned_Tweets'].apply(getSubjectivity)
kndi_stock_df['Polarity'] = kndi_stock_df['Cleaned_Tweets'].apply(getPolarity)
rivian_stock_df['Subjectivity'] = rivian_stock_df['Cleaned_Tweets'].apply(getSubjectivity)
rivian_stock_df['Polarity'] = rivian_stock_df['Cleaned_Tweets'].apply(getPolarity)


# Function to get the sentiment of the text
def getSentiment(score):
  if score < 0:
    return 'Negative'
  elif score == 0:
    return 'Neutral'
  else:
    return 'Positive'

# Create a column to store the sentiment of the text
tesla_stock_df['Sentiment'] = tesla_stock_df['Polarity'].apply(getSentiment)
kndi_stock_df['Sentiment'] = kndi_stock_df['Polarity'].apply(getSentiment)
rivian_stock_df['Sentiment'] = rivian_stock_df['Polarity'].apply(getSentiment)