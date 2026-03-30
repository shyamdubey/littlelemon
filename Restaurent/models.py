from django.db import models

# Create your models here.


class Booking(models.Model):
    id:models.BigAutoField(primary_key=True)
    name:models.CharField(max_length=255)
    no_of_guests:models.IntegerField()
    booking_date:models.DateField(auto_now=False)



class Menu(models.Model):
    id:models.BigAutoField(primary_key=True)
    title:models.CharField(max_length=255)
    price:models.FloatField()
    inventory:models.IntegerField()