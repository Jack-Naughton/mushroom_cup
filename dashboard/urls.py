from django.urls import path

from . import views

urlpatterns = [
    # path('', views.dashboard, name='dashboard'),
    path('temperature', views.temperature, name='temperature'),
    path('co2', views.co2, name='co2'),
    path('humidity', views.humidity, name='humidity'),
]
