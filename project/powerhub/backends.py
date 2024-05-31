from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, contact=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(contact=contact)
            print("User found:", user)  # Debugging output
        except User.DoesNotExist:
            print("User not found")  # Debugging output
            return None

        if user.check_password(password):
            print("Password correct")  # Debugging output
            return user
        print("Password incorrect")  # Debugging output
        return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None