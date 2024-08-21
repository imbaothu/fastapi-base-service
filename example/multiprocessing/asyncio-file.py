import asyncio
import aiofiles

async def read_and_write_file(output_file):
    async with aiofiles.open(output_file, 'a') as f:
        await f.write("hello world")

async def main():
    tasks = []
    for i in range(1, 5):
        output_file = f'output_file_{i}.txt'
        tasks.append(read_and_write_file(output_file))

    await asyncio.gather(*tasks)

asyncio.run(main())