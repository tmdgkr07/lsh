from django.db import models

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=50, default="")
    time = models.CharField(max_length=30, default="")
    menu = models.CharField(max_length=200, default="")

class Weather(models.Model):
    place = models.FloatField(max_length=50, default="")
    status = models.FloatField(max_length=50, default="")
    temperature = models.FloatField(max_length=50, default="") 
    
       
# Create your models here.
