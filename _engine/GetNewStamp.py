import os

import getTableData
import dropSqlTable
import createSqliteTableFromList

import CheckIfFileChanged




def GetNewStamp():

    filename=GetDataFromDatabase(dataName='newFileLocation')

    Newstamp = os.stat(filename).st_mtime

    CheckIfFileChanged.CheckIfFileChanged(Newstamp=Newstamp)

    # WriteDataDatabase(data=Newstamp, dataName='Newstamp')

# def WriteDataDatabase(data, dataName):
#     Dictionary=getTableData.GetTableData()
#     Dictionary[dataName]=data

#     del Dictionary['id']

#     dropSqlTable.DropTable()

#     createSqliteTableFromList.SetValues(Dictionary=Dictionary)

def GetDataFromDatabase(dataName):
    dictValue=getTableData.GetTableData()

    data=dictValue[dataName]

    return data


GetNewStamp()