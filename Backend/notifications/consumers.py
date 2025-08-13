from channels.generic.websocket import AsyncJsonWebsocketConsumer

class AdminAlertsConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("admin_alerts", self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard("admin_alerts", self.channel_name)

    async def admin_alert(self, event):
        await self.send_json(event["data"])

class TruckPositionsConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("truck_positions", self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard("truck_positions", self.channel_name)

    async def truck_position(self, event):
        await self.send_json(event["data"])
