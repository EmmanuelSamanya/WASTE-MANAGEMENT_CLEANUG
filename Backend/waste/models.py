from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class PickupRequest(models.Model):
    STATUS = (('PENDING','Pending'),('ASSIGNED','Assigned'),('COMPLETED','Completed'))
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pickup_requests')
    address = models.CharField(max_length=255)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return f"{self.requester} - {self.status}"

class WasteReport(models.Model):
    REPORT_TYPE = (('ILLEGAL_DUMP','Illegal Dumping'),('MISSED_PICKUP','Missed Pickup'))
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    report_type = models.CharField(max_length=30, choices=REPORT_TYPE)
    description = models.TextField(blank=True)
    lat = models.FloatField()
    lng = models.FloatField()
    photo_url = models.URLField(blank=True)
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return f"{self.report_type} @ {self.lat},{self.lng}"


