"""Create endpoints to access sensor data from """
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Sensor
from .serializers import SensorSerializer
from django.core.exceptions import ObjectDoesNotExist



@api_view(['GET', 'POST'])
def sensor_list(request):
    """
    Function to take GET & POST request
    of all the sensor data, serialize 
    and return json
    """
    if request.method == 'GET':
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return JsonResponse({'sensors': serializer.data})

    if request.method == 'POST':
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def sensor_detail(request, id):
    """Function to GET, POST, DELETE sensor data"""

    try:
        sensor = Sensor.objects.get(pk=id)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SensorSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pass
