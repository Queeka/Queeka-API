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
from rest_framework import viewsets, response, status
from rest_framework.decorators import api_view
from django.http import JsonResponse
import logging


logger = logging.getLogger(__name__)


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
    queryset = ShipmentStatus.objects.all()
    serializer_class = ShipmentStatusSerializer


class DeliveryServiceView(viewsets.ModelViewSet):
    queryset = DeliveryService.objects.all()
    serializer_class = DeliveryServiceSerializer



@api_view(["GET"])
def track_shipment(request, tracking_id=None):
    """Allow Clients/Customers to Track their Order"""
    if not tracking_id:
        return JsonResponse({"status": "error", "message": "Input tracking ID"})

    # Get the Shipment related to the tracking_id
    shipment = Shipment.objects.filter(tracking_id=tracking_id).first()

    if not shipment:
        return JsonResponse({"status": "error", "message": "Shipment not found"})


    # Serialize the shipment statuses
    shipment_status_data = ShipmentSerializer(shipment).data

    return JsonResponse({"status": "success", "data": shipment_status_data})


class GetAndUpdateShipmentStatus(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        try:
            shipmentstatus = ShipmentStatus.objects.filter(id=pk).first()
            data=ShipmentStatusSerializer(shipmentstatus).data
            return response.Response({"status": "success", "data": data}, status=status.HTTP_200_OK)
        
        except Exception as e:
            logger.error(str(e))
            return response.Response({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk=None):
        new_status = request.query_params.get("new_status")
        
        if not pk:
            return JsonResponse({"status": "Error", "message": "Input Shipment ID"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Get related Shipment
        shipment_instance = Shipment.objects.get(id=pk)
        
        if not shipment_instance:
            return JsonResponse({"status": "error", "message": "Shipment not found"}, status=status.HTTP_404_NOT_FOUND)
        
        shipment_status = ShipmentStatus.objects.filter(shipment=shipment_instance).first()
        shipment_status.status = new_status
        shipment_status.save()
        return response.Response({"status": "success", "message": "Status Updated Successfully", "data": ShipmentStatusSerializer(shipment_status).data}, status=status.HTTP_200_OK)