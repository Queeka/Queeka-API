from rest_framework import serializers
from django.utils.timesince import timesince
from . import NotificationSystem

class NotificationSerializer(serializers.ModelSerializer):
    timesince_created = serializers.SerializerMethodField()
    class Meta:
        model = NotificationSystem
        fields = "__all__"
        
    def to_representation(self, instance):
        representation = super(NotificationSerializer, self).to_representation(instance)
        representation["user"] = f"{instance.user.first_name} {instance.user.last_name}"
        return representation
    
    def get_timesince_created(self, obj):
        return timesince(obj.created_at)