from pysqlitecipher import sqlitewrapper
import os

from importedDataPyDTs import *
from importedDataPycommaReplaceData import *
import EncodeDecode4Db
# import DeleteAllFilesInFolder
import FilePathFromPython
import RemoveExtraSlashes




def WriteTableSecuredList(ItemNameList,colValueList):



    # TextToRemoveSlashes = colValueList
    # = RemoveExtraSlashes.RemoveExtraSlashes(TextToRemoveSlashes=TextToRemoveSlashes)
    
    
    # colValueList0 = []
    # for colValue in colValueList:
    #     TextToRemoveSlashes = colValue
    #     colValueList= RemoveExtraSlashes.RemoveExtraSlashes(TextToRemoveSlashes=colValue)
    #     colValueList0.append(colValue)

    colValueList0 = RemoveExtraSlashes.RemoveExtraSlashesList(ListToRemoveSlashes=colValueList)

    colValueList1 = colValueList0

    # print(ItemNameList[0])

    # print('ItemNameList above that will be written')


    # tableNameList = ItemNameList

    iDValue = 0
    colname = 'Col0'

    [OriginalItemValuesList0], OriginalItemNamesList0 = GetAllTableSecuredData()

    # print(OriginalItemNamesList0)

    # print(OriginalItemValuesList0)
    # print('OriginalItemValuesList0')

    OriginalItemValuesList = str(OriginalItemValuesList0).replace('"', '').replace("'", '').replace('[', '').replace(']', '').replace(' ', '').split(',')    

    OriginalItemNamesList = str(OriginalItemNamesList0).replace('"', '').replace("'", '').replace('[', '').replace(']', '').replace(' ', '').split(',')    

    # LocationToDeleteFIles = os.getcwd()

    LocationToDeleteFIles = FilePathFromPython.FilePathFromPython()

    # DeleteAllFilesInFolder.DeleteAllFilesInFolder(LocationToDeleteFIles=LocationToDeleteFIles)

    NewItemValuesLIst = colValueList1
    NewItemNameLIst = ItemNameList

    # print('ok')
    # print(type(OriginalItemNamesList))
    # print(len(OriginalItemNamesList[0]))
    for Id in range(len(OriginalItemNamesList)):

        # print(OriginalItemNamesList)
        # print('OriginalItemNamesList')
        OriginalName = OriginalItemNamesList[Id]
        # print(OriginalName)
        # print(ItemNameList)
        # print('items above')
        if OriginalName in ItemNameList:
           pass
        else: 
            # print('value added')
            if OriginalName == '':
                pass
            
            else:
                NewItemNameLIst.append(OriginalName)
                NewItemValuesLIst.append(OriginalItemValuesList[Id])

    # print(NewItemValuesLIst)
    # print(NewItemNameLIst)
    obj = sqlitewrapper.SqliteCipher(dataBasePath = dataBasePath , checkSameThread = False , password = pqw)


    for i in range(len(ItemNameList)):
        try:
            obj.deleteDataInTable(ItemNameList[i] , iDValue , commit = True , raiseError = True , updateId = True)
        except Exception as e:
            if str(e) == 'ID = 0 not found while deletion process':
                pass



    for i in range(len(NewItemNameLIst)):
        datatype = 'TEXT'

        colList = [[colname , datatype]]

        # print(colName[i])

        # print(colList)
        # TableCreated = False


        try:
            obj.createTable(tableName = NewItemNameLIst[i] , colList = colList , makeSecure=True , commit=True)

            # print('table created now')
        except Exception as e:
            if str(e) == 'table name already exist in data base':
                # print('Table already created')
                pass
            else:
                # print(e)
                pass


        # try:
        #     obj.deleteDataInTable(tableNameList[i] , iDValue , commit = True , raiseError = True , updateId = True)
        # except Exception as e:
        #     if str(e) == 'ID = 0 not found while deletion process':
        #         pass

        # colList = [colValueList[i], datatype]

        obj.insertIntoTable(tableName=NewItemNameLIst[i] , insertList=colList , commit = True)
      
        # print(tableNameList[i])
        # print(TableData2)
   

        stringToEncode = str(NewItemValuesLIst[i]).replace(', ', commaReplaceData1).replace(',', commaReplaceData2)
        
        colValueToAdd = EncodeDecode4Db.encodeBase64Db(stringToEncode)
        
        obj.updateInTable(NewItemNameLIst[i] , iDValue , colName=colname , colValue = colValueToAdd , commit = True , raiseError = True)

        # # # print(TableData2)

        # # print(tableNameList[i])
        # # print(TableData2)

        # # print('Done')




        # if len(GetAllTableSecuredData())<len(OriginalItemNamesList): #blcok this after error testing
        #     print(len(GetAllTableSecuredData()))
        #     print(len(OriginalItemNamesList))
        #     try:
        #         x = 20/0      #blcok this after error testing
        #     except:
                # raise


def WriteTableSecuredDictionary(InputDictionary):

    # no need to remove slashes

    ItemNameList = [*InputDictionary]
    
    colValueList = [*InputDictionary.values()]

    WriteTableSecuredList(ItemNameList = ItemNameList, colValueList = colValueList)


def WriteTableSecuredIten(ItemName, ItenValue):

    TextToRemoveSlashes = ItenValue
    ItenValue= RemoveExtraSlashes.RemoveExtraSlashes(TextToRemoveSlashes=TextToRemoveSlashes)


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

    stringToEncode = str(ItenValue).replace(', ', commaReplaceData1).replace(',', commaReplaceData2)
        
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




# print(GetTableItensListSecuredData(ItemNameList))

# print(GetTableItensDictionarySecuredData(ItemNameList))


# import pprint
# pprint.pprint(GetAllTableSecuredData())

# print(GetAllTableDictionarySecuredData())

# ItemName = 'Item2'

# print(GetTableSingleItensSecuredData(ItemName))

# ItemName = 'Item10'
# ItenValue = 'Itzzzzzez\\\\m5V\\alueTT2'

# WriteTableSecuredIten(ItemName,ItenValue)

import pprint
pprint.pprint(GetAllTableSecuredData())


# [ItemValues], ItemNames = GetAllTableSecuredData()

# print(ItemValues)

# print(ItemNames)