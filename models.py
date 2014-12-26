from django.db import models
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
import datetime
from django.utils import timezone

class Weather(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    created_at = models.DateField(default=timezone.now)
#    updated_at = models.AutoDateTimeField(default=timezone.now)

    stantion_date = models.DateTimeField('weather station date')

    bmp180temp = models.FloatField()
    bmp180pres = models.FloatField()
    v_bat = models.FloatField()
    v_ref = models.FloatField()
    v_sun = models.FloatField()
    humid = models.FloatField()

    comment = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)
