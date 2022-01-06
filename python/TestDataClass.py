# -*- coding: utf-8 -*-


# pip install dataclasses-avroschema

from dataclasses import dataclass

import typing

from dataclasses_avroschema import AvroModel
from datetime import date, datetime

@dataclass
class Address(AvroModel):
    "An Address"
    street: str
    street_number: int

@dataclass
class User(AvroModel):
    "User with multiple Address"
    name: str
    age: int
    birthdate: date
    addresses: typing.List[Address]
    mutation: datetime

    class Meta:
        namespace = "kdg.User.v1"
        aliases = ["kdg.user-v1", "kdg super user"]

if __name__ == "__main__":
    adress = Address(street="Lörenmattstrasse", street_number=218)
    print(adress)
    user = User(name="Don Kusi", age=47, birthdate=date(year=1974, month=1, day=21), addresses=[adress], mutation=datetime.now())
    print(user)
    print(type(user))
    print(user.avro_schema())
    d = user.serialize(serialization_type="avro")
    print(d)
    ret_user = User.deserialize(data=d)
    print(type(ret_user))
    print(ret_user)

