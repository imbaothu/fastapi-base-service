from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

def event_generator():
    count = 0
    while True:
        time.sleep(1)  # Simulate a delay between events
        count += 1
        if count > 5:
            break
        yield f"data: The time is {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"

@app.get("/sse")
async def sse_endpoint(request: Request):
    return StreamingResponse(event_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8091)
