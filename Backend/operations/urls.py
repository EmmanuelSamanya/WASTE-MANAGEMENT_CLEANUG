from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ZoneViewSet, RouteViewSet, TruckViewSet, AssignmentViewSet,
    TruckLocationIngestView, KPIView
)

router = DefaultRouter()
router.register('zones', ZoneViewSet)
router.register('routes', RouteViewSet)
router.register('trucks', TruckViewSet)
router.register('assignments', AssignmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('telemetry/', TruckLocationIngestView.as_view(), name='telemetry'),
    path('kpis/', KPIView.as_view(), name='kpis'),
]
