from django.db import models
from base.models.Topic import Topic
from django.contrib.auth.models import User


# Create your models here.

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200,blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-update', '-create']

    def __str__(self):
        return self.name