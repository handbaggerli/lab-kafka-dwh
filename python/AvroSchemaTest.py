# -*- coding: utf-8 -*-
import json

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from random import randint
from datetime import date, datetime, timedelta

class MainApp:
    def __init__(self):
        self.schema = None
        self.__readSchema()


    def __readSchema(self):
        self.schema = avro.schema.parse(open("UserSchema.json", "rb").read())

    def __randDate(self, startDate: date ,endDate: date) -> date:
        delta = startDate - endDate
        int_delta = delta.days
        random_days = randint(0, int_delta)
        return startDate + timedelta(days=random_days)

    def __randTimestamp(self, startTS: datetime, endTs: datetime) -> datetime:
        delta = endTs - startTS
        int_delta = delta.days * 24 * 60 * 60 + delta.seconds
        random_second = randint(0, int_delta)
        return startTS + timedelta(seconds=random_second)


    def writeExampleData(self):
        myDate = date.today()
        print(myDate)
        print(type(myDate))
        print(int(myDate))
        with DataFileWriter(open("users.avro", "wb"), DatumWriter(), self.schema) as writer:
            writer.append({"name": "Alyssa", "favorite_number": 256, "birthdate": myDate})
            writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red", "birthdate": myDate})

    def readExampleData(self):
        with DataFileReader(open("users.avro", "rb"), DatumReader()) as reader:
            for user in reader:
                print(user)

    def writeBigDataExample(self):
        names1 = ["Fritz", "Hans", "Kusi", "Steffi", "Betty", "Moni", "Ficki", "Nudi", "Susi", "Taylee", "Niti"]
        names2 = ["Meier", "Müller", "Brunner", "Schmied", "Sexy", "Spritzi", "Stöni", "Muschi", "Lochi", "Ficki"]
        colours = ["rot", "blau", "gelb", "grün"]
        data = []
        for i in range(100000):
            d = [f"{names1[randint(0, 10)]} {names2[randint(0, 9)]}", randint(0, 300), f"{colours[randint(0, 3)]}", date.today(), datetime.now()]
            s = {"name": d[0], "favorite_number": d[1], "favorite_color": d[2], "birthdate": d[3], "writeTime": d[4]}
            data.append(s)
        with DataFileWriter(open("bigDataExample.avro", "wb"), DatumWriter(), self.schema) as writer:
            for el in data:
                writer.append(el)
        with open("bigDataExample.json", "w") as f:
            for el in data:
                f.writelines(json.dumps(el))


    def readBigDataExample(self):
        index = 0
        with DataFileReader(open("bigDataExample.avro", "rb"), DatumReader()) as reader:
            for user in reader:
                print(f"Index: {index} - Daten: {user}")
                index += 1


if __name__ == "__main__":
    mainApp = MainApp()
    mainApp.writeExampleData()
    mainApp.readExampleData()
    mainApp.writeBigDataExample()
    mainApp.readBigDataExample()

