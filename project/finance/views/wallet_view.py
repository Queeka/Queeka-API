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

class CreateVirtualAccount(APIView):
    def post(self, request):
        user = request.user
        # amount = request.data.get("amount")
        
        url = "https://api.flutterwave.com/v3/virtual-account-numbers"
        
        payload = {
            "email": user.email,
            "is_permanent": True,
            "tx_ref": self.generate_tx_ref(),
            "phonenumber": user.contact,
            "firstname": user.first_name,
            "lastname": user.last_name,
            "narration": "Queeka Wallet",
            "is_permanent": False,
            "amount": 500
        }
        
        SECRET_KEY = test_settings.TEST_SECRET_KEY
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {SECRET_KEY}'
        }
        
        res = requests.post(url, headers=headers, json=payload)
        
        if res.status_code == 200:
            return Response(res.json(), status=status.HTTP_200_OK)
        else:
            logger.error("Failed to create virtual account. Status code: %s, Response: %s", res.status_code, res.text)
            return Response({"error": "Failed to create virtual account"}, status=res.status_code)

    def generate_tx_ref(self):
        """ Generate a unique transaction reference using timestamp and UUID """
        timestamp = str(int(time.time()))
        uid = str(uuid.uuid4().hex)
        tx_ref = timestamp + "_" + uid
        return tx_ref