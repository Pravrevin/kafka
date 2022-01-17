from kafka import KafkaProducer
import json
import data
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer = json_serializer)

if __name__ == "__main__":
    while 1 == 1:
        registered = data.get_registered_user()
        print(registered)
        producer.send("registered_user",registered)
        time.sleep(2)
