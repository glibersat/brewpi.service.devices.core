# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-28 16:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HumiditySensor',
            fields=[
                ('sensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='device.Sensor')),
                ('value', models.FloatField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('device.sensor',),
        ),
        migrations.CreateModel(
            name='TemperatureSensor',
            fields=[
                ('sensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='device.Sensor')),
                ('value', models.FloatField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('device.sensor',),
        ),
    ]
