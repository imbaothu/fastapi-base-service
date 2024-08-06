"""
usage 
client websocket
aiohttp, session
"""

from aiohttp import (
    ClientSession,
    ClientTimeout,
)
from logger import logger
from fastapi import WebSocket
import json


TIMEOUT = 1.0


class SSEClient:
    """
    Connect and works with SSE remote server
    """

    def __init__(self) -> None:
        self.server = ""
        self.session: ClientSession = None  # annotation

    def init_config(self, config: dict):
        self.server = config["uri"]

    async def connect(self):
        self.session = ClientSession(self.server, timeout=ClientTimeout(TIMEOUT))

    async def disconnect(self):
        if self.session:
            await self.session.close()

    # recevice stream messages from sse server 
    async def stream(self, path:str):
        async with self.session.get(path) as response:
            async for line in response.content:
                if line:
                    data = {
                        'data' : json.dumps(line),
                    }
                    yield data

