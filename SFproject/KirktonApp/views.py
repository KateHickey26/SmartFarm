from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView
from django.forms import Form
# from KirktonApp.models import *
# from KirktonApp.forms import UserForm
from django_jsonforms.forms import JSONSchemaForm
from .forms import UserForm, UserProfileForm, JSONSchemaField

import copy
from django.template.loader import render_to_string
from django.template.loader import get_template
import json


# forms
class JSONTestFormStatic(Form):
    json = JSONSchemaField(schema='schema.json', options={})


class JSONTestFormDouble(Form):
    json1 = JSONSchemaField(schema='schema.json', options={})
    json2 = JSONSchemaField(schema='schema.json', options={})


class JSONTestForm(Form):
    json = JSONSchemaField(
        schema={
            "type": "Feature",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Sensor Title",
                    "minLength": 2,
                    "default": "Enter the title of the sensor to be added"
                },
                "description": {
                    "type": "string",
                    "description": "Description of sensor",
                    "default": "Enter a description of the sensor or location"
                }
            },
            "geometry": {
                "type": {
                    "type": "string",
                    "description": "type of geometry",
                    "default": "Point expected"
                },
                "coordinates": {
                    "type": "string",
                    "description": "coordinates of sensor",
                    "default": "Enter the coordinates, e.g. [-4.4040, 56.2519]"
                }
            }
        },
        options={}
    )


# Create your views here.

# def index(request):
# return HttpResponse("Testing views.py")


def home(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section

    mapbox_access_token = 'pk.my_mapbox_access_token'

    # sensors = Sensor.objects.all()  # could add status equals here

    # request.session.set_test_cookie()

    return render(request, 'KirktonApp/default.html',
                  {'mapbox_access_token': mapbox_access_token})
    # {'sensors':sensors}


# about page
def about(request):
    # if request.session.test_cookie_worked():
    #     print("Test Cookie worked")
    #     request.session.delete_test_cookie()

    return render(request, 'KirktonApp/about.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # when logged in, user directed to homepage
                return redirect(reverse('default.html'))
            else:
                # an inactive account was used
                return HttpResponse("Your account is disabled.")
        else:
            # incorrect log in details were provided
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
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


class JSONFormView(FormView):
    template_name = "addSensorForm.html"
    form_class = JSONTestForm

    def get_success_url(self):
        return reverse('success')


class JSONFormViewStatic(FormView):
    template_name = "addSensorForm.html"
    form_class = JSONTestFormStatic

    def get_success_url(self):
        return reverse('success')


class JSONFormViewDouble(FormView):
    template_name = "AddSensorForm.html"
    form_class = JSONTestFormDouble

    def get_success_url(self):
        return reverse('success')


def success_view(request):
    return HttpResponse('<p id=\"success\">Success</p>')

# # @login_required
# def add_sensor_form(request):
#     form = AddSensorForm()
#
#     output = form.as_p()
#     print(output.find('class=\"editor_holder\"'))
#     media = str(form.media)
#     print(media.find('jsoneditor.min.js'))
#     return render(request, 'KirktonApp/addSensorForm.html', {'form': form})
