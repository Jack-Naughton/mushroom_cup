from django.urls import path
from django.views.generic.base import RedirectView


from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='co2'), name='dashboard'),
    path('co2', views.co2, name='co2'),
    path('humidity', views.humidity, name='humidity'),
    path('temperature', views.temperature, name='temperature'),
]
