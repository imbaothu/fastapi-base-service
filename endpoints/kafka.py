from aiokafka import AIOKafkaConsumer, AIOKafkaProducer


class KafkaClient:
    def __init__(self) -> None:
        self.bootstrap_servers = ""
        self.producer: AIOKafkaProducer = None
        self.consumer: AIOKafkaConsumer = None

    def init_config(self, config):
        self.bootstrap_servers = config["uri"]

    async def connect(self, my_topic: str, consumer_group_id: str):
        self.producer = AIOKafkaProducer(bootstrap_servers=self.bootstrap_servers)
        self.consumer = AIOKafkaConsumer(
            my_topic,
            bootstrap_servers=self.bootstrap_servers,
            group_id=consumer_group_id,
        )
    
    async def disconnect(self):
        await self.producer.stop()
        await self.consumer.stop()

    async def consume(self):
        await self.consumer.start()

        try:
            # consume messages:
            async for msg in self.consumer:
                yield msg
        finally:
            await self.consumer.stop()

    async def produce(self, my_topic: str, mess: str):
        await self.producer.start()
        try:
            await self.producer.send_and_wait(my_topic, mess.encode())
        finally:
            # Wait for all pending messages to be delivered or expire.
            await self.producer.stop()
