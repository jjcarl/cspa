from __future__ import unicode_literals

from django.db import models


class Treatment(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=10)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
