import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

musktweets = pd.read_json('Cameron/tweets_from_tesla.json')
tsla = pd.read_csv('Cameron/tsla_account_data.csv')

#omits the time from the created_at parameter
def tweets_per_day(df):
    df['created_at'] = df['created_at'].dt.date
    return df[['text']].groupby(df['created_at']).count()

tweets_per_day(musktweets)

freq = list(musktweets['created_at'].value_counts())

fig1 = px.scatter(tsla,y='Close', size = freq)
fig2 = px.line(tsla,y='Close')

fig3 = go.Figure(data=fig1.data + fig2.data)
fig3.update_layout(title = 'TSLA\'s stock price and Tesla\'s tweet frequency', yaxis_title = 'Close price', xaxis_title = 'Days')

fig3.show()