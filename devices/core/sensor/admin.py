from django.contrib import admin

from device.admin import DeviceAdmin, SensorInline

from brewpi_webservice.admin import admin_site
from .models import Sensor, TemperatureSensor

@admin.register(TemperatureSensor, site=admin_site)
class TemperatureSensorAdmin(DeviceAdmin):
    base_model = TemperatureSensor

class TemperatureSensorInline(SensorInline):
    model = TemperatureSensor
