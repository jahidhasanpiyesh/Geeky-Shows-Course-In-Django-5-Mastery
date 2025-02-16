from django.db import models

# Create your models here.
class home(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)


class homeapp(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=30)