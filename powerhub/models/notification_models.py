from . import User, QueekaBusiness
from django.db import models
from django.utils.timesince import timesince

class NotificationSystem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=False)
    text = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_timesince_created(self, obj):
        return timesince(obj.created_at)