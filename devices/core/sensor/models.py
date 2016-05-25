from django.db import models
from django.utils.translation import ugettext as _

from device.models import Sensor, ElectronicDeviceMixin

class TemperatureSensor(Sensor, ElectronicDeviceMixin):
    value = models.FloatField(null=True)

