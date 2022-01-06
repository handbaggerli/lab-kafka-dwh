# -*- coding: utf-8 -*-

from kafka import KafkaProducer

class MyProducer:

    def __init__(self, bootstrap_servers:str):
        self.__producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
        self.__partition = 0

    @property
    def patition(self) -> int:
        self.__partition += 1
        if self.__partition > 9:
            self.__partition = 0
        return self.__partition

    def produceData(self, topic: str, msg: bytes):
#        self.__producer.send(topic=topic, value=msg, partition=self.patition)
        self.__producer.send(topic=topic, value=msg)
        self.__producer.flush()



if __name__ == "__main__":
    bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
    topicName = 'kdg-buddenbrooks'

    myProd = MyProducer(bootstrap_servers=bootstrap_servers)
    lineNr = 0

    with open("../producer_input/buddenbrooks.txt", "r", encoding="utf-8") as f:
        for line in f:
            lineNr += 1
            msg = f"{lineNr} - {line}"
            myProd.produceData(topic=topicName, msg=msg.encode('utf-8'))

