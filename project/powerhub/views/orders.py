from . import (
    Order,
    Package, 
    OrderSerializer, 
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

class OrderView(viewsets.ModelViewSet):
    """
    Viewset for viewing and editing Order Order
    """
    queryset = Order.objects.select_related("vendor").prefetch_related("package")
    serializer_class = OrderSerializer