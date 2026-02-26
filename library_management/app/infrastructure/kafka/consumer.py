from kafka import KafkaConsumer
import json

# Listen to multiple topics

consumer = KafkaConsumer(
    bootstrap_servers="kafka:9092",
    auto_offset_reset="earliest",
    group_id="test-group-1",  # new group
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

consumer.subscribe(["book-events", "member-events"])

print("Listening to book and member events...")
for message in consumer:
    print(f"Topic: {message.topic} | Event received: {message.value}")
 

#docker exec -it library_api python app/infrastructure/kafka/consumer.py