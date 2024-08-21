import json
import asyncio
from aiokafka import AIOKafkaProducer

import time

def serializer(value):
    return json.dumps(value).encode()

async def produce():
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=serializer,
        compression_type="gzip")

    await producer.start()
    data = {"a": 123.4, "b": "fuckkkkk"}
    await producer.send('momo', data)
    data = [1,2,3,4]
    await producer.send('momo', data)
    await producer.stop()

asyncio.run(produce())