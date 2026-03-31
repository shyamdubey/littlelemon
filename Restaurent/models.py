from django.db import models

# Create your models here.


class Booking(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, default=None)
    no_of_guests = models.IntegerField(default=0)
    booking_date = models.DateField(auto_now=False, default=None)



class Menu(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, default=None)
    price = models.FloatField(0)
    inventory = models.IntegerField(0)