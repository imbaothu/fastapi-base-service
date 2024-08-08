"""
usage 
client websocket
aiohttp, session
"""

from aiohttp import (
    ClientSession,
    ClientTimeout,
)
from aiohttp_sse_client import client as sse_client

from logger import logger


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
        self.session = ClientSession(self.server, timeout=ClientTimeout(1))

    async def disconnect(self):
        if self.session:
            await self.session.close()

    async def stream(self, path:str):
        async with self.session as session:
            async with session.get(path) as response:
                async for line in response.content:
                    if line:
                        data = line.decode('utf-8').strip()
                        # Modify the data here
                        modified_data = f"Modified: {data}"
                        yield f"data: {modified_data}\n\n"
