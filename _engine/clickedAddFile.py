import pandas 
# import sqlite3
import shutil 
import os

import CreateRow
import getTableData
import StringListIntoList
import CloseEspecificWorkbook
# import changeDirectory
import readSqlDatabase
import writeToSqlite
import DeleteAllFilesInFolder

def clickedAddFile(): #### call on this valuesList from database and remove calling from input

    #### the bellow data is for excel values
    #### it must find which direction to go from by getting the data that says
    #### if it is excel image or word (pdf files will be turned into a ground of image files saved in an location and to continue the user will need to select an image file)

    DatabaseName="AutoFormFiller.db"



    TableDataGotten = getTableData.GetTableData()
   
    ExtensionType = TableDataGotten['ExtensionType']

    valuesList = TableDataGotten['AddToTablevaluesList']

    if ExtensionType=='excel':
        listOfRows = TableDataGotten['listOfRows']

        listOfColumns  = TableDataGotten['listOfColumns']

        listOfRows=StringListIntoList.StringListIntoList(StringList=listOfRows)

        listOfColumns=StringListIntoList.StringListIntoList(StringList=listOfColumns)
    
    if ExtensionType=='image':
        listOfRows0 = TableDataGotten['finalLocationsYList']

        listOfColumns0  = TableDataGotten['finalLocationsXList']

        newFontSize = TableDataGotten['FontSize']

        newFont = TableDataGotten['newFont']

        listOfRows = listOfRows0.replace("[",'').replace(" ",'').replace("]",'').replace("'",'').split(',')

        listOfColumns = listOfColumns0.replace("[",'').replace(' ','').replace("]",'').replace("'",'').split(',')


    valuesList=StringListIntoList.StringListIntoList(StringList=valuesList, brakets=False, Splitter=",")

    listOfValueNames=[]
    for i in range(len(listOfRows)):
        
        value="["+ str(listOfRows[i]) +", "+ str(listOfColumns[i])+"]"

        listOfValueNames.append(value)

    columns=listOfValueNames
    row=valuesList

    frame=CreateRow.CreateDataframeWithOneRow(columns=columns,row=row)

    newFileSavedLocation=getTableData.GetDataFromDatabase(dataName='newFileLocation0')
    datafillName=getTableData.GetDataFromDatabase(dataName='datafillName')

    UPPERdf = datafillName.upper()

    PDFfile=getTableData.GetDataFromDatabase(dataName='PDFfile')

    Skip=False

    SqlDatase=True

    AllTables=getTableData.GetTableData()

    FilesInDatabaseLocation='FilesInDatabase'

    if ExtensionType=='image':
        
        if PDFfile == 'false':
            InPDFdatafillName = ''
            InPDFdatafillNameUPPER = ''
 
        if PDFfile == 'true':

            InPDFdatafillName=getTableData.GetDataFromDatabase(dataName='InPDFdatafillName')

            InPDFdatafillNameUPPER = InPDFdatafillName.upper()
   
    columnsFileinDatabase= ['Job Item', 'Job Name', 'File KEY', 'File Saved Location']

    Skip=False
    
    SheetName="KEY_" + datafillName.split('.')[0] 

    storedValues=frame


    DatabaseNameBACKUP =  writeToSqlite.GetDatePartName(DatabaseNameInput= DatabaseName)
    
    Skip= OpenDeleteRecreateSheet(filename=SheetName, frame=storedValues,columnList=listOfValueNames, SqlDatase=SqlDatase, DatabaseName= DatabaseName, DatabaseNameBACKUP= DatabaseNameBACKUP)
    
    if Skip==False:

        if ExtensionType=='image':

                if PDFfile == 'false':

                    #this is where the Files in database table is created

                    PdfUsed =''

                    InPDFdatafillName = ''

                    JobItem = InPDFdatafillName + ' / ' + datafillName

                    InputDataList=[JobItem, datafillName,SheetName,newFileSavedLocation]

                    TableName=FilesInDatabaseLocation

                    columnsInDatabase=columnsFileinDatabase

                    Skip = AddTabletoSql(InputDataList=InputDataList,TableName=TableName,columnsInDatabase=columnsInDatabase, DatabaseName = DatabaseName, DatabaseNameBACKUP=DatabaseNameBACKUP)


                if PDFfile == 'true':              
                    PdfUsed = getTableData.GetDataFromDatabase(dataName='PdfLocation') 

                    InPDFdatafillName=getTableData.GetDataFromDatabase(dataName='InPDFdatafillName')

                    JobItem = InPDFdatafillName + ' / ' + datafillName

                    InputDataList=[JobItem, datafillName,SheetName,newFileSavedLocation]

                    TableName=FilesInDatabaseLocation

                    columnsInDatabase=columnsFileinDatabase

                    Skip = AddTabletoSql(InputDataList=InputDataList,TableName=TableName,columnsInDatabase=columnsInDatabase, DatabaseName = DatabaseName, DatabaseNameBACKUP=DatabaseNameBACKUP)

                else:
                    pass

        if Skip==False:
            if ExtensionType=='image':

                if PDFfile == 'false':
                    FromPdf = 'No'

                    InPDFdatafillName= ''

                    InPDFdatafillNameUPPER = ''

                    JobItem = InPDFdatafillName + ' / ' + datafillName

                    InputDataList2=[JobItem, datafillName,SheetName,newFont,newFontSize, FromPdf, PdfUsed, InPDFdatafillName,ExtensionType, InPDFdatafillNameUPPER, UPPERdf]

                    TableName2='FontAndItsSize'

                    columnsInDatabase2 =  ['Job Item', 'Job Name', 'File KEY', 'FontName', 'FontSize', 'FromPdf', 'PdfUsed', 'InPDFdatafillName','ExtensionType', 'InPDFdatafillNameUPPER', 'UPPER']

                    Skip = AddTabletoSql(InputDataList=InputDataList2,TableName=TableName2,columnsInDatabase=columnsInDatabase2, DatabaseName=DatabaseName, DatabaseNameBACKUP=DatabaseNameBACKUP)
                    
                if PDFfile=='true':
                    FromPdf = 'Yes'

                    InPDFdatafillNameUPPER = InPDFdatafillName.upper()

                    JobItem = InPDFdatafillName + ' / ' + datafillName

                    InputDataList2=[JobItem, datafillName,SheetName,newFont,newFontSize, FromPdf, PdfUsed, InPDFdatafillName,ExtensionType, InPDFdatafillNameUPPER, UPPERdf]

                    TableName2='FontAndItsSize'

                    columnsInDatabase2 =  ['Job Item', 'Job Name', 'File KEY', 'FontName', 'FontSize', 'FromPdf', 'PdfUsed', 'InPDFdatafillName','ExtensionType', 'InPDFdatafillNameUPPER', 'UPPER']

                    Skip = AddTabletoSql(InputDataList=InputDataList2,TableName=TableName2,columnsInDatabase=columnsInDatabase2,DatabaseName= DatabaseName, DatabaseNameBACKUP=DatabaseNameBACKUP)
                                
            if ExtensionType=='excel':

                # add for extension excel must have infill data = '' in the ones that does not apply


                pass

            if ExtensionType=='word':

                # add for extension word

                pass
                
            if Skip==False:

                # copy original file to desired folder location

                TableDataGotten = getTableData.GetTableData()

                if PDFfile=='true':
                    fileLocation = TableDataGotten['newFileLocationImg']
                
                elif PDFfile=='false':
                    fileLocation = TableDataGotten['fileLocation']

                    filePath = TableDataGotten['filePath']

                    TempFolderLocation = filePath +"\\Temp"

                    LocationToDeleteFIles = TempFolderLocation
                    DeleteAllFilesInFolder.DeleteAllFilesInFolder(LocationToDeleteFIles = LocationToDeleteFIles)
                    
                else:                    
                    fileLocation = TableDataGotten['fileLocation']

                newFileLocation0 = TableDataGotten['newFileLocation0']

                try:
                    LocationToAddFileOnApp = TableDataGotten['LocationToAddFileOnApp']
                except KeyError:
                    pass

                try:
                    NewfinalSavedLocation=shutil.copy(fileLocation, newFileLocation0)

                except Exception as e:
                    pass

                #### this closing file is for excel the program will get the variable telling which type of file it is and close the correct one this can be done in an separate python file for easy access
                #### and so this saving mecanism can be used in other areas and changed for all areas easilly
                CloseEspecificWorkbook.CloseEspecificWorkbook(fileName=newFileLocation0)

                try:
                    #this is the image or pdf file being used temporatily to add data
                    #pdf will not be added here in this function
                    os.remove(LocationToAddFileOnApp)  
                except UnboundLocalError:
                    pass

                except FileNotFoundError:
                    pass


                # print("DONE!!!")




def AddTabletoSql(InputDataList,TableName,columnsInDatabase, DatabaseName, DatabaseNameBACKUP):

    InputData=InputDataList

    SqlDatase=True

    FilesInDatabase , FilesInDatabaseExists = readSqlDatabase.readSqlDatabase(table_name=TableName,columns=columnsInDatabase)

    if FilesInDatabaseExists==False:
        FilesInDatabase=pandas.DataFrame(columns=[])
        for i in range(len(columnsInDatabase)):

            FilesInDatabase[columnsInDatabase[i]]= pandas.Series(InputData[i])
    
    if FilesInDatabaseExists==True:
        TempFilesInDatabase=pandas.DataFrame(columns=[])
        for i in range(len(columnsInDatabase)):

            TempFilesInDatabase[columnsInDatabase[i]]= pandas.Series(InputData[i])
            
        FilesInDatabase=pandas.concat([FilesInDatabase,TempFilesInDatabase])
        
        pandas.DataFrame.sort_values(FilesInDatabase, by=['Job Item']+columnsInDatabase,ignore_index=True, inplace=True)
            
    Skip= OpenDeleteRecreateSheet(filename=TableName, frame=FilesInDatabase,columnList=columnsInDatabase, SqlDatase=SqlDatase,DatabaseName= DatabaseName, DatabaseNameBACKUP= DatabaseNameBACKUP)

    return Skip


    
def OpenDeleteRecreateSheet(filename,frame,columnList, DatabaseName, DatabaseNameBACKUP, SqlDatase=True, noColumnList=False):
    
    if SqlDatase==True:
        writeToSqlite.writeToSqlite(frame=frame, table_name=filename, DatabaseName= DatabaseName, DatabaseNameBACKUP =DatabaseNameBACKUP)
        Skip=False
        
    return Skip








clickedAddFile()