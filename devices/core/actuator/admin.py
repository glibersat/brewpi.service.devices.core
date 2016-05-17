from django.contrib import admin

from brewpi_webservice.admin import admin_site

from device.models import Actuator
from device.admin import DeviceAdmin, ActuatorInline

from .models import DS2413Actuator, ManualValve, MotorizedValve


@admin.register(DS2413Actuator, site=admin_site)
class DS2413ActuatorAdmin(DeviceAdmin):
    base_model = DS2413Actuator

class DS2413ActuatorInline(ActuatorInline):
    model = DS2413Actuator


@admin.register(ManualValve, site=admin_site)
class ManualValveAdmin(DeviceAdmin):
    base_model = ManualValve

class ManualValveInline(ActuatorInline):
    model = ManualValve

@admin.register(MotorizedValve, site=admin_site)
class MotorizedValveAdmin(DeviceAdmin):
    base_model = MotorizedValve

class MotorizedValveInline(ActuatorInline):
    model = MotorizedValve

