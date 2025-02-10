from django.db import models

# Create your models here.
class All_Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=40)
    city = models.CharField(max_length=60)