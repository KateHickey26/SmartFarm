#from django.urls import path
from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from KirktonApp import views

app_name = 'KirktonApp'

urlpatterns = [
    #path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('about/', views.about, name='about'),
    path('add_sensor_form/', views.add_sensor_form, name='add_sensor_form'),
    path('register_user/', views.register_user, name='registerUser'),
]


