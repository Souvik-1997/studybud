from django.db import models
# from django.contrib.auth.models import User
from base.models.User import User
from base.models.Room import Room

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        app_label = "base"
        ordering = ['-created_at']

    def __str__(self):
        return self.body[0:50]