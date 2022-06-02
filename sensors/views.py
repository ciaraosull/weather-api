"""Create endpoints to access sensor data from """
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Sensor
from .serializers import SensorSerializer


@api_view(['GET', 'POST'])
def sensor_list(request, format=None):  # for url patterns to be formatted
    """
    Function to take GET & POST request
    of all the sensor data, serialize
    and return json
    """
    if request.method == 'GET':
        sensors = Sensor.objects.all()  # to reach inside model an return all
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)  # not json specific for panel view

    if request.method == 'POST':
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # if valid save the new sensor data
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def sensor_detail(request, id, format=None):  # get a sensor by id
    """Function to GET, PUT, DELETE sensor data"""

    try:
        sensor = Sensor.objects.get(pk=id)  # if id valid request
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)  # return the sensor data with GET

    elif request.method == 'PUT':
        serializer = SensorSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
