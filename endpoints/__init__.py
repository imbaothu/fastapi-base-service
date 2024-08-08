"""
usage 
all endpoints will have init_config method to initialize the config
init_config : maybe have no auto-complete code :v 
"""

from .mongo import MongoClient
from .ws import WsClient
from endpoints.ws import WsClient
from endpoints.mongo import MongoClient
from endpoints.sse import SSEClient
from users.model import User
from conversations.model import Conversation
from config import app_config as global_config


class EndpointManager:
    def __init__(self) -> None:
        self.mongo = MongoClient()
        self.ws_client = WsClient()
        self.sse_client = SSEClient()

    def init_config(self, config: dict):
        self.mongo.init_config(config["mongo"])
        self.ws_client.init_config(config["ws_client"])
        self.sse_client.init_config(config["sse_client"])

    async def connect(self):
        await self.mongo.connect(
            [
                User,
                Conversation,
            ]
        )
        await self.ws_client.connect()
        await self.sse_client.connect()

    async def disconnect(self):
        await self.mongo.disconnect()
        await self.ws_client.disconnect()
        await self.sse_client.disconnect()


endpoint_manager = EndpointManager()
endpoint_manager.init_config(global_config)
