"""Register models in admin"""
from django.contrib import admin
from .models import Sensor


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    """
    Class to register the sensors to the admin panel
    and display & filter specific information
    """
    list_display = ('sensor_id', 'country', 'city')
    search_fields = ('sensor_id', 'date')
    list_filter = ('sensor_id', 'date')
