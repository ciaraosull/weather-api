import pytest
from django.urls import reverse
from rest_framework.response import Response
from sensors.models import Sensor
from sensors.serializers import SensorSerializer


@pytest.mark.django_db  # gives access to database
def test_sensor_list(client):
    """Function to get URL, call the request
    and validate our data using asserts.
    """
    url = reverse('sensor-list')
    response = client.get(url)

    sensor = Sensor.objects.all()
    expected_data = SensorSerializer(sensor, many=True).data

    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db  # gives access to database
def test_sensor_details(client):
    """Function for put"""
    url = reverse('sensor-list')
    response = client.get(url)

    sensor = Sensor.objects.get(pk=id)
    serializer = SensorSerializer(sensor)
    serializer.save()
    expected_data = Response(serializer.data)

    assert response.data == expected_data
