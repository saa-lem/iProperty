from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
# Create your models here.



class Property(models.Model):
    name = models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    image = ImageField(blank=True, manual_crop='')
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'+ ": $" + str(self.price)