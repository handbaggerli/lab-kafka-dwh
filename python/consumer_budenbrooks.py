# -*- coding: utf-8 -*-
import time

from kafka import KafkaConsumer, TopicPartition


class MyConsumer:

    def __init__(self, bootstrap_servers: list, topic: str, group_id: str, timeout_ms: int, output_file: str):
        self.__bootstrap_servers = bootstrap_servers
        self.__topic = topic
        self.__group_id = group_id
        self.__timeout_ms = timeout_ms
        self.__output_file = open(output_file, "w+", encoding="utf-8")


    def consumeMessages(self):
        consumer = KafkaConsumer(self.__topic, bootstrap_servers=self.__bootstrap_servers,
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=True,
                                 auto_commit_interval_ms=1000,
                                 group_id=self.__group_id,
                                 consumer_timeout_ms=self.__timeout_ms)
        for message in consumer:
            self.__output_file.write(message.value.decode("utf-8"))

        self.__output_file.close()



class MyConsumerPart:

    def __init__(self, bootstrap_servers: list, topic: str, group_id: str, timeout_ms: int, output_file: str):
        self.__bootstrap_servers = bootstrap_servers
        self.__topic = topic
        self.__group_id = group_id
        self.__timeout_ms = timeout_ms
        self.__output_file = open(output_file, "w+", encoding="utf-8")


    def consumeMessages(self):
        consumer = KafkaConsumer(bootstrap_servers=self.__bootstrap_servers,
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=True,
                                 auto_commit_interval_ms=1000,
                                 group_id=self.__group_id,
                                 consumer_timeout_ms=self.__timeout_ms)
        for i in range(10):
            consumer.assign([TopicPartition(self.__topic, i)])

            for message in consumer:
                self.__output_file.write(message.value.decode("utf-8"))

        self.__output_file.close()


if __name__ == "__main__":
    bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
    topicName = 'kdg-buddenbrooks'
    group_id = "grp_1_kdg-buddenbrooks"
    output_file = "../consumer_output/buddenbrooks_out.txt"
    myConsume = MyConsumer(bootstrap_servers=bootstrap_servers,
                           topic=topicName,
                           group_id=group_id,
                           timeout_ms=10000,
                           output_file=output_file)
    myConsume.consumeMessages()
    print("Consumer finito wegen keinen Daten mehr im Stream")
