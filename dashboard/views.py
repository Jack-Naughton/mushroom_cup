from django.shortcuts import render

import pandas as pd


def dashboard(request):
    # temps = pd.read_csv('dashboard/data/temp.csv')
    return render(request, 'dashboard/index.html', {'temperatures': [
        {'date': '2021-09-02', 'temp': 90},
        {'date': '2021-09-03', 'temp': 91},
        {'date': '2021-09-04', 'temp': 90},
        {'date': '2021-09-05', 'temp': 94},
    ]})
