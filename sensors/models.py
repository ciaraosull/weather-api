"""Model for Sensors"""
from django.db import models


class Sensors(models.Model):
    """Model to describe the Sensors Class"""
    sensor_id = models.IntegerField(null=True, blank=True, unique=True)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    average_temperature = models.FloatField()
    average_humidity = models.FloatField()
    average_wind_speed = models.FloatField()
    date = models.DateField(auto_now=False)

    class Meta:
        """Helper class for ordering by sensor id"""
        ordering = ['sensor_id']

    def __str__(self):
        """
        Dunder (double underscore) str method to return
        a string representation of the object
        """
        return f'Sensor Id No: {self.sensor_id}'
