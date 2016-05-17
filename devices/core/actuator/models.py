from django.db import models
from django.utils.translation import ugettext as _

from device.models import PWMActuator, Actuator

class Valve(Actuator):
    """
    An abstract Valve
    """
    pass

class ManualValve(Valve):
    """
    A manual valve, toggled by the user
    """
    pass

class MotorizedValve(Valve):
    """
    A 1-wire, motorized Valve
    """
    pass


class DS2413Actuator(PWMActuator):
    """
    1-wire, 2 canals PWM Actuator
    """
    class Meta:
        verbose_name = 'DS2413'
        verbose_name_plural = 'DS2413'

    PIO_CHOICES = (
        (0, 'A'),
        (1, 'B')
    )

    pio = models.PositiveIntegerField(choices=PIO_CHOICES, default=0, help_text=_("PIO number of the addressable switch"))
    inverted = models.BooleanField(default=False, help_text=_("If the switch is inverted"))

    @property
    def get_status(self):
        return 0
