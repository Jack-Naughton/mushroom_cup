from django.shortcuts import render

import plotly.express as px
import pandas as pd


def dashboard(request):
    df = pd.read_csv('dashboard/data/temp.csv')

    fig = px.line(df,
                  x="date",
                  y="temp",
                  title='Temperature in Fahrenheit',
                  labels={'date': 'Date', 'temp': 'Degrees Fahrenheit'}
                  )

    plot_div = fig.to_html(full_html=False, include_plotlyjs=False)

    return render(request, "dashboard/index.html", context={'plot_div': plot_div})
