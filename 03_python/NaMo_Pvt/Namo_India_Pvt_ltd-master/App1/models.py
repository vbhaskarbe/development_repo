from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor


# Create your models here.
class Newuser(models.Model):
    Username = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    pwd = models.CharField(max_length=150)
    PhoneNumber = models.IntegerField()
    
    class Meta:
        db_table = "App1_newuser"


class Registration(models.Model):
    Name = models.CharField(max_length=120)
    Email = models.CharField(max_length=120)
    PhoneNumber = models.IntegerField()
    Gender = models.CharField(max_length=120)
    Prerequisite = models.CharField(max_length=120)
    Education = models.CharField(max_length=120)
    Description = models.CharField(max_length=250)