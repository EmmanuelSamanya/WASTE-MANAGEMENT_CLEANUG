from django.urls import re_path
from .consumers import AdminAlertsConsumer, TruckPositionsConsumer

websocket_urlpatterns = [
    re_path(r'ws/admin/alerts/$', AdminAlertsConsumer.as_asgi()),
    re_path(r'ws/trucks/positions/$', TruckPositionsConsumer.as_asgi()),
]
