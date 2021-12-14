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
    # Kandi Technologies Group data dictionary
    dict(
        x=electric_car_sentimental_analysis.kndi_stock_df['Polarity'],
        y=electric_car_sentimental_analysis.kndi_stock_df['Subjectivity'],
        type='scatter',
        mode='markers',
        marker=dict(size=12, color='red', opacity=0.3),
        visible=False
    ),
    # Rivian data dictionary
    dict(
        x=electric_car_sentimental_analysis.rivian_stock_df['Polarity'],
        y=electric_car_sentimental_analysis.rivian_stock_df['Subjectivity'],
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
                    label='Kandi Stock',
                    method='update',
                    args=[{'visible': [False, True, False]},
                          {'title': "Kandi Stock"}]
                ),
                dict(
                    label='Rivian Stock',
                    method='update',
                    args=[{'visible': [False, False, True]},
                          {'title': "Rivian Stock"}]
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