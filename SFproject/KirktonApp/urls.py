#from django.urls import path
from django.conf.urls import url
from KirktonApp import views

app_name = 'KirktonApp'

urlpatterns = [
    #path('', views.index, name='index'),
    url(r'', views.default_map, name="default"),
]
