# Creates bar showing how many tweets are considered positive,
# neutral, or negative.

import plotly.io as pio
import sentimentanalysis

data = [
  # Tesla stock data dictionary
  dict(
    x = ['Positive', 'Neutral', 'Negative'],
    y = [
        sentimentanalysis.stock_df['Sentiment'].value_counts()['Positive'],
        sentimentanalysis.stock_df['Sentiment'].value_counts()['Neutral'],
        sentimentanalysis.stock_df['Sentiment'].value_counts()['Negative']
    ],
    type = 'bar',
    marker = dict(color = 'blue')
  ),
  # Elon Musk data dictionary
  dict(
    x = ['Positive', 'Neutral', 'Negative'],
    y = [
        sentimentanalysis.elon_df['Sentiment'].value_counts()['Positive'],
        sentimentanalysis.elon_df['Sentiment'].value_counts()['Neutral'],
        sentimentanalysis.elon_df['Sentiment'].value_counts()['Negative']
    ],
    type = 'bar',
    marker = dict(color = 'red'),
    visible = False
  ),
  # Telsa cars data dictionary
  dict(
    x = ['Positive', 'Neutral', 'Negative'],
    y = [
        sentimentanalysis.cars_df['Sentiment'].value_counts()['Positive'],
        sentimentanalysis.cars_df['Sentiment'].value_counts()['Neutral'],
        sentimentanalysis.cars_df['Sentiment'].value_counts()['Negative']
    ],
    type = 'bar',
    marker = dict(color = 'green'),
    visible = False
  )
]



layout = dict(
  title = 'Tesla Stock',
  updatemenus = [
    dict(
      buttons = list([
        dict(
          label = 'Tesla Stock',
          method = 'update',
          args=[{'visible': [True, False, False]},
          {'title' : "Tesla Stock"}]
        ),
        dict(
          label = 'Elon Musk',
          method = 'update',
          args=[{'visible': [False, True, False]},
          {'title' : "Elon Musk"}]
        ),
        dict(
          label = 'Tesla Vehicles',
          method = 'update',
          args=[{'visible': [False, False, True]},
          {'title' : "Tesla Cars"}]
        )]),
        direction="down",
        pad={"r": 10, "t": 10},
        showactive=True,
        x=0.0,
        xanchor="left",
        y=1.15,
        yanchor="top"
      
    )
  ]
)

fig_dict = dict(data = data, layout = layout)

pio.show(fig_dict, validate = False)