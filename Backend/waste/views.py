from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import PickupRequest, WasteReport
from .serializers import PickupRequestSerializer, WasteReportSerializer

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return getattr(obj, 'requester', None) == request.user or request.user.is_staff

class PickupRequestViewSet(viewsets.ModelViewSet):
    queryset = PickupRequest.objects.all().order_by('-created_at')
    serializer_class = PickupRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(requester=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return self.queryset
        return self.queryset.filter(requester=user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def mark_completed(self, request, pk=None):
        obj = self.get_object()
        obj.status = 'COMPLETED'
        obj.save()
        return Response({'status':'ok'})

class WasteReportViewSet(viewsets.ModelViewSet):
    queryset = WasteReport.objects.all().order_by('-created_at')
    serializer_class = WasteReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)

