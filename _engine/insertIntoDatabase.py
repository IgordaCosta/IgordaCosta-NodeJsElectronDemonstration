import sys

from importedFNUDataPyDTs import *
from importedDataPyDTs import *
import getTableData
# import dropSqlTable
# import GBTdat
import DeleteAllTempFiles



# GBTdat.WriteFl(fileName=fileNameUsed)


stringOfChars = sys.argv[1]

print(stringOfChars)

print('stringOfChars')


DeleteAllTempFiles.DeleteAllTempFiles()




spllitter2 = '],'

spllitter1 = '], '

ReplaceSpliter = '#$5@$'



StringList = str(stringOfChars).replace("'",'').replace('"','').replace(spllitter1, ReplaceSpliter).replace(spllitter2, ReplaceSpliter).split(ReplaceSpliter)

print(StringList)

print('StringList')

print(len(StringList))

ListSize = len(StringList)

ValueList = ''
if ListSize == 1:


    StringList1 = str(StringList[0])

    StringList = StringList1.replace('[','').replace(']','').replace(', ', '#$@*').replace(',', '#$@*').split('#$@*')

    # [data, dataName, TableName, Database] = StringList

    print(StringList)

    print('2 StringList')

    data = StringList[0]

    dataName = StringList[1]

    TableName = StringList[2]

    Database = StringList[3]


    ValueList = False

elif ListSize > 1:
    ValueList = True

    data = StringList[0].replace('[','').replace(', ', '#$@*').replace(',', '#$@*').split('#$@*')

    dataName = StringList[1].replace('[','').replace(', ', '#$@*').replace(',', '#$@*').split('#$@*')


    RestListData = StringList[2].replace(']','').replace(', ', '#$@*').replace(',', '#$@*').split('#$@*')

    TableName = RestListData[0]

    Database = RestListData[1]

    

    # print(data)

    # print('data')
    # print(dataName)

    # print(TableName)

    # print(Database)

    if len(data) == 1:
        data = data[0]
        dataName = dataName[0]

        ValueList = False

        print(data)

        print('data')
        print(dataName)

 
else:
    pass






if ValueList:

    # dropSqlTable.DropSqlTable(TableName=TableName)

    dataNameList = dataName
    dataList = data


    getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)

elif ValueList == False:
    
    # dropSqlTable.DropSqlTable(TableName=TableName)


    getTableData.WriteDataDatabase(data=data,dataName=dataName)
    
else:
    pass



