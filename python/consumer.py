# -*- coding: utf-8 -*-

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
        """
        consumer = KafkaConsumer(bootstrap_servers=self.__bootstrap_servers,
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=True,
                                 auto_commit_interval_ms=1000,
                                 group_id=self.__group_id,
                                 consumer_timeout_ms=self.__timeout_ms)
        tp0 = TopicPartition(topic=self.__topic, partition=0)
        tp1 = TopicPartition(topic=self.__topic, partition=1)
        tp2 = TopicPartition(topic=self.__topic, partition=2)
        tp3 = TopicPartition(topic=self.__topic, partition=3)
        tp4 = TopicPartition(topic=self.__topic, partition=4)
        tp5 = TopicPartition(topic=self.__topic, partition=5)
        tp6 = TopicPartition(topic=self.__topic, partition=6)
        tp7 = TopicPartition(topic=self.__topic, partition=7)
        tp8 = TopicPartition(topic=self.__topic, partition=8)
        tp9 = TopicPartition(topic=self.__topic, partition=9)
        consumer.assign([tp0, tp1, tp2, tp3, tp4, tp5, tp6, tp7, tp8, tp9])
        consumer.seek(tp0, offset=0)
        consumer.seek(tp1, offset=0)
        consumer.seek(tp2, offset=0)
        consumer.seek(tp3, offset=0)
        consumer.seek(tp4, offset=0)
        consumer.seek(tp5, offset=0)
        consumer.seek(tp6, offset=0)
        consumer.seek(tp7, offset=0)
        consumer.seek(tp8, offset=0)
        consumer.seek(tp9, offset=0)
        """
        for message in consumer:
            self.__output_file.write(message.value.decode("utf-8"))

        self.__output_file.close()





if __name__ == "__main__":
    bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
    topicName = 'kdg-dwh-test'
    group_id = "kdg-dwh-test-group1"
    output_file = "buddenbrooks_out.txt"
    myConsume = MyConsumer(bootstrap_servers=bootstrap_servers,
                           topic=topicName,
                           group_id=group_id,
                           timeout_ms=10000,
                           output_file=output_file)
    myConsume.consumeMessages()
    print("Consumer finito wegen keinen Daten mehr im Stream")
