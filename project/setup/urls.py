from powerhub.views.auth import (
    SignUpUserViewSet, 
    RegisterBusinessView,
verify_confirmation_code
)

from powerhub.views.orders import (
    ShipmentView,
    PackageView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

router.register("signup/client", SignUpUserViewSet, basename='sign_up_client')
router.register("register/business", RegisterBusinessView, basename='queeka-business')
router.register("create-package", PackageView, basename='shipment-package')
router.register("create-shipment", ShipmentView, basename='shipment')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('queeka/', include(router.urls)),
    path('queekas/', include('finance.urls')),
    
    
    # Auth
    path('signin/client', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("verify/otp", verify_confirmation_code, name="verify")
]