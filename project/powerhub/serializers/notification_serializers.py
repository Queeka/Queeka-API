from rest_framework import serializers
from . import NotificationSystem

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSystem
        fields = "__all__"
        
    def to_representation(self, instance):
        representation = super(NotificationSerializer, self).to_representation(instance)
        representation["user"] = f"{instance.user.first_name} {instance.user.last_name}"
        return representation