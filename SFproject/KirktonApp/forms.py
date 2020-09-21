from django import forms
from django.contrib.auth.models import User
from django.forms import Form
from django_jsonforms.forms import JSONSchemaField


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    # this widget keeps the password hidden


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    # this widget keeps the password hidden

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_staff', 'is_superuser',)


# beginning of the form for entering a new sensor for the map
class AddSensorForm(Form):
    json = JSONSchemaField(schema={
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
        options={"theme": "bootstrap3"}, ajax=True)
