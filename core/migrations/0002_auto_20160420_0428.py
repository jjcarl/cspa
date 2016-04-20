# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0002_remove_appointment_product'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='appointment',
            field=models.ManyToManyField(related_name='products', to='scheduling.Appointment'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
