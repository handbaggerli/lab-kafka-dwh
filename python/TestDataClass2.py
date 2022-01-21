# -*- coding: utf-8 -*-


# pip install dataclasses-avroschema

from dataclasses import dataclass
import typing

from dataclasses_avroschema import AvroModel
from datetime import date, datetime


@dataclass
class ColumnDef(AvroModel):
    "Enthaelt die Column Info"
    columnId: int
    columnName: str
    dataType: str
    dataScale: int
    dataPrec: int

    class Meta:
        namespace = "kdg.ColumnDef.v1"


@dataclass
class TableDef(AvroModel):
    "Enthaelt die Table Info"
    tableId: int
    tableName: str
    tableType: str
    hasPartition: bool
    columnInfoDict: typing.Dict[str, ColumnDef]

    class Meta:
        namespace = "kdg.TableDef.v1"



if __name__ == "__main__":

    print(TableDef.avro_schema())


    myTableData: TableDef = TableDef(tableId=1, tableName="Sugus", tableType="Normale", hasPartition=False,
                                     columnInfoDict={})
    for i in range(10):
        myTableData.columnInfoDict[f"Col{i}"] = ColumnDef(columnId=i, columnName=f"Col{i}", dataType="Varchar2", dataScale=2*i, dataPrec=3*i)

    out = myTableData.serialize()
    print(out)

    print(myTableData.columnInfoDict["Col3"].columnName)



