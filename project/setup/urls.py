from powerhub.views.auth import (
    SignUpUserViewSet, 
    RegisterBusinessView,
    verify_confirmation_code,
    # SignInUserView
)

# Shipment & Package
from powerhub.views.orders import (
    ShipmentView,
    PackageView,
    DeliveryServiceView, 
    GetAndUpdateShipmentStatus
)

# Notification
from powerhub.views.notifications import (
    NotificationView
    )

# Dashboard
from dashboard.views.counts import (
    OngoingShipments
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

# Authenticate
router.register("signup/client", SignUpUserViewSet, basename='sign_up_client')
router.register("register/business", RegisterBusinessView, basename='queeka-business')

# Shipment & Package
router.register("create-package", PackageView, basename='shipment-package')
router.register("create-shipment", ShipmentView, basename='shipment')
router.register("delivery-service", DeliveryServiceView, basename='services')
router.register("shipment", GetAndUpdateShipmentStatus, basename='update-shipment')

# Dashboard
router.register('ongoing-shipments', OngoingShipments, basename='ongoing-shipments')

# Notification
router.register("notifications", NotificationView, basename="notification")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('queeka/', include(router.urls)),
    path('queekas/', include('finance.urls')),
    path('api/', include('powerhub.urls')),
    path('dashboard/', include('dashboard.urls')),
    
    # Auth
    path('signin/client', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("verify/otp/<str:contact>", verify_confirmation_code, name="verify")
]