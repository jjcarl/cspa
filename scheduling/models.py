from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from core.models import Treatment, Product


class StartTime(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    scheduled = models.BooleanField(default=False)


class Appointment(models.Model):
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now_add=True)
    start_time = models.OneToOneField(StartTime)
    treatment = models.ForeignKey(Treatment)
    product = models.ForeignKey(Product, null=True)
