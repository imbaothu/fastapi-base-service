from fastapi import FastAPI, WebSocket
import uvicorn
import asyncio

app = FastAPI()

@app.websocket("/example")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await websocket.send_text(f"From remote server 1")
        await asyncio.sleep(1)
        await websocket.send_text(f"From remote server 2")
        await asyncio.sleep(1)
        await websocket.send_text(f"From remote server 3")
        break

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8090)