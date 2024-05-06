from django.urls import path
from .views.wallet_view import CreateVirtualAccount

urlpatterns = [
    path('create-virtual-account', CreateVirtualAccount.as_view(), name='flutter')
]
