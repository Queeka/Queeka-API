from rest_framework import viewsets, response
from . import (
    # Models
    NotificationSystem, 
    
    # Serializers
    NotificationSerializer
    )


class NotificationView(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    lookup_field = "user"

    def get_queryset(self):
        user = self.kwargs.get(self.lookup_field)
        return NotificationSystem.objects.select_related("user").filter(user=user)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)