from . import (
    # Models
    Shipment, 
    Package, 
    
    # Serializers
    ShipmentSerializer)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.db.models import Avg, Sum, Count, Min, Max



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


class OngoingShipments(viewsets.ModelViewSet):
    serializer_class = ShipmentSerializer

    def get_queryset(self):
        return Shipment.objects.filter(status__status="EN").distinct()
        #TODO Adjust this to only return needed data
        
    
    
