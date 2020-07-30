from django.urls import path
from KirktonApp import views

app_name = 'KirktonApp'

urlpatterns = [
    path('', views.index, name='index'),
]
