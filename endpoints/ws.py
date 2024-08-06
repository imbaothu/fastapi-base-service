"""
usage 
client websocket
aiohttp, session
"""

from aiohttp import (
    ClientSession,
    ClientTimeout,
    WSMsgType,
    WebSocketError,
)
from logger import logger
from fastapi import WebSocket


TIMEOUT = 1.0


class WsClient:
    """
    Connect and works with ws remote server
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

    # receive message from server and send to client
    async def relay_messages(self, client_ws: WebSocket, path: str):
        async with self.session.ws_connect(path) as remote_ws:
            try:
                async for msg in remote_ws:
                    # here : don't have autocomplete or hint for msg.type. 
                    # If you need use check instance(WSMsg Object)
                    if msg.type == WSMsgType.TEXT:
                        await client_ws.send_text(msg.data)
                    if msg.type == WSMsgType.CLOSE:
                        await client_ws.close()
            except WebSocketError as e:
                logger.error(f"Websocket error: {e}")
