from django.db import models
from django.core.exceptions import ValidationError


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()
    booking_slot = models.SmallIntegerField(default=10)

    def __str__(self):
        return f'{self.name} : {str(self.booking_date)} {str(self.booking_slot)}:00H'
