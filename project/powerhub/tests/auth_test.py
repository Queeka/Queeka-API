from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from powerhub.models.auth_models import User

# Create your tests here.
class AuthTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/signin/client'
    
    def test_user_login(self):
        login_successful  = self.client.login(contact="+2349184757560", password="Johnddoe@19")
        if login_successful:
            print("Login successful")
        else:
            print("Login failed")
        self.assertTrue(login_successful)