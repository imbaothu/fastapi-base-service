from fastapi import APIRouter, WebSocket
from endpoints import endpoint_manager
from fastapi.responses import StreamingResponse

router = APIRouter()
import aiohttp

@router.websocket("/websocket")
async def ws_example_function(ws: WebSocket):
    """
    Connect to ws remote server and send item to client by another websocket
    """
    await ws.accept()
    await endpoint_manager.ws_client.relay_messages(client_ws=ws, path="/example")

@router.get("/sse")
async def sse_proxy():
    return StreamingResponse(endpoint_manager.sse_client.stream("/sse"), media_type="text/event-stream")


