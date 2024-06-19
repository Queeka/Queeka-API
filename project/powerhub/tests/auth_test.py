from django.test import TestCase
from django.urls import reverse, path, include
from rest_framework.test import APITestCase, RequestsClient
from rest_framework import status, routers
from powerhub.models.auth_models import User

# Create your tests here.
class AuthTest(APITestCase):
    def setUp(self):
        User.objects.create(first_name="adewale", last_name="subaru", 
                            email="adesuba@gmail.com",
                            contact="+2349028277384", password="@10aLPHA")

    def test_client_signup(self):
        """
        Ensure we can register a client
        """
        url = '/queeka/signup/client/'
        data = {"first_name":"Adewale", "last_name":"subaru", 
                "email":"Adesuba11@gmail.com", "contact":"+2349023277388", 
                "password":"@10aLPHA"}
        
        response = self.client.post(url, data, format='json')
        # print(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], 'Adewale')
        
    def test_client_login(self):
        """
        Test Client Login Process, and assert it returns
        status code 200
        """
        url = reverse('token_obtain_pair')
        data = {"contact": "+2349028277384", "password": "@10aLPHA"}
        response = self.client.post(url, data, format='json')
        # print(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)