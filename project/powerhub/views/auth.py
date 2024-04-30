from rest_framework import viewsets, permissions, response, status
# from rest_framework_simplejwt.views import TokenObtainPairView
from . import (
    # Models
    User, 
    QueekaBusiness, 
    ConfirmationCode,
    # Serializers
    SignUpUserSerializer,
    QueekaBusinessSerializer
    )

from rest_framework.decorators import api_view


class SignUpUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpUserSerializer


class RegisterBusinessView(viewsets.ModelViewSet):
    """
    Register Business Accounts for Clients
    """
    queryset= QueekaBusiness.objects.select_related("owner")
    serializer_class = QueekaBusinessSerializer
    
    
# Function to verify confirmation code
@api_view(["POST"])
def verify_confirmation_code(request, **kwargs):
    submitted_code = request.query_params.get("code")
    user = request.user
    # print(type(submitted_code))
    try:
        confirmation = ConfirmationCode.objects.get(user=user)
        print("Generated code:", type(confirmation.generated_confirmation_code))  # Add this line for debugging
        if confirmation.generated_confirmation_code == int(submitted_code):
            confirmation.verified = True
            confirmation.save()
            return response.Response("OTP Verified Successfully", status=status.HTTP_202_ACCEPTED)
            logger.info("OTP Verified")
        else:
            return response.Response("Incorrect Confirmation Code", status=status.HTTP_401_UNAUTHORIZED)

    except ConfirmationCode.DoesNotExist:
        return response.Response("Confirmation Code Does Not Exist", status=status.HTTP_404_NOT_FOUND)
        logger.error("Confirmation Code Does Not Exist")
        return