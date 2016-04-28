from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class StartTime(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    scheduled = models.BooleanField(default=False)

    def __str__(self):
        return self.start_time.strftime('%A, %d %b %Y %H:%M')


class Appointment(models.Model):
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now_add=True)
    start_time = models.OneToOneField(StartTime)
    treatment = models.ForeignKey('core.Treatment')

    def __str__(self):
        return "{} with {}".format(self.start_time, self.user.username)
