from __future__ import unicode_literals

from django.db import models
from scheduling.models import Appointment


class Treatment(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=10)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    description = models.TextField()
    appointment = models.ManyToManyField(Appointment, related_name='products')

    def __str__(self):
        return self.name
