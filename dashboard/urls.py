from .views.counts import DashboardCounts, ShipmentFilterList
from django.urls import path

urlpatterns = [
    path("counts/<str:business_sn>", DashboardCounts.as_view(), name="dashboard-count"),
    path("shipment-filter", ShipmentFilterList.as_view(), name="shipmentFilter")
]

