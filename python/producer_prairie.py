# -*- coding: utf-8 -*-

from kafka import KafkaProducer

if __name__ == "__main__":
    bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
    topicName = 'kdg-prairie'

#    myProd = MyProducer(bootstrap_servers=bootstrap_servers)
    lineNr = 0
    pic = None

    with open("../producer_input/Prairie_korrektur01.png", "rb") as f:
        pic = f.read()

