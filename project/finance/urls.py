from django.urls import path
from .views.wallet_view import CreateBusinessWallet

urlpatterns = [
    path('create-wallet', CreateBusinessWallet.as_view(), name='flutter')
]
