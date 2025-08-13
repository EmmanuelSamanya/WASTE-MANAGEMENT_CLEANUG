from django.urls import path
from .views import SendAdminAlert

urlpatterns = [
    path('alert/', SendAdminAlert.as_view(), name='send_alert'),
]
