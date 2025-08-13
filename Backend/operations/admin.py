from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Zone, Route, Truck, TruckLocation, Assignment, KPI
admin.site.register(Zone)
admin.site.register(Route)
admin.site.register(Truck)
admin.site.register(TruckLocation)
admin.site.register(Assignment)
admin.site.register(KPI)

