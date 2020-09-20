from django.urls import path
from KirktonApp import views


app_name = 'KirktonApp'


urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('about/', views.about, name='about'),
    path('sensor_graph/', views.sensor_graph, name='sensor_graph'),
    path('add_sensor_form/', views.add_sensor_form, name='add_sensor_form'),
    path('register_user/', views.register_user, name='register_user'),
    path('my_account/', views.my_account, name='my_account'),
]
