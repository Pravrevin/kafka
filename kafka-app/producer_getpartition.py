from kafka import KafkaProducer
import json
import data
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def get_partition(key,all,aviliable):
    return 0

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer = json_serializer,
                         partitioner = get_partition)
print(producer)
if __name__ == "__main__":
    while 1==1:
        registered = data.get_registered_user()
        print(registered)
        producer.send("revin",registered)
        time.sleep(4)
