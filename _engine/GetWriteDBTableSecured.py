from pysqlitecipher import sqlitewrapper
import os

from importedDataPyDTs import *
from importedDataPycommaReplaceData import *
import EncodeDecode4Db
import FilePathFromPython
import RemoveExtraSlashes




def WriteTableSecuredList(ItemNameList,colValueList):

    for itemToSaveID in range(len(ItemNameList)):

        ItemName = ItemNameList[itemToSaveID]
        ItemValue = colValueList[itemToSaveID]
        WriteTableSecuredIten(ItemName=ItemName, ItemValue=ItemValue)

def WriteTableSecuredDictionary(InputDictionary):

    # no need to remove slashes

    ItemNameList = [*InputDictionary]
    
    colValueList = [*InputDictionary.values()]

    WriteTableSecuredList(ItemNameList = ItemNameList, colValueList = colValueList)


def WriteTableSecuredIten(ItemName, ItemValue):


    # print(str(ItemName), str(ItemValue))
    TextToRemoveSlashes = ItemValue
    ItemValue= RemoveExtraSlashes.RemoveExtraSlashes(TextToRemoveSlashes=TextToRemoveSlashes)

    # print(ItemValue)
    


    iDValue = 0
    colname = 'Col0'

    obj = sqlitewrapper.SqliteCipher(dataBasePath = dataBasePath , checkSameThread = False , password = pqw)

    datatype = 'TEXT'

    colList = [[colname , datatype]]

    try:
        obj.createTable(tableName = ItemName , colList = colList , makeSecure=True , commit=True)

        # print('table created now')
    except Exception as e:
        if str(e) == 'table name already exist in data base':
            # print('Table already created')
            pass
        else:
            # print(e)
            pass


    try:
        obj.deleteDataInTable(ItemName, iDValue , commit = True , raiseError = True , updateId = True)
    except Exception as e:
        if str(e) == 'ID = 0 not found while deletion process':
            # print('ID does not exist')
            pass

    obj.insertIntoTable(tableName=ItemName , insertList=colList , commit = True)

    stringToEncode = str(ItemValue).replace(', ', commaReplaceData1).replace(',', commaReplaceData2)
        
    colValueToAdd = EncodeDecode4Db.encodeBase64Db(stringToEncode)





  
    obj.updateInTable(ItemName , iDValue , colName=colname , colValue = colValueToAdd , commit = True , raiseError = True)


    # print('Done')



def GetAllTableSecuredData(InPythonFunction=False):


    obj = sqlitewrapper.SqliteCipher(dataBasePath = dataBasePath , checkSameThread = False , password = pqw)

    # print(obj.getAllTableNames()[2][0])

    Itens = obj.getAllTableNames()

    # print(Itens)

    # print(tableNameList)

    ItemNameList = []
    OuptputList = []
    for i in range(len(Itens)-2):

        ItenToAppend = Itens[i+2][0]
        TableData02 = obj.getDataFromTable(ItenToAppend, raiseConversionError = True , omitID = True)

        TextToRemoveSlashes = TableData02
        try:
            TableData2= RemoveExtraSlashes.RemoveExtraSlashes(TextToRemoveSlashes=TextToRemoveSlashes)
        
        except:
            TableData2 = RemoveExtraSlashes.RemoveExtraSlashesList(ListToRemoveSlashes=TextToRemoveSlashes)

        # print(TableData2)
        
        ItemNameList.append(ItenToAppend)

        # print(tableNameList[i])
        # print(TableData2)

        # print(TableData2[1][0][0])
        OutputValueToAppend0 = TableData2[1][0][0]

        stringToDecode = str(OutputValueToAppend0)

        # print(stringToDecode)

        # print('stringToDecode above')

        OutputValueToAppend = EncodeDecode4Db.decodeBase64Db(stringToDecode)

        if InPythonFunction:
            OutputValueToAppend2 = str(OutputValueToAppend).replace(', ', commaReplaceData1).replace( ',', commaReplaceData2)

        else:   
            # print('OUTfuntion')

            OutputValueToAppend2 = str(OutputValueToAppend).replace(commaReplaceData1, ', ').replace( commaReplaceData2, ',')


        # print(OutputValueToAppend2)

        # print('OutputValueToAppend2 above')


        OuptputList.append(OutputValueToAppend2)

    return [OuptputList], ItemNameList





def GetAllTableDictionarySecuredData(InPythonFunction=False):

    # no need to add function to remove slashes

    Datalist, names = GetAllTableSecuredData(InPythonFunction = InPythonFunction)

    try: 
        Datalist=Datalist[0]

        dictValue = dict(zip(names, Datalist))
    
    except Exception as e:
        # print(e)
        pass

    return dictValue

    


def GetTableItensListSecuredData(ItemNameList, InPythonFunction=False):


    tableNameList = ItemNameList

    obj = sqlitewrapper.SqliteCipher(dataBasePath = dataBasePath , checkSameThread = False , password = pqw)

    # print(obj.getAllTableNames()[2][0])

    # print(tableNameList)

    OuptputList = []
    for i in range(len(tableNameList)):

        TableData02 = obj.getDataFromTable(tableNameList[i], raiseConversionError = True , omitID = True)

        TextToRemoveSlashes = TableData02
        try:
            TableData2 = RemoveExtraSlashes.RemoveExtraSlashes(TextToRemoveSlashes=TextToRemoveSlashes)
        
        except:
            TableData2 = RemoveExtraSlashes.RemoveExtraSlashesList(ListToRemoveSlashes=TextToRemoveSlashes)
        # print(TableData2)

        # print(tableNameList[i])
        # print(TableData2)

        # print(TableData2[1][0][0])

        OutputValueToAppend0 = str(TableData2[1][0][0])

        stringToDecode = OutputValueToAppend0

        OutputValueToAppend = EncodeDecode4Db.decodeBase64Db(stringToDecode)

        if InPythonFunction:
            OutputValueToAppend2 = str(OutputValueToAppend).replace(', ', commaReplaceData1).replace( ',', commaReplaceData2)

            # print('infuntion')
        else:   
            # print('OUTfuntion')

            OutputValueToAppend2 = str(OutputValueToAppend).replace(commaReplaceData1, ', ').replace( commaReplaceData2, ',')


        OuptputList.append(OutputValueToAppend2)

    return [OuptputList], ItemNameList





def GetTableItensDictionarySecuredData(ItemNameList, InPythonFunction=False):

    # no need to add remove slashes function

    Datalist, names = GetTableItensListSecuredData(ItemNameList = ItemNameList, InPythonFunction = InPythonFunction)

    try: 
        Datalist=Datalist[0]

        dictValue = dict(zip(names, Datalist))
    
    except Exception as e:
        # print(e)
        pass

    return dictValue




def GetTableSingleItensSecuredData(ItemName, InPythonFunction=False):
    

    obj = sqlitewrapper.SqliteCipher(dataBasePath = dataBasePath , checkSameThread = False , password = pqw)

    # print(obj.getAllTableNames()[2][0])

    # print(tableNameList)


    TableData02 = obj.getDataFromTable(ItemName, raiseConversionError = True , omitID = True)

    TextToRemoveSlashes = TableData02
    
    try:
        TableData2 = RemoveExtraSlashes.RemoveExtraSlashes(TextToRemoveSlashes=TextToRemoveSlashes)
    
    except:
        TableData2 = RemoveExtraSlashes.RemoveExtraSlashesList(ListToRemoveSlashes=TextToRemoveSlashes)
        # print(TableData2)

        # print(tableNameList[i])
        # print(TableData2)

        # print(TableData2[1][0][0])

 

    OutputIten0 = str(TableData2[1][0][0])

    stringToDecode = OutputIten0

    OutputIten = EncodeDecode4Db.decodeBase64Db(stringToDecode)

    if InPythonFunction:
            OutputIten2 = str(OutputIten).replace(', ', commaReplaceData1).replace( ',', commaReplaceData2)

            # print('infuntion')
    else:   
        # print('OUTfuntion')


        OutputIten2 = str(OutputIten).replace(commaReplaceData1, ', ').replace( commaReplaceData2, ',')


    return OutputIten2



# def DeleteDb():

#     # CurrentWorkingPath = FilePathFromPython.FilePathFromPython()    


#     # fileLocation = CurrentWorkingPath + '\\' + Dasv

#     fileLocation = dataBasePath
#     try:
#         os.remove(fileLocation)
#     except:
#         pass




# print(dataBasePath)

# print('dataBasePath above')






# CurrentWorkingPath = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2\CSSAutoFormFiller'

# # ItenValue = 'data22'

# # ItemName = 'dataname22'


# print(GetAllTableSecuredData())

# print(GetAllTableDictionarySecuredData()['ExtensionType'])




# WriteTableSecuredIten(CurrentWorkingPath, ItemName, ItenValue)

# Database = "pysqlitecipher.db"


# ItemNameList = ['Item1', 'Item2' ]       # item to add
# colValueList = ['NewValue1', 'NewValue2']    # item value

# WriteTableSecuredList(ItemNameList,colValueList)



# ItemNameList = ['Item1', 'Item2', 'Item3' ]       # item to add
# colValueList = ['NewValue1', 'NewValue2', 'NewValu3']    # item value


# WriteTableSecuredList(ItemNameList,colValueList)


# ItemNameList = ['Item1', 'Item2' ]       # item to add
# colValueList = ['NewValue1', 'NewValue2']    # item value

# WriteTableSecuredList(ItemNameList,colValueList)



# colValueList = ['adfadf', 'Itxxxxx\\\\\\\\\em5', 'ite\\\\mm u\\\\\\\\\\\\mon',5.5 ]       # item to add
# ItemNameList = ['Name4', 'Name5', 'Name7',5]    # item value

# WriteTableSecuredList(ItemNameList,colValueList)



# print(GetTableItensListSecuredData(ItemNameList))

# print(GetTableItensDictionarySecuredData(ItemNameList))


# import pprint
# pprint.pprint(GetAllTableSecuredData())

# print(GetAllTableDictionarySecuredData())

# ItemName = 'Item2'

# print(GetTableSingleItensSecuredData(ItemName))

# ItemName = 'Item15'
# ItenValue = 'Itzz\\\\\\\\\\\\z77777zzez\\\\m5V\\alueTT2'/////////////////////////////.

# WriteTableSecuredIten(ItemName,ItenValue)

# import pprint
# # pprint.pprint(GetAllTableSecuredData())

# pprint.pprint(GetAllTableDictionarySecuredData())


# [ItemValues], ItemNames = GetAllTableSecuredData()

# print(ItemValues)

# print(ItemNames)