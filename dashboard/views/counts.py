from . import (
    # Models
    Shipment, 
    Package, 
    User,
    QueekaBusiness,
    
    # Serializers
    ShipmentSerializer)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.db.models import Avg, Sum, Count, Min, Max
from django_filters import rest_framework as filters
from django.shortcuts import get_object_or_404

class DashboardCounts(APIView):
    def get(self, request, business_sn=None):
        if business_sn is None:
            return Response({"status": "error", "message": "To Get Dashboard Counts You need to add the business id to the url"}, status=status.HTTP_404_NOT_FOUND)
    
        try:
            total_shipments = Shipment.objects.filter(vendor__business_sn=business_sn).aggregate(Count('id'))
            ongoing_shipments = Shipment.objects.filter(status__status="EN", vendor__business_sn=business_sn).distinct().aggregate(Count('id'))
            cancelled_shipments = Shipment.objects.filter(status__status="CANC", vendor__business_sn=business_sn).distinct().aggregate(Count('id'))
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"status": "success", "data": {"total_shipments": total_shipments["id__count"], 
                                                        "ongoing_shipments": ongoing_shipments["id__count"], 
                                                        "cancelled_shipments": cancelled_shipments["id__count"]}}, status=status.HTTP_200_OK)




class ShipmentFilter(filters.FilterSet):
    status = filters.CharFilter(field_name="status__status")

    class Meta:
        model = Shipment
        fields = ['status']
        

class ShipmentFilterList(generics.ListAPIView):
    serializer_class = ShipmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShipmentFilter
    
    def get_queryset(self):
        user = self.request.user
        owner = get_object_or_404(User, id=user.id)
        business = get_object_or_404(QueekaBusiness, owner=owner)
        return Shipment.objects.filter(vendor=business)
        
