from django.db import models

# Create your models here.
class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    des = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Phone_Number(models.Model):
    
    text = models.CharField(max_length=50)
    number = models.CharField(max_length=24)

class NewsLater(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=300)
    
