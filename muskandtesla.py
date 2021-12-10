import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

tsla = yf.download('TSLA', period = '18d', interval='1d')
musktweets = pd.read_json('tweets_from_elon.json')

#omits the time from the created_at parameter
def tweets_per_day(df):
    df['created_at'] = df['created_at'].dt.date
    return df[['text']].groupby(df['created_at']).count()

tweets_per_day(musktweets)

freq = list(musktweets['created_at'].value_counts())

fig = go.Figure()
fig.add_trace(go.Scatter(y=tsla['Close'], mode = 'lines'))
fig.add_trace(go.Scatter(y=tsla['Close'], mode = 'markers', size=freq))

fig.update_layout(title = 'TSLA Data', yaxis_title = 'Close price', xaxis_title = 'Days')

fig.show()