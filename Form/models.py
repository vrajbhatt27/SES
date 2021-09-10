from django.db import models
from django.db.models.base import Model

# Create your models here.
class User(models.Model):
    uid = models.IntegerField(null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name
        
class Event(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    eid = models.IntegerField(null=True)
    event_name = models.CharField(max_length=50, null=True)
        
    def __str__(self):
        return self.event_name
