from django.shortcuts import render

import plotly.express as px
import pandas as pd


def _render_chart(file, x, y, title, labels):
    """ Helper method to render a plotly chart"""

    df = pd.read_csv(file)

    fig = px.line(df,
                  x=x,
                  y=y,
                  title=title,
                  labels=labels
                  )

    return fig.to_html(full_html=False, include_plotlyjs=False)


def temperature(request):
    chart = _render_chart(
        file='dashboard/data/temp.csv',
        x='date',
        y='temp',
        title='Temperature',
        labels={'date': 'Date', 'temp': 'Degrees Fahrenheit'}
    )

    return render(request, "dashboard/index.html", context={'chart': chart})


def co2(request):
    chart = _render_chart(
        file='dashboard/data/co2.csv',
        x='date',
        y='co2',
        title='CO2',
        labels={'date': 'Date', 'co2': 'PPM'}
    )

    return render(request, "dashboard/index.html", context={'chart': chart})


def humidity(request):
    chart = _render_chart(
        file='dashboard/data/humidity.csv',
        x='date',
        y='humidity',
        title='Humidity',
        labels={'date': 'Date', 'co2': '% Humidity'}
    )

    return render(request, "dashboard/index.html", context={'chart': chart})
