# Creates a scatter plot of the subjectivity of the tweets
# against the polarity. Those values are computed using the
# TextBlob library.

import plotly.io as pio
import electric_car_sentimental_analysis

data = [
    # Tesla stock data dictionary
    dict(
        x=electric_car_sentimental_analysis.tesla_stock_df['Polarity'],
        y=electric_car_sentimental_analysis.tesla_stock_df['Subjectivity'],
        type='scatter',
        mode='markers',
        marker=dict(size=12, color='blue', opacity=0.3)
    ),
    # BMW data dictionary
    dict(
        x=electric_car_sentimental_analysis.bmw_stock_df['Polarity'],
        y=electric_car_sentimental_analysis.bmw_stock_df['Subjectivity'],
        type='scatter',
        mode='markers',
        marker=dict(size=12, color='red', opacity=0.3),
        visible=False
    ),
    # Volkswagen data dictionary
    dict(
        x=electric_car_sentimental_analysis.volkswagen_stock_df['Polarity'],
        y=electric_car_sentimental_analysis.volkswagen_stock_df['Subjectivity'],
        type='scatter',
        mode='markers',
        marker=dict(size=12, color='green', opacity=0.3),
        visible=False
    )
]

layout = dict(
    xaxis=dict(title='Polarity'),
    yaxis=dict(title='Subjectivity'),
    title='Tesla Stock',
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    label='Tesla Stock',
                    method='update',
                    args=[{'visible': [True, False, False]},
                          {'title': "Tesla Stock"}]
                ),
                dict(
                    label='BMW Stock',
                    method='update',
                    args=[{'visible': [False, True, False]},
                          {'title': "BMW Stock"}]
                ),
                dict(
                    label='Volkswagen Stock',
                    method='update',
                    args=[{'visible': [False, False, True]},
                          {'title': "Volkswagen Stock"}]
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

fig_dict = dict(data=data, layout=layout)

pio.show(fig_dict, validate=False)