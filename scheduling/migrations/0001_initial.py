# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(to='core.Product', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StartTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField()),
                ('scheduled', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='start_time',
            field=models.OneToOneField(to='scheduling.StartTime'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='treatment',
            field=models.ForeignKey(to='core.Treatment'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
