from django.db import models
from django.utils.translation import ugettext as _

from device.models import Sensor


class TemperatureSensor(Sensor):
    value = models.FloatField(null=True)
