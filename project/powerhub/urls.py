from django.urls import path
from .views.orders import track_shipment
from .views.auth import retrieve_user_info

urlpatterns = [
    path("track-shipment/<str:tracking_id>", track_shipment, name="track"),
    path("user-info", retrieve_user_info, name="info")
    
]