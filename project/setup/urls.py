from powerhub.views.auth import (
    SignUpUserViewSet, 
    RegisterBusinessView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

router.register("signup/client", SignUpUserViewSet, basename='sign-up-client')
router.register("register/business", RegisterBusinessView, basename='queeka-business')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('queeka/', include(router.urls)),
    
    # Auth
    path('signin/client', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
