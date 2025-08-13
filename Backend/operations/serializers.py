from rest_framework import serializers
from .models import Zone, Route, Truck, TruckLocation, Assignment, KPI

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ['id','name']

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id','zone','name']

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ['id','name','company','plate']

class TruckLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckLocation
        fields = ['id','truck','lat','lng','timestamp']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id','route','truck','scheduled_for','status']

class KPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = ['id','label','value']
