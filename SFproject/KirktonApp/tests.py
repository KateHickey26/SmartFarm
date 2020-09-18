from django.urls import reverse

from .models import UserProfile
from django.test import TestCase, Client, override_settings
from django.contrib import auth
from django.contrib.auth.models import User
import django

django.setup()
# from populate import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import Client


@override_settings(SECURE_SSL_REDIRECT=False)
class KirktonApp(TestCase):

    # creating a test user profile
    def setUp(self):
        self.user = User.objects.create(username="test")
        self.user.email = "test@test.com"
        self.user.set_password("password")
        self.user_is_active = True
        self.user.save()
        self.profile = UserProfile(user=self.user)
        self.profile.save()
        self.client = Client()

    # def test_home(self):
    #     response = self.c.post('/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.context['title'], 'empty')

    # Testing that the test user profile is in the database
    def test_user_profile_exists(self):
        self.assertIsNotNone(self.user, "User exists i.e. is not null")
        profile = self.user.userprofile
        self.assertIsNotNone(profile, "Profile exists i.e. is not null")

    # Testing that the test user profile is saved correctly
    def test_user_profile_attributes(self):
        self.assertEqual(self.user.username, "test", "Username saved correctly")
        self.assertEqual(self.user.email, "test@test.com", "User email saved correctly")

    # HOME PAGE TESTS ###################################################
    # Testing that the home page has buttons for logging in and out
    def test_home_page_elements(self):
        response = self.client.get("/")
        self.assertContains(response, "Login", msg_prefix="Home page has login button")
        # self.assertContains(response, "Logout", msg_prefix="Home page has logout button")
        self.assertContains(response, "Add Sensor", msg_prefix="Home page has add sensor button")
        self.assertContains(response, "Map", msg_prefix="Home page contains mapbox map")
        self.assertContains(response, "Sensors", msg_prefix="Home page contains sensors sidebar")

    # ABOUT PAGE TESTS ###################################################
    def test_about_page(self):
        response = self.client.get(reverse('KirktonApp:about'))
        self.assertEqual(response.status_code, 200)

# class LoginViewTests(TestCase):
# # LOGIN PAGE TESTS ###################################################
# # Testing login page
#     def test_login_page(self):
#         self.client.login(username="test", password="password")
#         user = auth.get_user(self.client)
#         self.assertTrue(user.is_authenticated(), "User login successful")
#
# # Testing login page redirect
#     def test_redirect_after_login(self):
#         response = self.client.post(reverse('KirktonApp:login'), {"username": "test", "password": "password"})
#         self.assertRedirects(response, reverse('KirktonApp:home'))
#         self.assertEqual(response.status_code, 200)
