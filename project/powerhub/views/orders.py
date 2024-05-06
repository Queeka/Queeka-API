from . import (
    Shipment,
    Package, 
    ShipmentSerializer, 
    PackageSerializer
    )
from rest_framework.views import APIView
from rest_framework import viewsets

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