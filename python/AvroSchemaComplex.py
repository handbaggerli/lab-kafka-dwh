# -*- coding: utf-8 -*-


# pip install dataclasses-avroschema
from uuid import uuid4
from enum import Enum
from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel

class Haarfarbe(Enum):
    Blond = "blond"
    Rot = "rot"
    Schwarz = "schwarz"
    Braun = "braun"
    Grau = "grau"
    Weiss = "weiss"
    Mehrere = "mehrere"
    Andere = "andere"

class Geschlecht(Enum):
    Weiblich = 1
    Maennlich = 2
    Anderes = 3

class Schauschieler(BaseModel):
    ModelId: str
    Vorname: str
    Nachname: str
    Geschlecht: Geschlecht
    Geburtsdatum: Optional[date] = None
    Taetowiert: Optional[bool] = None
    RecordCreated: datetime = datetime.now()




if __name__ == "__main__":
    s_vreni = Schauschieler(ModelId=str(uuid4()), Vorname="Vreni", Nachname="Stoeni", Geschlecht=Geschlecht.Weiblich, Geburtsdatum=date(year=2000, month=2, day=22))
    print(s_vreni.json())

