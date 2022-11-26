from pysqlitecipher import sqlitewrapper
# import os

# import FilePathFromPython
import EncodeDecode4Db

from importedDataPyDTs import *
from importedDataPycommaReplaceData import *
# from importedFNUDataPyDTs import *









# ItemNameList = ['Item1', 'Item2', 'Item3']       # item to add
# colValueList = ['NewValue5', 'NewValue6', 'NewValue8']    # item value










# def GetDbtPathDasvpqw():
#     TableDataValueSS3, TableDataValueSS2 = GBTdat.GetFlInf(fileName=fileNameUsed)

#     Dasv = TableDataValueSS3
#     pqw= ';' +  TableDataValueSS2
#     dataBasePath = FilePathFromPython.FilePathFromPython()  + '\\' + Dasv

#     return Dasv, pqw, dataBasePath


# Dasv, pqw, dataBasePath = GetDbtPathDasvpqw()



def WriteTableSecuredList(ItemNameList,colValueList):

    # print(ItemNameList[0])

    # print('ItemNameList above that will be written')

    # CurrentWorkingPath = FilePathFromPython.FilePathFromPython()

    # Database = CurrentWorkingPath  + '\\' + Dasv

    tableNameList = ItemNameList

    # password = pqw

    # DbLocation = ''
    # DbName = "pysqlitecipher.db"

    # dataBasePath = DbLocation + DbName

    # dataBasePath = Database

    iDValue = 0
    colname = 'Col0'

    # Dasv, pqw, dataBasePath = GetDbtPathDasvpqw()

    obj = sqlitewrapper.SqliteCipher(dataBasePath = dataBasePath , checkSameThread = False , password = pqw)


    for i in range(len(tableNameList)):
        # print(tableNameList[i])

        datatype = 'TEXT'

        colList = [[colname , datatype]]

        # print(colName[i])

        # print(colList)
        # TableCreated = False
        try:
            obj.createTable(tableName = tableNameList[i] , colList = colList , makeSecure=True , commit=True)

            # print('table created now')
        except Exception as e:
            if str(e) == 'table name already exist in data base':
                # print('Table already created')
                pass
            else:
                # print(e)
                pass


        try:
            obj.deleteDataInTable(tableNameList[i] , iDValue , commit = True , raiseError = True , updateId = True)
        except Exception as e:
            if str(e) == 'ID = 0 not found while deletion process':
                # print('ID does not exist')
                pass


        # colList = [colValueList[i], datatype]

        colList = [colValueList[i], datatype]

        obj.insertIntoTable(tableName=tableNameList[i] , insertList=colList , commit = True)

        # TableData2 = obj.getDataFromTable(tableNameList[i] , raiseConversionError = True , omitID = False)
        
        # print(tableNameList[i])
        # print(TableData2)

      

        stringToEncode = str(colValueList[i]).replace(', ', commaReplaceData1).replace(',', commaReplaceData2)
        
        colValueToAdd = EncodeDecode4Db.encodeBase64Db(stringToEncode)
        
        obj.updateInTable(tableNameList[i] , iDValue , colName=colname , colValue = colValueToAdd , commit = True , raiseError = True)


        # TableData2 = obj.getDataFromTable(tableNameList[i] , raiseConversionError = True , omitID = False)
        # # print(TableData2)

        # print(tableNameList[i])
        # print(TableData2)

        # print('Done')




def WriteTableSecuredDictionary(InputDictionary):

    # CurrentWorkingPath = FilePathFromPython.FilePathFromPython()

    


    # ItemNameList = InputDictionary.keys()
    ItemNameList = [*InputDictionary]
    
    # colValueList = InputDictionary.values()
    colValueList = [*InputDictionary.values()]


    WriteTableSecuredList(ItemNameList = ItemNameList, colValueList = colValueList)

    





def WriteTableSecuredIten(ItemName, ItenValue):

    # CurrentWorkingPath = FilePathFromPython.FilePathFromPython()

    # Database = CurrentWorkingPath + '\\' + Dasv

    # password = pqw


    # dataBasePath = Database

    # Dasv, pqw, dataBasePath = GetDbtPathDasvpqw()

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


    




    # colList = [ItemName, datatype]

    obj.insertIntoTable(tableName=ItemName , insertList=colList , commit = True)

   
    
    # stringToEncode = ItenValue

    

    stringToEncode = str(ItenValue).replace(', ', commaReplaceData1).replace(',', commaReplaceData2)



        
    colValueToAdd = EncodeDecode4Db.encodeBase64Db(stringToEncode)


  
    obj.updateInTable(ItemName , iDValue , colName=colname , colValue = colValueToAdd , commit = True , raiseError = True)


    # print('Done')



def GetAllTableSecuredData(InPythonFunction=False):

    # CurrentWorkingPath = FilePathFromPython.FilePathFromPython()

    # Database = Dasv


    # tableNameList = ItemNameList

    # password = pqw

    # DbLocation = CurrentWorkingPath  + '\\'
    # # DbName = "pysqlitecipher.db"

    # dataBasePath = DbLocation + Database


    # dataBasePath = Database

    # Dasv, pqw, dataBasePath = GetDbtPathDasvpqw()


    obj = sqlitewrapper.SqliteCipher(dataBasePath = dataBasePath , checkSameThread = False , password = pqw)

    # print(obj.getAllTableNames()[2][0])

    Itens = obj.getAllTableNames()

    # print(Itens)

    # print(tableNameList)

    ItemNameList = []
    OuptputList = []
    for i in range(len(Itens)-2):

        ItenToAppend = Itens[i+2][0]
        TableData2 = obj.getDataFromTable(ItenToAppend, raiseConversionError = True , omitID = True)

       



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

            # OutputValueToAppend2 = EncodeDecode4Db.decodeBase64Db(OutputValueToAppend)
            # print('infuntion')
        else:   
            # print('OUTfuntion')




            OutputValueToAppend2 = str(OutputValueToAppend).replace(commaReplaceData1, ', ').replace( commaReplaceData2, ',')




            # pass
            # OutputValueToAppend = EncodeDecode4Db.decodeBase64Db(stringToDecode)

            # OutputValueToAppend2 = OutputValueToAppend


        # print(OutputValueToAppend2)

        # print('OutputValueToAppend2 above')

        # OutputValueToAppend2 = EncodeDecode4Db.decodeBase64Db(OutputValueToAppend)

        OuptputList.append(OutputValueToAppend2)

    return [OuptputList], ItemNameList





def GetAllTableDictionarySecuredData(InPythonFunction=False):

    # CurrentWorkingPath = FilePathFromPython.FilePathFromPython()

    

    Datalist, names = GetAllTableSecuredData(InPythonFunction = InPythonFunction)

    try: 
        Datalist=Datalist[0]

        dictValue = dict(zip(names, Datalist))
    
    except Exception as e:
        # print(e)
        pass

    return dictValue

    



def GetTableItensListSecuredData(ItemNameList, InPythonFunction=False):

    # CurrentWorkingPath = FilePathFromPython.FilePathFromPython()

    # dataBasePath = CurrentWorkingPath  + '\\' + Dasv

    # Database = Dasv

    tableNameList = ItemNameList

    # password = pqw

    # DbLocation = CurrentWorkingPath + '\\'
    

    # dataBasePath = DbLocation + Dasv


    # dataBasePath = Database

    # Dasv, pqw, dataBasePath = GetDbtPathDasvpqw()


    obj = sqlitewrapper.SqliteCipher(dataBasePath = dataBasePath , checkSameThread = False , password = pqw)

    # print(obj.getAllTableNames()[2][0])

    # Itens = obj.getAllTableNames()

    # print(tableNameList)

    OuptputList = []
    for i in range(len(tableNameList)):

        TableData2 = obj.getDataFromTable(tableNameList[i], raiseConversionError = True , omitID = True)
        # print(TableData2)

        # print(tableNameList[i])
        # print(TableData2)

        # print(TableData2[1][0][0])

        OutputValueToAppend0 = str(TableData2[1][0][0])

        stringToDecode = OutputValueToAppend0

        OutputValueToAppend = EncodeDecode4Db.decodeBase64Db(stringToDecode)


        if InPythonFunction:


            OutputValueToAppend2 = str(OutputValueToAppend).replace(', ', commaReplaceData1).replace( ',', commaReplaceData2)

            # OutputValueToAppend2 = EncodeDecode4Db.decodeBase64Db(OutputValueToAppend)
            # print('infuntion')
        else:   
            # print('OUTfuntion')




            OutputValueToAppend2 = str(OutputValueToAppend).replace(commaReplaceData1, ', ').replace( commaReplaceData2, ',')




        OuptputList.append(OutputValueToAppend2)

    return [OuptputList], ItemNameList





def GetTableItensDictionarySecuredData(ItemNameList, InPythonFunction=False):

    # CurrentWorkingPath = FilePathFromPython.FilePathFromPython()

    

    Datalist, names = GetTableItensListSecuredData(ItemNameList = ItemNameList, InPythonFunction = InPythonFunction)

    try: 
        Datalist=Datalist[0]

        dictValue = dict(zip(names, Datalist))
    
    except Exception as e:
        # print(e)
        pass

    return dictValue




def GetTableSingleItensSecuredData(ItemName, InPythonFunction=False):
    
    # CurrentWorkingPath = FilePathFromPython.FilePathFromPython()

    # Database = CurrentWorkingPath + '\\' + Dasv


    # tableNameList = ItemName

    # password = pqw

    # DbLocation = ''
    # DbName = "pysqlitecipher.db"

    # dataBasePath = DbLocation + DbName


    # dataBasePath = Database

    # Dasv, pqw, dataBasePath = GetDbtPathDasvpqw()


    obj = sqlitewrapper.SqliteCipher(dataBasePath = dataBasePath , checkSameThread = False , password = pqw)

    # print(obj.getAllTableNames()[2][0])

    # Itens = obj.getAllTableNames()

    # print(tableNameList)

    # OuptputList = []
    # for i in range(len(tableNameList)):

    TableData2 = obj.getDataFromTable(ItemName, raiseConversionError = True , omitID = True)
        # print(TableData2)

        # print(tableNameList[i])
        # print(TableData2)

        # print(TableData2[1][0][0])

        # OuptputList.append(TableData2[1][0][0])]

  

    OutputIten0 = str(TableData2[1][0][0])

    stringToDecode = OutputIten0

    OutputIten = EncodeDecode4Db.decodeBase64Db(stringToDecode)



    if InPythonFunction:


            OutputIten2 = str(OutputIten).replace(', ', commaReplaceData1).replace( ',', commaReplaceData2)

            # OutputValueToAppend2 = EncodeDecode4Db.decodeBase64Db(OutputValueToAppend)
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


ItemNameList = ['Item1', 'Item2']       # item to add

# ItemNameList = ['Item2', 'Item1']       # item to add
colValueList = ['NewValue1', 'NewValue2']    # item value

# WriteTableSecuredList(ItemNameList,colValueList)



# print(GetTableItensListSecuredData(ItemNameList))

# print(GetTableItensDictionarySecuredData(ItemNameList))


# import pprint
# pprint.pprint(GetAllTableSecuredData())

# print(GetAllTableDictionarySecuredData())

# ItemName = 'Item2'

# print(GetTableSingleItensSecuredData(ItemName))

# ItemName = 'Item5'
# ItenValue = 'Item5ValueTT'

# WriteTableSecuredIten(ItemName,ItenValue)

import pprint
pprint.pprint(GetAllTableSecuredData())