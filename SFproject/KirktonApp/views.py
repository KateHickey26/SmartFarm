from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
# from KirktonApp.models import *
# from KirktonApp.forms import UserForm
from django_jsonforms.forms import JSONSchemaForm
from .forms import AddSensorForm, UserForm, UserProfileForm

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

    # sensors = Sensor.objects.all()  # could add status equals here

    request.session.set_test_cookie()

    return render(request, 'KirktonApp/default.html',
                  {'mapbox_access_token': mapbox_access_token})
    # {'sensors':sensors}


# about page
def about(request):
    if request.session.test_cookie_worked():
        print("Test Cookie worked")
        request.session.delete_test_cookie()

    return render(request, 'KirktonApp/about.html')


# @login_required
def add_sensor_form(request):
    form = AddSensorForm()

    output = form.as_p()
    print(output.find('class=\"editor_holder\"'))
    media = str(form.media)
    print(media.find('jsoneditor.min.js'))
    return render(request, 'KirktonApp/addSensorForm.html', {'form': form})

