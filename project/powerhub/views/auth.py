from rest_framework import viewsets
from . import (
    # Models
    User, 
    QueekaBusiness, 
    
    # Serializers
    SignUpUserSerializer,
    QueekaBusinessSerializer
    )


class SignUpUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpUserSerializer


class RegisterBusinessView(viewsets.ModelViewSet):
    queryset= QueekaBusiness.objects.select_related("owner")
    serializer_class = QueekaBusinessSerializer