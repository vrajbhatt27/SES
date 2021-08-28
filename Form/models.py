from django.db import models
from django.db.models.base import Model

# Create your models here.
class User(models.Model):
    uid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name