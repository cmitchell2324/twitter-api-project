# This file contains creates dataframes that store sentiment 
# analysis information that will be used to create visualizations.

from textblob import TextBlob
import pandas as pd
import re

stock_df = pd.read_csv('Jacob/tslatweets.csv')
elon_df = pd.read_csv('Jacob/elonmusktweets.csv')
cars_df = pd.read_csv('Jacob/carstweets.csv')

# Function to clean the tweets
def cleanTwt(twt):
  twt = re.sub('#tsla', 'tsla', twt) # Remove the # symbol
  twt = re.sub('#TSLA', 'TSLA', twt) # Remove the # symbol
  twt = re.sub('#[A-Za-xz0-9]+', '', twt) # Removes any string with a hashtag
  twt = re.sub('\\n', '', twt) # Remove newline characters
  twt = re.sub('https?:\/\/\S+', '', twt) # Remove URLS
  return twt

# Clean the tweets
stock_df['Cleaned_Tweets'] = stock_df['Tweets'].apply(cleanTwt)
elon_df['Cleaned_Tweets'] = elon_df['Tweets'].apply(cleanTwt)
cars_df['Cleaned_Tweets'] = cars_df['Tweets'].apply(cleanTwt)

# Function to get the subjectivity
def getSubjectivity(twt):
  return TextBlob(twt).sentiment.subjectivity

# Function to get the polarity
def getPolarity(twt):
  return TextBlob(twt).sentiment.polarity

#Create new columns 'subjectivity' and 'polarity'
stock_df['Subjectivity'] = stock_df['Cleaned_Tweets'].apply(getSubjectivity)
stock_df['Polarity'] = stock_df['Cleaned_Tweets'].apply(getPolarity)
elon_df['Subjectivity'] = elon_df['Cleaned_Tweets'].apply(getSubjectivity)
elon_df['Polarity'] = elon_df['Cleaned_Tweets'].apply(getPolarity)
cars_df['Subjectivity'] = cars_df['Cleaned_Tweets'].apply(getSubjectivity)
cars_df['Polarity'] = cars_df['Cleaned_Tweets'].apply(getPolarity)


# Function to get the sentiment of the text
def getSentiment(score):
  if score < 0:
    return 'Negative'
  elif score == 0:
    return 'Neutral'
  else:
    return 'Positive'

# Create a column to store the sentiment of the text
stock_df['Sentiment'] = stock_df['Polarity'].apply(getSentiment)
elon_df['Sentiment'] = elon_df['Polarity'].apply(getSentiment)
cars_df['Sentiment'] = cars_df['Polarity'].apply(getSentiment)