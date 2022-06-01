"""Create endpoints to access sensor data from """
from django.shortcuts import render
from django.http import JsonResponse
from .models import Sensor
from .serializers import SensorSerializer


def sensor_list(request):
    """Function to get all the sensor data, serialize and return json """
    sensors = Sensor.objects.all()
    serializer = SensorSerializer(sensors, many=True)
    return JsonResponse({'sensors': serializer.data}, safe=False)
