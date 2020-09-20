from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
# from django_jsonforms.forms import JSONSchemaForm
from .forms import AddSensorForm, UserForm

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

    #request.session.set_test_cookie()

    return render(request, 'KirktonApp/default.html',
                  {'mapbox_access_token': mapbox_access_token})


# about page
def about(request):
    # if request.session.test_cookie_worked():
    #     print("Test Cookie worked")
    #     request.session.delete_test_cookie()

    return render(request, 'KirktonApp/about.html')


def sensor_graph(request):

    return render(request, 'KirktonApp/sensorGraph.html')


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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # when logged in, user directed to homepage
                return redirect(reverse('KirktonApp:home'))
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
    return redirect(reverse('KirktonApp:home'))


@login_required
def my_account(request):
    user = request.user

    # if post, change data
    if request.method == 'POST':
        newname = request.POST.get('username')
        newpassword = request.POST.get('password')
        print(request.FILES)
        if newname is not "":
            user.username = newname
        if newpassword is not "":
            user.set_password(newpassword)
        user.save()
        return render(request, 'KirktonApp/myAccount.html')

    else:

        return render(request, 'KirktonApp/myAccount.html')


@login_required
def register_user(request):
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes value to
    # True when registration succeeds.
    registered = False

    # if its an http request, process form data
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        # profile_form = UserForm(request.POST)

        # if the two forms are valid, save users form to database
        if user_form.is_valid():
            user = user_form.save()

            # hash the password with set_password method and update the user object
            user.set_password(user.password)
            user.save()

            # commit = False because we need to set the user attribute ourselves
            # avoids any integrity problems with saving the model until we are ready to.
            # Stops django saving the data to the database in the first instance.
            # Attempting to save the new instance in an incomplete state would raise a referential integrity error
            # profile = profile_form.save(commit=False)
            # profile.user = user

            # manually saves the new instance to the database
            # profile.save()

            # update variable to indicate the template registration was successful
            registered = True
        else:
            # prints to terminal if mistakes or invalid form
            print(user_form.errors)
    else:
        # if not an Http post render using two ModelForm instances
        user_form = UserForm()

    return render(request,
                  'KirktonApp/registerUser.html',
                  context={'user_form': user_form,
                           'registered': registered})
    return redirect(reverse('KirktonApp:home'))
