"""Create endpoints to access sensor data from """
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Sensor
from .serializers import SensorSerializer


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
