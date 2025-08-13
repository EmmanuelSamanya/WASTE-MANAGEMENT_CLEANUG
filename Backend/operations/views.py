from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, views
from rest_framework.response import Response
from django.utils import timezone
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Zone, Route, Truck, TruckLocation, Assignment, KPI
from .serializers import (
    ZoneSerializer, RouteSerializer, TruckSerializer, TruckLocationSerializer,
    AssignmentSerializer, KPISerializer
)

class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    permission_classes = [permissions.IsAuthenticated]

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated]

class TruckViewSet(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    permission_classes = [permissions.IsAuthenticated]

class TruckLocationIngestView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = TruckLocationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        # broadcast to WebSocket group
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "truck_positions",
            {"type":"truck_position","data":{
                "truck": obj.truck.id, "lat": obj.lat, "lng": obj.lng, "timestamp": obj.timestamp.isoformat()
            }}
        )
        return Response({"ok": True})

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class KPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        # simple demo KPIs (replace with real queries)
        totals = {k.label: k.value for k in KPI.objects.all()}
        totals.setdefault('pickups_today', 0)
        totals.setdefault('incidents_today', 0)
        totals['server_time'] = timezone.now().isoformat()
        return Response(totals)

