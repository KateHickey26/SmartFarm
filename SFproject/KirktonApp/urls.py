#from django.urls import path
from django.conf.urls import url
from django.urls import path, include
from KirktonApp import views

app_name = 'KirktonApp'

urlpatterns = [
    #path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
