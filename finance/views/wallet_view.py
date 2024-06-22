from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import random, string, uuid, time, requests, logging
from setup.settings import test_settings

from . import (
    # Models
    BusinessWallet, 
    
    # Serializer
    BusinessWalletSerializer,
)

logger = logging.getLogger(__name__)

class CreateBusinessWallet(APIView):
    def post(self, request):
        user = request.user
        collect = request.data
        secret_key = test_settings.TEST_SECRET_KEY
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {secret_key}" 
        }
        
        customer_code, customer_response = self.create_customer(user, collect, headers)
        
        if customer_code:
            # If the customer was created successfully, create a business account
            business_account_response = self.create_business_account(user, collect, headers, customer_code)
            return business_account_response
        else:
            # If creating the customer failed, return the customer response
            return customer_response # Return the response from create_customer

    def create_customer(self, user, collect, headers):
        url = "https://api.paystack.co/customer"
        
        data = { 
            "email": collect.get("email"),
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone": str(user.contact)
        }
        
        try:
            resp = requests.post(url, json=data, headers=headers)
            # Check if the request was successful
            if resp.status_code == 200:
                # Extract customer code from the response
                customer_code = resp.json()["data"]["customer_code"]
                return customer_code, Response({"message": "Customer created successfully", "data": resp.json()}, status=200)
            else:
                # Return None for customer code and the error response
                return None, Response({"error": f"Failed to create customer: {resp.text}"}, status=resp.status_code)
        except Exception as e:
            # Return None for customer code and the error response
            return None, Response({"error": str(e)}, status=500)
    
    def create_business_account(self, user, collect, headers, customer_code):
        url = "https://api.paystack.co/dedicated_account"
    
        data = {
            "customer": customer_code,
            "preferred_bank": "wema-bank"
        }

        try:
            resp = requests.post(url, json=data, headers=headers)
            # Check if the request was successful
            if resp.status_code == 200:
                # Return a success response
                return Response({"message": "Business account created successfully", "data": resp.json()}, status=200)
            else:
                # Return an error response with the status code
                return Response({"error": f"Failed to create business account: {resp.text}"}, status=resp.status_code)
        except Exception as e:
            # Return an error response if an exception occurs
            return Response({"error": str(e)}, status=500)
        