import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = "brewpi.service.devices.core",
    description='Core device support for the BrewPi Service',
    version = "0.1",
    packages = find_packages(),
    include_package_data=True,
    long_description=README,
    namespace_packages = ['devices.core'],
    entry_points = {
        'controller.device.model': [
            'ds2413 = devices.core.actuator.models:DS2413Actuator',
            'motorized_valve = devices.core.actuator.models:MotorizedValve',
            'temp_sensor = devices.core.sensor:TemperatureSensor',
        ],
        'controller.device.admin': [
            'ds2413 = devices.core.actuator.admin:DS2413ActuatorAdmin',
            'motorized_valve = devices.core.actuator.admin:MotorizedValveAdmin',
            'temp_sensor = devices.core.sensor.admin:TemperatureSensorAdmin',
        ],
        'controller.device.inline_admin': [
            'ds2413 = devices.core.actuator.admin:DS2413ActuatorInline',
            'motorized_valve = devices.core.actuator.admin:MotorizedValveInline',
            'temp_sensor = devices.core.sensor.admin:TemperatureSensorInline',
        ]
    }
)
