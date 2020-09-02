from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
#from KirktonApp.models import *
from django_jsonforms.forms import JSONSchemaForm
from .forms import AddSensorForm

# from KirktonApp.forms import UserForm
import copy
from django.template.loader import render_to_string
from django.template.loader import get_template
import json


# Create your views here.

# def index(request):
# return HttpResponse("Testing views.py")


def home(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section

    mapbox_access_token = 'pk.my_mapbox_access_token'

    sensors = Sensor.objects.all()

    return render(request, 'KirktonApp/default.html',
                  {'mapbox_access_token': mapbox_access_token})
    # {'sensors':sensors}


# about page
def about(request):
    return render(request, 'KirktonApp/about.html')


# def add_sensor_form(request):
#     form = AddSensorForm()
#
#     # output = form.as_p()
#     return render(request, 'KirktonApp/addSensorForm.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('default.html'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'KirktonApp/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('KirktonApp/default.html'))
