from django.urls import path

urlpatterns = [
    path("signin/", SignInUserView.as_view(), name="sign-in"),
    
]