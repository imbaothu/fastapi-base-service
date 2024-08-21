import threading
import aiofiles
import time
import asyncio
import tracemalloc
import requests
import aiohttp

# Simulating a network I/O bound task with threading
def fetch_url_thread(url, output_file):
    response = requests.get(url)
    with open(output_file, 'a') as f:
        f.write(response.text[:100])  # Writing only the first 100 characters for simplicity

# Threading example with network I/O
def threading_example(urls):
    threads = []
    for i, url in enumerate(urls):
        output_file = f'output_file_{i}.txt'
        thread = threading.Thread(target=fetch_url_thread, args=(url, output_file))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Asyncio equivalent of the network I/O task
async def fetch_url_async(session, url, output_file):
    async with session.get(url) as response:
        content = await response.text()
        async with aiofiles.open(output_file, 'a') as f:
            await f.write(content[:100])  # Writing only the first 100 characters for simplicity

# Asyncio example with network I/O
async def asyncio_example(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, url in enumerate(urls):
            output_file = f'output_file_{i}.txt'
            tasks.append(fetch_url_async(session, url, output_file))
        await asyncio.gather(*tasks)

# URLs to be fetched
urls = [
    'https://www.example.com',
    'https://www.example.org',
    'https://www.example.net',
    # Add more URLs to increase load
] * 10  # Multiplied by 10 to increase the number of tasks

# Measure memory and time for threading
start_time = time.time()
tracemalloc.start()
threading_example(urls)
snapshot = tracemalloc.take_snapshot()
end_time = time.time()
print(f"Threading: Time = {end_time - start_time} seconds")
print(f"Threading: Memory usage = {snapshot.statistics('lineno')[0].size / 1024:.2f} KiB")

# Measure memory and time for asyncio
start_time = time.time()
tracemalloc.start()
asyncio.run(asyncio_example(urls))
snapshot = tracemalloc.take_snapshot()
end_time = time.time()
print(f"Asyncio: Time = {end_time - start_time} seconds")
print(f"Asyncio: Memory usage = {snapshot.statistics('lineno')[0].size / 1024:.2f} KiB")


# Results 
# Threading: Time = 0.9466688632965088 seconds
# Threading: Memory usage = 15.56 KiB
# Asyncio: Time = 0.8783159255981445 seconds
# Asyncio: Memory usage = 7681.67 KiB