from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class SendAdminAlert(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        data = request.data or {"title":"Alert","message":"Hello Admin"}
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("admin_alerts", {"type":"admin_alert","data": data})
        return Response({"sent": True, "data": data})

