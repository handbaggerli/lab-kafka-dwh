# -*- coding: utf-8 -*-
import decimal
from dataclasses import dataclass

from dataclasses_avroschema import AvroModel, types
from datetime import date, datetime, time
from uuid import uuid4
import typing
from enum import Enum

class Haarfarbe(Enum):
    Blond = 0
    Braun = 1
    Schwarz = 2
    Rot = 3
    Grau = 4
    Weiss = 5
    Mehrere = 98
    Andere = 99


class Frisur(Enum):
    Glatze = "glatze"
    Irok = "irok"
    Mili = "mili"
    Normal = "normal"
    Lang = "lang"

@dataclass
class Schauspieler(AvroModel):
    "Definition eines Schauspielers"
    schaupielerId: uuid4
    recordCreated: datetime
    vorName: str
    nachName: str
    isTaetowiert: bool
    gewohnHeiten: typing.List[str]
    taschenGeld: float
    kopfFrisur: str
    geschlecht: types.Enum = types.Enum(["Weiblich", "Maennlich", "Anderes"])
    kopfHaarFarben: typing.List[int] = None
    schamHaarFarbe: int = None
    achselHaarFarbe: int = None
    geburtsDatum: date = None

    class Meta:
        namespace = "Schauspieler.v1"
        aliases = ["schauspieler-v1", "schauspieler"]

print(Schauspieler.avro_schema())

@dataclass
class Film(AvroModel):
    "Definiert einen Film"
    filmId: uuid4
    recordCreated: datetime
    filmName: str
    ablagePfad: str
    laenge: time
    besetzung: typing.List[Schauspieler]

    class Meta:
        namespace = "Film.v1"
        aliases = ["film-v1", "film"]

print(Film.avro_schema())


if __name__ == "__main__":
    s_vreni = Schauspieler(schaupielerId=uuid4(),
                           recordCreated=datetime.now(),
                           vorName="Vreni",
                           nachName="Stoeni",
                           isTaetowiert=True,
                           gewohnHeiten=["bumsen", "blasen", "anal"],
                           taschenGeld=123456.789,
                           kopfFrisur=Frisur.Irok.value,
                           geschlecht="Weiblich",
                           kopfHaarFarben=[Haarfarbe.Blond.value, Haarfarbe.Rot.value],
                           schamHaarFarbe=Haarfarbe.Schwarz.value,
                           achselHaarFarbe=Haarfarbe.Schwarz.value,
                           geburtsDatum=date(year=2000, month=2, day=22)
                           )
    s_moni = Schauspieler(schaupielerId=uuid4(),
                           recordCreated=datetime.now(),
                           vorName="Moni",
                           nachName="Bravi",
                           isTaetowiert=False,
                           gewohnHeiten=["bumsen", "blasen", "anal"],
                           taschenGeld=1456.79,
                           kopfFrisur=Frisur.Lang.value ,
                           geschlecht="Weiblich",
                           kopfHaarFarben=[Haarfarbe.Schwarz.value],
                           schamHaarFarbe=Haarfarbe.Schwarz.value,
                           geburtsDatum=date(year=1999, month=12, day=14)
                           )
    s_kusi = Schauspieler(schaupielerId=uuid4(),
                           recordCreated=datetime.now(),
                           vorName="Kusi",
                           nachName="Spritzi",
                           isTaetowiert=False,
                           gewohnHeiten=["bumsen", "blasen", "anal"],
                           taschenGeld=140056.79,
                           kopfFrisur=Frisur.Lang.value,
                           geschlecht="Maennlich",
                           kopfHaarFarben=[Haarfarbe.Braun.value],
                           schamHaarFarbe=Haarfarbe.Rot.value,
                           achselHaarFarbe=Haarfarbe.Braun.value,
                           geburtsDatum=date(year=1974, month=1, day=21)
                           )
    s_film = Film(filmId=uuid4(),
                  recordCreated=datetime.now(),
                  filmName="Spritzen ist Geil",
                  ablagePfad=r"c:/filme/spritzenistgeil.mkv",
                  laenge=time(hour=2, minute=34, second=22),
                  besetzung=[s_kusi, s_vreni, s_moni])

    s_film1 = Film(filmId=uuid4(),
                  recordCreated=datetime.now(),
                  filmName="Spritzen ist Geil mit Vreni",
                  ablagePfad=r"c:/filme/spritzenistgeilmitvreni.mkv",
                  laenge=time(hour=1, minute=22, second=2),
                  besetzung=[s_kusi, s_vreni])

    s_film = Film(filmId=uuid4(),
                  recordCreated=datetime.now(),
                  filmName="Spritzen ist Geil mit Moni",
                  ablagePfad=r"c:/filme/spritzenistgeilmitmoni.mkv",
                  laenge=time(hour=1, minute=44, second=52),
                  besetzung=[s_kusi, s_moni])


    print(s_film.serialize(serialization_type='avro-json'))
    print(s_film.serialize())



