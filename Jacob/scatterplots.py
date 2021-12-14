# Creates a scatter plot of the subjectivity of the tweets 
# against the polarity. Those values are computed using the 
# TextBlob library.

import plotly.io as pio
import sentimentanalysis

data = [
  # Tesla stock data dictionary
  dict(
    x = sentimentanalysis.stock_df['Polarity'],
    y = sentimentanalysis.stock_df['Subjectivity'],
    type = 'scatter',
    mode = 'markers',
    marker = dict(size = 12, color = 'blue', opacity = 0.3)
  ),
  # Elon Musk data dictionary
  dict(
    x = sentimentanalysis.elon_df['Polarity'],
    y = sentimentanalysis.elon_df['Subjectivity'],
    type = 'scatter',
    mode = 'markers',
    marker = dict(size = 12, color = 'red', opacity = 0.3),
    visible = False
  ),
  # Telsa cars data dictionary
  dict(
    x = sentimentanalysis.cars_df['Polarity'],
    y = sentimentanalysis.cars_df['Subjectivity'],
    type = 'scatter',
    mode = 'markers',
    marker = dict(size = 12, color = 'green', opacity = 0.3),
    visible = False
  )
]

layout = dict(
  xaxis = dict(title = 'Polarity'),
  yaxis = dict(title = 'Subjectivity'),
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