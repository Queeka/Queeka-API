from django.urls import path
from .views.orders import track_shipment

urlpatterns = [
    path("track-shipment/<str:tracking_id>", track_shipment, name="track")
    
]