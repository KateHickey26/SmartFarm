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

    return render(request, 'KirktonApp/default.html',
                  {'mapbox_access_token': mapbox_access_token})
    # {'sensors':sensors}


# about page
def about(request):
    return render(request, 'KirktonApp/about.html')


# @login_required
def add_sensor_form(request):
    form = AddSensorForm()

    output = form.as_p()
    print(output.find('class=\"editor_holder\"'))
    media = str(form.media)
    print(media.find('jsoneditor.min.js'))
    return render(request, 'KirktonApp/addSensorForm.html', {'form': form})


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


def register_user(request):
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes value to
    # True when registration succeeds.
    registered = False

    # if its an http request, process form data
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        # if the two forms are valid, save users form to database
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            # hash the password with set_password method and update the user object
            user.set_password(user.password)
            user.save()

            # commit = False because we need to set the user attribute ourselves
            # avoids any integrity problems with saving the model until we are ready to.
            # Stops django saving the data to the database in the first instance.
            # Attempting to save the new instance in an incomplete state would raise a referential integrity error
            profile = profile_form.save(commit=False)
            profile.user = user

            # manually saves the new instance to the database
            profile.save()

            # update variable to indicate the template registration was successful
            registered = True
        else:
            # prints to terminal if mistakes or invalid form
            print(user_form.errors, profile_form.errors)
    else:
        # if not an Http post render using two ModelForm instances
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'KirktonApp/registerUser.html',
                  context = {'user_form': user_form,
                             'profile_form': profile_form,
                             'registered': registered})

