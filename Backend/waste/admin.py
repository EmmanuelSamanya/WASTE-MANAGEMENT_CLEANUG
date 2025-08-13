from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PickupRequest, WasteReport
admin.site.register(PickupRequest)
admin.site.register(WasteReport)
