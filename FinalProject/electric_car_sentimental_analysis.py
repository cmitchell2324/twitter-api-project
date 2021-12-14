# This file contains creates dataframes that store sentiment
# analysis information that will be used to create visualizations.

from textblob import TextBlob
import pandas as pd
import re

tesla_stock_df = pd.read_csv('tslatweets.csv')
bmw_stock_df = pd.read_csv('bmwyy_tweets.csv')
volkswagen_stock_df = pd.read_csv('vlkaf_tweets.csv')

# Function to clean the tweets
def cleanTwt(twt):
  twt = re.sub('#tsla', 'tlsa', twt)  # Remove the # symbol
  twt = re.sub('#TSLA', 'TSLA', twt)  # Remove the # symbol
  twt = re.sub('#bmwyy', 'bmwyy', twt) # Remove the # symbol
  twt = re.sub('#BMWYY', 'BMWYY', twt) # Remove the # symbol
  twt = re.sub('#vlkaf', 'vlkaf', twt)  # Remove the # symbol
  twt = re.sub('#VLKAF', 'VLKAF', twt)  # Remove the # symbol
  twt = re.sub('#[A-Za-xz0-9]+', '', twt) # Removes any string with a hashtag
  twt = re.sub('\\n', '', twt) # Remove newline characters
  twt = re.sub('https?:\/\/\S+', '', twt) # Remove URLS
  return twt

# Clean the tweets
tesla_stock_df['Cleaned_Tweets'] = tesla_stock_df['Tweets'].apply(cleanTwt)
bmw_stock_df['Cleaned_Tweets'] = bmw_stock_df['Tweets'].apply(cleanTwt)
volkswagen_stock_df['Cleaned_Tweets'] = volkswagen_stock_df['Tweets'].apply(cleanTwt)

# Function to get the subjectivity
def getSubjectivity(twt):
  return TextBlob(twt).sentiment.subjectivity

# Function to get the polarity
def getPolarity(twt):
  return TextBlob(twt).sentiment.polarity

#Create new columns 'subjectivity' and 'polarity'
tesla_stock_df['Subjectivity'] = tesla_stock_df['Cleaned_Tweets'].apply(getSubjectivity)
tesla_stock_df['Polarity'] = tesla_stock_df['Cleaned_Tweets'].apply(getPolarity)
bmw_stock_df['Subjectivity'] = bmw_stock_df['Cleaned_Tweets'].apply(getSubjectivity)
bmw_stock_df['Polarity'] = bmw_stock_df['Cleaned_Tweets'].apply(getPolarity)
volkswagen_stock_df['Subjectivity'] = volkswagen_stock_df['Cleaned_Tweets'].apply(getSubjectivity)
volkswagen_stock_df['Polarity'] = volkswagen_stock_df['Cleaned_Tweets'].apply(getPolarity)


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
bmw_stock_df['Sentiment'] = bmw_stock_df['Polarity'].apply(getSentiment)
volkswagen_stock_df['Sentiment'] = volkswagen_stock_df['Polarity'].apply(getSentiment)