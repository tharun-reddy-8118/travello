from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    description = models.TextField()
    offer = models.BooleanField(default=False)
    link = models.CharField(max_length=100)

class Place(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    description = models.TextField()
    link = models.CharField(max_length=100)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.TextField()
    message = models.TextField()
    subject = models.CharField(max_length=100)

class Trips(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.TextField()
    date = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='pics')