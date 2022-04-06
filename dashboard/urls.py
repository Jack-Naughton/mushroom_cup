from django.urls import path

from . import views

urlpatterns = [
    # path('', views.dashboard, name='dashboard'),
    path('temperature', views.temperature, name='dashboard'),
    path('co2', views.co2, name='dashboard'),
    path('humidity', views.humidity, name='dashboard'),
]
