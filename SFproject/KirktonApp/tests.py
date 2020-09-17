from django.urls import reverse

from SFproject.KirktonApp.models import UserProfile
from django.test import TestCase, Client, override_settings
from django.contrib import auth
import os
import django
django.setup()
#from populate import *

# Creating a test user profile
def setUp(self):
        self.user = UserProfile.objects.create(username="testperson")
        self.user.email = "testperson@test.com"
        self.user.set_password("password1")
        self.user.save()
        self.profile = UserProfile(user=self.user)
        self.profile.save()
        self.client = Client()


# Testing that the test user profile is in the database
def test_user_profile_exists(self):
        self.assertIsNotNone(self.user, "User exists i.e. is not null")
        profile = self.user.userprofile
        self.assertIsNotNone(profile, "Profile exists i.e. is not null")


# Testing that the test user profile is saved correctly
def test_user_profile_attributes(self):
        self.assertEqual(self.user.username, "testperson", "Username saved correctly")
        self.assertEqual(self.user.email, "testperson@test.com", "User email saved correctly")


# HOME PAGE TESTS ###################################################
# Testing that the home page has buttons for logging in and out
def test_login_logout_buttons(self):
        response = self.client.get("/")
        self.assertContains(response, "Login", msg_prefix="Home page has login button")
        self.assertContains(response, "Logout", msg_prefix="Home page has logout button")


# ABOUT PAGE TESTS ###################################################
def test_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'KirktonApp/about.html')


# LOGIN PAGE TESTS ###################################################
# Testing login page
def test_login_page(self):
    self.client.login(username="testperson", password="password1")
    user = auth.get_user(self.client)
    self.assertTrue(user.is_authenticated(), "User login successful")

# Testing login page redirect
def test_redirect_after_login(self):
        response = self.client.post(reverse('KirktonApp:login'), {"username": "testperson", "password": "password1"})
        self.assertRedirects(response, reverse('KirktonApp:home'))