import pandas
import os


import getTableData
import ChangeStartupDirectoryT
import getItemFromSameLineDb
import TestIfTableValueExists
import StringListIntoList
import getUniqueAddFileEnd
import ReplaceInDoubleList
import CopyFileAnContinue
import CreateTempSaveLoationName






def placeValuesInFile():


    ListToPrint = []
    ######## first run checkIfDocumentSaved()
    Folder='AutoFormFillerKey'
    ChangeStartupDirectoryT.ChangeStartupDirectory(Folder)

    # home = os.path.expanduser('~')

    # ValueToCheck='storedValues'
    
    # ItEsists=TestIfTableValueExists.TestIfTableValueExists(ValueToCheck=ValueToCheck)

    dataName='datafillName'

    datafillName=getTableData.GetDataFromDatabase(dataName=dataName)

    dataNameList=['datafillName','rw','dataframe', 'FolderSaveLocation', 'columnList', 'JsInitTimeInMliSeconds', 'HalfPassed']

    OutputDictionary=getTableData.GetMultipleDataFromDatabase(dataNameList=dataNameList)


    # dataNameList1 = ['Job Name','File KEY', 'FontName', 'FontSize', 'ExtensionType']

    TableName1 = 'FontAndItsSize'

    # dataName2 = 'File Saved Location'

    # TableName2 = 'FilesInDatabase'

    OutputDictionaryTableName1=getTableData.GetTableDataFromTable(TableName=TableName1)

    # FileSavedLocation=getTableData.GetDataFromDatabase(dataName=dataName2,TableName=TableName2)

    TableData = OutputDictionaryTableName1[0]

    TableColumns = OutputDictionaryTableName1[1]

    dfTable1 = pandas.DataFrame(TableData,columns=TableColumns)

    valueToCheck = 'File KEY'

    FileKey= (dfTable1[valueToCheck][dfTable1['Job Name']==datafillName]).values[0]

    valueToCheck = 'ExtensionType'

    ExtensionType= (dfTable1[valueToCheck][dfTable1['Job Name']==datafillName]).values[0]

    print(ExtensionType)

    if ExtensionType == 'image':

        valueToCheck = 'Job Name'

        valueToCheck = 'FontName'

        FontName= (dfTable1[valueToCheck][dfTable1['Job Name']==datafillName]).values[0]

        valueToCheck = 'FontSize'

        FontSize= (dfTable1[valueToCheck][dfTable1['Job Name']==datafillName]).values[0]

        TableName3 = FileKey

        OutputTableName3 = getTableData.GetTableData(TableName=TableName3)

        spaceReplaceData = '$%3&*&'

        OutputTableName3Keys0 = str(list(OutputTableName3.keys())).replace('"',"'").replace("]', '[", "', '[").split("', '[")
        
        OutputTableName3Keys = [d.replace('[','').replace(']','').replace('"','').replace("'", '').replace(' ','').split(',') for d in OutputTableName3Keys0 ]    

        RealListOfColumnnames = OutputDictionary['columnList'].replace('[','').replace(']','').replace('"','').replace("'",'').replace(", ",',').replace(" ,",',').replace(spaceReplaceData, ' ').split(',') #turns text to list of strings

    datafillName = OutputDictionary['datafillName']

    LocationAsked = OutputDictionary['FolderSaveLocation']

    rw = int(OutputDictionary['rw'])




    # rw = 0 # block this after tests

    # print('this is the rw data: ' + str(rw)) # block this after tests

    # # print(len(OutputDictionary['dataframe']))/
    # print('numberOfRowsAbove')






    dataframe1 = OutputDictionary['dataframe']

    # stringCheked = str(dataframe1)

    StringList=dataframe1

    dataframe0=StringListIntoList.StringListIntoList(StringList=StringList,DoubleListCutAmount=3,DoublesSeparator1="'], ['", DoublesSeparator2=", ",DoubleList=True)

    commaReplace = '#3B&a$'

    DoubleList = dataframe0

    Item = commaReplace

    Subtitution = ', '

    dataframe = ReplaceInDoubleList.ReplaceInDoubleList(DoubleList=DoubleList, Item=Item, Subtitution=Subtitution)

    BaseFileLocation00=str(getItemFromSameLineDb.getDatafillName())

    # print(BaseFileLocation00)

    # print('BaseFileLocation00')

    BaseFileLocation0 =  BaseFileLocation00

    # print(BaseFileLocation0)

    # print('BaseFileLocation0')

    BaseFileLocation2=BaseFileLocation0
   

    BaseFileLocation3=BaseFileLocation0.split(".")

    uniqueValue = getUniqueAddFileEnd.getUniqueAddFileEnd()

    BaseFileLocation=BaseFileLocation3[0] + '__' + uniqueValue + "_temp."+BaseFileLocation3[-1]

    if ExtensionType == 'image':

        TimeNameFull = CreateTempSaveLoationName.CreateTempSaveLoationName(BaseFileLocation)

        noError = False

        print(len(dataframe))

        print('len(dataframe)')

        CopyFileAnContinue.CopyFileAnContinue(BaseFileLocation2= BaseFileLocation2,BaseFileLocation = BaseFileLocation,dataframe = dataframe,OutputDictionary = OutputDictionary,RealListOfColumnnames= RealListOfColumnnames,  ListToPrint = ListToPrint, LocationAsked = LocationAsked, FontName = FontName, FontSize = FontSize, dataframe0 = dataframe0, datafillName = datafillName, OutputTableName3Keys =  OutputTableName3Keys, noError = noError, rw = rw, TimeNameFull = TimeNameFull)
        












placeValuesInFile()










# data=0                        # block this after test

# dataName='rw'                 # block this after test

# getTableData.WriteDataDatabase(data,dataName)             # block this after test



