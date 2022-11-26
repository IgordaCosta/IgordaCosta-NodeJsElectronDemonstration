import sqlite3
import os

import changeDirectory
import dropSqlTable
import createSqliteTableFromList
import GetKeyfileNameType
import GetWriteDBTableSecured
# import FilePathFromPython



#todo change 1 function
# adapt 3 function after changing the dependent corresponding functions


#this does not need to change and will not be used in secured table
#ok
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
   
            TableList.append(value)

        c.close() 
        conn.close()

        return TableList

    else:
        # print("could not find file!")
        pass


#################################### change this
#GetAllTableSecuredData(Database)
#ok
def GetTableDataFromTable(Database="AutoFormFiller.db",TableName='',TableNumber='',ErrorIfNotFound=True, InPythonFunction = False):

    # print('starting')

    changeDirectory.ChangeTokey()

    TableOk=False

    TableOptions = ['FontAndItsSize','FilesInDatabase','qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq','KEY_']

    if TableNumber !='':
        TableList=GetAllTableNamesFromDatabase(Database)
        TableName=TableList[TableNumber]

        # print(TableNumber)
    
    TableNameUsed = ''
    
    if TableName !='':

        spaceReplaceDataUserImput = '$%78&*&'

        # TableName= TableName.replace(" ", spaceReplaceDataUserImput)

        TableName0 = TableName

        # TableName = ' '.join(TableName0.split(spaceReplaceDataUserImput))

        TableName = spaceReplaceDataUserImput.join(TableName0.split(' '))

        Datalist, names= '',''
        
        if TableName == 'qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq':
            TableNameUsed = TableOptions[2]
            TableOk = True
            # print('settable')

        else:

            # print('settableelse')

            conn = sqlite3.connect(Database) 
            c = conn.cursor() 
 
            if TableName == 'FontAndItsSize':
                TableNameUsed = TableOptions[0]
                TableOk = True

            elif TableName == 'FilesInDatabase':
                TableNameUsed = TableOptions[1]
                TableOk = True

            elif TableName[:4] == 'KEY_':

                KeyFilename = TableName
                TableNameUsed = GetKeyfileNameType.GetKeyfileNameType(KeyFilename)
                TableOk = True

            else:
                pass


    else:
        TableNameUsed = TableOptions[2]
        TableOk = True
        # print('settableEmpty')



    if TableOk:

        if TableNameUsed == 'qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq':

            # Datalist, names = GetWriteDBTableSecured.GetAllTableSecuredData()

            Datalist, names = GetWriteDBTableSecured.GetAllTableSecuredData(InPythonFunction=InPythonFunction)

            return Datalist, names 

        else:

            try:

                c.execute("SELECT * FROM "+ TableNameUsed)

                names = [description[0] for description in c.description]

                rows = c.fetchall()

                Datalist=[]
                for row in rows:

                    Datalist.append(list(row))

            except Exception as e:
                pass

            c.close() 
            conn.close() 

            if Datalist=='' and ErrorIfNotFound:
                raise Exception("The variable was not found!")
            
            return Datalist, names

#this does not need to change and will not be used in secured table
#ok
def getTables():

    Database="AutoFormFiller.db"

    TableList=GetAllTableNamesFromDatabase(Database=Database)

    return TableList

# change this
# GetAllTableDictionarySecuredData(Database)
# ok
def GetTableData(TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq',ErrorIfNotFound=True):


    if TableName == 'qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq':

        dictValue = GetWriteDBTableSecured.GetAllTableDictionarySecuredData()

        return dictValue

    else:

        spaceReplaceDataUserImput = '$%78&*&'

        # TableName= TableName.replace(" ", spaceReplaceDataUserImput)

        TableName0 = TableName

        # TableName = ' '.join(TableName0.split(spaceReplaceDataUserImput))

        TableName = spaceReplaceDataUserImput.join(TableName0.split(' '))


        TableName=TableName
        Database="AutoFormFiller.db"

        dictValue = {}

        Datalist, names=GetTableDataFromTable(Database=Database,TableName=TableName,ErrorIfNotFound=ErrorIfNotFound)
        try: 
            Datalist=Datalist[0]

            dictValue = dict(zip(names, Datalist))
        
        except Exception as e:
            # print(e)
            pass

        return dictValue

# change this
# GetTableSingleItensSecuredData(Database, ItemName)
# ok
def GetDataFromDatabase(dataName, TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq'):

    if TableName == 'qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq':

        ItemName = dataName

        data = GetWriteDBTableSecured.GetTableSingleItensSecuredData(ItemName=ItemName)

        return data

    else:
        
        spaceReplaceDataUserImput = '$%78&*&'

        # TableName= TableName.replace(" ", spaceReplaceDataUserImput)

        TableName0 = TableName

        # TableName = ' '.join(TableName0.split(spaceReplaceDataUserImput))

        TableName = spaceReplaceDataUserImput.join(TableName0.split(' '))

        dictValue=GetTableData(TableName = TableName)

        data=dictValue[dataName]

        return data


# change this
# GetTableItensDictionarySecuredData(Database, ItemNameList)
# ok
def GetMultipleDataFromDatabase(dataNameList, TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq'):

    if TableName == 'qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq':

        ItemNameList = dataNameList

        Dictionary = GetWriteDBTableSecured.GetTableItensDictionarySecuredData(ItemNameList=ItemNameList)

        return Dictionary

    else:

        spaceReplaceDataUserImput = '$%78&*&'

        # TableName= TableName.replace(" ", spaceReplaceDataUserImput)

        TableName0 = TableName

        # TableName = ' '.join(TableName0.split(spaceReplaceDataUserImput))

        TableName = spaceReplaceDataUserImput.join(TableName0.split(' '))



        dictValue=GetTableData(TableName=TableName)

        Dictionary={}
        for i in range(len(dataNameList)):
            data=dictValue[dataNameList[i]]
            Dictionary[dataNameList[i]]=data


        return Dictionary

#+++++++++++++++++++++++++ change this
# WriteTableSecuredIten(Database, ItemName,ItemValue)
# ok
def WriteDataDatabase(data,dataName):

    ItemName = dataName

    ItemValue = data

    GetWriteDBTableSecured.WriteTableSecuredIten(ItemName=ItemName,ItemValue=ItemValue)


    # Dictionary=GetTableData(ErrorIfNotFound=False)
    # Dictionary[dataName]=data

    # try:
    #     del Dictionary['id']
    # except:
    #     pass

    # dropSqlTable.DropTable()

    # createSqliteTableFromList.SetValues(Dictionary=Dictionary)


#++++++++++++++++++++++ change this
#WriteTableSecuredList(Database, ItemNameList,colValueList)
# ok
def MultipleListWriteDataDatabase(dataList,dataNameList):

    ItemNameList = dataNameList
    colValueList = dataList

    GetWriteDBTableSecured.WriteTableSecuredList(ItemNameList=ItemNameList,colValueList=colValueList)


    # Dictionary=GetTableData(ErrorIfNotFound=False)
    # for i in range(len(dataNameList)):
    #     Dictionary[dataNameList[i]]=dataList[i]

    # try:
    #     del Dictionary['id']
    # except:
    #     pass

    # dropSqlTable.DropTable()

    # createSqliteTableFromList.SetValues(Dictionary=Dictionary)

#+++++++++++++++++++++++++++ change this
# WriteTableSecuredDictionary(Database, InputDictionary)
# ok
def MultipleDictionaryWriteDataDatabase(DictionaryAdd,TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq'):

    if TableName == 'qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq':

        InputDictionary = DictionaryAdd

        GetWriteDBTableSecured.WriteTableSecuredDictionary(InputDictionary=InputDictionary)

    else:

        # spaceReplaceDataUserImput = '$%78&*&'

        # TableName= TableName.replace(" ", spaceReplaceDataUserImput)

        # TableName0 = TableName

        # TableName = spaceReplaceDataUserImput.join(TableName0.split(' '))

        # TableName = spaceReplaceDataUserImput.join(TableName0.split(' '))



        Dictionary0=GetTableData(ErrorIfNotFound=False)

        Dictionary = dict(list(Dictionary0.items()) + list(DictionaryAdd.items()))
        
        try:
            del Dictionary['id']
        except:
            pass

        dropSqlTable.DropTable(TableName=TableName)

        createSqliteTableFromList.SetValues(TableName=TableName, Dictionary=Dictionary)







# CurrentWorkingPath = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2\CSSAutoFormFiller'

# # data = 'data1'

# # dataName = 'dataname1'


# # WriteDataDatabase(data,dataName)


# print(GetTableDataFromTable(Database="AutoFormFiller.db",TableName='KEY_test$%78&*&b$%78&*&space2',TableNumber='',ErrorIfNotFound=True))

# print(GetTableDataFromTable(Database="AutoFormFiller.db",TableName='',TableNumber='',ErrorIfNotFound=True))

# print(getTables())

# GetTableDataFromTable(Database="AutoFormFiller.db",TableName='KEY_file1',TableNumber='')

# data=0
# dataName="rw"

# WriteDataDatabase(data,dataName)

# print(GetTableData()['ExtensionType'])

# print(GetTableDataFromTable(Database="AutoFormFiller.db",TableName='',TableNumber='',ErrorIfNotFound=True))

# # dropSqlTable.DropTable()

# dictValue=GetTableData()


# print("bellow is the data1")

# print(dictValue['fileLocation'])



# DictionaryAdd={'Data100': '11','Data200': '22','Data300': '33'}

# MultipleDictionaryWriteDataDatabase(DictionaryAdd)


# dictValue=GetTableData()


# print("bellow is the data2")

# print(dictValue)

# print("bellow is the data2")
# import pprint
# pprint.pprint(dictValue)

# # fname=dictValue['fname']

# # filePath=dictValue['filePath']

# # fileNameOnly=dictValue['fileNameOnly']



# # col1=dictValue['col1']

# # print(col1)



# import pprint


# TableOptions = ['FontAndItsSize','FilesInDatabase','qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq','KEY_img17']

# TableName = TableOptions[1]

# pprint.pprint(GetTableDataFromTable(Database="AutoFormFiller.db",TableName=TableName,TableNumber='',ErrorIfNotFound=True, InPythonFunction = False))



# print(getTables())

# dataList = ['a', 'b', 'c', 'd']

# dataNameList =['item1', 'item2', 'item3', 'item4']


# MultipleListWriteDataDatabase(dataList,dataNameList)

# import pprint


# pprint.pprint( GetTableData())

# pprint.pprint(GetTableDataFromTable())