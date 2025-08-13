from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PickupRequestViewSet, WasteReportViewSet

router = DefaultRouter()
router.register('pickups', PickupRequestViewSet, basename='pickups')
router.register('reports', WasteReportViewSet, basename='reports')

urlpatterns = [ path('', include(router.urls)), ]
