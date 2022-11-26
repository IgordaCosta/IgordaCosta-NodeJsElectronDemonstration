import sqlite3
import os

import changeDirectory

import dropSqlTable

import createSqliteTableFromList


#todo change 1 function
# adapr 3 function after changing the dependent corresponding functions


#this does not need to change
def GetAllTableNamesFromDatabase(Database):

    changeDirectory.ChangeTokey()


    Exists=os.path.isfile(Database)

    if Exists:
        conn = sqlite3.connect(Database) 
        c = conn.cursor() 

        c.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'") 
        conn.commit() 

        rows = c.fetchall()

        TableList=[]
        for row in rows:
            value=list(row)[0]
            # print(value)
            TableList.append(value)

        # print(TableList)
        print("Done Database Read")

        c.close() 
        conn.close()

        return TableList

    else:
        print("could not find file!")


#################################### this needs to change (independent)
def GetTableDataFromTable(Database="AutoFormFiller.db",TableName='',TableNumber='',ErrorIfNotFound=True):

    changeDirectory.ChangeTokey()
    

    if TableNumber !='':
        TableList=GetAllTableNamesFromDatabase(Database)
        TableName=TableList[TableNumber]
        # print(TableName,"TableName used")
    
    if TableName !='':
        Datalist, names= '',''

        conn = sqlite3.connect(Database) 
        c = conn.cursor() 

        try:
            c.execute("SELECT * FROM "+ TableName)

            names = [description[0] for description in c.description]

            rows = c.fetchall()

            Datalist=[]
            for row in rows:
                # print(row)
                Datalist.append(list(row))

            # print(Datalist)

            # print(Datalist[0][4])

            # print('Datalist')

            # print(names)

            # print("names")

        except Exception as e:
            print(e)

        c.close() 
        conn.close() 

        if Datalist=='' and ErrorIfNotFound:
            raise Exception("The variable was not found!")


        return Datalist, names

#this does not need to change
def getTables():

    Database="AutoFormFiller.db"

    TableList=GetAllTableNamesFromDatabase(Database=Database)

    return TableList

# this does not need to change
def GetTableData(TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq',ErrorIfNotFound=True):

    TableName=TableName
    Database="AutoFormFiller.db"

    dictValue = {}

    Datalist, names=GetTableDataFromTable(Database=Database,TableName=TableName,ErrorIfNotFound=ErrorIfNotFound)
    try: 
        Datalist=Datalist[0]

        dictValue = dict(zip(names, Datalist))
    
    except Exception as e:
        print(e)

    return dictValue

#this does not need to change
def GetDataFromDatabase(dataName, TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq'):
    dictValue=GetTableData(TableName = TableName)

    print('dictValue: ',dictValue)

    data=dictValue[dataName]

    return data

#this does not need to change
def GetMultipleDataFromDatabase(dataNameList, TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq'):
    dictValue=GetTableData(TableName=TableName)

    Dictionary={}
    for i in range(len(dataNameList)):
        data=dictValue[dataNameList[i]]
        Dictionary[dataNameList[i]]=data


    return Dictionary

#+++++++++++++++++++++++++ this is dependent on outside functions and might need to adapt
def WriteDataDatabase(data,dataName):
    Dictionary=GetTableData(ErrorIfNotFound=False)
    Dictionary[dataName]=data

    try:
        del Dictionary['id']
    except:
        pass

    dropSqlTable.DropTable()

    createSqliteTableFromList.SetValues(Dictionary=Dictionary)


#++++++++++++++++++++++ This is dependent on outside functions and might need to adapt
def MultipleListWriteDataDatabase(dataList,dataNameList):
    Dictionary=GetTableData(ErrorIfNotFound=False)
    for i in range(len(dataNameList)):
        Dictionary[dataNameList[i]]=dataList[i]

    try:
        del Dictionary['id']
    except:
        pass

    dropSqlTable.DropTable()

    createSqliteTableFromList.SetValues(Dictionary=Dictionary)

#+++++++++++++++++++++++++++ this is dependent on outside functions and might need to adapt
def MultipleDictionaryWriteDataDatabase(DictionaryAdd,TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq'):
    Dictionary0=GetTableData(ErrorIfNotFound=False)

    Dictionary = dict(list(Dictionary0.items()) + list(DictionaryAdd.items()))

    # print(Dictionary)
    
    try:
        del Dictionary['id']
    except:
        pass

    dropSqlTable.DropTable(TableName=TableName)

    createSqliteTableFromList.SetValues(TableName=TableName, Dictionary=Dictionary)




# getTables()

# GetTableDataFromTable(Database="AutoFormFiller.db",TableName='KEY_file1',TableNumber='')

# data=0
# dataName="rw"

# WriteDataDatabase(data,dataName)

# # GetTableData()

# # dropSqlTable.DropTable()

# dictValue=GetTableData()


# print("bellow is the data1")

# print(dictValue)



# DictionaryAdd={'Data100': '11','Data200': '22','Data300': '33'}

# MultipleDictionaryWriteDataDatabase(DictionaryAdd)


# dictValue=GetTableData()


# print("bellow is the data2")

# print(dictValue)

# # fname=dictValue['fname']

# # filePath=dictValue['filePath']

# # fileNameOnly=dictValue['fileNameOnly']



# # col1=dictValue['col1']

# # print(col1)





