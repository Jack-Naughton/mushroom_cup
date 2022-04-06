from django.shortcuts import render

import plotly.express as px
import pandas as pd


def temperature(request):
    df = pd.read_csv('dashboard/data/temp.csv')

    fig = px.line(df,
                  x="date",
                  y="temp",
                  title='Temperature',
                  labels={'date': 'Date', 'temp': 'Degrees Fahrenheit'}
                  )

    plot_div = fig.to_html(full_html=False, include_plotlyjs=False)

    return render(request, "dashboard/index.html", context={'plot_div': plot_div})


def co2(request):
    df = pd.read_csv('dashboard/data/co2.csv')

    fig = px.line(df,
                  x="date",
                  y="co2",
                  title='CO2',
                  labels={'date': 'Date', 'co2': 'PPM'}
                  )

    plot_div = fig.to_html(full_html=False, include_plotlyjs=False)

    return render(request, "dashboard/index.html", context={'plot_div': plot_div})


def humidity(request):
    df = pd.read_csv('dashboard/data/humidity.csv')

    fig = px.line(df,
                  x="date",
                  y="humidity",
                  title='Humidity',
                  labels={'date': 'Date', 'humidity': '% Humidity'}
                  )

    plot_div = fig.to_html(full_html=False, include_plotlyjs=False)

    return render(request, "dashboard/index.html", context={'plot_div': plot_div})
