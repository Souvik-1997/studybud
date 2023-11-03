from django.db import models
# from django.contrib.auth.models import User as User
from base.models.User import User


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name