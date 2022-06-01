"""Process going from Python to JSON"""
from rest_framework import serializers
from .models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    """Class for returning sensor model data to api"""
    class Meta:
        """Describing model"""
        model = Sensor
        fields = [
            'sensor_id',
            'country',
            'city',
            'average_temperature',
            'average_humidity',
            'average_wind_speed',
            'date'
            ]
