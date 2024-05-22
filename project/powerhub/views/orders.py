from . import (
    # Models
    Shipment,
    Package,
    ShipmentStatus,
    DeliveryService,
    
    # Serializers
    ShipmentSerializer,
    ShipmentStatusSerializer,
    PackageSerializer,
    DeliveryServiceSerializer
    )
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse


class PackageView(viewsets.ModelViewSet):
    """
    Viewset for viewing and editing Order Packages
    """
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class ShipmentView(viewsets.ModelViewSet):
    """
    Viewset for viewing and editing Order Order
    """
    queryset = Shipment.objects.select_related("vendor").prefetch_related("package")
    serializer_class = ShipmentSerializer
    
    
class ShipmentStatusView(viewsets.ModelViewSet):
    queryset = ShipmentStatus.objects.select_related("shipment")
    serializer_class = ShipmentStatusSerializer


class DeliveryServiceView(viewsets.ModelViewSet):
    queryset = DeliveryService.objects.all()
    serializer_class = DeliveryServiceSerializer



@api_view(["GET"])
def track_shipment(request, tracking_id=None):
    """Allow Clients/Customers Track their Order"""
    if not tracking_id:
        return JsonResponse({"status": "error", "message": "Input tracking ID"})

    # Get Related Shipment
    shipment = Shipment.objects.filter(tracking_id=tracking_id).first()

    if not shipment:
        return JsonResponse({"status": "error", "message": "Shipment not found"})

    shipment_data = ShipmentSerializer(shipment).data

    return JsonResponse({"status": "success", "data": shipment_data})

