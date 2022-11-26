import os

import getTableData
import dropSqlTable
import createSqliteTableFromList


def GetOldStamp():

    filename=GetDataFromDatabase(dataName='newFileLocation')

    oldStamp = os.stat(filename).st_mtime

    WriteDataDatabase(data=oldStamp, dataName='oldStamp')


def WriteDataDatabase(data, dataName):
    Dictionary=getTableData.GetTableData()
    Dictionary[dataName]=data

    del Dictionary['id']

    dropSqlTable.DropTable()

    createSqliteTableFromList.SetValues(Dictionary=Dictionary)

def GetDataFromDatabase(dataName):
    dictValue=getTableData.GetTableData()

    data=dictValue[dataName]

    return data


GetOldStamp()