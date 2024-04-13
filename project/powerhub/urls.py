from django.urls import path
from .views.auth import SignInUserView

urlpatterns = [
    path("signin/", SignInUserView.as_view(), name="sign-in")
]