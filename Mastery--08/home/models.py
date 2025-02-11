from django.db import models

# Create your models here.
class home(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=40)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # show name admin pnale
    

class home_app(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=40)
    city = models.CharField(max_length=100)
    roll = models.IntegerField()

    def __str__(self):
        return str(self.roll)  # show roll admin pnale convert to string