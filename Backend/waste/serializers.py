from rest_framework import serializers
from .models import PickupRequest, WasteReport

class PickupRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickupRequest
        fields = ['id','requester','address','lat','lng','notes','status','created_at']
        read_only_fields = ['requester','status','created_at']

class WasteReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteReport
        fields = ['id','reporter','report_type','description','lat','lng','photo_url','resolved','created_at']
        read_only_fields = ['reporter','resolved','created_at']
