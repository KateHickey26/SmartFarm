from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_text
from six import python_2_unicode_compatible

# Create your models here.




class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    username = models.CharField(blank=False, max_length=25, default="username")

    # method to return a meaningful value when a string
    # representation of a user profile is requested
    def __str__(self):
        return self.user.username

