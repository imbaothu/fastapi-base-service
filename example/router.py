from fastapi import FastAPI, APIRouter, WebSocket
from fastapi.responses import StreamingResponse
from endpoints import endpoint_manager

router = APIRouter()

@router.websocket("")
async def ws_example_function(ws: WebSocket):
    """
    Connect to ws remote server and send item to client by another websocket
    """
    await ws.accept()
    await endpoint_manager.ws_client.relay_messages(client_ws=ws, path="/example")
