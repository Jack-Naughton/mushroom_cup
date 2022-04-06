from django.shortcuts import render

import plotly.express as px
import pandas as pd


def _render_chart(file, x, y, title, labels, plot_color=None):
    """ Helper method to render a plotly chart"""

    df = pd.read_csv(file)

    df['date'] = pd.to_datetime(df['date'])

    fig = px.scatter(df,
                     x=x,
                     y=y,
                     title=title,
                     labels=labels,
                     opacity=.3,
                     trendline='rolling',
                     trendline_options={'window': 300, 'center': True},
                     trendline_color_override='darkred',
                     )

    fig.update_traces(marker={'color': plot_color})

    mean = df[y].mean()

    fig.add_hline(
        y=mean,
        line_dash='dash',
        annotation_text='avg',
        annotation_font_size=20,
    )

    fig.add_hline(
        y=mean + df[y].std(),
        line_dash='dot',
        annotation_text='+1 std',
        annotation_font_size=20,
    )

    fig.add_hline(
        y=mean + df[y].std(),
        line_dash='dot',
        annotation_text='+1 std',
        annotation_font_size=20,
    )

    fig.add_hline(
        y=mean - df[y].std(),
        line_dash='dot',
        annotation_text='-1 std',
        annotation_font_size=20,
    )

    return fig.to_html(full_html=False, include_plotlyjs=False)


def temperature(request):
    chart = _render_chart(
        file='dashboard/data/temp.csv',
        x='date',
        y='temp',
        title='Temperature',
        labels={'date': 'Date', 'temp': 'Degrees Fahrenheit'},
        plot_color='blue',
    )

    return render(request, "dashboard/index.html", context={'chart': chart})


def co2(request):
    chart = _render_chart(
        file='dashboard/data/co2.csv',
        x='date',
        y='co2',
        title='CO2',
        labels={'date': 'Date', 'co2': 'PPM'},
    )

    return render(request, "dashboard/index.html", context={'chart': chart})


def humidity(request):
    chart = _render_chart(
        file='dashboard/data/humidity.csv',
        x='date',
        y='humidity',
        title='Humidity',
        labels={'date': 'Date', 'humidity': '% Humidity'},
        plot_color='green',
    )

    return render(request, "dashboard/index.html", context={'chart': chart})
