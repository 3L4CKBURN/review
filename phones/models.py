from django.db import models

# Create your models here.


class Product(models.Model):
    image = models.CharField(max_length=2000)
    company = models.CharField(max_length=255)
    model =models.CharField(max_length=20)
    price = models.FloatField()

class Offer(models.Model) :
    code=models.CharField(max_length=10)  
    description=models.CharField(max_length=200)
    discount=models.FloatField()

