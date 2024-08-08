import aiohttp
import asyncio

# async def listen_to_sse(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             async for line in response.content:
#                 if line:
#                     yield f"Received: {line.decode('utf-8').strip()}"


async def stream(path:str):
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:8091/sse") as response:
            async for line in response.content:
                if line:
                    print({line.decode('utf-8').strip()})
                    yield "minhdan"

async def main():
    sse_url = "http://localhost:8091/sse"
    async for data in stream(sse_url):
        print("fick")

# Run the client
asyncio.run(main())
