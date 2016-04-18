from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from core.models import Treatment, Product


class Appointment(models.Model):
    user = models.ForeignKey(User)
    start_time = models.DateTimeField()
    treatment = models.ForeignKey(Treatment)
    product = models.ForeignKey(Product, null=True)
