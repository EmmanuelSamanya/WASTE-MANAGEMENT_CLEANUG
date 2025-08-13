from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Zone(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self): return self.name

class Route(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='routes')
    name = models.CharField(max_length=120)
    def __str__(self): return f"{self.zone} - {self.name}"

class Truck(models.Model):
    name = models.CharField(max_length=120)
    company = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='company_trucks')  # company user
    plate = models.CharField(max_length=50, blank=True)
    def __str__(self): return self.name

class TruckLocation(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, related_name='locations')
    lat = models.FloatField()
    lng = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Assignment(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='assignments')
    truck = models.ForeignKey(Truck, on_delete=models.SET_NULL, null=True, blank=True)
    scheduled_for = models.DateTimeField()
    status = models.CharField(max_length=20, default='SCHEDULED')  # SCHEDULED/ACTIVE/DONE

class KPI(models.Model):
    label = models.CharField(max_length=64, unique=True)
    value = models.IntegerField(default=0)
