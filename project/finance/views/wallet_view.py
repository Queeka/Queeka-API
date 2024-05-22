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
        request.user
        