from rest_framework import viewsets, response
from . import (
    # Models
    NotificationSystem, 
    
    # Serializers
    NotificationSerializer
    )


class NotificationView(viewsets.ModelViewSet):
    queryset = NotificationSystem.objects.select_related("user")
    serializer_class = NotificationSerializer