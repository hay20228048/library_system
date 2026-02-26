import time
from kafka import KafkaProducer, errors
import json
import os

KAFKA_SERVER = os.getenv("KAFKA_SERVER", "kafka:9092")

for _ in range(10):
    try:
        producer = KafkaProducer(
            bootstrap_servers=[KAFKA_SERVER],
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        print("Connected to Kafka!")
        break
    except errors.NoBrokersAvailable:
        print("Kafka not ready, retrying in 5s...")
        time.sleep(5)
else:
    raise Exception("Kafka broker not available after 10 retries")





def publish_event(topic: str, event: dict):
    try:
        producer.send(topic, event)
        producer.flush()
        print(f"[KAFKA] Event sent -> {topic}: {event}")
    except Exception as e:
        print(f"[KAFKA ERROR] {e}")

